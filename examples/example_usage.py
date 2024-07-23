
import pandas as pd
from synthetic_marketing_data import SyntheticMarketingData
from synthetic_marketing_data.scenarios.market_scenarios import MarketScenarioSimulator

def generate_and_save_base_data(num_customers=10000, num_campaigns=10, output_dir='output'):
    # Initialize the synthetic data generator
    generator = SyntheticMarketingData(seed=42)

    # Generate the dataset
    customers, campaigns, interactions = generator.generate_dataset(num_customers, num_campaigns)

    # Save the generated data to CSV files
    customers.to_csv(f'{output_dir}/customers.csv', index=False)
    campaigns.to_csv(f'{output_dir}/campaigns.csv', index=False)
    interactions.to_csv(f'{output_dir}/interactions.csv', index=False)

    return customers, campaigns, interactions

def run_scenario_analysis(customers, output_dir='output'):
    # Initialize the scenario simulator
    simulator = MarketScenarioSimulator(customers)

    # Run different scenarios
    seasonal_data = simulator.simulate_seasonal_trend()
    shock_data = simulator.simulate_market_shock()
    competitor_data = simulator.simulate_competitor_entry()

    # Save scenario results to CSV files
    seasonal_data.to_csv(f'{output_dir}/seasonal_scenario.csv', index=False)
    shock_data.to_csv(f'{output_dir}/market_shock_scenario.csv', index=False)
    competitor_data.to_csv(f'{output_dir}/competitor_entry_scenario.csv', index=False)

    return seasonal_data, shock_data, competitor_data

def analyze_scenario_results(base_data, seasonal_data, shock_data, competitor_data):
    # Perform some basic analysis
    results = {
        'base_avg_spending': base_data['spending'].mean(),
        'seasonal_avg_spending': seasonal_data['seasonal_spending'].mean(),
        'shock_avg_spending': shock_data['adjusted_spending'].mean(),
        'competitor_avg_conversion': competitor_data['adjusted_conversion_rate'].mean()
    }

    # Convert results to a DataFrame and save to CSV
    results_df = pd.DataFrame([results])
    results_df.to_csv('output/scenario_analysis_results.csv', index=False)

    return results

def main():
    # Generate and save base data
    customers, campaigns, interactions = generate_and_save_base_data()
    print("Base data generated and saved.")

    # Run scenario analysis
    seasonal_data, shock_data, competitor_data = run_scenario_analysis(customers)
    print("Scenario analysis completed and results saved.")

    # Analyze and save results
    results = analyze_scenario_results(customers, seasonal_data, shock_data, competitor_data)
    print("Analysis results:")
    print(results)

if __name__ == "__main__":
    main()