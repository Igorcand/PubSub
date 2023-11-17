# PubSub #

## QUESTÃO 1: ##

### SOBRE ###
O código do roteamento de mensagens foi desenvolvido utilizando 3 classes, uma servindo como Publisher, na qual envia a mensagem para as pessoas inscritas em seu canal, outra como Subscriber, ou seja, a pessoa que deseja receber as mensagens enviadas pelos Publishers, e tambem a classe Gateway, que serve como um roteamento de mensagens para as respectivas filas. Foi utilizado um arquivo json como banco de dados para salvar as mensagens enviadas por tipo de fila.
Caso fosse permitido o uso de tecnologias externas, utilizaria o redis como fila para processaras requisições e salvar num banco de dados MongoDB.
O projeto foi desenvolvidos sem muitos problemas, e os testes foram criados sem o uso de biblioteca externa.

### COMO RODAR O CÓDIGO ###
```bash
# Fazer o clone do repositório
git clone https://github.com/Igorcand/PubSub.git

# Entrar na pasta
cd PubSub/

# Executar o código
python run.py

```

![Image](./img/run.png)

Ao executar o exemplo, poderá analisar que existem 3 subscribers que receberam as mensagens (Eduardo, Maria e José) enviadas pelos Publishers (Cifra Club e Palco MP3) as respectiavs mensagens 'É o maior site de ensino de música do Brasil' e 'É o maior serviço de música independente do Brasil' 


### COMO RODAR OS TESTES ###
```bash
# Fazer o clone do repositório
git clone https://github.com/Igorcand/PubSub.git

# Entrar na pasta
cd PubSub/

# Rodar os testes de Publisher
python test_publisher.py

# Rodar os testes de Subscriber
python test_subscriber.py

# Rodar os testes de Gateway
python test_gateway.py

```

Ao executar os testes, se todos estiverem corretos, exibirá um print na tela escrito "All gateway tests were successful", caso haja erro, irá mostrar um erro no terminal

OBS: Existem melhores formas de criar testes unitários utilizando a biblioteca Pytest e a UniTest, porém, está na regra do desafio que é proibido utilizar bibliotecas externas.

## QUESTÃO 2: ##

### QUESTÃO 2.1 ###
As tabelas "Books", "Books_rating" e "Books_comments" são componentes de um banco de dados robusto e o fato de essas tabelas possuírem relacionamentos many-to-many com outras tabelas mostra a necessidade de otimização de consultas para um desempenho eficiente. Para aprimorar a eficiência das consultas nessas tabelas, a implementação de índices se torna uma estratégia essencial. 

Ao considerar a cardinalidade das tabelas, observamos que os relacionamentos many-to-many implicam em uma multiplicidade de registros associados entre as tabelas, ou seja, os registros das tabelas se referenciam entre si. O uso de índices em colunas que representam esses relacionamentos pode resultar em boas melhoras. A expectativa ao implementar índices nessas tabelas é a redução do tempo de resposta das consultas, especialmente aquelas que envolvem junções complexas e filtros. Quando os índices são aplicados as colunas, o mecanismo do banco de dados pode localizar registros de maneira mais eficiente, diminuindo a necessidade de percorrer grandes linhas de dados.


### QUESTÃO 2.2 ###
Para otimizar a consulta fornecida, que busca registros na tabela books onde released_at está entre '2015-01-01 00:00:01' e o momento atual, existem várias medidas que podem ser tomadas para reduzir o subset e agilizar a execução. Aqui estão algumas sugestões:

- Criar um índice na coluna released_at para facilitar a busca por registros que satisfaçam a condição de intervalo. 

- Considerar o particionamento da tabela com base na coluna released_at. Permitindo que o banco de dados ignore partições que não contêm dados relevantes para a consulta.

- Se a consulta é executada frequentemente, considerar o uso de cache para armazenar resultados de consultas anteriores e evitar a reexecução da consulta quando os mesmos resultados são necessários.

### QUESTÃO 2.3 ###
Algumas medidas de otimização para o contexto do banco de dados, considerando a query fornecida:

Índices Adequados:
    Pro: Melhora a velocidade de pesquisa.
    Contra: Pode aumentar o custo de inserção, atualização e exclusão. Pode consumir mais espaço em disco.

Utilização de Cache de Resultados:
    Pro: Evita a execução da consulta se os resultados não foram alterados desde a última execução.
    Contra: Requer lógica adicional para gerenciar o cache, e os resultados podem ficar desatualizados.

Particionamento de Tabelas:
    Pro: Pode melhorar o desempenho de consultas que envolvem grandes volumes de dados.
    Contra: A implementação do particionamento pode ser complexa e pode não ser eficaz em todas as situações.


## QUESTÃO 3: ##
Para atender os requisitios e realizar uma query no banco com milhoes de linhas, seria necessário algumas modificações, como:

- Adicionar um sistema de cache para armazenar os históricos mais recentes em memória, 
- Fazer uma indexação adequada para otimizar a busca de históricos.
- Particionar a tabela para não ficar muito grandepara distribuir os dados.



## QUESTÃO 4: ##

Analisando o cenário proposto, existem potenciais vulnerabilidades de segurança que podem ser identificadas:

-  Falta de autenticação na visualização de boletos, então qualquer pessoa poder acessar um boleto apenas através do link, sem autenticação, pode ter vulnerabilidades. Isso significa que, qualquer pessoa que tenha o link pode visualizar informações sensíveis como CPF e endereço, gerando exposição indevida de informações pessoais e financeiras dos clientes, violação de privacidade. Com isso, deve implementar uma autenticação para acessar os boletos, seja por meio de login no site ou por um token seguro no link. Isso garantirá que apenas usuários autorizados tenham acesso aos boletos.

- Falta de controle de acesso de como o sistema controla o acesso aos boletos. Se não existir um controle, é possível que um usuário mal-intencionado consiga acessar boletos de outros clientes, manipulando o parâmetro 'id' nos endpoint e acessando informações confidenciais de outros clientes. Para resolver isso deve implementar um sistema, garantindo que cada cliente só possa acessar os boletos associados à sua conta.

- Falta de criptografia na comunicação entre o cliente e o servidor. Se a comunicação não for criptografada, as informações podem ser interceptadas por terceiros durante a transmissão. Por isso, deve implementar SSL/TLS para criptografar a comunicação entre o cliente e o servidor, garantindo a segurança dos dados durante a transmissão.

## QUESTÃO 5: ##

![Image](./img/db_relations.png)

Relacionamentos:

- Aluno - Matrícula (Relacionamento 1 para 1): Um aluno pode ter no máximo uma matrícula, e uma matrícula pertence a apenas um aluno.
- Professor - Disciplina (Relacionamento Muitos para Muitos): Um professor pode lecionar várias disciplinas, e uma disciplina pode ser lecionada por vários professores.
- Turma - Disciplina (Relacionamento Muitos para 1): Uma turma está associada a apenas uma disciplina, mas uma disciplina pode ter várias turmas.
- Nota - Aluno (Relacionamento Muitos para Muitos): Um aluno pode ter várias notas, e uma nota está associada a vários alunos (pode ser uma nota coletiva para toda a turma).
- Nota - Disciplina (Relacionamento Muitos para 1): Uma nota está associada a apenas uma disciplina, mas uma disciplina pode ter várias notas (notas de diferentes avaliações).
- Presença - Aluno (Relacionamento Muitos para Muitos): Um aluno pode ter várias presenças registradas, e uma presença está associada a vários alunos (pode ser uma presença coletiva para toda a turma).
- Presença - Turma (Relacionamento 1 para Muitos): Uma presença está associada a apenas uma turma, mas uma turma pode ter várias presenças registradas em diferentes datas.


## QUESTÃO 6: ##

O bloco de código mostra um método chamado 'Find' que pertence a uma estrutura ou tipo de dados Repository, e esse método recebe alguns parâmetros, como:

- ctx, do tipo contextContext
- id, do tipo string
- table, string
- transaction, do tipo Transaction, opcional

O método controi uma consulta SQL usando a função fmt.Sprintf para formatar a string da consulta. Dependendo da transação, se for bem sucedida ou não, a consulta éexecutada usando a transação ou uma 
uma conexão de leitura padrão. O método verifica se houve algum erro ao escanear a linha resultante da consulta para a estrutura entity usando row.StructScan(&entity). Se ocorrer um erro, o método verifica se é um erro indicando que a consulta não retornou resultados (stdsql.ErrNoRows). Se for esse o caso, o método retorna nil, nil, indicando que a entidade não foi encontrada. Caso contrário, o método retorna nil, err. Se a consulta for bem-sucedida, o método retorna um ponteiro para a entidade recuperada e nil para o erro.


Possíveis problemas no código:
- Segurança contra Injeção de SQL: O código utiliza a concatenação de strings para construir a consulta SQL, o que pode ser propenso a ataques de injeção de SQL. Recomenda-se o uso de parâmetros de consulta preparados ou a função Queryx de sqlx que lida automaticamente com isso.

- Tratamento de Erros: O código assume que qualquer erro durante o StructScan é devido à ausência de linhas (ErrNoRows). No entanto, outros erros também podem ocorrer, e seria útil logar ou lidar de forma diferente com esses erros para uma melhor depuração.

- Conversão de ID para String na Consulta SQL: A concatenação direta de id na string da consulta SQL pode resultar em problemas se id não for uma string. Deve-se garantir que id seja convertido corretamente para uma string na consulta SQL.

- Gestão de Conexão: O método usa uma conexão de leitura padrão se não for fornecida uma transação. A gestão de conexões pode ser complexa, e seria útil garantir que as conexões sejam adequadamente abertas e fechadas para evitar vazamentos de recursos.

