from ..models.models import Medico
from ..conexion.medico_conexion import (select_all, 
                                         select_by_especialidad,
                                         crear_medico, 
                                         eliminar_medico)

def servicio_medicos_all():
    medicos = select_all()
    print(medicos)
    return medicos

def servicio_consultar_especialidad(especialidad: str):
    if len(especialidad) != 0:
        medicos = select_by_especialidad(especialidad)
        print(medicos)
        return medicos
    else:
        return select_all()
    
def servicio_crear_medico(usuario_id: int, especialidad: str):
    medico = Medico(usuario_id=usuario_id, especialidad=especialidad)
    return crear_medico(medico)

def servicio_eliminar_medico(id: int):
    return eliminar_medico(id)
