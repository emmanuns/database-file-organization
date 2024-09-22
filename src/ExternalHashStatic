import os
import hashlib
import pickle

class ExternalHash:
    def __init__(self, filename, num_buckets=10):
        self.filename = filename
        self.num_buckets = num_buckets
        self.bucket_size = 5  # Máximo de itens por balde
        if not os.path.exists(filename):
            self._create_empty_buckets()
        else:
            self._load_buckets()

    def _create_empty_buckets(self):
        """Cria o arquivo com buckets vazios."""
        self.buckets = [[] for _ in range(self.num_buckets)]
        self._save_buckets()

    def _load_buckets(self):
        """Carrega os buckets do arquivo."""
        with open(self.filename, 'rb') as f:
            self.buckets = pickle.load(f)

    def _save_buckets(self):
        """Salva os buckets no arquivo."""
        with open(self.filename, 'wb') as f:
            pickle.dump(self.buckets, f)

    def _hash(self, key):
        """Calcula o índice do bucket baseado no hash da chave."""
        hash_object = hashlib.sha256(key.encode())
        return int(hash_object.hexdigest(), 16) % self.num_buckets

    def insert(self, key, value):
        """Insere uma chave-valor na tabela de hash."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        # Verifica se a chave já existe
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Atualiza o valor se a chave já existir
                self._save_buckets()
                return

        # Verifica se há espaço no bucket
        if len(bucket) < self.bucket_size:
            bucket.append((key, value))
        else:
            raise OverflowError(f"Bucket {bucket_index} está cheio!")

        self._save_buckets()

    def search(self, key):
        """Procura um valor associado à chave."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Remove um par chave-valor."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._save_buckets()
                return True
        return False

    def display(self):
        """Mostra todos os buckets e seus itens."""
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")
