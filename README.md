
Synthetic Marketing Data Library
---------------------------------


https://pypi.python.org/pypi/syn_data_gen

https://travis-ci.com/gunjantitiya/syn_data_gen

https://syn-data-gen.readthedocs.io/en/latest/?version=latest



Overview
----------
The Synthetic Marketing Data Library is a Python package designed to generate realistic synthetic data for marketing analytics and machine learning purposes. It allows data scientists and marketers to create custom datasets for testing, development, and scenario analysis without using sensitive real-world data.


* Free software: MIT license


Features
--------

* Generate synthetic customer profiles with realistic attributes
* Create synthetic marketing campaigns and customer interactions
* Apply custom probability distributions to various data points
* Implement feature correlations for more realistic data relationships
* Simulate various market scenarios (seasonal trends, market shocks, competitor entry)
* Easy-to-use API for generating complete datasets or specific components

Installation
--------------
You can install the Synthetic Marketing Data Library using pip:

    pip install synthetic-marketing-data

Quick Start
Here's a simple example to get you started:

    from synthetic_marketing_data import SyntheticMarketingData
    # Initialize the data generator
    generator = SyntheticMarketingData(seed=42)
    # Generate a complete dataset
    customers, campaigns, interactions = generator.generate_dataset(num_customers=10000, num_campaigns=5)

    # Print the first few rows of each dataset
    print(customers.head())
    print(campaigns.head())
    print(interactions.head())

Advanced Usage
For more advanced usage, including scenario simulations:

    from synthetic_marketing_data import SyntheticMarketingData
    from synthetic_marketing_data.scenarios.market_scenarios import MarketScenarioSimulator

    # Generate base data
    generator = SyntheticMarketingData(seed=42)
    customers, _, _ = generator.generate_dataset(num_customers=10000, num_campaigns=5)

    # Initialize scenario simulator
    simulator = MarketScenarioSimulator(customers)

    # Run scenarios
    seasonal_data = simulator.simulate_seasonal_trend()
    shock_data = simulator.simulate_market_shock()
    competitor_data = simulator.simulate_competitor_entry()

    # Analyze results
    print("Average spending (base):", customers['spending'].mean())
    print("Average spending (seasonal):", seasonal_data['seasonal_spending'].mean())
    print("Average spending (after shock):", shock_data['adjusted_spending'].mean())
    print("Average conversion rate (competitor entry):", competitor_data['adjusted_conversion_rate'].mean())

License
---------
This project is licensed under the MIT License - see the LICENSE <LICENSE>_ file for details.

Contact
--------
For any questions or feedback, please open an issue on our GitHub repository https://github.com/gunjantitiya/syn_data_gen

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
