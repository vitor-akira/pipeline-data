import json
import csv

class Data:
    def __init__(self, path, data_type):
        self.path = path
        self.data_type = data_type
        self.data = self.read_data()
        self.column_name = self.get_columns()
        self.len_lines = self.size_data()

    def read_json(self):
        data_json = []
        with open(self.path, 'r') as file:
            data_json = json.load(file)
        return data_json

    def read_csv(self):
        data_csv = []
        with open(self.path, 'r') as file:
            spamreader = (csv.DictReader(file, delimiter=',')) 
            for row in spamreader:
                data_csv.append(row) 
        return data_csv

    def read_data(self):
        data = []
        if self.data_type == 'csv':
            data = self.read_csv()
        elif self.data_type == 'json':
            data = self.read_json()
        elif self.data_type == 'list':
            data = self.path
            self.path = 'list in memory'
        
        return data
    
    def get_columns(self):
        return list(self.data[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_data = []
        for old_dict in self.data:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)
        self.data = new_data
        self.column_name = self.get_columns()

    def size_data(self):
        return len(self.data)
    
    def join(dataA, dataB):
        combined_list = []
        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)

        return Data(combined_list, 'list')
    
    def transform_data_chart(self):
        combined_data_chart = [self.column_name]

        for row in self.data:
            line = []
            for column in self.column_name:
                line.append(row.get(column, 'Indisponivel'))
            combined_data_chart.append(line)

        return combined_data_chart
    
    def save_data(self, path):
        combined_data_chart = self.transform_data_chart()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(combined_data_chart)