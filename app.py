import os
from flask import Flask, jsonify, request
from modulos.livros.apresentacao.rotas import rotas_livros
from modulos.carrinho.apresentacao.rotas import rotas_carrinho
from modulos.favoritos.apresentacao.rotas import rotas_favoritos
from modulos.reservas.apresentacao.rotas import rotas_reservas


def criar_app():
    app = Flask(__name__)

    for modulo in (
        rotas_livros,
        rotas_carrinho,
        rotas_favoritos,
        rotas_reservas,
    ):
        app.register_blueprint(modulo)

    origens_permitidas = {
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        resposta.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    }

    url_frontend = os.getenv("FRONTEND_URL", "").rstrip("/")

    if url_frontend:
        origens_permitidas.add(url_frontend)

    @app.before_request
    def verificar_preflight():
        if request.method == "OPTIONS":
            return "", 204

    @app.after_request
    def permitir_frontend(resposta):
        origem = request.headers.get("Origin")

        if origem in origens_permitidas:
            resposta.headers["Access-Control-Allow-Origin"] = origem
            resposta.headers["Vary"] = "Origin"
            resposta.headers["Access-Control-Allow-Methods"] = (
                "GET, POST, DELETE, OPTIONS"
            )
            resposta.headers["Access-Control-Allow-Headers"] = (
                "Content-Type"
            )

        return resposta

    @app.errorhandler(ValueError)
    def erro_validacao(erro):
        return jsonify({"erro": str(erro)}), 400

    @app.errorhandler(404)
    def nao_encontrado(erro):
        return jsonify({"erro": "Recurso não encontrado."}), 404

    @app.get("/api/saude")
    def saude():
        return jsonify({"status": "ok"})

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
