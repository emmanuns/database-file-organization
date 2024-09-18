class Header:
    def __init__(self, table_name, record_count, block_size):
        self.table_name = table_name
        self.record_count = record_count
        self.block_size = block_size
        self.deleted_pointer = None

class FixedRecord:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Heap:
    def __init__(self, block_size):
        self.records = []
        self.block_size = block_size
        self.header = Header("Alunos", 0, block_size)

    def insert(self, record):
        self.records.append(record)
        self.header.record_count += 1

    def select(self, key):
        for record in self.records:
            if record.key == key:
                return record
        return None

    def delete(self, key):
        for record in self.records:
            if record.key == key:
                self.records.remove(record)
                self.header.record_count -= 1
                return