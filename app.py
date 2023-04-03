# 1. Objetivo - Criar uma API que disponibiliza a consulta, criacao, edicao e exclusao de livros
# 2. URL base - localhost
# 3. Endpoints - 
    # - localhost/livros (GET)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros (POST)
    # - localhost/livros/id (DELETE)

# 4. Quais os recursos - Livros


from flask import Flask, jsonify, request
import json


app = Flask(__name__)

with open("livrojson.json", "r") as arquivo:
    for linha in arquivo:
        try:
            livros = json.load(arquivo)
        except json.decoder.JSONDecodeError:
            print('Erro ao decodificar objeto JSON')

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    with open ("livrojson.json", "r") as arquivo:
        livros = json.load(arquivo)
    return jsonify(livros)


# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livros)


# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    
# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)