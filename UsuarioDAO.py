from CursorDelPool import  CursorDelPool
from Usuario import Usuario
from logger_base import log

class UsuarioDao:
    '''
    DAO -> DATA ACCESS OBJECT

    '''
    _SELECCIONAR='SELECT * FROM usuarios'
    _INSERTAR='INSERT INTO usuarios(username,password)' \
              ' VALUES(%s,%s)'
    _ACTUALIZAR='UPDATE usuarios SET username=%s,password=%s ' \
                'WHERE id_usuario=%s'

    _ELIMINAR='DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            usuarios=[]
            for registro in registros:
                usuario=Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            valores=(usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Se insertaron {cursor.rowcount} registros')

    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            valores=(usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Se actualizo {cursor.rowcount} registros')

    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            valores=(usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'Se elimino {cursor.rowcount} registros')


if __name__=="__main__":
    usuario=Usuario(id_usuario=1)
    UsuarioDao.eliminar(usuario)