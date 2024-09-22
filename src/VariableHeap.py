import json

class VariableSizeHeap:
    def __init__(self, filename):
        self.records = []
        self.deleted_indices = []
        self.insert_count = 0  
        self.delete_count = 0  
        self.filename = filename
        self.load_from_file()  

    def insert(self, record):
        if self.deleted_indices:
            index = self.deleted_indices.pop(0)
            self.records[index] = record
        else:
            self.records.append(record)

        self.insert_count += 1
        if self.insert_count >= 10:
            self.save_to_file()  
            self.insert_count = 0  

    def delete(self, key):
        for i, record in enumerate(self.records):
            if record is not None and record.get('key') == key:
                self.records[i] = None
                self.deleted_indices.append(i)
                self.delete_count += 1
                
                if self.delete_count >= 10:
                    self.save_to_file()  
                    self.delete_count = 0 
                return True
        return False

    def select(self, key):
        for record in self.records:
            if record is not None and record.get('key') == key:
                return record
        return None 

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
        self.deleted_indices.clear()
        self.save_to_file() 

    def __str__(self):
        return str(self.records)
