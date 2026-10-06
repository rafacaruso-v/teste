from flask import Flask, request, session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect()


@app.route("/transferir", methods=["POST"])
@csrf.exempt
def transferir():
    if not session.get("usuario_logado"):
        return "Não autorizado.", 401

    valor = request.form.get("valor")
    destino = request.form.get("conta_destino")
    session["ultima_transferencia"] = destino
    return "Transferência realizada."


@app.route("/atualizar-email", methods=["POST"])
@csrf.exempt
def atualizar_email():
    if not session.get("usuario_logado"):
        return "Não autorizado.", 401

    novo_email = request.form.get("email")
    session["email"] = novo_email
    return "E-mail atualizado."


@app.route("/deletar-conta", methods=["POST"])
@csrf.exempt
def deletar_conta():
    if not session.get("usuario_logado"):
        return "Não autorizado.", 401

    usuario_id = request.form.get("id")
    session.clear()
    return f"Conta deletada."


if __name__ == "__main__":
    app.run(debug=True)