import os
import hashlib
import pickle

class Bucket:
    def __init__(self, bucket_size):
        self.elements = []
        self.overflow = []
        self.bucket_size = bucket_size
    
    def insert(self, key, value):
        if len(self.elements) < self.bucket_size:
            self.elements.append((key, value))
        else:
            self.overflow.append((key, value))

class ExternalHashStatic:
    def __init__(self, num_buckets:int, bucket_size:int):
        self.num_buckets = num_buckets
        self.bucket_size = bucket_size
        self.buckets = [Bucket(bucket_size) for _ in range(num_buckets)]

    def hash_function(self, key):
        if type(key) == str:
            key = len(key)
        return key % self.num_buckets

    def insert(self, key, value):
        index = self.hash_function(key)
        self.buckets[index].insert(key, value)

    def remove(self, key):
        index = self.hash_function(key)
        for i in self.buckets:
            for j, (k, v) in enumerate(i.elements):
                if k == key:
                    del self.buckets[j]
                    return True
        return False

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket.elements:
            if k == key:
                return v
        for k, v in bucket.overflow:
            if k == key:
                return v
        return None

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket.elements}, Overflow: {bucket.overflow}")
