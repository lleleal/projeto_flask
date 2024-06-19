from flask import Flask, render_template

lista_produtos = [
    {"nome": "Coca-cola", "descricao": "veneno"},
    {"nome": "Pepsi", "descricao": "ruim"},
    {"nome": "Doritos", "descricao": "delicia"},
]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produto():
    return render_template("produtos.html", produtos = lista_produtos) 

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return f"{produto['nome']}, {produto['descricao']}"
        
        return "Produto não existe!"
    
    app.run