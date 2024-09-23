import unittest
import os
from src.FixedHeap import FixedSizeHeap

def generate_fixed_size_record(show_id):
    return {
        'show_id': show_id.ljust(5),
        'type': 'movie'.ljust(7),
        'title': 'Title'.ljust(100),
        'director': 'Director'.ljust(50),
        'cast': 'Cast'.ljust(150),
        'country': 'Country'.ljust(20),
        'date_added': '2023-01-01'.ljust(10),
        'release_year': '2023'.ljust(4),
        'rating': '5'.ljust(5),
        'duration': '90min'.ljust(9)
    }

class TestFixedSizeHeap(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_fixed_heap.json'
        self.heap = FixedSizeHeap(filename=self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_insert_and_get_record(self):
        record = generate_fixed_size_record('1')
        self.heap.insert(record)
        self.assertEqual(self.heap.get_record(0), self.heap.serialize_record(record))

    def test_delete_and_get_record(self):
        record = generate_fixed_size_record('2')
        self.heap.insert(record)
        self.heap.delete(0)
        self.assertIsNone(self.heap.get_record(0))

    def test_get_record_by_show_id(self):
        record = generate_fixed_size_record('3')
        self.heap.insert(record)
        found_record = self.heap.get_record_by_show_id('3')
        self.assertEqual(found_record, record)

if __name__ == '__main__':
    unittest.main()
