from LSH import LSH
from Shingle import Shingle

path = "./DataSet"
shingle = Shingle('word')

lsh = LSH(128, shingle.searchFile(path))
lsh.buildMatrix(path)

lsh.buildSignatures()


# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# arr[1][0] = 5
# print(arr)

# arr = {}
# arr.update({"d": [1, 1, 0 , 1]})
# arr.update({"s": [1, 1, 0 , 1]})
# arr.update({"s": [1, 1, 0 , 1]})
#
# for (key, value) in arr.items():
#     print(key, value)
