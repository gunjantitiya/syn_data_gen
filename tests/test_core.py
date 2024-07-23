import pytest
from synthetic_marketing_data import SyntheticMarketingData

def test_generate_customer_profiles():
    generator = SyntheticMarketingData(seed=42)
    profiles = generator.generate_customer_profiles(num_customers=100)
    
    assert len(profiles) == 100
    assert set(profiles.columns) == {'customer_id', 'age', 'gender', 'income', 'location', 'signup_date'}
    assert profiles['age'].between(18, 80).all()
    assert set(profiles['gender'].unique()) == {'Male', 'Female', 'Other'}

def test_generate_campaign_interactions():
    generator = SyntheticMarketingData(seed=42)
    profiles = generator.generate_customer_profiles(num_customers=10)
    interactions = generator.generate_campaign_interactions(profiles, num_campaigns=3)
    
    assert len(interactions) == 10 * 3  # 10 customers, 3 campaigns
    assert set(interactions.columns) == {'customer_id', 'campaign', 'email_sent', 'email_opened', 'link_clicked', 'converted'}
    assert set(interactions['campaign'].unique()) == {'Campaign_1', 'Campaign_2', 'Campaign_3'}
