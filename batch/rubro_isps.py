"""rubro proveedores de internet en capital segun Gonzalo"""
from  polls.models import *

def categorias(self):
        varDef= VariableDefCreate('demora para instalar',['dentro de las 48hs','dentro de los 10 dias','dentro del mes','Nunca vinieron']) 
        varDef= VariableDefCreate('cortes de servicio',['nunca','uno por mes','uno por semana','uno por dia'])
        varDef= VariableDefCreate('soporte tecnico ante incidentes',['solucion inmediata','solucion en 24hs','solucion en 48 hs','no dan solucion'])
        varDef= VariableDefCreate('atencion al cliente',['personalizada y eficiente','personalizada e ineficiente','automatizada y eficiente','automatizada e ineficiente'])
        varDef= VariableDefCreate('baja del servicio',['tramite telefonico/mail','hay que ir a una oficina una vez','hay que ir varias veces'])
	rubro1= RubroCreate("proveedores internet en capital",["demora para instalar","cortes de servicio","soporte tecnico ante incidentes","atencion al cliente","baja del servicio"])

        candidato1= Candidato(desc="Speedy", rubro= rubro1).save()
        candidato1= Candidato(desc="Arnet", rubro= rubro1).save()
        candidato1= Candidato(desc="Iplan", rubro= rubro1).save()
	candidato1= Candidato(desc="Fibertel", rubro= rubro1).save()
	candidato1= Candidato(desc="Telecentro", rubro= rubro1).save()
