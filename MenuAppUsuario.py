import logging
import sys

import UsuarioDAO
from UsuarioDAO import UsuarioDao

from Usuario import Usuario

while(True):
    print('MENU APP'.center(50,'*'))
    print('''
    1)Listas Usuarios
    2)Agregar Usuarios
    3)Actualizar Usuario
    4)Eliminar Usuario
    5)Salir
    ''')
    opcion=int(input('Digite una Opcion: '))
    if(opcion==1):
        print(f'Lista de Usuarios')
        for usuario in UsuarioDao.seleccionar():
            logging.debug(f'{usuario}\n')
    elif opcion==2:
        print(f'Digite Datos del usuario a insertar: ')
        username = input('Nombre de Usuario: ')
        password = input('Password de Usuario')
        usuario = Usuario(username=username, password=password)
        UsuarioDao.insertar(usuario)
    elif opcion==3:
        nuevoUsername=input('Nuevo Nombre: ')
        nuevoPassword=input('Nuevo Password: ')
        idUsuario=input('idUsuario a modificar: ')
        usuario=Usuario(idUsuario,nuevoUsername,nuevoPassword)
        UsuarioDao.actualizar(usuario)
    elif opcion==4:
        id_usuario_eliminar=input('Id de usuario a a eliminar: ')
        usuario=Usuario(id_usuario=id_usuario_eliminar)
        UsuarioDao.eliminar(usuario)
    elif opcion==5:
        break
    else:
        print('Opcion No Valida')