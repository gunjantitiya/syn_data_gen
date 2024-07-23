
import numpy as np
import pandas as pd

def add_correlated_feature(df, base_feature, new_feature, correlation, noise=0.1):
    """Add a new feature to the dataframe correlated with an existing feature."""
    base_values = df[base_feature].values
    new_values = correlation * base_values + (1 - correlation) * np.random.randn(len(df)) * noise
    df[new_feature] = new_values
    return df

def correlate_features(df, correlation_matrix):
    """Correlate multiple features based on a correlation matrix."""
    L = np.linalg.cholesky(correlation_matrix)
    uncorrelated = np.random.standard_normal((len(df), len(correlation_matrix)))
    correlated = np.dot(uncorrelated, L.T)
    
    for i, column in enumerate(correlation_matrix.index):
        df[column] = correlated[:, i]
    
    return df
