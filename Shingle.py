import re
import glob

class Shingle:
    shingles = set()

    def __init__(self, shingle_type, shingle_number=None):
        self.shingle_type = shingle_type
        self.shingle_number = shingle_number

    def buildShingles(self, document):
        if self.shingle_type == 'word':
            text = re.sub(r'[^\w\s]', '', document)
            shingles = text.lower()
            shingles = shingles.split()
            return list(set(shingles))
        else:
            shingles = [document[i:i + self.shingle_number] for i in range(len(document))][:-self.shingle_number]
            return list(set(shingles))

    def append(self, document):
        self.shingles.update(self.buildShingles(document))
        return list(self.shingles)

    def searchFile(self, path):
        text_files = glob.glob(path + "/**/*.txt", recursive=True)
        for text_file in text_files:
            self.append(open(text_file, "r").read())

        return list(self.shingles)
