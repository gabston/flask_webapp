from flask import Flask, render_template, request, redirect


app = Flask(__name__)
lista = list()

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def jogoteca():
    return render_template('lista.html', titulo='Games', jogos=lista)

@app.route('/novo')
def novo_jogo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    print(request.form)
    return redirect('/')

app.run(debug=True)