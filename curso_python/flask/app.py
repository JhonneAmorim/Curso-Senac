from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
  nomes = ["Sergio","Airton"]
  return render_template("index.html", nome  = nomes )

if __name__ == '__main__':
  app.run(debug=True)