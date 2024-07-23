
import pytest
import numpy as np
from synthetic_marketing_data.distributions.custom_distributions import pareto_spending, poisson_visits, normal_age, exponential_time_between_purchases

def test_pareto_spending():
    spending = pareto_spending(1000, shape=2, scale=100)
    assert len(spending) == 1000
    assert np.all(spending >= 100)

def test_poisson_visits():
    visits = poisson_visits(1000, lam=5)
    assert len(visits) == 1000
    assert np.all(visits >= 0)
    assert np.mean(visits) == pytest.approx(5, rel=0.1)

def test_normal_age():
    ages = normal_age(1000)
    assert len(ages) == 1000
    assert np.all(ages >= 18) and np.all(ages <= 80)
    assert np.mean(ages) == pytest.approx(35, rel=0.1)

def test_exponential_time_between_purchases():
    times = exponential_time_between_purchases(1000)
    assert len(times) == 1000
    assert np.all(times >= 0)
    assert np.mean(times) == pytest.approx(30, rel=0.1)