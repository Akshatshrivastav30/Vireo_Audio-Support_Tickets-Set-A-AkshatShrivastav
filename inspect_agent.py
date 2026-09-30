import pandas as pd

agents = pd.read_csv('../1bb95ea8-f7cb-44b6-b5d2-2fb20c9a4e47-agents.csv')
print("--- Agents CSV Preview ---")
print(agents.head(10))
print("\n--- Columns ---")
print(agents.columns)
print("\n--- Unique Tiers ---")
print(agents['tier'].unique() if 'tier' in agents.columns else "No tier column")