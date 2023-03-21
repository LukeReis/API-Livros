API de Livros
Este é um projeto de API Flask que disponibiliza a consulta, criação, edição e exclusão de livros.

Endpoints
GET /livros: retorna todos os livros cadastrados.
GET /livros/<int:id>: retorna o livro correspondente ao id informado.
PUT /livros/<int:id>: atualiza os dados do livro correspondente ao id informado.
POST /livros: adiciona um novo livro ao cadastro.
DELETE /livros/<int:id>: remove o livro correspondente ao id informado.
Recursos
Os recursos manipulados pela API são livros. Cada livro é representado por um objeto JSON com os seguintes campos:

id (int): identificador único do livro.
titulo (str): título do livro.
autor (str): nome do autor do livro.
Execução
Para executar a API, basta executar o script app.py. A API estará disponível em http://localhost:5000/.

Observações
Este é um projeto de exemplo, e não foi desenvolvido com foco em segurança ou performance.
É recomendado que seja utilizado algum sistema de autenticação para proteger os endpoints que realizam operações de escrita (POST, PUT e DELETE).
Para fins de teste, pode-se utilizar a ferramenta Postman para enviar requisições à API.
