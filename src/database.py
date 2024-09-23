import csv
from OrderedFile import OrderedFile 

class NetflixDatabase:
    def __init__(self, csv_file, record_size_fixed):
        self.csv_file = csv_file
        self.ordered_file = OrderedFile(record_size_fixed)
        self.load_data()

    def load_data(self):
        with open(self.csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = [
                    row['show_id'],
                    row['type'],
                    row['title'],
                    row['director'],
                    row['cast'],
                    row['country'],
                    row['date_added'],
                    row['release_year'],
                    row['rating'],
                    row['duration']
                ]
                self.ordered_file.insert(record)

    def get_record(self, index):
        return self.ordered_file.get_record(index)
