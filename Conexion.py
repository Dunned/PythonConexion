from logger_base import log
from psycopg2 import pool
import sys #terminar programa

class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD='eduardojr'
    _DB_PORT='5432'
    _HOST='localhost'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool=pool.SimpleConnectionPool(minconn=cls._MIN_CON,maxconn=cls._MAX_CON,
                                                    host=cls._HOST,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    database=cls._DATABASE,
                                                    port=cls._DB_PORT)
                log.debug(f'Creacion del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error {e} al obtener el Pool')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion=cls.obtenerPool().getconn() # retornna objeto conexion del pool  de conexiones
        log.debug(f'Conexion Obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la Conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall() #cierran todos los objetos


if __name__=='__main__':
    conexion1=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2=Conexion.obtenerConexion()
    conexion3=Conexion.obtenerConexion()
    conexion4=Conexion.obtenerConexion()
    conexion5=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6=Conexion.obtenerConexion()
