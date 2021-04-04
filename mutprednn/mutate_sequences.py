import pandas as pd
from Bio import SeqIO
import csv

class WriteMutationSeqTable:
    def __init__(self,
                 mutation_data_path,
                 fasta_files_path,
                 delimiter,
                 pid_head,
                 aa_pos_head,
                 aa_wt_head,
                 aa_mut_head):
        self.mutation_data_path = mutation_data_path
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
        self.fasta_dir = fasta_files_path

    def wt_fasta_seq(self, p_idx):
        fasta = SeqIO.read(self.fasta_dir + "/" + self.pid[p_idx] + ".fasta", "fasta")
        wt_seq = fasta.seq
        return str(wt_seq)

    def mut_fasta_seq(self, p_idx):
        fasta = SeqIO.read(self.fasta_dir + "/" + self.pid[p_idx] + ".fasta", "fasta")
        seq = fasta.seq
        mutable_seq = seq.tomutable()
        pos = int(self.aapos[p_idx])
        mutable_seq[pos] = self.aamut[p_idx]
        mut_seq = mutable_seq.toseq()
        return str(mut_seq)

    def protein_mutation(self, p_idx):
        mutation = "p" + str(self.aawt[p_idx]) + str(self.aapos[p_idx]) + str(self.aamut[p_idx])
        return mutation

    def write_row(self, p_idx, output_file_path):
        protein_id = self.pid[p_idx]
        mutation = self.protein_mutation(p_idx)
        wt_seq = self.wt_fasta_seq(p_idx)
        mut_seq = self.mut_fasta_seq(p_idx)
        row = [protein_id, mutation, wt_seq, mut_seq]
        f = open(output_file_path)
        with f:
            writer = csv.writer(f)
            writer.writerow(row)

    def write_table(self, output_file_path):
        for i in self.pid:
            self.write_row(i, output_file_path)


def main():
    pass


if __name__ == '__main__':
    main()
