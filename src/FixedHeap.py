class FixedSizeHeap:
    def __init__(self, record_size):
        self.record_size = record_size
        self.records = []
        self.deleted_records = []

    def insert(self, record):
        # if len(record) != self.record_size:
        #     raise ValueError("O tamanho do registro deve ser fixo.")
        if self.deleted_records:
            index = self.deleted_records.pop(0)
            self.records[index] = record
        else:
            self.records.append(record)

    def delete(self, index):
        if 0 <= index < len(self.records):
            self.records[index] = None  
            self.deleted_records.append(index)
        else:
            raise IndexError("Índice fora do intervalo.")

    def get_record(self, index):
        if 0 <= index < len(self.records):
            return self.records[index]
        else:
            raise IndexError("Índice fora do intervalo.")

