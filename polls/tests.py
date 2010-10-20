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
        self.failUnlessEqual(vv["XOpt2"], 1)

        votarDefOptForCandidato(candidato1, "XCategoria1", "XOpt2")
        vv= votoCntForCandidato(candidato1)
        self.failUnlessEqual(vv["XOpt2"], 2)

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

