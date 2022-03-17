from flask import Flask, render_template, request

app = Flask(__name__)

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/jogoteca')
def jogoteca():
    jogo1 = Jogo('Daniel', 'Comédia', 'Vida Real')
    jogo2 = Jogo('Rafael', 'Pornô', 'Vida Real')
    jogo3 = Jogo('Elden Ring', 'RPG', 'Xbox, Playstation, PC')
    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Games', jogos=lista_jogos)

@app.route('/novo')
def novo_jogo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar')
def criar():
    nome = request.form['nome']

app.run()