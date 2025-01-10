import json
import csv

def read_json(path_json):
    data_json = []
    with open(path_json, 'r') as file:
        data_json = json.load(file)
    return data_json

def read_csv(path_csv):
    data_csv = []
    with open(path_csv, 'r') as file:
        spamreader = (csv.DictReader(file, delimiter=',')) 
        for row in spamreader:
            data_csv.append(row) 
    return data_csv

def read_data(path, archive_type):
    data = []
    if archive_type == 'csv':
        data = read_csv(path)
    elif archive_type == 'json':
        data = read_json(path)

    return data

def get_columns(data):
    return list(data[-1].keys())

def rename_columns(data, key_mapping):
    new_data_csv = []

    # processo de passar por cada um dos dados:
    # old_dict são os dados atualmente, pegando um dicionario antigo a cada um dos registros que existe no data_csv ele vai 
    # pegar o dicionario e vai passar por cada uma das chaves, copiando os dados e criando uma nova coluna.
    for old_dict in data:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_data_csv.append(dict_temp)
    
    return new_data_csv

def size_data(data):
    return len(data)

def join(dataA, dataB):
    combined_list = []
    combined_list.extend(dataA)
    combined_list.extend(dataB)
    return combined_list

def transform_data_chart(data, column_names):
    combined_data_chart = [column_names]

    for row in data:
        line = []
        for column in column_names:
            line.append(row.get(column, 'Indisponivel'))
        combined_data_chart.append(line)

    return combined_data_chart

    path_json = 'data_raw/dados_empresaA.json'
    path_csv = 'data_raw/dados_empresaB.csv'

def save_data(data, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# iniciando a leitura
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

data_json = read_data(path_json, 'json')
column_name_json = get_columns(data_json)
data_size_json = size_data(data_json)
print(f"Column name JSON: {column_name_json}")
print(f"JSON size: {data_size_json}")

data_csv = read_data(path_csv, 'csv')
column_name_csv = get_columns(data_csv)
data_size_csv = size_data(data_csv)
print(f"Column name CSV: {column_name_csv}")
print(f"CSV size: {data_size_csv}")

# transformação dos dados
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque':  'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

data_csv = rename_columns(data_csv, key_mapping)
column_name_csv = get_columns(data_csv)
print(column_name_csv)

data_fusion = join(data_json,data_csv)
column_name_fusion = get_columns(data_fusion)
data_size_fusion = size_data(data_fusion)
print(column_name_fusion)
print(data_size_fusion)

# salvando dados
data_fusion_chart = transform_data_chart(data_fusion, column_name_fusion)

path_data_combined = 'data_processed/data_combined.csv'

save_data(data_fusion_chart, path_data_combined)

print(path_data_combined)