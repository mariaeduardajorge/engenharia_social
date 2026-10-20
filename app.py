from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/simulador", methods=["POST"])
def simulador():
    data = request.get_json(silent=True) or {}
    scenario_id = data.get("scenario_id")
    scenarios = {
        "urgencia": {
            "answer": "suspeita",
            "title": "Boa análise: há sinais de phishing.",
            "explanation": "A mensagem cria urgência e ameaça uma consequência para pressionar a pessoa a agir sem verificar. Serviços legítimos não devem ser confirmados por links recebidos inesperadamente.",
            "actions": ["Não clique no link.", "Abra o serviço pelo aplicativo ou endereço oficial.", "Confirme o pedido por outro canal.", "Denuncie a mensagem se parecer fraudulenta."]
        },
        "colega": {
            "answer": "suspeita",
            "title": "A identidade precisa ser confirmada.",
            "explanation": "Um nome ou foto conhecidos não comprovam quem controla uma conta. Um pedido inesperado de senha, código ou acesso deve ser confirmado por um canal independente.",
            "actions": ["Não envie senhas nem códigos.", "Confirme com a pessoa por outro canal.", "Verifique o perfil e o contexto.", "Avise a plataforma ou a equipe escolar se necessário."]
        },
        "oficial": {
            "answer": "legitima",
            "title": "O cenário apresenta menos sinais de risco.",
            "explanation": "A mensagem orienta a pessoa a abrir o aplicativo oficial por conta própria e não solicita credenciais por link. Mesmo assim, avalie o contexto: nenhum indicador isolado garante legitimidade.",
            "actions": ["Acesse o serviço diretamente pelo aplicativo oficial.", "Nunca compartilhe códigos de autenticação.", "Ative MFA ou passkeys quando disponíveis.", "Mantenha alertas de acesso ativos."]
        }
    }
    result = scenarios.get(scenario_id)
    if not result:
        return jsonify({"error": "Cenário inválido."}), 400
    choice = data.get("choice")
    result["correct"] = choice == result["answer"]
    result["chosen"] = choice
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
