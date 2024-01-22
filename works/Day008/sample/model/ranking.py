import collections
import csv
import os
import pathlib

RANKING_COLUMN_NAME = 'NAME'
RANKING_COLUMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'

class CsvModel:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()