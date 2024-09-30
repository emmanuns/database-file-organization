import csv
import json

class OrderedFile:
    def __init__(self, filename=None):
        self.main_file = []
        self.deleted_records = []
        self.extension_file = []
        self.deleted_extension_records = []
        
        if filename:
            self.load_from_file(filename)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                file = json.load(f)
                self.main_file.append(file)
        except FileNotFoundError:
            self.records = []

    def insert(self, records, column_size):
        data_ids = []
        for record in records:
            record = self.serialize_record(record)
            for key, value in record.items():
                if len(value) > column_size[key]:
                    raise ValueError(f"O dado '{value}' é maior que o tamanho permitido {column_size[key]} e possui {len(value)} caracteres")
            if self.deleted_extension_records:
                index = self.deleted_extension_records.pop(0)
                self.extension_file[index] = record
            else:
                self.extension_file.append(record)
            data_ids.append(record['show_id'])
    
            if len(self.extension_file) >= 500 and None not in self.extension_file:  
                self.reorganize()
        return data_ids

    def delete(self, indexes):
        if not isinstance(indexes, list):
            indexes = [indexes]
        
        if self.extension_file:
            for file_idx, record in enumerate(self.extension_file):
                if record is not None and record['show_id'].strip() in indexes:
                    self.extension_file[file_idx] = None
                    self.deleted_extension_records.append(file_idx)
            return True
        for main_idx, records in enumerate(self.main_file):
            for file_idx, record in enumerate(records):
                if record is not None and record['show_id'].strip() in indexes:
                    self.main_file[main_idx][file_idx] = None
                    self.deleted_records.append((main_idx, file_idx))
                    self.deleted_records = sorted(self.deleted_records)
        return True
        
    def reorganize(self):
        self.main_file.append(self.extension_file)
        def get_min_show_id(sublist):
            return min(sublist, key=lambda record: record['show_id'])['show_id'] if sublist else 'z' * 10

        self.main_file = sorted(self.main_file, key=get_min_show_id)
        self.extension_file = []
        self.deleted_extension_records = []
        self.deleted_records = []
        return self.main_file

    def select(self, index = None):
        if index is None:
            return self.main_file
        if not isinstance(index, list):
            index = [index]
        result = []
        """Seleciona um registro pelo índice."""
        for records in self.main_file:
            for record in records:
                if record is not None and record['show_id'].strip() in index:
                    result.append(record)
        return result
    
    def truncate_string(self, data, max_length):
        if data is None:
            return ""
        if len(data) > max_length:
            return data[:max_length]
        return data
    
    def serialize_record(self, record):
        return {'show_id': f"{self.truncate_string(str(record['show_id']), 5):<5}",
                'type': f"{self.truncate_string(str(record['type']), 7):<7}",  
                'title': f"{self.truncate_string(str(record['title']), 100):<100}",
                'director': f"{self.truncate_string(str(record['director']), 50):<50}",
                'cast': f"{self.truncate_string(str(record['cast']), 150):<150}",
                'country': f"{self.truncate_string(str(record['country']), 20):<20}",
                'date_added': f"{self.truncate_string(record['date_added'], 10):<10}", 
                'release_year': f"{self.truncate_string(str(record['release_year']), 4):<4}", 
                'rating':f"{self.truncate_string(str(record['rating']), 5):<5}", 
                'duration': f"{self.truncate_string(str(record['duration']), 9):<9}"
        }    