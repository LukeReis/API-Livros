# API Rest de Gerenciamento de Livros
Este é um programa escrito em Python que implementa uma API RESTful para gerenciamento de livros em formato JSON. A API permite que um cliente faça as seguintes operações:

Consultar todos os livros
Consultar um livro por ID
Editar um livro por ID
Incluir um novo livro
Excluir um livro por ID
Tecnologias utilizadas
O programa utiliza a biblioteca Flask para a criação da API RESTful. A biblioteca json é utilizada para lidar com o formato JSON.

# Estrutura do programa
O programa é composto por uma função principal carregar_livros() que carrega os dados do arquivo JSON "livrojson.json" e os retorna em formato JSON.

A função obter_livros() é associada à rota "/livros" e permite que o cliente consulte todos os livros da biblioteca.

A função obter_livro_por_id(id) é associada à rota "/livros/int:id" e permite que o cliente consulte um livro específico através de seu ID.

A função editar_livro_por_id(id) é associada à rota "/livros/int:id" e permite que o cliente edite um livro específico através de seu ID.

A função incluir_novo_livro() é associada à rota "/livros" e permite que o cliente inclua um novo livro na biblioteca.

A função excluir_livro(id) é associada à rota "/livros/int:id" e permite que o cliente exclua um livro específico da biblioteca.

O programa é executado através da chamada app.run(port=5000, host='localhost', debug=True).

# Utilização
O programa pode ser executado a partir do terminal com o comando python nome_do_arquivo.py. Em seguida, o cliente pode fazer requisições HTTP para a API através de um cliente REST, como o Postman.

Para consultar todos os livros, deve-se enviar uma requisição GET para a rota "/livros". Para consultar um livro específico, deve-se enviar uma requisição GET para a rota "/livros/int:id", substituindo <int:id> pelo ID do livro desejado.

Para editar um livro, deve-se enviar uma requisição PUT para a rota "/livros/int:id", substituindo <int:id> pelo ID do livro a ser editado e incluindo as informações do livro a serem alteradas no corpo da requisição em formato JSON.

Para incluir um novo livro, deve-se enviar uma requisição POST para a rota "/livros" com as informações do novo livro no corpo da requisição em formato JSON.

Para excluir um livro, deve-se enviar uma requisição DELETE para a rota "/livros/int:id", substituindo <int:id> pelo ID do livro a ser excluído.

# Observações
O arquivo "livrojson.json" deve estar presente no mesmo diretório do programa.
A API está configurada para executar na porta 5000 e no endereço "localhost", mas essas configurações podem ser alteradas de acordo com a necessidade. O parâmetro "debug=True" permite a exibição de mensagens de debug no terminal.
