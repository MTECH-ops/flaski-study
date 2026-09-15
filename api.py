# Importa a classe Flask do pacote flask para criar o site
from flask import Flask, jsonify, request # requisição com cliente externo
from flask_cors import CORS # 1. Importe o CORS

# Cria a instância do aplicativo e defino o ponto de partida do código
app = Flask(__name__)
CORS(app) # 2. Ative o CORS para todas as rotas

# Define a rota para a página principal (a raiz "/") do site
@app.route("/")

# Criar a função para enviar requisição
def start():
    return jsonify({
        "biblioteca": "API",
        "versao": "1.0"
    })

livros = [
    {
        "id": 10,
        "titulo": "A volta dos que nao foram",
        "autor": "Eu"
    },
    {
        "id": 11,
        "titulo": "Senhor dos aneis",
        "autor": "Eu"
    },
    {
        "id": 12,
        "titulo": "Dom Casmurro",
        "autor": "Eu"
    }
] # vetor

@app.route("/livros", methods=["GET"])
def listar():
    return jsonify(livros)

@app.route("/livros/<int:id>", methods=["GET"]) 
def buscar(id):

    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)
    
    return jsonify({
        "Erro": "Livro nao encontrado", # erro 404 # pode ser pedido na prova
        "animacao": "animacao_livro_nao_encontrado"
    })

# Método POST

@app.route("/livros", methods=["POST"])
def cadastrar(): 

    dados = request.get_json()

    livros.append(dados)

    return jsonify({
        "Aviso": "Livro cadastrado com sucesso!",
        "Livro": dados,
        "animacao": "animacao_livro_cadastrado"
    })

# Método DELETE
@app.route('/livros', methods=['DELETE']) # Rota sem o <id>
def deletar():
    dados = request.get_json()
    id_para_deletar = dados.get('id') # Pega o ID enviado no JSON
    
    for indice, livro in enumerate(livros):
        if livro['id'] == id_para_deletar:
            livro_removido = livros.pop(indice)
            return jsonify({
                "Aviso": "Livro excluido com sucesso!",
                "Livro": livro_removido,
                "animacao": "animacao_livro_removido"
            })
            
    return jsonify({"Erro": "Livro nao encontrado"}), 404 # Tratamento de erro

# Método PUT

@app.route('/livros', methods=['PUT']) # Rota sem o <id>
def alterar():
    dados = request.get_json()

    id_para_alterar = dados.get('id') # Pega o ID enviado no JSON

    for indice, livro in enumerate(livros):
        if livro['id'] == id_para_alterar:
            # Atualiza o dicionário diretamente na lista usando o índice
            livros[indice] = dados 
            return jsonify({"mensagem": "Livro alterado com sucesso", "livro": dados, "animacao": "animacao_livro_cadastro_alterado"}), 200
    
    return jsonify({"mensagem": "Livro nao encontrado"}), 404 # Tratamento de erro # alt, shift e seta para baixo duplica a linha

if __name__ == "__main__":
    app.run(debug=True) 