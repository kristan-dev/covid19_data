import pandas as pd
import io
from itertools import islice
import logging
from src.config import cfg
import src.logger


class CSVParser:  
    @classmethod
    def parse_csv_from_file(cls, file_name):

        flag = True
        logging.info("Processing Dataframe as chunks")
        for chunk in pd.read_csv(file_name,chunksize=1000000,delimiter=",",keep_default_na=False,):
            if flag is True:
                keys = chunk.columns.to_list()
                flag = False
            for row in chunk.iterrows():
                yield cls.form_data(keys=keys, value=row)

    @staticmethod
    def form_data(keys, value):
        value = value[1]
        data = {}
        for key in keys:
            data[key] = value[key]
        return data


if __name__ == "__main__":
    # csv_rows = CSVParser.parse_csv()
    # batch_size = 10000
    # while True:
    #   rows =list(islice(csv_rows, 0, batch_size))
    #   if len(rows) <= 0:
    #       break
    pass
