from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def repetir_nome():
  nome = "Joao" 
  return render_template('index.html', nomes = nome)

app.run(debug=True)