import os
import sys
import time
import json
from FixedHeap import FixedSizeHeap
from VariableHeap import VariableSizeHeap
from OrderedFile import OrderedFile
from HashTable import HashTable

# Add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# Constants for file paths
CONFIG_PATH = r'data\config.json'
INITIAL_DATA_PATH = r'data\initial_data.json'
TEST_DATA_PATH = r'data\test_data.json'

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time, result

def test_fixed_heap(data, column_sizes, delete_keys, select_keys, insert_data):
    print("==== TESTE HEAP FIXO ====\n")
    fixed_heap = FixedSizeHeap(INITIAL_DATA_PATH)
    
    insert_time, data_ids = measure_time(fixed_heap.insert, data, column_sizes)
    print(f"Tempo de inserção no heap fixo (4615 registros): {insert_time:.6f} segundos.")
    delete_time, _ = measure_time(fixed_heap.delete, delete_keys)
    print(f"Tempo de deleção no heap fixo (200 registros): {delete_time:.6f} segundos")
    select_time, result = measure_time(fixed_heap.select, select_keys)
    print(f"Tempo de select no heap fixo(200 registros): {select_time:.6f} segundos.")
    print()

    insert_time, data_ids = measure_time(fixed_heap.insert, insert_data, column_sizes)
    print(f"Tempo de inserção no heap fixo (1 registro): {insert_time:.6f} segundos.")

    delete_time, _ = measure_time(fixed_heap.delete, 's1')
    print(f"Tempo de deleção no heap fixo (1 registro): {delete_time:.6f} segundos")

    select_time, result = measure_time(fixed_heap.select, 's2')
    print(f"Tempo de select no heap fixo (1 registro): {select_time:.6f} segundos.")

    select_time, result = measure_time(fixed_heap.select)
    print(f"Tempo de select no heap fixo (select all): {select_time:.6f} segundos.")

def test_variable_heap(data, delete_keys, select_keys, insert_data):
    print("\n==== TESTE HEAP VARIÁVEL ====\n")
    variable_heap = VariableSizeHeap(INITIAL_DATA_PATH)
    
    insert_time, result = measure_time(variable_heap.insert, data)
    print(f"Tempo de inserção no heap variável (4615): {insert_time:.6f} segundos")
    delete_time, result = measure_time(variable_heap.delete, delete_keys)
    print(f"Tempo de deleção no heap variável (200 registros): {delete_time:.6f} segundos")
    select_time, result = measure_time(variable_heap.select, select_keys)
    print(f"Tempo de seleção no heap variável (200 registros): {select_time:.6f} segundos")

    insert_time, result = measure_time(variable_heap.insert, insert_data)
    print(f"Tempo de inserção no heap variável (1 registro): {insert_time:.6f} segundos")
    delete_time, result = measure_time(variable_heap.delete, "s1")
    print(f"Tempo de deleção no heap variável (1 registro): {delete_time:.6f} segundos")
    select_time, result = measure_time(variable_heap.select, "s2")
    print(f"Tempo de seleção no heap variável (1 registro): {select_time:.6f} segundos")
    select_time, result = measure_time(variable_heap.select)
    print(f"Tempo de seleção no heap variável (select all): {select_time:.6f} segundos")

def test_ordered_file(data, column_sizes, delete_keys, select_keys, insert_data):
    print("\n==== TESTE ARQUIVO ORDENADO ====\n")
    ordered_file = OrderedFile(INITIAL_DATA_PATH)
    
    insert_time, result = measure_time(ordered_file.insert, data, column_sizes)
    print(f"Tempo de inserção no arquivo ordenado (4615 registros): {insert_time:.6f} segundos")
    delete_time, result = measure_time(ordered_file.delete, delete_keys)
    print(f"Tempo de deleção no arquivo ordenado (200 registros): {delete_time:.6f} segundos")
    select_time, result = measure_time(ordered_file.select, select_keys)
    print(f"Tempo de seleção no arquivo ordenado (200 registros): {select_time:.6f} segundos")

    insert_time, result = measure_time(ordered_file.insert, insert_data, column_sizes)
    print(f"Tempo de inserção no arquivo ordenado (1 registro): {insert_time:.6f} segundos")
    delete_time, result = measure_time(ordered_file.delete, "s1")
    print(f"Tempo de deleção no arquivo ordenado (1 registro): {delete_time:.6f} segundos")
    select_time, result = measure_time(ordered_file.select, "s2")
    print(f"Tempo de seleção no arquivo ordenado (1 registro): {select_time:.6f} segundos")
    select_time, result = measure_time(ordered_file.select)
    print(f"Tempo de seleção no arquivo ordenado (select all): {select_time:.6f} segundos")

def test_hash_table(data, delete_keys, select_keys, insert_data):
    print("\n==== TESTE Static Hash ====\n")
    hash_table = HashTable(filename=INITIAL_DATA_PATH, num_buckets=10000, bucket_size=100)
    
    insert_time, result = measure_time(hash_table.insert, data)
    print(f"Tempo de inserção no hash estático (4615 registros): {insert_time:.6f} segundos")
    delete_time, result = measure_time(hash_table.delete, delete_keys)
    print(f"Tempo de deleção no hash estático (200 registros): {delete_time:.6f} segundos")
    select_time, result = measure_time(hash_table.select, select_keys)
    print(f"Tempo de seleção no hash estático (200 registros): {select_time:.6f} segundos")

    insert_time, result = measure_time(hash_table.insert, insert_data)
    print(f"Tempo de inserção no hash estático (1 registro): {insert_time:.6f} segundos")
    delete_time, result = measure_time(hash_table.delete, "s1")
    print(f"Tempo de deleção no hash estático (1 registro): {delete_time:.6f} segundos")
    select_time, result = measure_time(hash_table.select, "s2")
    print(f"Tempo de seleção no hash estático (1 registro): {select_time:.6f} segundos")

    select_time, result = measure_time(hash_table.select)
    print(f"Tempo de seleção no hash estático (select all): {select_time:.6f} segundos")

def main():
    config = load_config(CONFIG_PATH)
    column_sizes = config['data_sizes']['sizes']
    delete_keys = config['delete_keys']
    select_keys = config['select_keys']
    insert_data = config['insert_data']
    test_data = load_data(TEST_DATA_PATH)

    print("---- TESTE DE DESEMPENHO ----\n")
    
    test_fixed_heap(test_data, column_sizes, delete_keys, select_keys, insert_data)
    test_variable_heap(test_data, delete_keys, select_keys, insert_data)
    test_ordered_file(test_data, column_sizes, delete_keys, select_keys, insert_data)
    test_hash_table(test_data, delete_keys, select_keys, insert_data)

if __name__ == "__main__":
    main()