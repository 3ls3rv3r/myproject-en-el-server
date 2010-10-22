from  polls.models import *

#productos y servicios
VariableDefCreate('tarda_conseguir','conseguirla me llevo',['minutos','1 hora','1 dia','1 semana','1 mes','varios meses'])
VariableDefCreate('tarda_poder_usar','hasta poder usarlo tuve que esperar',['nada','menos de 24 horas','menos de 48 horas', 'más de dos dias']) 
VariableDefCreate('freq_problemas','tengo problemas',['nunca','una vez por mes','una vez por semana','todos los dias'])

#servicios
VariableDefCreate('tarda_solucion','solucinarlo me llevo',['minutos','1h','1 dia','1 semana','1 mes','varios meses'])
VariableDefCreate('baja_medio','baja del servicio',['tramite telefonico/mail','hay que ir a una oficina una vez','hay que ir varias veces'])

#productos, arreglos
VariableDefCreate('vida_util','duracion',['meses','12 meses','24 meses','60 meses','120 meses'])

#productos, pintura
VariableDefCreate('preparacion_superficie','preparacion superficie',['sup. libre de otra pintura','primer','nada'])

#XXX: refinar: atiende una maquina? cuanto costo encontrar la respuesta? (tiempo)
VariableDefCreate('asesoramiento','asesoramiento',['visita','telefono','video','escrito','nada'])

"""rubro proveedores de telefonia celular segun Gonzalo"""
rubro1= RubroCreate("celu-caba","teléfono móvil - caba",["tarda_poder_usar","freq_problemas","baja_medio"])
CandidatosCreate(rubro1,["Movistar","Personal","Claro","Nextel"])

"""rubro proveedores de internet en capital segun Gonzalo"""
rubro1= RubroCreate("isp-caba","proveedores internet en capital",["tarda_poder_usar","freq_problemas","baja_medio"])
CandidatosCreate(rubro1,["Speedy","Arnet","IPlan","Fibertel","Telecentro"])

"""rubro pintura casco de barco segun mauri"""
rubro1= RubroCreate("pintura-barco-casco","pintura casco barco",["vida_util","tarda_conseguir","asesoramiento"])
CandidatosCreate(rubro1,["Revesta","Steelcot","Carboline","Schori"])
