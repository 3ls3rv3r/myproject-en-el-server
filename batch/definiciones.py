from  polls.models import *

#productos y servicios
VariableDefCreateWithOpts('tarda_conseguir','conseguirla me llevo',['minutos','1 hora','1 dia','1 semana','1 mes','varios meses'])
VariableDefCreateWithOpts('tarda_poder_usar','hasta poder usarlo tuve que esperar',['nada','menos de 24 horas','menos de 48 horas', 'más de dos dias']) 
VariableDefCreateWithOpts('freq_problemas','tengo problemas',['nunca','una vez por mes','una vez por semana','todos los dias'])

VariableDefCreateWithRange('costo_menor','el mas barato costaba',1.0,999999.0)
VariableDefCreateWithRange('costo_mayor','el mas caro costaba',1.0,999999.0)
VariableDefCreateWithRange('costo','este costaba',1.0,999999.0)

#servicios
VariableDefCreateWithOpts('tarda_solucion','solucinarlo me llevo',['minutos','1h','1 dia','1 semana','1 mes','varios meses'])
VariableDefCreateWithOpts('baja_medio','baja del servicio',['tramite telefonico/mail','hay que ir a una oficina una vez','hay que ir varias veces'])

#productos, arreglos
VariableDefCreateWithOpts('vida_util','duracion',['meses','12 meses','24 meses','60 meses','120 meses'])

#productos, pintura
VariableDefCreateWithOpts('preparacion_superficie','preparacion superficie',['sup. libre de otra pintura','primer','nada'])

#XXX: refinar: atiende una maquina? cuanto costo encontrar la respuesta? (tiempo)
VariableDefCreateWithOpts('asesoramiento','asesoramiento',['visita','telefono','video','escrito','nada'])

"""rubro proveedores de telefonia celular segun Gonzalo"""
rubro1= RubroCreate("celu-caba","teléfono móvil - caba",["tarda_poder_usar","freq_problemas","baja_medio"])
CandidatosCreate(rubro1,["Movistar","Personal","Claro","Nextel"])

"""rubro proveedores de internet en capital segun Gonzalo"""
rubro1= RubroCreate("isp-caba","proveedores internet en capital",["tarda_poder_usar","freq_problemas","baja_medio"])
CandidatosCreate(rubro1,["Speedy","Arnet","IPlan","Fibertel","Telecentro"])

"""rubro pintura casco de barco segun mauri"""
rubro1= RubroCreate("pintura-barco-casco","pintura casco barco",["vida_util","tarda_conseguir","asesoramiento","costo_menor","costo_mayor","costo"])
CandidatosCreate(rubro1,["Revesta","Steelcot","Carboline","Schori"])
