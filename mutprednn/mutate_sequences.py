import os.path
import urllib.parse
import urllib.request
import pandas as pd
from Bio import SeqIO


# class SeqMut:
#     def __init__(self, input_seq, position, mut_res):
#         self.input_seq = input_seq
#         self.position = position
#         self.mut_res = mut_res
#
#     def mutant(self):
#         seq = list(self.input_seq)
#         seq[self.position] = self.mut_res
#         return str(seq)
#
#     def wild_type(self):
#         return str(self.input_seq)


def main():
    datafilepath = '/home/kevinchangwang/RothLab/MutPred/datasets/VARITY_R_training.csv'
    delimiter = ','
    pid_head = 'p_vid'
    aapos_head, aaref_head, aaalt_head = 'aa_pos', 'aa_ref', 'aa_alt'
    fasta_dir = '/home/kevinchangwang/RothLab/MutPred/fasta_files'

    data = ReadMutationTable(datafilepath, delimiter, pid_head, aapos_head, aaref_head, aaalt_head)
    data.get_uniprot_canonical_seq(fasta_dir)
    print('Fasta files downloaded from UniProt located in' + fasta_dir)


if __name__ == '__main__':
    main()
