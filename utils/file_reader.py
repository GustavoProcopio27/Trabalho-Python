from os import listdir
from os.path import join, isfile
class Reader:

    @staticmethod
    def read_csv(year:int):
        path=f"data/{year}" 
        for file in listdir(path):
            full_path=join(path,file)
            if not isfile(full_path):
                raise IOError()
            with open(file=full_path,mode="r",encoding="latin-1") as f:
                print(f.readlines())
