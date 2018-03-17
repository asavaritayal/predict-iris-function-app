import azure.functions
import pickle
import sys
import os

import numpy as np


def main(req: azure.functions.HttpRequest):

    # load the model
    f = open('IrisSample/model.pkl', 'rb')
    model = pickle.load(f)

    # gather new sample
    s_len = float(req.params['slen'])
    s_wid = float(req.params['swid'])
    p_len = float(req.params['plen'])
    p_wid = float(req.params['pwid'])

    X_new = [[s_len, s_wid, p_len, p_wid]]

    # add random features to match the training data
    n=40
    random_state = np.random.RandomState(0)
    X_new_with_random_features = np.c_[X_new, random_state.randn(1, n)]

    # score on the new sample
    pred = model.predict(X_new_with_random_features)

    return np.array_str(pred)

    # return 'Hello'
