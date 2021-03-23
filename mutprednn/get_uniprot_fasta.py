import os.path
import urllib.parse
import urllib.request
import pandas as pd


class ReadMutationTable:
    def __init__(self, data_file_path, delimiter, pid_head, aapos_head, aaref_head, aaalt_head):
        self.data_file_path = data_file_path
        self.delimiter = delimiter
        self.pid_head = pid_head
        self.aapos_head = aapos_head
        self.aaref_head = aaref_head
        self.aaalt_head = aaalt_head
        self.data = pd.read_table(self.data_file_path, sep=self.delimiter)
        self.prot_id = self.data[self.pid_head]
        self.aa_pos = self.data[self.aapos_head]
        self.aa_ref = self.data[self.aaref_head]
        self.aa_alt = self.data[self.aaalt_head]

    def get_uniprot_canonical_seq(self, save_path):
        unique_ids = self.prot_id.unique()
        for prot_symbol in unique_ids:
            fasta_url = "https://www.uniprot.org/uniprot/"+str(prot_symbol)+'.fasta'
            save_file_name = prot_symbol+".fasta"
            savefile_path = os.path.join(save_path, save_file_name)
            urllib.request.urlretrieve(fasta_url, savefile_path)

#Set current directory and make sure that the correct subdirectories are present.
#/datasets for the .csv containing protein ids and /fasta_files for the retrieved sequence files.


def main():
    current_dir = "/home/f/froth/kcwang"
    datafilepath = current_dir+"/datasets/VARITY_R_training.csv"
    delimiter = ','
    pid_head = 'p_vid'
    aapos_head, aaref_head, aaalt_head = 'aa_pos', 'aa_ref', 'aa_alt'
    fasta_dir = current_dir+'/fasta_files'

    data = ReadMutationTable(datafilepath, delimiter, pid_head, aapos_head, aaref_head, aaalt_head)
    data.get_uniprot_canonical_seq(fasta_dir)


if __name__ == '__main__':
    main()
