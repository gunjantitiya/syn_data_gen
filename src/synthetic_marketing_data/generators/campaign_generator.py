
import numpy as np
import pandas as pd

class CampaignGenerator:
    def __init__(self, seed=None):
        if seed is not None:
            np.random.seed(seed)

    def generate_campaigns(self, num_campaigns=5):
        campaigns = []
        for i in range(num_campaigns):
            campaign = {
                'campaign_id': f'Campaign_{i+1}',
                'start_date': pd.Timestamp.now() - pd.Timedelta(days=np.random.randint(1, 365)),
                'end_date': pd.Timestamp.now() + pd.Timedelta(days=np.random.randint(1, 30)),
                'channel': np.random.choice(['Email', 'Social Media', 'Display Ads'], p=[0.5, 0.3, 0.2]),
                'budget': np.random.uniform(1000, 10000),
            }
            campaigns.append(campaign)
        
        return pd.DataFrame(campaigns)

    def generate_interactions(self, customer_profiles, campaigns):
        interactions = []
        for _, customer in customer_profiles.iterrows():
            for _, campaign in campaigns.iterrows():
                interaction = {
                    'customer_id': customer['customer_id'],
                    'campaign_id': campaign['campaign_id'],
                    'interaction_date': np.random.choice(pd.date_range(campaign['start_date'], campaign['end_date'])),
                    'channel': campaign['channel'],
                }
                
                if interaction['channel'] == 'Email':
                    interaction['email_sent'] = True
                    interaction['email_opened'] = np.random.choice([True, False], p=[0.3, 0.7])
                    interaction['link_clicked'] = interaction['email_opened'] and np.random.choice([True, False], p=[0.2, 0.8])
                elif interaction['channel'] == 'Social Media':
                    interaction['impression'] = True
                    interaction['engagement'] = np.random.choice([True, False], p=[0.1, 0.9])
                else:  # Display Ads
                    interaction['impression'] = True
                    interaction['click'] = np.random.choice([True, False], p=[0.05, 0.95])
                
                interaction['converted'] = np.random.choice([True, False], p=[0.01, 0.99])
                
                interactions.append(interaction)
        
        return pd.DataFrame(interactions)