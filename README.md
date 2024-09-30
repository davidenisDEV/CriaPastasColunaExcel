## Projeto 1: Criador de Pastas com Condições Baseadas em Planilha Excel

### Descrição

Este script em Python utiliza a biblioteca `pandas` para ler uma planilha Excel e criar pastas automaticamente com base nas informações presentes em colunas específicas. Ele verifica o status de cada pasta antes de criá-las, evitando que pastas com o status de "bloqueada" sejam geradas.

### Funcionalidades

- Lê uma planilha Excel e extrai os dados das colunas especificadas.
- Cria pastas automaticamente com base nos valores da coluna "Nome da pasta".
- Verifica se a pasta já existe antes de tentar criá-la.
- Verifica o status da pasta e apenas cria pastas que não estejam bloqueadas.

### Estrutura de Funcionamento

1. O script lê o arquivo Excel especificado no caminho (`file_path`).
2. Para cada linha da planilha, o código extrai o nome da pasta e o status.
3. Se o status não for "bloqueada" ou estiver vazio, o script cria a pasta com o nome correspondente. Caso contrário, a pasta não será criada, e o status será informado no console.

### Exemplo de Planilha Excel

A planilha Excel deve conter pelo menos duas colunas:

| Nome da Pasta            | Status     |
|--------------------------|------------|
| pasta_cliente_1           |            |
| pasta_cliente_2           | bloqueada  |
| pasta_cliente_3           |            |

### Pré-requisitos

- Python 3.x
- Instalar dependências com:

   ```bash
   pip install pandas
   ```

### Como Usar

1. Altere o caminho do arquivo Excel no script:

   ```python
   file_path = r'C:\Seu\Caminho\Para\O\Arquivo.xlsx'
   ```

2. Execute o script:

   ```bash
   python criar_pastas.py
   ```

3. O script criará as pastas e exibirá mensagens de status no console.

### Exemplo de Saída

```
Nomes das colunas: Index(['Nome da Pasta', 'Status'], dtype='object')
Pasta "pasta_cliente_1" criada.
Pasta "pasta_cliente_2" Não foi criada. Status: "bloqueada".
Pasta "pasta_cliente_3" criada.
```

---
