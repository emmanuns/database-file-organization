import unittest
from src.FixedHeap import FixedSizeHeap
from src.VariableHeap import VariableSizeHeap

class TestHeaps(unittest.TestCase):

    def setUp(self):
        self.fixed_heap = FixedSizeHeap(128, 'data/fixed_heap_test.json')
        self.variable_heap = VariableSizeHeap('data/variable_heap_test.json')

    def test_fixed_heap_insert(self):
        record = ['data'] * 128  # Registro fixo
        self.fixed_heap.insert(record)
        self.assertEqual(len(self.fixed_heap.records), 1)

    def test_variable_heap_insert(self):
        record = {"key": "test_key", "value": "test_value"}
        self.variable_heap.insert(record)
        self.assertEqual(len(self.variable_heap.records), 1)

    def test_fixed_heap_delete(self):
        record = ['data'] * 128
        self.fixed_heap.insert(record)
        self.fixed_heap.delete(0)
        self.assertEqual(len(self.fixed_heap.records), 1) 

    def test_variable_heap_delete(self):
        record = {"key": "test_key", "value": "test_value"}
        self.variable_heap.insert(record)
        self.variable_heap.delete("test_key")
        self.assertEqual(len(self.variable_heap.records), 1)

if __name__ == "__main__":
    unittest.main()
