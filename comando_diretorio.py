import os

import pandas as pd

# Obter o diretório atual (pasta "scripts")
diretorio_atual = os.getcwd()

# Combinar os diretórios da "pasta mãe", dos "dados" (ou nome que estiver) e o arquivo CSV
caminho_pasta_mae = os.path.abspath(os.path.join(diretorio_atual, ".."))
caminho_pasta_dados = os.path.join(caminho_pasta_mae, "dados")
caminho_arquivo = os.path.join(caminho_pasta_dados, "nome_do_arquivo.csv")

# Carregar a base de dados
base = pd.read_csv(caminho_arquivo)
base.shape
