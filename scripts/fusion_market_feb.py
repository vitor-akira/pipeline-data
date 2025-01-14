from data_process import Data

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# extract
data_A = Data(path_json, 'json')
print(f"Dados empresa A: {data_A.column_name}")
print(f"Quantia de itens: {data_A.len_lines}")

data_B = Data(path_csv, 'csv')
print(f"Dados empresa B: {data_B.column_name}")
print(f"Quantia de itens: {data_B.len_lines}")

# transform
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque':  'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

data_B.rename_columns(key_mapping)
print(f"Dados A∩B: {data_B.column_name}")

fusion_data = Data.join(data_A, data_B)
print(fusion_data.column_name)
print(fusion_data.len_lines)

# load 
path_data_combined = 'data_processed/data_combined.csv'
fusion_data.save_data(path_data_combined)
print(path_data_combined)

