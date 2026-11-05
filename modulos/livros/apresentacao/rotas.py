from flask import Blueprint, request, jsonify
from modulos.livros.negocio import servico
rotas_livros = Blueprint("livros", __name__, url_prefix="/api/livros")

@rotas_livros.get("")
def listar():
    return jsonify(servico.listar(request.args.get("busca", "")))

@rotas_livros.post("")
def cadastrar():
    dados = request.get_json(silent=True) or {}
    return jsonify(servico.cadastrar(dados.get("titulo", ""), dados.get("autor", ""))), 201

@rotas_livros.delete("/<int:id_livro>")
def excluir(id_livro):
    servico.excluir(id_livro)
    return "", 204
