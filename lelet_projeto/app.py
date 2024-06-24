from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF

lista_produtos = [
        {"nome": "Coca-cola", "descricao": "Bom", "preco":10.30,"imagem":"https://images.tcdn.com.br/img/img_prod/858764/refrigerante_coca_cola_lata_350ml_c_12_359_1_20201021152315.jpg"} ,
        {"nome": "Doritos", "descricao": "Suja a mão", "preco":11.20,"imagem":"https://m.media-amazon.com/images/I/610trEtCQuS._AC_UF1000,1000_QL80_.jpg"},
        {"nome": "Pepsi", "descricao": "Bom!", "preco":12.15, "imagem":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRn3osZEStoppgdE63CiRtAPMHW3HuJ2-nqNw&s"},
 ]
    
app = Flask(__name__)

@app.route("/")
def home():
     return "<h1>Home</h1>"

# anota com uma rota
# fn
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
def cadastro_produto():
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

@app.route("/criarcpf")
def gerar_cpf():
    cpf = CPF()
    new_cpf = cpf.generate()
    masked_cpf = cpf.mask(new_cpf)
    return render_template('cadastrar-produto.html', show_cpf=masked_cpf)

@app.route("/validarcpf", methods=['POST'])
def validar_cpf():
    cpf_validate = CPF
    cpf = request.form['cpf'] 
    
    if cpf_validate:
        return redirect(url_for())
    else:
        return redirect(url_for())



app.run

