from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  numero = int(input("Digite um número: "))
  return render_template('index.html', num=numero)

if __name__ == '__main__':
  app.run(debug=True)  