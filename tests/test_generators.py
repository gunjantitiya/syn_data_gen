
import pytest
from synthetic_marketing_data.generators.customer_generator import CustomerGenerator
from synthetic_marketing_data.generators.campaign_generator import CampaignGenerator

def test_customer_generator():
    generator = CustomerGenerator(seed=42)
    customers = generator.generate_customers(num_customers=100)
    
    assert len(customers) == 100
    assert set(customers.columns) == {'customer_id', 'age', 'gender', 'income', 'location', 'signup_date', 'customer_segment'}
    assert customers['age'].between(18, 80).all()
    assert set(customers['gender'].unique()) == {'Male', 'Female', 'Other'}
    assert set(customers['customer_segment'].unique()) == {'Low Value', 'Medium Value', 'High Value'}

def test_campaign_generator():
    customer_generator = CustomerGenerator(seed=42)
    campaign_generator = CampaignGenerator(seed=42)
    
    customers = customer_generator.generate_customers(num_customers=10)
    campaigns = campaign_generator.generate_campaigns(num_campaigns=3)
    interactions = campaign_generator.generate_interactions(customers, campaigns)
    
    assert len(campaigns) == 3
    assert set(campaigns.columns) == {'campaign_id', 'start_date', 'end_date', 'channel', 'budget'}
    assert len(interactions) == 10 * 3  # 10 customers, 3 campaigns
    assert set(interactions['channel'].unique()) == {'Email', 'Social Media', 'Display Ads'}
