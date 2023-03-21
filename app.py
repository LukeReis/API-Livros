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

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Hells Angel - A vida e a época de Sonny Barger e do Hells Angels Motorcycle Club',
        'autor': 'Sonny Barger'
    },
    {
        'id': 2,
        'titulo': 'A Guerra dos Tronos - A tormenta de Espadas',
        'autor': 'George R. R. Martin'
    },
    {
        'id': 3,
        'titulo': 'King of Thorns',
        'autor': 'Mark Lawrence'
    },
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


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