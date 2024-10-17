from datetime import date
from datetime import datetime
from decimal import Decimal

import mysql.connector


class mySQL:

    def __init__(self, table: str) -> object:
        self.connection = mysql.connector.connect(host='localhost', user='root', password='senha', database='EasyPark')
        self.cursor = self.connection.cursor()
        self.table = table

    def selectAll(self):
        self.cursor.execute(f"Select * from {self.table};")
        results = self.__format(self.cursor.fetchall())
        return results

    def selectCols(self, columns: tuple):
        select = "SELECT "
        length = len(columns)
        for i, j in zip(columns, range(1, length+1)):
            if j == length:
                select+= str(i)
            else:
                select+= str(i) + ','
        select += f" FROM {self.table} ORDER BY {columns[0]}"
        self.cursor.execute(select)
        results = self.__format(self.cursor.fetchall())
        return results

    def selectAllWhere(self, where: str):
        self.cursor.execute(f"Select * from {self.table} WHERE {where};")
        results = self.__format(self.cursor.fetchall())
        return results

    def selectColsWhere(self, columns: tuple, where: str):
        select = "SELECT "
        length = len(columns)
        for i, j in zip(columns, range(1, length+1)):
            if j == length:
                select+= str(i)
            else:
                select+= str(i) + ','
        select += f" FROM {self.table} WHERE {where} ORDER BY {columns[0]}"
        self.cursor.execute(select)
        results = self.__format(self.cursor.fetchall())
        return results

    def insert(self, nome: str, idade: int, data: str):
        inserirPessoas = f"INSERT INTO {self.table}(nome, idade, data_nasc) VALUES(%s, %s, %s)"
        valores = (nome, idade, data)
        self.cursor.execute(inserirPessoas, valores)
        self.connection.commit()

    def register(self, email: str, senha: str):
        insertLogin = f'INSERT INTO {self.table} (email, senha, data_criacao) VALUES(%s, %s, %s)'
        values = (email, senha, datetime.now())
        self.cursor.execute(insertLogin, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def registerUser(self, id_registro: int, nome: str, cpf: str, telefone: str, estado: str, cidade: str, cep: str,
                     rua: str, numero: int, data_nascimento: str):
        insertUser = f'INSERT INTO {self.table} (id_registro, nome, cpf, telefone, estado, cidade, cep, rua, numero, data_nascimento) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (id_registro, nome, cpf, telefone, estado, cidade, cep, rua, numero, data_nascimento)
        self.cursor.execute(insertUser, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def registerParking(self, id_dono: int, nome: str, estado: str, cidade: str, bairro: str,
                rua: str, numero: int, vagas_disponiveis: int, total_vagas: int, preco_hora: float, data_criacao: str):
        insertParking = f'INSERT INTO {self.table} (id_dono, nome, estado, cidade, bairro, rua, numero, vagas_disponiveis, total_vagas, preco_hora, data_criacao) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (id_dono, nome, estado, cidade, bairro, rua, numero, vagas_disponiveis, total_vagas, preco_hora, data_criacao)
        self.cursor.execute(insertParking, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def registerCar(self, placa: str, modelo: str, cor: str, marca: str):
        insertCar = f'INSERT INTO {self.table} (placa, modelo, cor, marca) VALUES(%s, %s, %s, %s)'
        values = (placa, modelo, cor, marca)
        self.cursor.execute(insertCar, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def registerOwner(self, id_dono: int, id_carro: int):
        insertOwner = f'INSERT INTO {self.table} (id_usuario, id_carro) VALUES(%s, %s)'
        values = (id_dono, id_carro)
        self.cursor.execute(insertOwner, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def _delete(self):
        self.cursor.execute(f'DELETE FROM {self.table}')
        self.cursor.execute(f'ALTER TABLE {self.table} AUTO_INCREMENT = 1')
        self.connection.commit()

    # def changePass(self, email: str, chave_de_confirmacao: str):

    def __format(self, results: list):
        resultado = []
        for index, valor in enumerate(results):
            columns = []
            for i in valor:
                if isinstance(i, Decimal):
                    i = int(i)
                elif isinstance(i, date) or isinstance(i, datetime):
                    i = str(i)
                columns.append(i)
            resultado.append(tuple(columns))
        return resultado

# if __name__ == '__main__':
#     tabela = mySQL(connection=conexao, cursor=cursor, table="pessoas")
#     colunas = []
#     colunas.append("id")
#     colunas.append("nome")
#
#
#     # results = tabela.selectCols(columns=colunas)
#     # results = tabela.selectAll()
#     # results = tabela.selectAllWhere(where="idade < 18")
#     # results = tabela.selectColsWhere(columns=colunas, where="idade = 18")
#     for i in results:
#         print(i)
#     cursor.close()
#     conexao.close()
