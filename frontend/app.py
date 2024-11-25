from flask import Flask, render_template, request, redirect, url_for, session, flash
from threading import Timer
from functools import wraps
from api import mySQL
import webbrowser
import os
from mysql.connector.errors import IntegrityError
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
            session['email'] = email
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    return render_template('login.html')

# Rota para a tela de cadastro
@app.route(rule='/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Captura os dados de cadastro do formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')
        phone = request.form.get('phone')
        endereco = request.form.get('endereco')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        rua = request.form.get('rua')
        numero = request.form.get('numero')

        try:
            idReg = registro.register(email=email, senha=senha)
            usuarios.registerUser(id_registro=idReg, nome=nome, cpf=cpf, telefone=phone, estado=estado, cidade=cidade,
                                  cep=cep, rua=rua, numero=numero, data_nascimento="2006-01-03")
        except IntegrityError as e:
            if e.errno == 1062:
                flash(f'Esse email já está cadastrado no sistema...')
            else:
                flash(f'Hove um erro de Integridade de dados do mysql: {e}')
            return render_template('cadastro.html')
        except Exception as e:
            flash(f'Houve algum erro na hora de realizar o login: {e}')
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

# Rota para a tela de perfil
@app.route('/seu_perfil')
@login_required
def perfil():
    info = usuarios.selectColsWhere(
        columns=("nome", "telefone", "rua", "numero", "cidade", "estado"),
        where=f'id_registro = {session['id_registro']}')[0]
    user_info = {"nome":info[0],
                 "email":session['email'],
                 "telefone":info[1],
                 "rua":info[2],
                 "numero":info[3],
                 "cidade":info[4],
                 "estado":info[5]
                 }
    return render_template(template_name_or_list='perfil.html', usuario=user_info)

# Rota para a tela de cadastro de estacionamento
@app.route('/cadastro-estacionamento', methods=['POST', 'GET'])
@login_required
def cadEstacionamento():
    if request.method == 'POST':
        nome = request.form.get('nome')
        estado = request.form.get('estado')
        cidade = request.form.get('cidade')
        bairro = request.form.get('bairro')
        rua = request.form.get('rua')
        numero = request.form.get('numero')
        vagas_disp = request.form.get('vagas_disp')
        total_vagas = request.form.get('total_vagas')
        preco_hora = request.form.get('preco_hora')
        data_cria = request.form.get('data_cria')

        estacionamentos.registerParking(id_dono=session['id_registro'], nome=nome, estado=estado, cidade=cidade,bairro=bairro,
                                        rua=rua, numero=numero, vagas_disponiveis=vagas_disp, total_vagas=total_vagas,
                                        preco_hora=preco_hora, data_criacao=data_cria)
        return render_template('tela_inicial.html')
    return render_template('cadEstacionamento.html')

# Rota para a tela de reserva de estacionamentos
@app.route('/reservar')
@login_required
def reservar():
    return render_template('reservar.html')

# Rota a tela de suas reservas
@app.route('/suas-reservas')
@login_required
def suas_reservas():
    return render_template('suasreservas.html')

# Rota para Logout do site
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('id_registro', None)
    return redirect(url_for('login'))

#______________________________________________________________________________________________________________________#
# Funções para funcionamento do Site
def openBrowser() -> None:
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
