import pandas as pd

print("--- VIREO AUDIO SUPPORT ANALYTICS TOOL ---")

# 1. Load data
tickets = pd.read_csv('tickets.csv')
agents = pd.read_csv('agents.csv')
# Convert dates
tickets['created_at'] = pd.to_datetime(tickets['created_at'])
tickets['resolved_at'] = pd.to_datetime(tickets['resolved_at'])

# 2. Calculate Financial Waste (Transfers)
tickets['transfers'] = pd.to_numeric(tickets['transfers'], errors='coerce').fillna(0)
total_transfers = tickets['transfers'].sum()
transfer_cost_total = total_transfers * 305  # ₹305 per transfer (Policy §4)

print(f"\n[Financial Insight]")
print(f"Total Internal Transfers: {int(total_transfers)}")
print(f"Estimated Cost of Transfers (at ₹305 each): ₹{transfer_cost_total:,.2f}")

# 3. Weekly Complaint Digest (Top Categories over time)
tickets['week'] = tickets['created_at'].dt.to_period('W')
print(f"\n[Weekly Complaint Volume - Top Categories]")
weekly_category = tickets.groupby(['week', 'category']).size().reset_index(name='count')
print(weekly_category.sort_values(by='count', ascending=False).head(10))

# 4. Agent Leaderboard (Volume & Tier breakdown)
# Deduplicate agents by taking the latest record or just dropping duplicates on agent_id
unique_agents = agents.drop_duplicates(subset=['agent_id'], keep='last').copy()
unique_agents['tier'] = unique_agents['tier'].astype(str) # Normalize tier for filtering

# Count resolved/closed tickets per agent
resolved_tickets = tickets[tickets['status'].isin(['resolved', 'closed'])]
agent_summary = resolved_tickets.groupby('agent_id').size().reset_index(name='tickets_closed')

# Merge with agent roster
agent_summary = agent_summary.merge(unique_agents[['agent_id', 'name', 'tier', 'team', 'site']], on='agent_id', how='left')

print("\n[Top Tier 1 Agents by Closed Tickets]")
tier1_leaders = agent_summary[agent_summary['tier'] == '1'].sort_values(by='tickets_closed', ascending=False)
print(tier1_leaders[['name', 'site', 'team', 'tickets_closed']].head(10))