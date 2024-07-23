
import numpy as np
import pandas as pd
from faker import Faker

class CustomerGenerator:
    def __init__(self, seed=None):
        self.fake = Faker()
        if seed is not None:
            Faker.seed(seed)
            np.random.seed(seed)

    def generate_customers(self, num_customers=1000):
        data = []
        for _ in range(num_customers):
            customer = {
                'customer_id': self.fake.uuid4(),
                'age': np.random.randint(18, 80),
                'gender': np.random.choice(['Male', 'Female', 'Other'], p=[0.49, 0.49, 0.02]),
                'income': np.random.lognormal(mean=10.5, sigma=0.5),
                'location': self.fake.city(),
                'signup_date': self.fake.date_between(start_date='-5y', end_date='today'),
                'customer_segment': np.random.choice(['Low Value', 'Medium Value', 'High Value'], p=[0.6, 0.3, 0.1]),
            }
            data.append(customer)
        
        return pd.DataFrame(data)