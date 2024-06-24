from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF

app = Flask(__name__) 

@app.route("/criarcpf")
def criar_cpf():
    cpf = CPF()
    new_cpf = cpf.generate()
    masked_cpf = cpf.mask(new_cpf)
    return render_template('criar-cpf.html', show_cpf=masked_cpf)

@app.route("/validarcpf", methods=['POST'])
def validar_cpf():
    cpf_validate = CPF
    cpf = request.form['cpf'] 
    
    if cpf_validate:
        return redirect(url_for())
    else:
        return redirect(url_for())

app.run