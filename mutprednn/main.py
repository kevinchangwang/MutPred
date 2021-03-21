import torch
from transformers import BertTokenizer, BertModel, pipeline
import re
import numpy as np
from Bio import SeqIO
import os
import requests
from tqdm.auto import tqdm
from mutprednn import mutate_sequences, model
import pandas as pd
import matplotlib
import seaborn
from collections import Counter

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, SGDRegressor

def euclidean_distance(wt_embed, mut_embed):
    dist = np.linalg.norm(wt_embed, mut_embed)
    return dist

def load_embedding():
    pass

class GridSearch:
    knn_grid = {
        'n_neighbors': [5, 10],
        'weights': ['uniform', 'distance'],
        'algorithm': ['ball_tree', 'kd_tree', 'brute'],
        'leaf_size': [15, 30],
        'p': [1, 2],
    }

    svm_grid = {
        'C': [0.1, 1.0, 10.0],
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'degree': [3],
        'gamma': ['scale'],
    }

    rfr_grid = {
        'n_estimators': [20],
        'criterion': ['mse', 'mae'],
        'max_features': ['sqrt', 'log2'],
        'min_samples_split': [5, 10],
        'min_samples_leaf': [1, 4]
    }

    def __init__(self):
        self.cls_list = [KNeighborsRegressor, SVR, RandomForestRegressor]
        self.param_grid_list = [self.knn_grid, self.svm_grid, self.rfr_grid]

    def run_search(self):
        result_list = []
        grid_list = []
        for cls_name, param_grid in zip(self.cls_list, self.param_grid_list)
            print(cls_name)
            grid = GridSearchCV(
                estimator= cls_name(),
                param_grid= param_grid,
                scoring= 'r2',
                verbose= 1,
                n_jobs= -1
            )
            grid.fit()


def main():
    pass


if __name__ == "__main__":
    main()
