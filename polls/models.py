from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from datetime import datetime

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

    was_published_today.short_description = 'Published today?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice

#S: Ponele los puntos
#S: definiciones
class VariableDef(models.Model):
    """ej. cuanto tardo en llegar"""
    desc = models.CharField(max_length=100)
    def __unicode__(self):
        return self.desc

    def optionWithDesc(self, desc):
        """ej. si self=puntualidad, devolveme la opcion 1h tarde"""
        return self.variableopt_set.all().filter(desc=desc)[0]

class VariableOpt(models.Model):
    """ej. tardo en llegar=20min"""
    variableDef= models.ForeignKey(VariableDef)
    desc= models.CharField(max_length=20)
    def __unicode__(self):
        return self.desc

class Rubro(models.Model):
    """ej. Plomero"""
    desc = models.CharField(max_length=100)
    def __unicode__(self):
        return self.desc

class VariableParaRubro(models.Model):
    """ej. para Plomero 'cuanto tardo en llegar'"""
    rubro= models.ForeignKey(Rubro)
    variableDef= models.ForeignKey(VariableDef)

#S: instancias
class Candidato(models.Model):
    """ej. Juan Plomero"""
    desc = models.CharField(max_length=100)
    rubro= models.ForeignKey(Rubro)
    #XXX: telefono, mail, otras formas de IDENTIFICARLO
    def __unicode__(self):
        return self.desc

class Voto(models.Model):
    """ej. Juan Plomero tardo 20 min en llegar"""
    #XXX: solo vale la pena si queremos distinguir por votante, PERO habria que agregar quien es el votante y agrupar los votos en una "votacion"
    candidato= models.ForeignKey(Candidato)
    variableOpt= models.ForeignKey(VariableOpt)
    def __unicode__(self):
        return self.variableOpt.desc

class VotoCount(models.Model):
    """ej. 100 personas dijeron que Juan Plomero tardo 20 min en llegar"""
    candidato= models.ForeignKey(Candidato)
    variableOpt= models.ForeignKey(VariableOpt)
    cnt= models.IntegerField()
    def __unicode__(self):
        return self.candidato.desc + "/" + self.variableOpt.desc + "=" + str(self.cnt)


#S: metodos comodos
def VariableDefCreate(desc, opts):
    varDef= VariableDef(desc=desc)
    varDef.save()

    for o in opts:
      varDef.variableopt_set.create(desc=o)

    return varDef

def RubroCreate(desc, varDefNames):
    rubro= Rubro(desc=desc)
    rubro.save()

    for o in varDefNames:
      vardef= VariableDef.objects.get(desc=o)
      rubro.variablepararubro_set.create(variableDef= vardef)

    return rubro

def votoCntForCandidato(candidato):
    vv= {'XOpt1': -1, 'XOpt2': -1, 'XOpt3': -1}
    for optCnt in candidato.votocount_set.all():
        vv[optCnt.variableOpt.desc]= optCnt.cnt
    return vv
 
@transaction.commit_on_success
def votarDefOptForCandidato(candidato, varDefName, varOptName):
    varDef= candidato.rubro.variablepararubro_set.get(variableDef__desc= varDefName).variableDef
    varOpt= varDef.variableopt_set.get(desc=varOptName)
    try:
        vc= candidato.votocount_set.get(variableOpt= varOpt)
        vc.cnt= vc.cnt+1
        vc.save()
    except ObjectDoesNotExist:
        candidato.votocount_set.create(variableOpt= varOpt, cnt= 1)

