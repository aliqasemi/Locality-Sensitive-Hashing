import glob


class LSH:
    document_sort = []

    def __init__(self, num_permutation, shingles):
        self.num_permutation = num_permutation
        self.shingles = shingles

    def buildMatrix(self, path):
        shingle_array = {}
        for shingle in self.shingles:
            text_files = glob.glob(path + "/**/*.txt", recursive=True)
            exist_array = []
            for text_file in text_files:

                if len(self.document_sort) < len(text_files):
                    self.document_sort.append(open(text_file, "r").name)

                document = open(text_file, "r").read()
                if shingle in document:
                    exist_array.append(1)
                else:
                    exist_array.append(0)
            shingle_array.update({shingle: exist_array})

        return shingle_array
