from json import load
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import time
from FixedHeap import FixedSizeHeap
from OrderedFile import OrderedFile
import pandas as pd

def load_records():
    data = pd.read_csv('data\Database_with_Name_and_Index.csv')
    print(data)
    return [tuple(row) for row in data.values]
    

class PerformanceTest:
    def __init__(self, record_count, record_size):
        self.record_count = record_count
        self.record_size = record_size
        self.records = load_records()
    
    def test_insertion(self, structure):
        start_time = time.time()
        for record in self.records:
            structure.insert(record)
        end_time = time.time()
        return end_time - start_time
    
    def test_search(self, structure):
        start_time = time.time()
        for i in [0, self.record_count // 2, self.record_count - 1]:
            structure.get_record(i)
        end_time = time.time()
        return end_time - start_time

    def test_deletion(self, structure):
        start_time = time.time()
        for i in [0, self.record_count // 2, self.record_count - 1]:
            structure.delete(i)
        end_time = time.time()
        return end_time - start_time
    
    def run_tests(self, structures):
        results = {}
        for name, structure in structures.items():
            print(f"Testing {name}...")
            results[name] = {
                'Insertion Time': self.test_insertion(structure),
                'Search Time': self.test_search(structure),
                'Deletion Time': self.test_deletion(structure)
            }
        return results

record_count = 10  
record_size = 100    

heap_fixed = FixedSizeHeap(record_size, "file")
orderred_file = OrderedFile(record_size)


structures = {
    'Heap Fixo': heap_fixed,
    "Ordered File": orderred_file
}

performance_test = PerformanceTest(record_count, record_size)
results = performance_test.run_tests(structures)

for structure, metrics in results.items():
    print(f"Resultados para {structure}:")
    for metric, time_taken in metrics.items():
        print(f"  {metric}: {time_taken:.4f} segundos")
