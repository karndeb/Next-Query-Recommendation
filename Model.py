from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
model = SentenceTransformer('roberta-base-nli-stsb-mean-tokens')


def get_scores(input_query, input_corpus, topk=5):
    emb_corpus = np.array(model.encode(input_corpus))
    emb_query = np.array(model.encode([input_query]))
    results = cosine_similarity(emb_query, emb_corpus)[0]
    topk = results.argsort()[-topk:][::-1]
    scores = results[topk]
    sentences = [input_corpus[idx] for idx in topk]
    return [str(s) for s in scores], sentences


def predict(df):
    # top_k = request.json['top_k']
    queries = df['Question'].tolist()
    req_format_list = []
    for query in queries:
        score_list, sentences_list = get_scores(query, queries, topk=6)
        if len(sentences_list) == 0:
            first = " "
        else:
            first = sentences_list[1]
            for i in range(2, len(sentences_list)):
                first = first + "$$$" + sentences_list[i]
        req_format_list.append(first)
    df['Recommendation'] = pd.Series(req_format_list)
    return df

