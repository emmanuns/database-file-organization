class OrderedFile:
    def __init__(self, record_size):
        self.record_size = record_size
        self.main_file = []
        self.extension_file = []
        self.deleted_marks = []

    def insert(self, record):
        if len(record) != self.record_size:
            raise ValueError("O tamanho do registro deve ser fixo.")
        self.extension_file.append(record)
        if len(self.extension_file) >= 5:  
            self.reorganize()

    def delete(self, index):
        if 0 <= index < len(self.main_file):
            self.main_file[index] = None
            self.deleted_marks.append(index)
        else:
            raise IndexError("Índice fora do intervalo.")

    def reorganize(self):
        self.main_file += self.extension_file
        self.main_file = sorted([r for r in self.main_file if r is not None])
        self.extension_file = []

    def get_record(self, index):
        if 0 <= index < len(self.main_file):
            return self.main_file[index]
        else:
            raise IndexError("Índice fora do intervalo.")
