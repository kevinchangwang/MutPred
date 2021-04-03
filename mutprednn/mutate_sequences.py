import os.path
import urllib.parse
import urllib.request
import pandas as pd
from Bio import SeqIO
import csv

class WriteMutationSeqTable:
    def __init__(self, mutation_data_path, file_type, delimiter, pid_head, aa_pos_head, aa_wt_head, aa_mut_head):
        self.mutation_data_path = mutation_data_path
        self.file_type = file_type
        self.delimiter = delimiter
        self.pid_head = pid_head
        self.aa_pos_head = aa_pos_head
        self.aa_wt_head = aa_wt_head
        self.aa_mut_head = aa_mut_head
        self.data = pd.read_table(self.mutation_data_path, sep=self.delimiter)
        self.pid = self.data[self.pid_head]
        self.aapos = self.data[self.aa_pos_head]
        self.aawt = self.data[self.aa_wt_head]
        self.aamut = self.data[self.aa_mut_head]

    def mutate_fasta_seq(self, concatenated_fasta_file_path):
        fastas = SeqIO.parse(concatenated_fasta_file_path, "fasta")
        return fastas

    def write_row(self, output_file_path):
        pass








def main():
    pass


if __name__ == '__main__':
    main()
