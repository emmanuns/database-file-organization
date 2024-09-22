import unittest
from VariableHeap import VariableSizeHeap  

class TestVariableSizeHeap(unittest.TestCase):

    def setUp(self):
        self.heap = VariableSizeHeap()

    def test_insert_and_select(self):
        for i in range(25):
            self.heap.insert({'key': f'{i:03}', 'value': f'Registro {i}'})

        for i in range(25):
            record = self.heap.select(f'{i:03}')
            self.assertEqual(record, {'key': f'{i:03}', 'value': f'Registro {i}'})

    def test_delete(self):
        for i in range(10):
            self.heap.insert({'key': f'{i:03}', 'value': f'Registro {i}'})

        self.heap.delete('003')
        self.assertIsNone(self.heap.select('003'))

        for i in range(10):
            if i != 3:
                record = self.heap.select(f'{i:03}')
                self.assertEqual(record, {'key': f'{i:03}', 'value': f'Registro {i}'})

    def test_compress(self):
        for i in range(10):
            self.heap.insert({'key': f'{i:03}', 'value': f'Registro {i}'})
        self.heap.delete('003')
        self.heap.delete('007')

        self.heap.compress()

        for i in range(10):
            if i in [3, 7]:
                self.assertIsNone(self.heap.select(f'{i:03}'))
            else:
                self.assertEqual(self.heap.select(f'{i:03}'), {'key': f'{i:03}', 'value': f'Registro {i}'})

if __name__ == '__main__':
    unittest.main()
