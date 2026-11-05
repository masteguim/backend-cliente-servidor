from flask import Flask, jsonify
from modulos.livros.apresentacao.rotas import rotas_livros
from modulos.carrinho.apresentacao.rotas import rotas_carrinho
from modulos.favoritos.apresentacao.rotas import rotas_favoritos
from modulos.reservas.apresentacao.rotas import rotas_reservas

def criar_app():
    app = Flask(__name__)
    for modulo in (rotas_livros, rotas_carrinho, rotas_favoritos, rotas_reservas):
        app.register_blueprint(modulo)

    @app.after_request
    def permitir_frontend(resposta):
        # Somente a origem local do frontend de desenvolvimento.
        resposta.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
        resposta.headers["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
        resposta.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return resposta

    @app.route("/api/<path:caminho>", methods=["OPTIONS"])
    def preflight(caminho):
        return "", 204

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
