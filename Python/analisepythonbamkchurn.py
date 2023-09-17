# -*- coding: utf-8 -*-
"""AnalisePythonBamkChurn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dlCYy-jv8KhsShrO0q24WwZWPfl_hDfx

- Passo 1: Importar a base de dados;
- Passo 2: Visualizar e tratar a base de dados;
- Passo 3: Olhar os dados para ter um panorama geral dos dados;
- Passo 4: Construir uma análise para identificar o motivo de cancelamento;
- Identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito.
"""

# Importa o conteúdo do Google Drive
from google.colab import drive
drive.mount('/content/drive')

"""#Tratamento de valores vazios e exibição do resumo das colunas da base de dados"""

# Importa a biblioteca Pandas com alias "pd"
import pandas as pd

# Lê o arquivo .csv e atribui o alias "tabela"
tabela = pd.read_csv("/content/BankChurners.csv")

# Faz o dop da Coluna (axis=1) "CLIENTNUM"
tabela = tabela.drop("CLIENTNUM", axis=1)

#Exibe a tabela
display(tabela)

# Renomeia o nome das colunas
tabela = tabela.rename(columns={'Attrition_Flag': 'Categoria',
                                'Customer_Age': 'Idade',
                                'Gender' :'Sexo',
                                'Dependent_count' : 'Dependentes',
                                'Education_Level' : 'Educacao',
                                'Marital_Status' : 'Estado_Civil',
                                'Income_Category' : 'Faixa_Salarial',
                                'Card_Category' : 'Categoria_do_Cartao',
                                'Months_on_book' : 'Meses_Como_Cliente',
                                'Total_Relationship_Count' : 'Produtos_Contratados',
                                'Months_Inactive_12_mon' : 'Inatividade_12m',
                                'Contacts_Count_12_mon' : 'Contatos_12m',
                                'Credit_Limit' : 'Limite_de_Credito',
                                'Total_Revolving_Bal' : 'Limite_Consumido',
                                'Avg_Open_To_Buy' : 'Limite_Disponivel',
                                'Total_Trans_Amt' : 'Valor_Transacoes_12m',
                                'Total_Trans_Ct' : 'Qtde_Transacoes_12m',
                                'Avg_Utilization_Ratio' : 'Taxa_de_Utilizacao_do_Cartao'
                                })

# Exibe o nome de todas as colunas da tabela d arquivo .csv
print(tabela.columns)

"""Análise das Colunas:

- Categoria - Attrition_Flag: Informa se o cliente ainda está com o cartão ativo ou se já cancelou o cartão;
- Idade - Customer_Age: Idade da pessoa;
- Sexo - Gender;
- Dependentes - Dependent_count: Informa o número de dependentes do cliente;
- Educacao - Education_Level: Nível de formação educacional dos clientes;
- Estado Civil - Marital_Status;
- Faixa Salarial - Income_Category: Informa o salário anual do cliente;
- Categoria do Cartao - Card_Category;
- Meses como Cliente - Months_on_book: Informa há quanto tempo a pessoa é cliente;
- Produtos Contratados - Total_Relationship_Count: Informa quantos produtos o cliente possui;
- Inatividade 12m - Months_Inactive_12_mon: Quanto tempo o cliente ficou inativo nos últimos 12 meses;
- Contatos 12m - Contacts_Count_12_mon: Quantos contatos o cliente fez com a instituição nos últimos 12 meses;
- Limite de Credito - Credit_Limit;
- Limite Consumido - Total_Revolving_Bal;
- Limite Disponivel - Avg_Open_To_Buy;
- Valor Transacoes 12m - Total_Trans_Amt: Valor das transações nos últimos 12 meses;
- Qtde Transacoes 12m - Total_Trans_Ct: Quantidade de transações feitas nos últimos 12 meses;
- Taxa de Utilizacao do Cartao - Avg_Utilization_Ratio: Média com um score de 0 a 1.
"""

# Exclui os valores vazios da tabela
tabela = tabela.dropna()

# Informações gerais sobre a tabela
display(tabela.info())

# Método Pandas que descreve a tabela e arredonda para uma casa decimal
display(tabela.describe().round(2))

display(tabela)

"""# Avaliar a divisão entre Clientes X Cancelados"""

# Contar valores da coluna Categoria em Quantidade
qtde_categoria = tabela["Categoria"].value_counts()
display(qtde_categoria)

# Contar valores da coluna Categoria em Porcentagem
qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
display(qtde_categoria_perc)

"""# Há várias maneiras de descobrir o motivo de cancelamento:
- Podemos olhar a comparação entre Clientes e Cancelados em cada uma das colunas da nossa base de dados, para verificar se essa informação traz algum novo insight;
- Verificar as principais causas: Pareto 80/20
"""

# Biblioteca do Python para exibição de gráficos
import plotly.express as px

# Exibir o gráfico com parâmetros de cor, com base na quantidade de clientes
grafico = px.histogram(tabela, x='Idade', color="Categoria")
grafico.show()

# For para exibir dados de diversas colunas da tabela - for linha in tabela.index
for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria") # Exibir o gráfico com parâmetros de cor
  grafico.show()

"""# Apontamentos da Análise;
- Quanto maior o número de produtos contratados, menor a chance de cancelamento;
- Quanto maior o número de transações efetuadas pelo cliente, menor a chance de cancelamento;
- Quanto maior o valor das transações efetuadas pelo cliente, menor a chance de cancelamento;
- Quanto maior a quantidade de contatos que o cliente efetua com a instituição, maiores as chances de cancelamento;
"""