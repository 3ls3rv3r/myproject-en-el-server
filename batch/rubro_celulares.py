"""rubro proveedores de telefonia celular segun Gonzalo"""
from  polls.models import *

def categorias(self):
        varDef= VariableDefCreate('habilitacion de linea',['inmediata','dentro de las 24 horas',,'dentro de las 48 horas', ,'mas de dos dias']) 
        varDef= VariableDefCreate('cortes de servicio',['nunca','uno por mes','uno por semana','uno por dia'])
        varDef= VariableDefCreate('soporte tecnico ante incidentes',['solucion inmediata','solucion en 24hs','solucion en 48 hs','no dan solucion'])
        varDef= VariableDefCreate('atencion al cliente',['personalizada y eficiente','personalizada e ineficiente','automatizada y eficiente','automatizada e ineficiente'])
        rubro1= RubroCreate("proveedores internet en capital",["demora para instalar","cortes de servicio","soporte tecnico ante incidentes","atencion al cliente"])

        candidato1= Candidato(desc="Speedy", rubro= rubro1).save()
        candidato1= Candidato(desc="Arnet", rubro= rubro1).save()
        candidato1= Candidato(desc="Iplan", rubro= rubro1).save()
	candidato1= Candidato(desc="Fibertel", rubro= rubro1).save()
	candidato1= Candidato(desc="Telecentro", rubro= rubro1).save()
