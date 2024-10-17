from api import mySQL

if __name__ == '__main__':
    registro = mySQL(table='registros')
    usuarios = mySQL(table='usuarios')
    estacionamentos = mySQL(table='estacionamentos')
    carros = mySQL(table='carros')
    usuario_carro = mySQL(table='usuario_carro')

    # idReg = registro.register(email='joaovsalazar@gmail.com', senha='jojajo06__')
    #
    # idUser = usuarios.registerUser(id_registro=idReg, nome="João Vitor Cortez Salazar", cpf="495.848.308-05",
    #                                telefone="(15)99626-0307", estado="SP", cidade="Sorocaba", bairro="Vila Sônia",
    #                                rua="Olegário Ribeiro", numero=906, data_nascimento="2006/01/03")
    #
    # idCar = carros.registerCar(placa="GIM7C33", modelo="Kicks", cor="Cinza", marca="Nissan")
    #
    # idUC = usuario_carro.registerOwner(id_dono=idUser, id_carro=idCar)

    results  = registro.selectAll()
    print("\nRegistros:")
    for i in results:
        print(i)
    print("\nUsuários:")
    results  = usuarios.selectAll()
    for i in results:
        print(i)
    print("\nCarros:")
    results  = carros.selectAll()
    for i in results:
        print(i)
    print("\nUsuario_Carro (tabela intermediária):")
    results  = usuario_carro.selectAll()
    for i in results:
        print(i)
