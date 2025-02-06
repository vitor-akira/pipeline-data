import json
import csv

class Data:
    def __init__(self, data):
        self.data = data
        self.column_name = self.__get_columns()
        self.len_lines = self.__size_data()

    def __read_json(path):
        data_json = []
        with open(path, 'r') as file:
            data_json = json.load(file)
        return data_json

    def __read_csv(path):
        data_csv = []
        with open(path, 'r') as file:
            spamreader = (csv.DictReader(file, delimiter=',')) 
            for row in spamreader:
                data_csv.append(row) 
        return data_csv

    @classmethod
    def read_data(cls, path, data_type):
        data = []
        if data_type == 'csv':
            data = cls.__read_csv(path)
        elif data_type == 'json':
            data = cls.__read_json(path)
        
        return cls(data)
    
    def __get_columns(self):
        return list(self.data[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_data = []
        for old_dict in self.data:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)
        self.data = new_data
        self.column_name = self.__get_columns()

    def __size_data(self):
        return len(self.data)
    
    def join(dataA, dataB):
        combined_list = []
        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)

        return Data(combined_list)
    
    def __transform_data_chart(self):
        combined_data_chart = [self.column_name]

        for row in self.data:
            line = []
            for column in self.column_name:
                line.append(row.get(column, 'Indisponivel'))
            combined_data_chart.append(line)

        return combined_data_chart
    
    def save_data(self, path):
        combined_data_chart = self.__transform_data_chart()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(combined_data_chart)