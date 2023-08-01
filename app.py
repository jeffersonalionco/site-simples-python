from flask import Flask, render_template #Biblioteca que ajudara na criação do site

app = Flask(__name__) #chamamos a biblioteca para nosso codigo(PAGINA)

@app.route("/") # Configurando a rota do site.
def index():
    return render_template('index.html')# Aqui retornamos a pagina HTML, que estara na pasta templates