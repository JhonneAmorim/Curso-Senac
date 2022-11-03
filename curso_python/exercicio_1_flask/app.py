from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def mostrar_informações():
  return render_template('primeiro_projeto.html', meu_nome="Jhonne Amorim",
  idade=23, objetivos_do_curso="Desenvolver meus conhecimentos com flask")

app.run()