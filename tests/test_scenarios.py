
import pytest
import pandas as pd
import numpy as np
from synthetic_marketing_data.scenarios.market_scenarios import MarketScenarioSimulator

@pytest.fixture
def base_data():
    return pd.DataFrame({
        'spending': np.random.uniform(50, 500, 1000),
        'conversion_rate': np.random.uniform(0.01, 0.1, 1000)
    })

def test_seasonal_trend(base_data):
    simulator = MarketScenarioSimulator(base_data)
    result = simulator.simulate_seasonal_trend()
    
    assert 'seasonal_factor' in result.columns
    assert 'seasonal_spending' in result.columns
    assert np.all(result['seasonal_spending'] != result['spending'])

def test_market_shock(base_data):
    simulator = MarketScenarioSimulator(base_data)
    result = simulator.simulate_market_shock()
    
    assert 'market_shock' in result.columns
    assert 'adjusted_spending' in result.columns
    assert np.all(result['adjusted_spending'] <= result['spending'])

def test_competitor_entry(base_data):
    simulator = MarketScenarioSimulator(base_data)
    result = simulator.simulate_competitor_entry()
    
    assert 'competitor_impact' in result.columns
    assert 'adjusted_conversion_rate' in result.columns
    assert np.all(result['adjusted_conversion_rate'] <= result['conversion_rate'])
