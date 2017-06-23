#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Steven C. Howell"

import sys
import pandas as pd
import sklearn.preprocessing
import sklearn.model_selection


def robust_scale(data, remove_cols=[]):
    """
    Rescale the data in a manner robust to outliers.
    Robert Tibshirani writes:

    The lasso method requires initial standardization of the regressors,
    so that the penalization scheme is fair to all regressors. For
    categorical regressors, one codes the regressor with dummy variables
    and then standardizes the dummy variables. As pointed out by a
    referee, however, the relative scaling between continuous and
    categorical variables in this scheme can be somewhat arbitrary.

    http://statweb.stanford.edu/~tibs/lasso/fulltext.pdf

    """

    df = pd.read_csv(data)  # read in the data
    scaler = sklearn.preprocessing.RobustScaler()  # setup rescale object
    col_to_scale = list(df.columns)  # get the column names

    # remove any binary column
    col_to_scale.remove('in_sf')

    # rescale the data
    for col in col_to_scale:
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))

    # write out the rescaled data
    out_fname = 'scaled-{}'.format(data)
    df.to_csv(out_fname)
    print('{} rescaled then saved to {}'.format(data, out_fname))

    return out_fname


if __name__ == "__main__":
    """
    Rescale data from command line, or the default housing data
    """
    if len(sys.argv) > 1:
        data = sys.argv[1]
    else:
        data = 'sf-ny-housing.csv'

    robust_scale(data)

    # potentially add a shuffle function as well