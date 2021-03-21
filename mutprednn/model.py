import numpy as np
from transformers import BertModel, BertTokenizer, pipeline, FillMaskPipeline


class ProtBertBFD:
    def __init__(self, model_dir, cdevice):
        self.model_dir = model_dir
        self.tokenizer = BertTokenizer.from_pretrained(model_dir, do_lower_case=False)
        self.model = BertModel.from_pretrained(model_dir)
        self.cdevice = cdevice

    def embedding(self, prot_seq):
        fe = pipeline("feature-extraction", model=self.model, tokenizer=self.tokenizer, device=self.cdevice)
        embedding = fe(prot_seq)
        return np.array(embedding)

    def predict_aa(self, masked_prot_seq):
        fm = FillMaskPipeline(model=self.model, tokenizer=self.tokenizer, device=self.cdevice)
        missing_aa_prob = fm(masked_prot_seq)
        return np.array(missing_aa_prob)
