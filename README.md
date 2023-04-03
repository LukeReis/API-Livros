# API RESTful de Livros
Este é um programa em Python que usa o framework Flask para implementar uma API RESTful para gerenciamento de livros. A API permite criar, editar, excluir e obter informações sobre livros.

O programa lê informações sobre os livros de um arquivo JSON chamado "livrojson.json". O arquivo contém uma lista de objetos JSON, onde cada objeto representa um livro e contém informações como título, autor e ID.

Abaixo estão as rotas disponíveis na API e o que cada uma faz:

# Consultar (todos)
/livros (Método GET)

Retorna todos os livros armazenados no arquivo "livrojson.json" em formato JSON.

# Consultar por ID
/livros/<int:id> (Método GET)

Retorna as informações do livro com o ID especificado no parâmetro <id>. Se não houver um livro com esse ID, retorna um erro 404.

# Editar
/livros/<int:id> (Método PUT)

Atualiza as informações do livro com o ID especificado no parâmetro <id>. As informações atualizadas são passadas no corpo da requisição em formato JSON. Se não houver um livro com esse ID, retorna um erro 404.

# Criar
/livros (Método POST)

Adiciona um novo livro com as informações passadas no corpo da requisição em formato JSON. O ID do livro é gerado automaticamente e adicionado ao arquivo "livrojson.json".

# Excluir
/livros/<int:id> (Método DELETE)

Remove o livro com o ID especificado no parâmetro <id> do arquivo "livrojson.json". Se não houver um livro com esse ID, retorna um erro 404.

# Executando o Programa
O programa é executado ao chamar o método run do objeto app do Flask. Ao executar o programa, um servidor web é iniciado na porta 5000 do host local.

Para testar a API, você pode usar ferramentas como o curl ou o Postman. Por exemplo, para obter todos os livros, você pode fazer uma requisição GET para a rota /livros. Para adicionar um novo livro, você pode fazer uma requisição POST para a rota /livros com as informações do livro no corpo da requisição em formato JSON.

# Observação 
É importante salientar que a implementação não inclui tratamento de autenticação ou autorização, o que pode ser uma preocupação de segurança, caso a API seja exposta na internet ou acesse informações sensíveis.
