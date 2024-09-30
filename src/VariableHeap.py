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
        for row in record:
            if self.deleted_indices:
                index = self.deleted_indices.pop(0)
                self.records[index] = row
            else:
                self.records.append(row)
            
            self.insert_count += 1
            if self.insert_count >= 10:
                self.save_to_file()  
                self.insert_count = 0  

    
    def delete(self, keys):
        if not isinstance(keys, list):
            keys = [keys]
        
        for i, record in enumerate(self.records):
            if record is not None and record.get('show_id') in keys:
                self.records[i] = None
                self.deleted_indices.append(i)
                self.delete_count += 1
        
        return True
    

    def select(self, keys = None):
        if keys is None:
            return self.records
        if not isinstance(keys, int):
            keys = [keys]
        result = []
        for record in self.records:
            if record is not None and record.get('show_id') in keys:
                result.append(record)
        return result


    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                self.records = json.load(f)
                #transformar em dict
                #self.records = [dict(record) for record in self.records]

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
