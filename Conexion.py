from psycopg2 import pool
from logger_base import log
import sys

class Conexion:
    _DATABASE='lab_Pool'
    _USERNAME='postgres'
    _PASSWORD='eduardojr'
    _HOST='localhost'
    _DB_PORT='5432'
    _MAX_CON=5
    _MIN_CON=0
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(minconn=cls._MIN_CON,
                                                      maxconn=cls._MAX_CON,
                                                      database=cls._DATABASE,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      host=cls._HOST,
                                                      port=cls._DB_PORT)
                log.debug(f'Pool Obtenido satisfactoriamente')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool : {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
            conexion=cls.obtenerPool().getconn()
            log.debug(f'Se obtuvo conexion {conexion}')
            return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Se libero la conexion')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug('Se libero todas las conexiones')

if __name__=='__main__':
    Conexion.obtenerPool()
    conexion1=Conexion.obtenerConexion()
    conexion2=Conexion.obtenerConexion()
    conexion3=Conexion.obtenerConexion()
    conexion4=Conexion.obtenerConexion()
    conexion5=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion6=Conexion.obtenerConexion()
    Conexion.cerrarConexiones()



