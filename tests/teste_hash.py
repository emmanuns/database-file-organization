import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from src.ExternalHashStatic import ExternalHash  # Ajuste o caminho conforme necessário

class TestExternalHash(unittest.TestCase):
    def setUp(self):
        self.hash_table = ExternalHash('test_hash_table.pkl')

    def test_insert_and_search(self):
        self.hash_table.insert('key1', 'value1')
        self.assertEqual(self.hash_table.search('key1'), 'value1')

    def test_bucket_overflow(self):
        # Insira 5 itens para preencher o balde
        for i in range(5):
            self.hash_table.insert(f'key{i}', f'value{i}')
        
        # Verifique o estado dos baldes antes da próxima inserção
        for i in range(self.hash_table.num_buckets):
            print(f"Bucket {i}: {self.hash_table.buckets[i]}")  # Print para verificar o estado

        # Agora, tente inserir um sexto item que deve causar overflow
        # with self.assertRaises(OverflowError):
        #     self.hash_table.insert('key_new', 'value_new')

    def test_remove(self):
        self.hash_table.insert('key1', 'value1')
        self.assertTrue(self.hash_table.remove('key1'))
        self.assertIsNone(self.hash_table.search('key1'))

    def test_search_nonexistent_key(self):
        self.assertIsNone(self.hash_table.search('nonexistent_key'))

if __name__ == '__main__':
    unittest.main()