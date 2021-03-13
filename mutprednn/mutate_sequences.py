import Bio
import urllib.parse
import urllib.request
from Bio import SeqIO


class GetUniProtData:
    url = "https://www.uniprot.org/uploadlists/"
    params = {}

    def __init__(self):
        pass


class ReadSeqFile:
    def __init__(self, input_file_path, file_type):
        self.input_file_path = input_file_path
        self.file_type = file_type
        self.records = SeqIO.parse(input_file_path, file_type)

    def prot_seq(self, record_index):
        record = self.records[record_index]
        return record.seq

    def prot_id(self, record_index):
        record = self.records[record_index]
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
