from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
        {"nome": "Coca-cola", "descricao": "Geladinha", "preco":3.50,"imagem":"https://images.tcdn.com.br/img/img_prod/858764/refrigerante_coca_cola_lata_350ml_c_12_359_1_20201021152315.jpg"} ,
        {"nome": "Doritos", "descricao": "Fedido que nem o Rodrigo", "preco":11.90,"imagem":"https://gizmodo.uol.com.br/wp-content/blogs.dir/8/files/2023/11/doritos-silent.jpg"},
        {"nome": "Pepsi", "descricao": "Eterno coadjuvante, mas bom", "preco":3.50, "imagem":"https://www.piramidesdistribuidora.com.br/images/original/3334-pepsi-lata-350ml-12un.20240613133557.png"},
 ]
    
app = Flask(__name__)

@app.route("/")
def home():
     return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos",methods=['GET','POST'])
def produtos():
    return render_template('produtos.html', produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome.lower():
            return render_template("produto.html",produto=produto)
            #f"Nome: {produto['nome']}, {produto['descricao']}"
            
    return "Produto não encontrado"

@app.route("/produtos/cadastro")
def cadastrar_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = {"nome":nome,"descricao":descricao,"preco":preco,"imagem":imagem}
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))

app.run

