from Conexion import Conexion
from Persona import Persona
from logger_base import log


class PersonaDAO:
    '''
    DAO(DATA ACCESS OBJECT )
    CRUD CREATE
         READ
         UPDATE
         DELETE
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls) -> list:
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada:  {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores=(persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona actualizada {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores=(persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'Se elimino {persona}')
                return cursor.rowcount

if __name__ == '__main__':
    # personas=PersonaDAO.seleccionar()
    # for persona in personas:
    #     log.debug(persona)


    # persona1=Persona(nombre="Cristiano",apellido='Ronaldo',email='CrisR@mail.com')
    # personas_insertadas=PersonaDAO.insertar(persona1)
    # log.debug(f'Se inserto: {personas_insertadas}')

    # persona1=Persona(35,'Robert','Lewandosly','rLewan@mail.com')
    # personas_actualizadas=PersonaDAO.actualizar(persona1)
    # log.debug(f'Se actualizo: {personas_actualizadas}')

    persona1=Persona(id_persona=35)
    registro_eliminados=PersonaDAO.eliminar(persona1)
    log.debug(f'Se limino {registro_eliminados} registros')
