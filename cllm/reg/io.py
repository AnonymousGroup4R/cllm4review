from pathlib import Path
from cllm.io import load_data
import pickle
import pandas as pd
import json
import numpy as np
import random
import logging 

def load_pickle(input_path):
    with open(input_path, 'rb') as rf:
        return pickle.load(rf)

def transform_data_to_pdf(gt_desc, gt_embedding, q_desc, q_embedding):
    df = pd.DataFrame(q_desc)
    # unifiy key
    df['id'] = df['id'].astype(str)
    df['emb'] = df['id'].apply(lambda x: q_embedding[x])
    # get gt id.
    gt_df = pd.DataFrame(gt_desc).set_index('id')
    df['gt_id'] = df['id'].apply(lambda x: int(x) if '-' not in x else int(x.split('-')[0]))
    df['gt_desc'] = df['gt_id'].apply(lambda x: gt_df.loc[x]['desc'])
    df['gt_emb'] = df['gt_id'].apply(lambda x: gt_embedding[x])
    # compute distance.
    # df['dist'] = np.linalg.norm(np.array(df['emb'].to_list()) - np.array(df['gt_emb'].to_list()), axis=1)
    # df['dist'] = df.apply(lambda x: np.linalg.norm(np.array(x['emb']) - np.array(x['gt_emb']).astype(np.float32)), axis=1)
    # print(df.columns)
    # print(df['emb'])
    df['dist'] = df.apply(lambda x: compute_cosine_distance(
        np.array(x['emb']), np.array(x['gt_emb'])
    ), axis=1)
    # df['dist2'] = df.apply(lambda x: np.linalg.norm(np.array(x['emb']) - np.array(x['gt_emb'])), axis=1)
    # pd.testing.assert_series_equal(df['dist'].rename('a'), df['dist2'].rename('a'))
    # df = df.drop(columns=['emb', 'desc', 'gt_desc', 'gt_emb'])
    df = df.drop(columns=['desc', 'gt_desc'])
    # drop useless data.
    return df

def compute_cosine_distance(x, y):
    x_norm = x / np.linalg.norm(x)
    y_norm = y / np.linalg.norm(y)

    # Step 2: Compute cosine similarity
    cosine_similarity = np.dot(x_norm, y_norm)

    # Step 3: Compute cosine distance
    cosine_distance = 1 - cosine_similarity
    return cosine_distance


def compute_pairwise_distance(pdf, all_gt):
    # for _, _row in pdf.iterrows():
    #     _row['dist_arr'] = np.linalg.norm(all_gt - np.array(_row['emb']).reshape(1, -1), axis=1)

    #     if _row['id'] == '46-0':
    #         print(_row['dist_arr'])
    def compute_dist_arr(x):
        # Step 1: Normalize the vectors (optional but recommended)
        x_norm = x / np.linalg.norm(x)
        all_gt_norm = all_gt / np.linalg.norm(all_gt, axis=1, keepdims=True)

        # Step 2: Compute cosine similarity
        cosine_similarities = np.dot(all_gt_norm, x_norm)

        # Step 3: Compute cosine distance
        cosine_distances = 1 - cosine_similarities
        return cosine_distances
        # _arr = np.linalg.norm(all_gt - np.array(x).reshape(1, -1), axis=1)
        # return _arr
    # WRONG: TODO FIX: 
    pdf['dist_arr'] = pdf['emb'].apply(compute_dist_arr)
    return pdf

def normalize_distance(pdf):
    # min-max normalization.
    all_min = np.inf
    all_max = 0
    for _id, _row in pdf.iterrows():
        _min = min(_row['dist_arr'])
        _max = max(_row['dist_arr'])
        all_min = min(_min, all_min)
        all_max = max(_max, all_max)
    def minmax_norm(x):
        return (x - all_min) / (all_max - all_min)
    pdf['dist_arr'] = pdf['dist_arr'].apply(minmax_norm)
    pdf['dist'] = pdf['dist'].apply(minmax_norm)
    return pdf


def transform_data_to_pdf_mgt_as_onegt(gt_desc, gt_embedding, q_desc, q_embedding):
    # construct pa
    
    df = pd.DataFrame(q_desc)
    # unifiy key
    df['id'] = df['id'].astype(str)
    df['emb'] = df['id'].apply(lambda x: q_embedding[x])
    # get gt id.
    gt_df = pd.DataFrame(gt_desc).set_index('id')

    # get oq_ids.
    dist_arr = []
    gt_emb_arr = []
    gt_desc_arr = []
    gt_id_arr = []
    for _id, _row in df.iterrows():
        # compute arr.
        _gt_embds = []
        _gt_dists = []
        for _gtid in _row['oq_ids']:
            # compute distances
            _emb = gt_embedding[_gtid]
            _dist = compute_cosine_distance(_emb, _row['emb'])
            _gt_embds.append(_emb)
            _gt_dists.append(_dist)
        _min_id = np.argmin(_gt_dists)
        dist_arr.append(_gt_dists[_min_id])
        gt_emb_arr.append(_gt_embds[_min_id])
        gt_desc_arr.append(gt_df.loc[_min_id]['desc'])
        gt_id_arr.append(_min_id)
    df['dist'] = dist_arr
    df['gt_emb'] = gt_emb_arr
    df['gt_desc'] = gt_desc_arr
    df['gt_id'] = gt_id_arr
    
    df = df.drop(columns=['desc', 'gt_desc'])
    return df


def load_std_mgt_as_one_data(split='aug_smgt', normalize=False, base_path='./datasets/STD'):
    base_path = Path(base_path)
    embedding_path = base_path / 'embedding'
    gt_desc = load_data(base_path / 'function_answers_desc_3.5.jsonl')
    gt_embedding = load_pickle(embedding_path / 'embedding_struct_funcs_desc_3.5.pkl')
    if split.startswith('aug'):
        q_embedding = load_pickle(embedding_path / 'embedding_struct_struct_more_outputs_gpt_desc_3.5_mgt.pkl')
        q_desc = load_data(base_path / 'struct_more_outputs_gpt_desc_3.5_mgt.jsonl')
    else:
        raise NotImplementedError()
    
    pdf = transform_data_to_pdf_mgt_as_onegt(gt_desc, gt_embedding, q_desc, q_embedding)
    # get all ground-truth.
    # get all gt_embeddings.
    all_gt_ids = []
    for _id_list in pdf['oq_ids']:
        all_gt_ids.extend(_id_list)
    all_gt_ids = sorted(list(set(all_gt_ids)))
    all_gt_embeddings = np.array([gt_embedding[x] for x in all_gt_ids])

    # all_gt_ids = sorted(pdf['gt_id'].unique())
    pdf['gt_idx'] = pdf['gt_id'].apply(lambda x: all_gt_ids.index(x))
    
    pdf = compute_pairwise_distance(pdf, all_gt_embeddings)
    if normalize:
        pdf = normalize_distance(pdf)

    # compute_k = True
    # if compute_k:
    #     pdf['dist'] = pdf.apply(lambda x: (x['dist_arr'] <= x['dist']).sum(), axis=1)
    #     pdf['dist_arr'] = pdf['dist_arr'].apply(lambda x: np.arange(1, len(x)+1))
    #     pdf['dist'].apply(lambda x: x/len(pdf))
    #     pdf['dist_arr'].apply(lambda x: x/len(pdf))
    # print(pdf)
    return pdf

def load_tbe2_data(split='aug', normalize=False, base_path='./datasets/TDE2/'):
    base_path = Path(base_path)
    embedding_path = base_path / 'embedding'
    gt_desc = load_data(base_path / 'function_answers_desc_3.5.jsonl')
    gt_embedding = load_pickle(embedding_path / 'embedding_function_desc_3.5.pkl')
    if split == 'aug':
        q_embedding = load_pickle(embedding_path / 'struct_more_embedding_desc_3.5.pkl')
        q_desc = load_data(base_path / 'struct_more_outputs_gpt_desc_3.5.jsonl')
    else:
        raise NotImplementedError()
    # gt embedding should with key type int.
    gt_embedding = {int(k): v for k, v in gt_embedding.items()}
    # construct pa
    pdf = transform_data_to_pdf(gt_desc, gt_embedding, q_desc, q_embedding)
    # get all ground-truth.
    # get all gt_embeddings.
    all_gt_ids = sorted(pdf['gt_id'].unique())
    pdf['gt_idx'] = pdf['gt_id'].apply(lambda x: all_gt_ids.index(x))
    all_gt_embeddings = np.array([gt_embedding[x] for x in all_gt_ids])
    pdf = compute_pairwise_distance(pdf, all_gt_embeddings)
    if normalize:
        pdf = normalize_distance(pdf)
    # we only 
    # compute_k = True
    # if compute_k:
    #     pdf['dist'] = (pdf['gt_idx']+1)/len(pdf)
    #     pdf['dist_arr'] = pdf['dist_arr'].apply(lambda x: np.arange(1, len(x)+1)/len(x))
    # print(pdf)
    return pdf

def balance_tbe_data(pdf: pd.DataFrame, seed=None):
    pdf['sample_id'] = pdf['id'].apply(lambda x: int(x.split('-')[1]))
    data = []
    permute_list = sorted(pdf['sample_id'].unique().tolist())
    if seed is not None:
        # randomly shuffle the list.
        random.Random(seed).shuffle(permute_list)
    for i in permute_list:
        data.append(pdf[pdf['sample_id'] == i])
    pdf = pd.concat(data)
    return pdf
