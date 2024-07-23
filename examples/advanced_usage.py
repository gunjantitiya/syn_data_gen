
from synthetic_marketing_data import SyntheticMarketingData
import matplotlib.pyplot as plt

# Create an instance of the synthetic data generator
generator = SyntheticMarketingData(seed=42)

# Generate a complete dataset
customers, campaigns, interactions = generator.generate_dataset(num_customers=10000, num_campaigns=10)

# Analyze customer segments
segment_spending = customers.groupby('customer_segment')['spending'].mean()
plt.figure(figsize=(10, 6))