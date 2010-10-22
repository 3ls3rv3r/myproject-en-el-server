from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from datetime import datetime

#S: mejoras a models.Model
class ModelGZM(models.Model):
	class Meta:
		abstract= True

	def save(self,**kwargs):
		# igual, pero devolvemos el objeto para permitir x= MiModelo(initval).save()
		models.Model.save(self,**kwargs)
		return self

#S: Ponele los puntos
#S: definiciones
class VariableDef(ModelGZM):
	"""ej. cuanto tardo en llegar"""
	key= models.CharField(max_length=50,primary_key=True)
	desc = models.CharField(max_length=100)
	def __unicode__(self):
		return self.desc

	def optionWithDesc(self, desc):
		"""ej. si self=puntualidad, devolveme la opcion 1h tarde"""
		return self.variableopt_set.filter(desc=desc)[0]

class VariableOpt(ModelGZM):
	"""ej. tardo en llegar=20min"""
	variableDef= models.ForeignKey(VariableDef)
	desc= models.CharField(max_length=20)
	def __unicode__(self):
		return self.desc

class Rubro(ModelGZM):
	"""ej. Plomero"""
	key= models.CharField(max_length=50,primary_key=True)
	desc = models.CharField(max_length=100)
	def __unicode__(self):
		return self.desc

class VariableParaRubro(ModelGZM):
	"""ej. para Plomero 'cuanto tardo en llegar'"""
	rubro= models.ForeignKey(Rubro)
	variableDef= models.ForeignKey(VariableDef)

#S: instancias
class Candidato(ModelGZM):
	"""ej. Juan Plomero"""
	desc = models.CharField(max_length=100)
	rubro= models.ForeignKey(Rubro)
	#XXX: telefono, mail, otras formas de IDENTIFICARLO
	def __unicode__(self):
		return self.desc

class TipoIdentificador(ModelGZM):
	"""ej. 15 6242 2222 identifica a Mauricio"""
	desc = models.CharField(max_length=100,primary_key=True)
	def __unicode__(self):
		return self.desc

class Identificador(ModelGZM):
	"""ej. 15 6242 2222 identifica a Mauricio"""
	desc = models.CharField(max_length=100)
	tipo= models.ForeignKey(TipoIdentificador)
	def __unicode__(self):
		return self.desc

class IdentificadorCandidato(ModelGZM):
	identificador = models.ForeignKey(Identificador)
	candidato = models.ForeignKey(Candidato)
	def __unicode__(self):
		return self.identificador.desc + " -> " + self.candidato.desc

class Voto(ModelGZM):
	"""ej. Juan Plomero tardo 20 min en llegar"""
	#XXX: solo vale la pena si queremos distinguir por votante, PERO habria que agregar quien es el votante y agrupar los votos en una "votacion"
	candidato= models.ForeignKey(Candidato)
	variableOpt= models.ForeignKey(VariableOpt)
	def __unicode__(self):
		return self.variableOpt.desc

class VotoCount(ModelGZM):
	"""ej. 100 personas dijeron que Juan Plomero tardo 20 min en llegar"""
	candidato= models.ForeignKey(Candidato)
	variableOpt= models.ForeignKey(VariableOpt)
	cnt= models.IntegerField()
	def __unicode__(self):
		return self.candidato.desc + "/" + self.variableOpt.desc + "=" + str(self.cnt)


#S: metodos comodos
def VariableDefCreate(key, desc, opts):
	varDef= VariableDef(key=key,desc=desc)
	varDef.save()

	for o in opts:
	  varDef.variableopt_set.create(desc=o)

	return varDef

def RubroCreate(key, desc, varDefNames):

	try: 
		rubro= Rubro.objects.get(pk=key)
	except ObjectDoesNotExist:
		rubro= Rubro(key=key,desc=desc)
		rubro.save()

	for o in varDefNames:
	  vardef= VariableDef.objects.get(key=o)
	  rubro.variablepararubro_set.create(variableDef= vardef)

	return rubro

def CandidatosCreate(rubro, candidatos):
	for c in candidatos:
		Candidato(desc=c,rubro=rubro).save()

def votoCntForCandidato(candidato):
	vv= dict()
	for optCnt in candidato.votocount_set.all():
		vv[optCnt.variableOpt.variableDef.desc +"/"+ optCnt.variableOpt.desc]= optCnt.cnt
	return vv
 

def votarDefOptForCandidato(candidato, varDefName, varOptName):
	varDef= candidato.rubro.variablepararubro_set.get(variableDef__desc= varDefName).variableDef
	varOpt= varDef.variableopt_set.get(desc=varOptName)
	return votarOptForCandidato(candidato, varOpt)

@transaction.commit_on_success
def votarOptForCandidato(candidato, varOpt):
	try:
		vc= candidato.votocount_set.get(variableOpt= varOpt)
		vc.cnt= vc.cnt+1
		vc.save()
	except ObjectDoesNotExist:
		candidato.votocount_set.create(variableOpt= varOpt, cnt= 1)

@transaction.commit_on_success
def identificarCandidatoPor(candidato, iden, tipo):
	"""registra un identificador para un candidato UNA SOLA VEZ"""
	isNew= False

	tipoO= TipoIdentificador.objects.get(desc= tipo)
	idenO= None
	try:
		idenO= Identificador.objects.get(desc= iden, tipo= tipoO)
		try:
			IdentificadorCandidato.objects.get(candidato=candidato, identificador= idenO)
		except ObjectDoesNotExist:
			isNew= True
	except ObjectDoesNotExist:
		idenO= Identificador(desc= iden, tipo= tipoO)
		idenO.save()
		isNew= True

	if isNew:
		IdentificadorCandidato(candidato= candidato, identificador= idenO).save()
