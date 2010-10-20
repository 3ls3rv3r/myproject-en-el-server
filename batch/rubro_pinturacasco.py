"""rubro pintura casco de barco segun mauri"""
from  polls.models import *

def categorias(self):
        varDef= VariableDefCreate('duracion',['meses','12 meses','24 meses','60 meses','120 meses'])
        varDef= VariableDefCreate('asesoramiento',['visita','telefono','video','escrito','nada'])
        varDef= VariableDefCreate('preparacion superficie',['sup. libre de otra pintura','primer','nada'])
        varDef= VariableDefCreate('tarde en conseguirla',['1 dia','1 semana','1 mes'])
        rubro1= RubroCreate("pintura casco",["duracion","asesoramiento","preparacion superficie","tarde en conseguirla"])

        candidato1= Candidato(desc="revesta", rubro= rubro1).save()
        candidato1= Candidato(desc="steelcot", rubro= rubro1).save()
        candidato1= Candidato(desc="carboline", rubro= rubro1).save()
        candidato1= Candidato(desc="schori", rubro= rubro1).save()


