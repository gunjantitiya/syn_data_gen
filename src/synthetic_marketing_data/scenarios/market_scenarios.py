
import pandas as pd
import numpy as np

class MarketScenarioSimulator:
    def __init__(self, base_data):
        self.base_data = base_data

    def simulate_seasonal_trend(self, season_factor=1.5):
        """Simulate seasonal trends in customer behavior."""
        self.base_data['seasonal_factor'] = np.sin(np.linspace(0, 2*np.pi, len(self.base_data))) * season_factor + 1
        self.base_data['seasonal_spending'] = self.base_data['spending'] * self.base_data['seasonal_factor']
        return self.base_data

    def simulate_market_shock(self, shock_magnitude=0.8, recovery_rate=0.05):
        """Simulate a market shock (e.g., economic downturn) and gradual recovery."""
        shock = np.ones(len(self.base_data))
        shock_point = len(self.base_data) // 2
        shock[shock_point:] *= shock_magnitude
        recovery = np.arange(len(self.base_data) - shock_point) * recovery_rate
        shock[shock_point:] += recovery
        self.base_data['market_shock'] = shock
        self.base_data['adjusted_spending'] = self.base_data['spending'] * self.base_data['market_shock']
        return self.base_data

    def simulate_competitor_entry(self, competitor_impact=0.2, adaptation_rate=0.01):
        """Simulate the entry of a new competitor into the market."""
        impact = np.ones(len(self.base_data))
        entry_point = len(self.base_data) // 3
        impact[entry_point:] *= (1 - competitor_impact)
        adaptation = np.arange(len(self.base_data) - entry_point) * adaptation_rate
        impact[entry_point:] += adaptation
        self.base_data['competitor_impact'] = impact
        self.base_data['adjusted_conversion_rate'] = self.base_data['conversion_rate'] * self.base_data['competitor_impact']
        return self.base_data