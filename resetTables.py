from importlib.metadata import files

from api import mySQL
import os

path = os.getcwd()

# _____________________________________________________________________________________________________________________#
# Código feito apenas para resetar as tabelas nos casos de teste.
if __name__ == '__main__':
    registro = mySQL(table='registros')
    usuarios = mySQL(table='usuarios')
    estacionamentos = mySQL(table='estacionamentos')
    carros = mySQL(table='carros')
    usuario_carro = mySQL(table='usuario_carro')

    usuario_carro.delete()
    carros.delete()
    estacionamentos.delete()
    usuarios.delete()
    registro.delete()
