from flask import Flask, render_template #Biblioteca que ajudara na criação do site

app = Flask(__name__) #chamamos a biblioteca para nosso codigo(PAGINA)

@app.route("/") # Configurando a rota do site.
@app.route("/index.html")
def index():
    return render_template('index.html')# Aqui retornamos a pagina HTML, que estara na pasta templates

@app.route("/contato.html") # Configurando a rota do site.
def contato():
    return render_template('contato.html')# Aqui retornamos a pagina HTML, que estara na pasta templates

@app.route("/about.html") # Configurando a rota do site.
def about():
    return render_template('about.html')# Aqui retornamos a pagina HTML, que estara na pasta templates
