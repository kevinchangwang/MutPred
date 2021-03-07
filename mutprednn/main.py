import torch
from transformers import BertTokenizer, BertModel, pipeline
import re
import numpy as np
import os
import requests
from tqdm.auto import tqdm
from mutprednn import sequence_mut
from mutprednn import input_params


class get_prot_seq_embedding:
    def __init__(self, model_dir, prot_seq):
        self.model_dir = model_dir
        self.prot_seq = prot_seq
        self.tokenizer = BertTokenizer.from_pretrained(model_dir, do_lower_case = False)
        self.model = BertModel.from_pretrained(model_dir)
    def generate_embedding(self):
        fe = pipeline("feature-extraction", model = self.model, tokenizer = self.tokenizer)
        embedding = fe(self.prot_seq)
        return np.array(embedding)

class get_euclidean_distance:
    def __init__(self,wt_embed, mut_embed):
        self.wt_embed = wt_embed
        self.mut_embed = mut_embed
    def calc_distance(self):
        dist = np.linalg.norm(self.wt_embed, self.mut_embed)
        return dist

class seq_mut:
    def __init__(self, input_seq, position, mut_res):
        self.input_seq = input_seq
        self.position = position
        self.mut_res = mut_res
    def mutant(self):
        self.input_seq[position] = self.mut_res
        return self.input_seq

class parse_input_file:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
    def read_input(self):
        pass ### YAML input file reading here 



def main():
    pass

if __name__ =="__main__":
    main()