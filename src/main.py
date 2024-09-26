import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import json
from FixedHeap import FixedSizeHeap
from VariableHeap import VariableSizeHeap

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    

def test_data_structure(structure, json_name, column_size_config = None):
        with open(rf'data\{json_name}_test.json', 'r') as file:
            records = json.load(file)
        if column_size_config:
            for data_row in records:
                structure.insert(data_row, column_size_config)
        else:
            for data_row in records:
                structure.insert(data_row)
    


def main():
    config = load_config(rf'C:\Users\Antonny\Repositorio\database-file-organization\data\config.json')
    column_size = config['fixed_heap']['sizes']

    fixed_heap = FixedSizeHeap('data/fixed_heap.json')
    variable_heap = VariableSizeHeap('data/variable_heap.json')

    test_data_structure(fixed_heap, 'fixed_heap', column_size)
    test_data_structure(variable_heap, 'variable_heap')


    fixed_heap.delete(0) 
    variable_heap.delete("s1") 

    print(fixed_heap.get_record(0))  
    print(variable_heap.select("s2"))  

if __name__ == "__main__":
    main()
