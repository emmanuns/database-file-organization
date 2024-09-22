import json
from FixedHeap import FixedSizeHeap
from VariableHeap import VariableSizeHeap

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def main():
    config = load_config('config.json')
    db_config = config['database']

    fixed_heap = FixedSizeHeap(db_config['record_size_fixed'], 'data/fixed_heap.json')
    variable_heap = VariableSizeHeap('data/variable_heap.json')

    try:
        for i in range(10):
            record_fixed = [f"record_fixed_{i}"] * db_config['record_size_fixed']
            fixed_heap.insert(record_fixed)

            record_variable = {"key": f"key_{i}", "value": f"value_{i}"}
            variable_heap.insert(record_variable)

    except ValueError as e:
        print(f"Erro ao inserir no heap fixo: {e}")

    fixed_heap.delete(0) 
    variable_heap.delete("key_0") 

    print(fixed_heap.get_record(0))  
    print(variable_heap.select("key_1"))  

if __name__ == "__main__":
    main()
