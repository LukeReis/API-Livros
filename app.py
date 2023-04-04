
from flask import Flask, jsonify, request
import json


app = Flask(__name__)


def carregar_livros():
    global arquivo
    with open("livrojson.json", "r+") as arquivo:
        global livros
        livros = json.load(arquivo)
    return jsonify(livros)

# Consultar (todos)


@app.route('/livros', methods=['GET'])
def obter_livros():
    carregar_livros()
    return carregar_livros()

# Consultar(id)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    carregar_livros()
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'erro': 'livro nao encontrado'})

# Editar


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    carregar_livros()

    livro_encontrado = False
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            livro_encontrado = True
            break

    if livro_encontrado:
        with open("livrojson.json", "w") as arquivo:
            json.dump(livros, arquivo, indent=4)
            return jsonify(livros[indice])
    else:
        return jsonify({'erro', 'livro não encontrado'})

# Criar


@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    carregar_livros()

    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)

    with open("livrojson.json", "w") as arquivo:
        json.dump(livros, arquivo, indent=4)

    return jsonify(livros)

# Excluir


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    carregar_livros()
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            with open("livrojson.json", "w")as arquivo:
                json.dump(livros, arquivo, indent=4)
            # informa ao Flask para nao manter o arquivo .json em cache
            app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
            return jsonify(livros)
    return jsonify({'erro': 'livro nao encontrado'})


app.run(port=5000, host='localhost', debug=True)
