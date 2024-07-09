<h1>Automatização de Cadastro de Produtos</h1>


<h2>Este projeto utiliza Python junto com as bibliotecas Pandas, PyAutoGUI e Time para automatizar o cadastro de produtos em um sistema web.</h2>

<h2>#Passos do Projeto#</h2>

<h3>Passo 1: Acesso ao Sistema da Empresa</h3>
Para iniciar o processo de automação, o script acessa o sistema da empresa através da seguinte URL:

https://dlp.hashtagtreinamentos.com/python/intensivao/login

<h3>Passo 2: Login no Sistema</h3>
Após acessar a URL, o script realiza o login utilizando as credenciais fornecidas:

Usuário: guilherme.dev@gmail.com
Senha: gui123

<h3>Passo 3: Importação da Base de Dados</h3>
O script importa a base de dados de produtos a partir de um arquivo CSV localizado em E:/Programacao/semanapython/automacao/produtos.csv.

<h3>Passo 4: Cadastro de Produtos</h3>
Para cada linha na tabela de produtos, o script realiza o seguinte procedimento:

<h4>Insere o código do produto.</h4>
<h4>Insere a marca.</h4>
<h4>Insere o tipo do produto.</h4>
<h4>Insere a categoria.</h4>
<h4>Insere o preço unitário.</h4>
<h4>Insere o custo do produto.</h4>
<h4>Insere observações, se aplicável.</h4>
<h4>Clica no botão de enviar para cadastrar o produto.</h4>
<h3>Passo 5: Repetição para Todos os Produtos</h3>
O processo de cadastro é repetido para todos os produtos listados na base de dados.

<h1>Bibliotecas Utilizadas</h1>
Pandas: Utilizado para a leitura e manipulação dos dados do arquivo CSV.
PyAutoGUI: Utilizado para automatizar interações com o teclado e o mouse.
Time: Utilizado para pausas entre as operações, garantindo que o sistema web possa responder adequadamente.


<h1>Para executar o script:</h1>

<h3>Clone este repositório.</h3>
<h3>Instale as bibliotecas necessárias utilizando o comando:</h3>
<h3>Copiar código</h3>
<h3>pip install pandas pyautogui</h3>
<h3>Execute o script Python:</h3>
<h3>Copiar código</h3>
<h3>python nome_do_script.py</h3>
<h3>Certifique-se de ajustar as coordenadas de clique (pyautogui.click(x, y)) de acordo com a sua tela e sistema operacional para garantir o funcionamento correto da automação.</h3>

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias através de pull requests.
