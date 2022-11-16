from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
  num = [5,3,2,4,1]
  maior_num = max(num)
  menor_num = min(num)
  return render_template("index.html", maior = maior_num, menor = menor_num)

if __name__ =='__main__':
  app.run(debug=True)  