import os.path
import urllib.parse
import urllib.request
import pandas as pd
from Bio import SeqIO

class

class SeqMut:
    def __init__(self, input_seq, position, mut_res):
        self.input_seq = input_seq
        self.position = position
        self.mut_res = mut_res

    def mutant(self):
        seq = list(self.input_seq)
        seq[self.position] = self.mut_res
        return str(seq)

    def wild_type(self):
        return str(self.input_seq)


def main():
    pass


if __name__ == '__main__':
    main()
