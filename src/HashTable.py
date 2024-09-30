import json

class HashTable:
    def __init__(self, filename, num_buckets, bucket_size):
        self.num_buckets = num_buckets  # Número de buckets primários
        self.bucket_size = bucket_size  # Tamanho de cada bucket
        self.buckets = [[] for _ in range(num_buckets)]  # Buckets primários
        self.overflow_buckets = []  # Buckets de overflow
        if filename:
            self.load_from_file(filename)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                file = json.load(f)
                self.insert(file)
        except FileNotFoundError:
            self.records = []


    def hash_function(self, key):
        # Função hash simples usando módulo
        return hash(key) % self.num_buckets

    def insert(self, records):
        for row in records:
            key = row['show_id']
            value = {k: v for k, v in row.items() if k != 'show_id'}

            bucket_index = self.hash_function(key)
            bucket = self.buckets[bucket_index]

            # Verificar se há espaço no bucket primário
            if len(bucket) < self.bucket_size:
                bucket.append((key, value))
            else:
                # Adicionar em um bucket de overflow
                print(f"Overflow occurred for key {key}.")
                self.overflow_buckets.append((bucket_index, key, value))
        

    def delete(self, keys):
        if not isinstance(keys, list):
            keys = [keys]
        for key in keys:
            bucket_index = self.hash_function(key)
            bucket = self.buckets[bucket_index]

            # Procurar e remover do bucket primário
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    break
            
            # Procurar e remover dos buckets de overflow
            for i, (b_index, k, v) in enumerate(self.overflow_buckets):
                if b_index == bucket_index and k == key:
                    del self.overflow_buckets[i]
                    break
            
            print(f"Key {key} not found.")
            return False
        return True

    def select(self, keys = None):
        if keys is None:
            # Selecionar todos os registros
            records = []
            for bucket in self.buckets:
                for k, v in bucket:
                    records.append({**{'show_id': k}, **v})
            for b_index, k, v in self.overflow_buckets:
                records.append({**{'show_id': k}, **v})
            return records
        
        if not isinstance(keys, list):
            keys = [keys]
        
        for key in keys:
           
            bucket_index = self.hash_function(key)
            bucket = self.buckets[bucket_index]

            # Procurar no bucket primário
            result = []
            for k, v in bucket:
                if k == key:
                    result.append({**{'show_id': k}, **v})
                    break
                    
            
            # Procurar nos buckets de overflow
            for b_index, k, v in self.overflow_buckets:
                if b_index == bucket_index and k == key:
                    result.append({**{'show_id': k}, **v})
                    break
            
            print(f"Key {key} not found.")
            return None
        
        return result
            
           
