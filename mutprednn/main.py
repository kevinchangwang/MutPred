import torch
from transformers import BertTokenizer, BertModel, pipeline
import re
import numpy as np
from Bio import SeqIO
import os
import requests
from tqdm.auto import tqdm
from mutprednn import input_params


class prot_seq_embedding_bert:
    def __init__(self, model_dir, prot_seq):
        self.model_dir = model_dir
        self.prot_seq = prot_seq
        self.tokenizer = BertTokenizer.from_pretrained(model_dir, do_lower_case=False)
        self.model = BertModel.from_pretrained(model_dir)
    def embedding(self):
        fe = pipeline("feature-extraction", model=self.model, tokenizer=self.tokenizer)
        embedding = fe(self.prot_seq)
        return np.array(embedding)

class euclidean_distance:
    def __init__(self,wt_embed, mut_embed):
        self.wt_embed = wt_embed
        self.mut_embed = mut_embed
    def distance(self):
        dist = np.linalg.norm(self.wt_embed, self.mut_embed)
        return dist

class seq_mut:
    def __init__(self, input_seq, position, mut_res):
        self.input_seq = input_seq
        self.position = position
        self.mut_res = mut_res
    def mutant(self):
        self.input_seq[self.position] = self.mut_res #edit so that the original self.input_seq is not altered
        return self.input_seq
    def wild_type(self):
        return self.input_seq


class seq_io:
    def __init__(self, input_file_path, file_type):
        self.input_file_path = input_file_path
        self.file_type = file_type
        self.record = SeqIO.read(input_file_path, file_type)
    def prot_seq(self, record_index=0):
        return record[record_index].seq

class read_param_file:





def main():
      fasta = seq_io(os.getcwd(), "fasta")
      sequence = fasta.prot_seq()
      sequence_pair = seq_mut(sequence, position, mut_res)
      seq_distance = euclidean_distance(sequence_pair.wild_type(),sequence_pair.mutant())
      return seq_distance.distance()


if __name__ =="__main__":
    main()