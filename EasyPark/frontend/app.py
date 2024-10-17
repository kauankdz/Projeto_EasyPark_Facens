from flask import Flask, render_template, request, redirect, url_for
from threading import Timer
import webbrowser
from api import mySQL

registro = mySQL(table='registros')
usuarios = mySQL(table='usuarios')
estacionamentos = mySQL(table='estacionamentos')
carros = mySQL(table='carros')
usuario_carro = mySQL(table='usuario_carro')

app = Flask(__name__)


# Rota para a tela de login
@app.route(rule='/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Capture os dados de login do formulário
        email = request.form.get('email')
        password = request.form.get('senha')

        acesso, idReg = verificar(email=email, senha=password)

        print(idReg)

        if acesso:
            # Redireciona para a tela inicial após o login
            return redirect(url_for('home'))
        else:
            return render_template('login.html')

    return render_template('login.html')


# Rota para a tela de cadastro
@app.route(rule='/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Capture os dados de cadastro do formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')
        phone = request.form.get('phone')
        endereco = request.form.get('endereco')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        rua, numero = endereco.split(',')
        numero = int(numero.strip())
        rua = rua.strip()

        idReg = registro.register(email=email, senha=senha)
        usuarios.registerUser(id_registro=idReg, nome=nome, cpf=cpf, telefone=phone, estado=estado, cidade=cidade,
                              cep=cep, rua=rua, numero=numero, data_nascimento="2006-01-03")
        # Aqui você pode adicionar lógica para salvar os dados no backend
        return redirect(url_for('login'))

    return render_template('cadastro.html')


# Rota para a tela inicial (após login)
@app.route('/home')
def home():
    return render_template('tela_inicial.html')

def openBrowser():
    webbrowser.get("firefox").open_new("http://127.0.0.1:5000/login")

def verificar(email: str, senha: str):
    acesso = False
    cols = ("email", "senha", "id")
    idReg = 0
    results = registro.selectCols(columns=cols)
    for valor in results:
        if email == valor[0] and senha == valor[1]:
            acesso = True
            idReg = valor[2]
            break
    return acesso, idReg

if __name__ == '__main__':
    Timer(1, openBrowser).start()
    app.run(debug=True, use_reloader=False)
