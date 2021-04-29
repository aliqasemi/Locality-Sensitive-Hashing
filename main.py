from LSH import LSH
from Shingle import Shingle

path = "./DataSet"
shingle = Shingle('word')

lsh = LSH(128, shingle.searchFile(path), path)
lsh.handle()
