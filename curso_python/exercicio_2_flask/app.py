from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def mostrar_lista():
  frutas = {
    1: 'melancia',
    2: 'banana',
    3: 'morango'
  }
  legumes = {
    1: 'cenoura',
    2: 'cogumelo',
    3: 'berinjela',
  }
  carnes = {}

  return render_template('segundo_projeto.html', fruta=frutas, legume=legumes, carne=carnes)

app.run()