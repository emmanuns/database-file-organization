import json

class FixedSizeHeap:
    def __init__(self, record_size=400, filename='data/fixed_heap.json'):
        self.record_size = record_size
        self.filename = filename
        self.records = []
        self.deleted_records = []
        self.insert_count = 0  
        self.delete_count = 0  
        self.load_from_file()  

    def insert(self, record):
        serialized_record = self.serialize_record(record)
        if len(serialized_record) != self.record_size:
            raise ValueError("O tamanho do registro deve ser fixo.")

        if self.deleted_records:
            index = self.deleted_records.pop(0)
            self.records[index] = serialized_record
        else:
            self.records.append(serialized_record)

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
        
    def get_record_by_show_id(self, show_id):
        for record in self.records:
            if record is not None and record[0:5].strip() == show_id:
                return self.deserialize_record(record)
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
        self.deleted_records.clear()
        self.save_to_file()  

    def serialize_record(self, record):
        return (f"{record['show_id']:<5}"              # show_id: máximo 5 caracteres
                f"{record['type']:<7}"               # type: máximo 7 caracteres
                f"{record['title']:<100}"            # title: sem limite específico
                f"{record['director']:<50}"          # director: sem limite específico
                f"{record['cast']:<200}"             # cast: sem limite específico
                f"{record['country']:<20}"           # country: máximo 20 caracteres
                f"{record['date_added']:<10}"        # date_added: fixo
                f"{record['release_year']:<4}"       # release_year: fixo
                f"{record['rating']:<5}"              # rating: máximo 5 caracteres
                f"{record['duration']:<9}")           # duration: máximo 7 caracteres se filme, 9 se tv show

    def deserialize_record(self, serialized_record):
        return {
            'show_id': serialized_record[0:5].strip(),
            'type': serialized_record[5:12].strip(),
            'title': serialized_record[12:112].strip(),
            'director': serialized_record[112:162].strip(),
            'cast': serialized_record[162:362].strip(),
            'country': serialized_record[362:382].strip(),
            'date_added': serialized_record[382:392].strip(),
            'release_year': serialized_record[392:396].strip(),
            'rating': serialized_record[396:401].strip(),
            'duration': serialized_record[401:410].strip(),
        }
