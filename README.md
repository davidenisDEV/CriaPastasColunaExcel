Criador de Pastas com Condições Baseadas em Planilha Excel

Este script em Python utiliza a biblioteca pandas para ler uma planilha Excel e criar pastas automaticamente com base nas informações presentes em colunas específicas. Ele verifica o status de cada pasta antes de criá-las, evitando que pastas com o status de "bloqueada" sejam geradas.
Funcionalidades

    Lê uma planilha Excel e extrai os dados das colunas especificadas.
    Cria pastas automaticamente com base nos valores da coluna "Nome da pasta".
    Verifica se a pasta já existe antes de tentar criá-la.
    Verifica o status da pasta, e apenas cria pastas que não estejam bloqueadas.

Como Funciona

O script utiliza as seguintes colunas do arquivo Excel:

    Nome da pasta: Nome que será utilizado para criar a pasta.
    Status da pasta: Define se a pasta pode ser criada ou não. Se o status for "bloqueada", a pasta não será gerada.

Estrutura de Funcionamento

    O script lê o arquivo Excel especificado no caminho (file_path).
    Para cada linha da planilha, o código extrai o nome da pasta e o status.
    Se o status não for "bloqueada" ou estiver vazio, o script cria a pasta com o nome correspondente. Caso contrário, a pasta não será criada, e o status será informado no console.

Exemplo de Planilha Excel

A planilha Excel que o script espera deve conter pelo menos duas colunas:
Nome da Pasta	Status
pasta_cliente_1	
pasta_cliente_2	bloqueada
pasta_cliente_3	

    Nome da Pasta: Nome da pasta a ser criada no sistema.
    Status: Caso o status seja "bloqueada", a pasta não será criada.

Pré-requisitos

    Python 3.x
    Pandas (pip install pandas)

Como Usar

    Instale as dependências:

    bash

pip install pandas

Modifique o caminho do arquivo Excel no script, na linha:

python

file_path = r'C:\Seu\Caminho\Para\O\Arquivo.xlsx'

Execute o script:

bash

    python criar_pastas.py

    O script irá ler o arquivo Excel, criar as pastas e exibir as mensagens no console conforme o status das pastas.

Exemplo de Saída

css

Nomes das colunas: Index(['Nome da Pasta', 'Status'], dtype='object')
Pasta "pasta_cliente_1" criada.
Pasta "pasta_cliente_2" Não foi criada. Status: "bloqueada".
Pasta "pasta_cliente_3" criada.

Personalizações

    Você pode personalizar os nomes das colunas na planilha Excel ajustando as referências às colunas no código, como row['Nome da Pasta'] e row['Status'].
    Para adicionar mais condições para a criação das pastas, basta modificar a lógica dentro do loop for.

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um Pull Request ou relatar problemas.
