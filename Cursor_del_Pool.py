from  logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion=None
        self._cursor=None

    def __enter__(self):
        log.debug('Inicio de meotod with __enter__')
        self._conexion=Conexion.obtenerConexion()
        self._cursor=self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta metodo __exit__')
        if exc_val is not None:
            self._conexion.rollback()
            log.error(f'Ocurrio un erro se hacve rollback: {exc_type},{exc_val},{exc_tb}')
        else:
            self._conexion.commit()
            log.debug(f'Se hizo Commit de la transaccion')

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__=='__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro de bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
