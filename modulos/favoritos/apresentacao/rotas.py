from flask import Blueprint, jsonify
from modulos.favoritos.negocio import servico
rotas_favoritos = Blueprint("favoritos", __name__, url_prefix="/api/favoritos")

@rotas_favoritos.get("")
def listar():
    return jsonify(servico.listar())

@rotas_favoritos.post("/<int:id_livro>/alternar")
def alternar(id_livro):
    servico.alternar(id_livro)
    return jsonify(servico.listar())
