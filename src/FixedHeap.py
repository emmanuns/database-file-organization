import json

class FixedSizeHeap:
    def __init__(self, record_size, filename):
        self.record_size = record_size
        self.filename = filename
        self.records = []
        self.deleted_records = []
        self.insert_count = 0  
        self.delete_count = 0  
        self.load_from_file()  

    def insert(self, record):
        if len(record) != self.record_size:
            raise ValueError("O tamanho do registro deve ser fixo.")

        if self.deleted_records:
            index = self.deleted_records.pop(0)
            self.records[index] = record
        else:
            self.records.append(record)

        self.insert_count += 1
        if self.insert_count >= 10:
            self.save_to_file()  
            self.insert_count = 0  

    def delete(self, index):
        if 0 <= index < len(self.records):
            self.records[index] = None
            self.deleted_records.append(index)
            self.delete_count += 1
            
            if self.delete_count >= 10:
                self.save_to_file() 
                self.delete_count = 0  
        else:
            raise IndexError("Índice fora do intervalo.")

    def get_record(self, index):
        if 0 <= index < len(self.records):
            return self.records[index]
        else:
            raise IndexError("Índice fora do intervalo.")

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                self.records = json.load(f)
        except FileNotFoundError:
            self.records = []

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(self.records, f)

    def compress(self):
        self.records = [record for record in self.records if record is not None]
        self.deleted_records.clear()
        self.save_to_file()  

