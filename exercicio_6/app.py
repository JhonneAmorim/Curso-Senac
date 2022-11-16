from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
  num = []
  for i in range(1, 11):
    passar_num = int(input("Digite numeros: "))
    num.append(passar_num)
    if passar_num < 2:
      return passar_num
    else:
      return passar_num
  somar_numeros = sum(num)
  media_numeros = somar_numeros / 2

  return render_template('index.html',numeros=i, soma=somar_numeros, media=media_numeros)

if __name__ == '__main__':
  app.run(debug=True)
  
