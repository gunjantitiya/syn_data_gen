
from synthetic_marketing_data import SyntheticMarketingData

# Create an instance of the synthetic data generator
generator = SyntheticMarketingData(seed=42)


from synthetic_marketing_data import SyntheticMarketingData

# Create an instance of the synthetic data generator
generator = SyntheticMarketingData(seed=42)

# Generate customer profiles
customer_profiles = generator.generate_customer_profiles(num_customers=1000)
print("Customer Profiles:")
print(customer_profiles.head())

# Generate campaign interactions
campaign_interactions = generator.generate_campaign_interactions(customer_profiles, num_campaigns=3)
print("\nCampaign Interactions:")
print(campaign_interactions.head())

# Basic analysis
print("\nConversion rates by campaign:")
conversion_rates = campaign_interactions.groupby('campaign')['converted'].mean()
print(conversion_rates)