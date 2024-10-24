from flask import Flask, render_template, request, redirect, url_for, session
from threading import Timer
from functools import wraps
from api import mySQL
import webbrowser
import os
# ^^ Importações ^^

#______________________________________________________________________________________________________________________#
# Cria o app e define as suas configurações
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 3600

#______________________________________________________________________________________________________________________#
# Definindo as variáveis das tabelas que podem ser usadas. (de acordo com o mySQL)
registro = mySQL(table='registros')
usuarios = mySQL(table='usuarios')
estacionamentos = mySQL(table='estacionamentos')
carros = mySQL(table='carros')
usuario_carro = mySQL(table='usuario_carro')

#______________________________________________________________________________________________________________________#
# Funções de rotas do Flask

# Rota para a tela de login
@app.route(rule='/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('senha')

        acesso, idReg = verificar(email=email, senha=password)

        # Verifica se email e senha estão corretas
        if acesso:
            session['logged_in'] = True
            session['id_registro'] = idReg
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
        return redirect(url_for('login'))

    return render_template('cadastro.html')

#______________________________________________________________________________________________________________________#
# Função para proteger rotas que só poderão ser acessadas se o usuário logar.
# Favor adicionar as rotas à serem protegidas a baixo dela.
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get('logged_in'):
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

# Rota para a tela inicial (após login)
@app.route('/home')
@login_required
def home():
    return render_template('tela_inicial.html')

# Rota para Logout do site
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('id_registro', None)
    return redirect(url_for('login'))

#______________________________________________________________________________________________________________________#
# Funções para funcionamento do Site
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

#______________________________________________________________________________________________________________________#
# Main (não tem muito o que falar dela kkkkk); Ela inicia o servidor do flask e abre um navegador para exibir o site.
if __name__ == '__main__':
    Timer(interval=1, function=openBrowser).start()
    app.run(host="127.0.0.1", port=5000,debug=True, use_reloader=False)
