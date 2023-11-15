# PubSub #

## QUESTÃO 1: ##

O código da questão 1 está feito no proprio repositório, com funcionalidade e testes prontos

## QUESTÃO 2: ##

...

## QUESTÃO 3: ##
Para atender aos requisitos não funcionais mencionados, algumas modificações significativas devem ser feitas no sistema. Aqui estão algumas sugestões:

Introdução de Cache:
    Implementar um sistema de cache para armazenar os históricos mais recentes em memória. Isso permitirá que a funcionalidade de histórico seja acessada mesmo quando o banco de dados estiver offline. O cache pode ser implementado usando uma solução de armazenamento em memória, como Redis.

Event Sourcing ou Log de Mudanças:
    Manter um log de mudanças ou usar o padrão de Event Sourcing para registrar todas as alterações nos históricos. Isso permite reconstruir o estado atual do histórico mesmo que o banco de dados esteja offline. As operações de leitura podem ser otimizadas lendo do log em vez de consultar diretamente o banco de dados.

Indexação Adequada:
    Garantir que o banco de dados esteja devidamente indexado para otimizar a busca de históricos. Considere a possibilidade de indexar campos relevantes para consulta, como user_id e news_id. Isso pode ajudar a reduzir o tempo de busca.

Particionamento da Tabela:
    Se a tabela de histórico estiver ficando muito grande, considere implementar um esquema de particionamento. Isso pode ajudar a distribuir os dados de maneira mais eficiente e melhorar o desempenho das consultas.

Replicação de Dados:
    Utilizar replicação de dados para garantir a disponibilidade mesmo em caso de falha de um nó do banco de dados. Isso ajudará a atender à exigência de que nenhuma visita seja perdida no cenário de indisponibilidade dos sistemas de armazenamento.

Tuning do Banco de Dados:
    Realizar otimizações específicas para o banco de dados em uso. Dependendo do banco de dados escolhido, ajustes de configuração, como tamanho de buffer, caches e índices, podem ser ajustados para melhorar o desempenho. 

Implementação de um Serviço de Busca Rápida:
    Criar um serviço dedicado para buscar rapidamente os históricos. Esse serviço pode ser otimizado para atender à exigência de tempo de latência inferior a 10ms em 80% dos casos.

Monitoramento Contínuo:
    Implementar um sistema robusto de monitoramento para rastrear o desempenho do sistema em tempo real. Isso ajudará a identificar gargalos e problemas de desempenho rapidamente. Como o prometheus e o grafana, podem coletar métricas do banco de dados e criar paineis de monitoramento e deshboards personalizados

Essas sugestões visam abordar os requisitos não funcionais, garantindo que a funcionalidade de histórico seja resistente a falhas, responsiva e atenda às expectativas dos usuários. É importante realizar testes extensivos após a implementação dessas modificações para validar o desempenho do sistema.


## QUESTÃO 4: ##

Analisando o cenário proposto, há algumas potenciais vulnerabilidades de segurança que podem ser identificadas:

Falta de Autenticação na Visualização de Boletos:
    Problema: O fato de qualquer pessoa poder acessar um boleto apenas através do link, sem autenticação, pode representar uma vulnerabilidade. Isso significa que qualquer pessoa que tenha o link pode visualizar boletos de terceiros, incluindo informações sensíveis como CPF e endereço.
    Possíveis danos: Exposição indevida de informações pessoais e financeiras dos clientes, violação de privacidade.

Solução Proposta:
    Implementar autenticação para acessar os boletos, seja por meio de login no site ou por um token seguro no link. Isso garantirá que apenas usuários autorizados tenham acesso aos boletos.

Falta de Controle de Acesso:
    Problema: Não há indicação de como o sistema controla o acesso aos boletos. Se não houver um controle adequado, é possível que um usuário mal-intencionado consiga acessar boletos de outros clientes, manipulando o parâmetro 'id' nos endpoints.
    Possíveis danos: Acesso não autorizado a informações confidenciais de outros clientes.

Solução Proposta:
    Implementar um sistema robusto de controle de acesso, garantindo que cada cliente só possa acessar os boletos associados à sua conta. Isso pode ser feito por meio de identificação e validação da sessão do usuário.

Exposição de Informações Sensíveis nos Logs de Requisição:
    Problema: Se as informações sensíveis, como CPF e endereço, estiverem presentes nos logs de requisição, eles podem ser alvo de acesso não autorizado ou vazamento de dados.
    Possíveis danos: Divulgação indevida de informações sensíveis.

Solução Proposta:
    Certificar-se de que as informações sensíveis não são registradas nos logs. Caso necessário, implementar técnicas de logging seguro, como a remoção ou mascaramento automático de dados sensíveis.

Falta de Criptografia na Comunicação:
    Problema: Não há menção à segurança na comunicação entre o cliente e o servidor. Se a comunicação não for criptografada, as informações podem ser interceptadas por terceiros mal-intencionados.
    Possíveis danos: Interceptação de dados confidenciais durante a transmissão.

Solução Proposta:
    Implementar SSL/TLS para criptografar a comunicação entre o cliente e o servidor, garantindo a segurança dos dados durante a transmissão.

É crucial realizar uma auditoria de segurança abrangente, incluindo testes de penetração e revisões de código, para identificar e corrigir outras possíveis vulnerabilidades. Além disso, é importante manter o sistema e as práticas de segurança atualizadas para mitigar novas ameaças.

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

