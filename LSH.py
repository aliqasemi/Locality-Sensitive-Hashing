import glob
import random
import numpy as np
from itertools import combinations


class LSH:
    def __init__(self, num_permutation, shingles, path):
        self.num_permutation = num_permutation
        self.shingles = shingles
        self.path = path
        self.signatures = np.full((self.num_permutation, len(self.document_sort)), "******************")

    document_sort = []
    matrix = set()

    def handle(self):
        self.buildMatrix(self.path)
        self.buildSignatures()
        self.similarity()
        self.combinations()

    def buildMatrix(self, path):
        shingle_array = {}
        for shingle in self.shingles:
            text_files = glob.glob(path + "/**/*.txt", recursive=True)
            exist_array = []
            for text_file in text_files:

                if len(self.document_sort) < len(text_files):
                    self.document_sort.append(open(text_file, "r").name)

                document = open(text_file, "r").read()
                if shingle in document.lower():
                    exist_array.append(1)
                else:
                    exist_array.append(0)
            shingle_array.update({shingle: exist_array})

        self.signatures = np.full((self.num_permutation, len(self.document_sort)), "******************")
        self.matrix = shingle_array

        return shingle_array

    def buildSignatures(self):

        permuteMatrix = self.matrix
        for permute in range(self.num_permutation):
            for x in range(0, len(self.document_sort)):
                for (item, value) in permuteMatrix.items():
                    if value[x] == 1:
                        position_row = permute
                        position_col = x
                        self.signatures[position_row][position_col] = item
                        position = [int(len(self.document_sort) * position_row + position_col)]
                        np.put(self.signatures, position, item)
                        break

            lists = list(permuteMatrix.items())
            random.shuffle(lists)
            permuteMatrix = dict(lists)

        return self.signatures

    def similarity(self):
        print(self.signatures)
        print(self.document_sort)

        for item in self.signatures:
            print(item)

    def combinations(self):
        iterate = [i for i in range(1, len(self.document_sort) + 1)]
        comb = combinations(iterate, 2)

        combines = list()

        for i in list(comb):
            combines.append(i)

        print(combines)

        return combines