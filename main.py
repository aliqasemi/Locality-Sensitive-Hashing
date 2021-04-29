from LSH import LSH
from Shingle import Shingle

path = "./DataSet"
shingle = Shingle('word')

lsh = LSH(128, shingle.searchFile(path))
print(lsh.buildMatrix(path))

# arr = {}
# arr.update({"d": [1, 1, 0 , 1]})
# arr.update({"s": [1, 1, 0 , 1]})
# arr.update({"s": [1, 1, 0 , 1]})
#
# for (key, value) in arr.items():
#     print(key, value)
