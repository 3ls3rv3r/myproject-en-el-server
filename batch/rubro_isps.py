"""rubro proveedores de internet en capital segun Gonzalo"""
from  polls.models import *

def categorias(self):
        varDef= VariableDefCreate('demora para instalar',['dentro de las 48hs,'dentro de los 10 dias','un 
mes',
meses','120 
meses'])
        varDef= VariableDefCreate('asesoramiento',['visita','telefono','video','escrito','nada'])
        varDef= VariableDefCreate('preparacion superficie',['sup. libre de otra pintura','primer','nada'])
        varDef= VariableDefCreate('tarde en conseguirla',['1 dia','1 semana','1 mes'])
        rubro1= RubroCreate("pintura casco",["duracion","asesoramiento","preparacion superficie","tarde en conseguirla"])

        candidato1= Candidato(desc="revesta", rubro= rubro1).save()
        candidato1= Candidato(desc="steelcot", rubro= rubro1).save()
        candidato1= Candidato(desc="carboline", rubro= rubro1).save()
        candidato1= Candidato(desc="schori", rubro= rubro1).save()


