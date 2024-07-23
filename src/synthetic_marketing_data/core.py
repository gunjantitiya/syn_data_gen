
from .generators.customer_generator import CustomerGenerator
from .generators.campaign_generator import CampaignGenerator
from .distributions.custom_distribution import pareto_spending, poisson_visits
from .correlations.feature_correlations import add_correlated_feature, correlate_features
from .scenarios.market_scenarios import MarketScenarioSimulator

class SyntheticMarketingData:
    def __init__(self, seed=None):
        self.customer_generator = CustomerGenerator(seed)
        self.campaign_generator = CampaignGenerator(seed)

    def generate_dataset(self, num_customers=1000, num_campaigns=5):
        customers = self.customer_generator.generate_customers(num_customers)
        campaigns = self.campaign_generator.generate_campaigns(num_campaigns)
        interactions = self.campaign_generator.generate_interactions(customers, campaigns)

        # Add custom distributions
        customers['spending'] = pareto_spending(len(customers), shape=2, scale=100)
        customers['website_visits'] = poisson_visits(len(customers), lam=5)

        # Add correlated features
        customers = add_correlated_feature(customers, 'income', 'spending_score', 0.7)
        
        # Simulate market scenarios
        simulator = MarketScenarioSimulator(customers)
        customers = simulator.simulate_seasonal_trend()
        customers = simulator.simulate_market_shock()
        customers = simulator.simulate_competitor_entry()

        return customers, campaigns, interactions

    # We can keep the original methods for backwards compatibility
    def generate_customer_profiles(self, num_customers=1000):
        return self.customer_generator.generate_customers(num_customers)

    def generate_campaign_interactions(self, customer_profiles, num_campaigns=5):
        campaigns = self.campaign_generator.generate_campaigns(num_campaigns)
        return self.campaign_generator.generate_interactions(customer_profiles, campaigns)