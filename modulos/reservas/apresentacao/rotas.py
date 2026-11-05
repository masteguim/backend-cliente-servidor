from flask import Blueprint, request, jsonify
from modulos.reservas.negocio import servico
rotas_reservas = Blueprint("reservas", __name__, url_prefix="/api/reservas")

@rotas_reservas.get("")
def listar():
    return jsonify(servico.listar())

@rotas_reservas.post("")
def criar():
    dados = request.get_json(silent=True) or {}
    try:
        identificador = int(dados.get("livro_id", 0))
    except (ValueError, TypeError):
        raise ValueError("Livro inválido.")
    servico.criar(identificador, dados.get("nome", ""))
    return jsonify({"mensagem": "Reserva registrada."}), 201

@rotas_reservas.delete("/<int:id_reserva>")
def cancelar(id_reserva):
    servico.cancelar(id_reserva)
    return "", 204
