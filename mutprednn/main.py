import torch
from transformers import BertTokenizer, BertModel, pipeline
import re
import numpy as np
import os
import requests
from tqdm.auto import tqdm


tokenizer = BertTokenizer.from_pretrained("/home/kevinchangwang/RothLab/MutPred/mutprednn/ProtTrans-BFD/", do_lower_case = False)
model = BertModel.from_pretrained("/home/kevinchangwang/RothLab/MutPred/mutprednn/ProtTrans-BFD/")
input_sequence = #get input sequence from file
fe = pipeline("feature-extraction", model = model, tokenizer = tokenizer, device = 0)
protein_sequence = sequence_mut(input_sequence)
embedding = fe(protein_sequence)
