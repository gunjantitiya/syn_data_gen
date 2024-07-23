
import pytest
import numpy as np
import pandas as pd
from synthetic_marketing_data.correlations.feature_correlations import add_correlated_feature, correlate_features

def test_add_correlated_feature():
    df = pd.DataFrame({'base': np.random.randn(1000)})
    df = add_correlated_feature(df, 'base', 'new', 0.7)
    
    assert 'new' in df.columns
    correlation = df['base'].corr(df['new'])
    assert correlation == pytest.approx(0.7, abs=0.1)

def test_correlate_features():
    df = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'])
    correlation_matrix = pd.DataFrame([[1.0, 0.5, -0.3],
                                       [0.5, 1.0, 0.2],
                                       [-0.3, 0.2, 1.0]], index=['A', 'B', 'C'], columns=['A', 'B', 'C'])
    
    df = correlate_features(df, correlation_matrix)
    
    actual_corr = df.corr()
    np.testing.assert_array_almost_equal(actual_corr, correlation_matrix, decimal=1)
