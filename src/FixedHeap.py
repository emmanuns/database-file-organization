import json

class FixedSizeHeap:
    def __init__(self, filename='data/fixed_heap.json'):
        self.filename = filename
        self.records = []
        self.deleted_records = []
        self.insert_count = 0  
        self.delete_count = 0  
        self.load_from_file()  

    def insert(self, records, column_size):
        """Insere um registro no heap fixo."""
        data_ids = []
        for record in records:
            record = self.serialize_record(record)
            for key, value in record.items():
                if len(value) > column_size[key]:
                    raise ValueError(f"O dado '{value}' é maior que o tamanho permitido {column_size[key]} e possui {len(value)} caracteres")
            if self.deleted_records:
                index = self.deleted_records.pop(0)
                self.records[index] = record
            else:
                self.records.append(record)

            self.insert_count += 1
            if self.insert_count >= 10:
                self.save_to_file()  
                self.insert_count = 0 
            data_ids.append(record['show_id'])
        
        return data_ids
             

    def delete(self, indexes):
        if not isinstance(indexes, list):
            indexes = [indexes]
        """Remove um registro pelo índice e marca como excluído."""
        for record in self.records:
            if record is not None and record['show_id'].strip() in indexes:
                record_index = self.records.index(record)
                self.records[record_index] = None
                self.deleted_records.append(record_index)
                self.delete_count += 1
                
                if self.delete_count >= 10:
                    self.compress()  
                    self.save_to_file()  
                    self.delete_count = 0
        return
        
    def select(self, index = None):
        if index is None:
            return self.records
        if not isinstance(index, list):
            index = [index]
        result = []
        """Seleciona um registro pelo índice."""
        for record in self.records:
            if record is not None and record['show_id'].strip() in index:
                result.append(record)
        return result
        
    def get_record_by_show_id(self, show_id):
        """Obtém um registro pelo show_id."""
        for record in self.records:
            if record is not None and record[0:5].strip() == show_id:
                return self.deserialize_record(record)
        return None

    def load_from_file(self, filename=None):
        """Carrega registros de um arquivo JSON."""
        try:
            with open(self.filename, 'r') as f:
                self.records = json.load(f)
        except FileNotFoundError:
            self.records = []

    def save_to_file(self):
        """Salva registros em um arquivo JSON."""
        with open(self.filename, 'w') as f:
            json.dump(self.records, f)

    def compress(self):
        """Compacta registros excluídos e limpa a lista de registros excluídos."""
        self.records = [record for record in self.records if record is not None]
        self.deleted_records.clear()
        self.save_to_file()  

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

    def deserialize_record(self, serialized_record):
        return {
            'show_id': serialized_record[0:5].strip(),
            'type': serialized_record[5:12].strip(),
            'title': serialized_record[12:112].strip(),
            'director': serialized_record[112:162].strip(),
            'cast': serialized_record[162:312].strip(),  # Ajustado para 150 caracteres
            'country': serialized_record[312:332].strip(),  # Ajustado para 20 caracteres
            'date_added': serialized_record[332:342].strip(),  # Ajustado para 10 caracteres
            'release_year': serialized_record[342:346].strip(),  # Ajustado para 4 caracteres
            'rating': serialized_record[346:351].strip(),  # Ajustado para 5 caracteres
            'duration': serialized_record[351:360].strip(),  # Ajustado para 9 caracteres
        }

