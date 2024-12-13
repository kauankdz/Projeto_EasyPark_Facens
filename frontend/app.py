from flask import Flask, render_template, request, redirect, url_for, session, flash
from threading import Timer
from functools import wraps
from api import mySQL
import webbrowser
import os
from mysql.connector.errors import IntegrityError
# ^^ Importações ^^

#______________________________________________________________________________________________________________________#
# Cria o aplicativo e define as suas configurações
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 3600

#______________________________________________________________________________________________________________________#
# Definindo as variáveis das tabelas que podem ser usadas. (conforme o mySQL)
registro: mySQL = mySQL(table='registros')
usuarios: mySQL = mySQL(table='usuarios')
estacionamentos: mySQL = mySQL(table='estacionamentos')
carros: mySQL = mySQL(table='carros')
usuario_carro: mySQL = mySQL(table='usuario_carro')

#______________________________________________________________________________________________________________________#
# Funções de rotas do Flask

# Rota para a tela de login
@app.route(rule='/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email: str = request.form.get('email')
        password: str = request.form.get('senha')

        acesso, id_reg = verificar(email=email, senha=password)

        # Verifica se e-mail e senha estão corretas
        if acesso:
            session['logged_in'] = True
            session['id_registro'] = id_reg
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
        nome: str = request.form.get('nome')
        email: str = request.form.get('email')
        senha: str = request.form.get('senha')
        cpf: str = request.form.get('cpf')
        phone: str = request.form.get('phone')
        cidade: str = request.form.get('cidade')
        estado: str = request.form.get('estado')
        cep: str = request.form.get('cep')
        rua: str = request.form.get('rua')
        numero: int = int(request.form.get('numero'))

        try:
            id_reg: int = registro.register(email=email, senha=senha)
            usuarios.registerUser(id_registro=id_reg, nome=nome, cpf=cpf, telefone=phone, estado=estado, cidade=cidade,
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
# Função para proteger rotas que só poderão ser acessadas se o usuário conectar-se.
# Favor adicionar as rotas a serem protegidas a baixo dela.
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
    info = usuarios.selectColsWhere(columns=("nome", "telefone", "rua", "numero", "cidade", "estado"),
                                    where=f'id_registro = {session['id_registro']}')[0]
    user_info = \
    {
        "nome":info[0],
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
def cad_estacionamento():
    if request.method == 'POST':
        nome: str = request.form.get('nome')
        estado: str = request.form.get('estado')
        cidade: str = request.form.get('cidade')
        bairro: str = request.form.get('bairro')
        rua: str = request.form.get('rua')
        numero: int = int(request.form.get('numero'))
        vagas_disp: int = int(request.form.get('vagas_disp'))
        total_vagas: int = int(request.form.get('total_vagas'))
        preco_hora: float = float(request.form.get('preco_hora'))
        data_cria: str = request.form.get('data_cria')

        estacionamentos.registerParking(id_dono=session['id_registro'], nome=nome, estado=estado, cidade=cidade,
                                        bairro=bairro, rua=rua, numero=numero, vagas_disponiveis=vagas_disp,
                                        total_vagas=total_vagas, preco_hora=preco_hora, data_criacao=data_cria)
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
def open_browser() -> None:
    webbrowser.get("firefox").open_new("http://127.0.0.1:5000/login")

def verificar(email: str, senha: str) -> tuple[bool, int]:
    acesso = False
    cols = ("email", "senha", "id")
    id_reg = 0
    results = registro.selectCols(columns=cols)
    for valor in results:
        if email == valor[0] and senha == valor[1]:
            acesso = True
            id_reg = valor[2]
            break
    return acesso, id_reg

#______________________________________________________________________________________________________________________#
# Main (não tem muito o que falar dela haha). Ela inicia o servidor do flask e abre um navegador para exibir o site.
if __name__ == '__main__':
    Timer(interval=1, function=open_browser).start()
    app.run(host="127.0.0.1", port=5000,debug=True, use_reloader=False)
