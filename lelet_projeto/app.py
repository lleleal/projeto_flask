from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

def obter_produtos():
    with open("produtos.csv",'r') as file:
        lista_produtos = []
        for linha in file:
            nome, descricao, preco, imagem = linha.strip().split(",")
            produto={
                "nome": nome,
                "descricao": descricao,
                "preço": float(preco),
                "imagem": imagem
            }

            lista_produtos.append(produto)
    return lista_produtos

def adicionar_produto(p): 
    linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
    with open("produtos.csv",'a') as file:
        file.write(linha)


# [
#         {"nome": "Coca-cola", "descricao": "Bom", "preco":10.30,"imagem":"https://images.tcdn.com.br/img/img_prod/858764/refrigerante_coca_cola_lata_350ml_c_12_359_1_20201021152315.jpg"} ,
#         {"nome": "Doritos", "descricao": "Suja a mão", "preco":11.20,"imagem":"https://m.media-amazon.com/images/I/610trEtCQuS._AC_UF1000,1000_QL80_.jpg"},
#         {"nome": "Pepsi", "descricao": "Bom!", "preco":12.15, "imagem":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRn3osZEStoppgdE63CiRtAPMHW3HuJ2-nqNw&s"},
#  ]

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
    return render_template('produtos.html', produtos=obter_produtos())

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
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
    
    adicionar_produto(produto)
    #lista_produtos.append(produto)

    return redirect(url_for("produtos"))

@app.route("/gerarcpf")
def gerar_cpf():
    cpf = CPF()
    new_cpf = cpf.generate()
    return render_template('gerar-cpf.html', show_cpf=new_cpf)

@app.route("/validar-cpf")
def validar_cpf_form():
    return render_template('validar-cpf.html')

@app.route("/validarcpf", methods=['POST'])
def validar_cpf():
    cpf_validate = request.form['cpf']
    cpf = CPF()
    if cpf.validate(cpf_validate):
        result = {"status":"CPF Válido","info":"cpf_validate"}
    else:
        result = {"status":"CPF Inválido","info":cpf_validate}
    return render_template('validar-result.html',result=result)

@app.route("/gerarcnpj")
def gerar_cnpj():
    cnpj=CNPJ()
    new_cnpj=cnpj.generate()
    return render_template('gerar-cnpj.html', show_cnpj=new_cnpj)

@app.route("/validar-cnpj")
def cnpj_form():
    return render_template('validar-cnpj.html')

@app.route("/validarcnpj", methods=['POST'])
def validar_cnpj():
    cnpj_validate = request.form['cnpj']
    cnpj = CNPJ()
    if cnpj.validate(cnpj_validate):
        result = {"status":"CNPJ Válido","info":cnpj_validate}
    else:
        result = {"status":"CNPJ Inválido","info":cnpj_validate}
    return render_template('validar-result.html',result=result)

app.run

