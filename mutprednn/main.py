import torch
from transformers import BertTokenizer, BertModel, pipeline
import re
import numpy as np
from Bio import SeqIO
import os
import requests
from tqdm.auto import tqdm
from mutprednn import mutate_sequences, model



def euclidean_distance(wt_embed, mut_embed):
    dist = np.linalg.norm(wt_embed, mut_embed)
    return dist

def main():
    pass


if __name__ =="__main__":
    main()