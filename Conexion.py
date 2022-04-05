from logger_base import log
import psycopg2 as bd
import sys #terminar programa

class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD='eduardojr'
    _DB_PORT='5432'
    _HOST='localhost'
    _conexion=None
    _cursor=None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion=bd.connect(database=cls._DATABASE,
                                         user=cls._USERNAME,
                                         password=cls._PASSWORD,
                                         host=cls._HOST,
                                         port=cls._DB_PORT)
                log.debug(f'Conexion Exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio una excepcion: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor=cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursosr : {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor


if __name__=='__main__':
    Conexion.obtenerCursor()
    