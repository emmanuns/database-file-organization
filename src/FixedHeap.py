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
        """Insere um registro no heap fixo."""
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
        """Remove um registro pelo índice e marca como excluído."""
        if 0 <= index < len(self.records):
            self.records[index] = None
            self.deleted_records.append(index)
            self.delete_count += 1
            
            if self.delete_count >= 10:
                self.compress()  # Pode ser uma boa ideia
                self.save_to_file() 
                self.delete_count = 0  
        else:
            raise IndexError("Índice fora do intervalo.")

    def get_record(self, index):
        """Obtém um registro pelo índice."""
        if 0 <= index < len(self.records):
            return self.records[index]
        else:
            raise IndexError("Índice fora do intervalo.")
        
    def get_record_by_show_id(self, show_id):
        """Obtém um registro pelo show_id."""
        for record in self.records:
            if record is not None and record[0:5].strip() == show_id:
                return self.deserialize_record(record)
        return None

    def load_from_file(self):
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

    def serialize_record(self, record):
        return (f"{record['show_id']:<5}"               # show_id: máximo 5 caracteres
                f"{record['type']:<7}"                # type: máximo 7 caracteres
                f"{record['title']:<100}"             # title: máximo 100 caracteres
                f"{record['director']:<50}"           # director: máximo 50 caracteres
                f"{record['cast']:<150}"               # cast: máximo 150 caracteres (reduzido)
                f"{record['country']:<20}"            # country: máximo 20 caracteres
                f"{record['date_added']:<10}"         # date_added: fixo (10 caracteres)
                f"{record['release_year']:<4}"        # release_year: fixo (4 caracteres)
                f"{record['rating']:<5}"               # rating: máximo 5 caracteres
                f"{record['duration']:<9}")            # duration: máximo 9 caracteres


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

