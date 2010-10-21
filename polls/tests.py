"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from  polls.models import *

from django.core.exceptions import ObjectDoesNotExist

class SimpleTest(TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}


class VotarYContarTest(TestCase):

	def test_votos_se_suman(self):
		varDef= VariableDefCreate('XCategoria1',['Xopt1','XOpt2','Xopt3'])
		varOpt2= varDef.optionWithDesc('XOpt2')

		rubro1= RubroCreate("XRubro",["XCategoria1"])

		candidato1= Candidato(desc="XCandidato1", rubro= rubro1)
		candidato1.save()

		votarDefOptForCandidato(candidato1, "XCategoria1", "XOpt2")
		vv= votoCntForCandidato(candidato1)
		self.failUnlessEqual(vv["XCategoria1/XOpt2"], 1)

		votarDefOptForCandidato(candidato1, "XCategoria1", "XOpt2")
		vv= votoCntForCandidato(candidato1)
		self.failUnlessEqual(vv["XCategoria1/XOpt2"], 2)

	def test_no_vota_si_no_es_del_rubro(self):
		varDef= VariableDefCreate('XCategoria2',['Xopt1','XOpt2','Xopt3'])
		varOpt2= varDef.optionWithDesc('XOpt2')

		rubro1= RubroCreate("XRubro",["XCategoria2"])

		candidato1= Candidato(desc="XCandidato2", rubro= rubro1)
		candidato1.save()

		try: 
			votarDefOptForCandidato(candidato1, "XCategoria1", "XOpt2")
			self.fail("Voto por una categoria que NO es del rubro")
		except ObjectDoesNotExist:
			pass
		except:
			self.fail("Voto por una categoria que No es del rubro y NO recibio DoesNotExist")

	   	try: 
			votarDefOptForCandidato(candidato1, "XCategoria2", "XOptNoExiste")
			self.fail("Voto por una opcion que NO es de la categoria")
		except ObjectDoesNotExist:
			pass
		except:
			self.fail("Voto por una opcion que No es del rubro y NO recibio DoesNotExist")

	def test_rubro_crear(self):
		varDef= VariableDefCreate('XCategoriaRubro',['Xopt1','XOpt2','Xopt3'])
		RubroCreate('XRubroNuevo',['XCategoriaRubro'])

		rr= Rubro.objects.filter(desc='XRubroNuevo')
		self.failUnlessEqual(len(rr),1)

		varDef= VariableDefCreate('XCategoriaRubro2',['Xopt1','XOpt2','Xopt3'])
		RubroCreate('XRubroNuevo',['XCategoriaRubro2'])

		rr= Rubro.objects.filter(desc='XRubroNuevo')
		self.failUnlessEqual(len(rr),1)
		try:
			rr[0].variablepararubro_set.get(variableDef__desc='XCategoriaRubro2')
		except ObjectDoesNotExist:
			self.fail("No agrego la categoria al rubro")

	def test_identificador(self):
		ttel= TipoIdentificador(desc="telefono").save()
		tmail= TipoIdentificador(desc="email").save()

		varDef= VariableDefCreate('XCategoriaRubro2',['Xopt1','XOpt2','Xopt3'])
		rubro= RubroCreate('XRubroNuevo',['XCategoriaRubro2'])
 
		c1= Candidato(desc="XCandidato1", rubro=rubro ).save()
		c2= Candidato(desc="XCandidato2", rubro=rubro ).save()
		
		identificadorForCandidatoRegistrar(c1,"4444-4441","telefono")
		identificadorForCandidatoRegistrar(c2,"4444-4442","telefono")
		identificadorForCandidatoRegistrar(c2,"4444-4442","telefono")
		identificadorForCandidatoRegistrar(c2,"candidato2@dominio.com","email")
		identificadorForCandidatoRegistrar(c2,"spammer@dominio.com","email")
		identificadorForCandidatoRegistrar(c1,"spammer@dominio.com","email")

		r1= IdentificadorCandidato.objects.filter(identificador__tipo__desc="telefono", identificador__desc="4444-4441")
		self.failUnlessEqual(len(r1),1)
		self.failUnlessEqual(r1[0].candidato, c1)

		r1= IdentificadorCandidato.objects.filter(identificador__tipo__desc="telefono", identificador__desc="4444-4442")
		self.failUnlessEqual(len(r1),1)
		self.failUnlessEqual(r1[0].candidato, c2)

		r1= IdentificadorCandidato.objects.filter(identificador__tipo__desc="email", identificador__desc="spammer@dominio.com")
		self.failUnlessEqual(len(r1),2)
		if (r1[0].candidato== c1 and r1[1].candidato== c2) or (r1[1].candidato== c1 and r1[0].candidato== c2):
			pass
		else:
			self.fail("spammer@dominio.com no trajo los candidatos correctos")


