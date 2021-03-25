# This script takes a list of UniProt IDs and retrieves the fasta files for each ID
# Author: Kevin Chang Wang
# Before running, create the appropriate directories and setting the current_dir variable value in main().

import os.path
import urllib.parse
import urllib.request
import pandas as pd


class ReadUniProtTable:
    def __init__(self, data_file_path, delimiter, pid_head):
        self.data_file_path = data_file_path
        self.delimiter = delimiter
        self.pid_head = pid_head
        self.data = pd.read_table(self.data_file_path, sep=self.delimiter)
        self.prot_id = self.data[self.pid_head]

    def get_uniprot_canonical_seq(self, save_path):
        unique_ids = self.prot_id.unique()
        for prot_symbol in unique_ids:
            fasta_url = "https://www.uniprot.org/uniprot/"+str(prot_symbol)+'.fasta'
            save_file_name = prot_symbol+".fasta"
            savefile_path = os.path.join(save_path, save_file_name)
            urllib.request.urlretrieve(fasta_url, savefile_path)


def main():
    current_dir = "/home/f/froth/kcwang"
    datafilepath = current_dir+"/datasets/VARITY_R_training.csv"
    delimiter = ','
    pid_head = 'p_vid'

    fasta_dir = current_dir+'/fasta_files'

    data = ReadUniProtTable(datafilepath, delimiter, pid_head)
    data.get_uniprot_canonical_seq(fasta_dir)


if __name__ == '__main__':
    main()
