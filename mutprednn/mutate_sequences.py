import os.path
from Bio import SeqIO
import urllib.parse
import urllib.request
import pandas as pd
from Bio import SeqIO

class ReadVarityMutationData:
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
        for prot_symbol in self.prot_id:
            fasta_url = "https://www.uniprot.org/uniprot/"+str(prot_symbol)+'.fasta'
            save_file_name = prot_symbol+".fasta"
            savefile_path = os.path.join(save_path, save_file_name)
            urllib.request.urlretrieve(fasta_url, savefile_path)

### Need to combine the SeqIOReadSeqFile class into ReadVarityMutationData 


class SeqIOReadSeqFile:
    def __init__(self, input_file_path, file_type):
        self.input_file_path = input_file_path
        self.file_type = file_type
        self.record = SeqIO.parse(input_file_path, file_type)

    def prot_seq(self, record_index):
        record = self.record[record_index]
        return record.seq

    def prot_id(self, record_index):
        record = self.record[record_index]
        return record.id


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
