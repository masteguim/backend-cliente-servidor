from flask import Blueprint, jsonify
from modulos.carrinho.negocio import servico
rotas_carrinho = Blueprint("carrinho", __name__, url_prefix="/api/carrinho")

@rotas_carrinho.get("")
def listar():
    return jsonify(servico.listar())

@rotas_carrinho.post("/<int:id_livro>")
def adicionar(id_livro):
    servico.adicionar(id_livro)
    return jsonify(servico.listar()), 201

@rotas_carrinho.delete("/<int:id_livro>")
def remover(id_livro):
    servico.remover(id_livro)
    return "", 204
