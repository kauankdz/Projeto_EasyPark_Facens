from api import mySQL

if __name__ == '__main__':
    registro = mySQL(table='registros')
    usuarios = mySQL(table='usuarios')
    estacionamentos = mySQL(table='estacionamentos')
    carros = mySQL(table='carros')
    usuario_carro = mySQL(table='usuario_carro')

    usuario_carro._delete()
    carros._delete()
    estacionamentos._delete()
    usuarios._delete()
    registro._delete()
