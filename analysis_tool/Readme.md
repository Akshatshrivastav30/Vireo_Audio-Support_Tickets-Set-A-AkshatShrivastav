
# Vireo Audio Support Analytics Tool

A lightweight, deterministic Python tool designed for Vireo Audio to analyze 18 months of customer support data, track financial leakage from internal team transfers, generate weekly complaint digests, and surface a Tier-1 filtered agent performance leaderboard.

## Prerequisites
- Python 3.8 or higher installed on your system.
- The `pandas` Python library.

## Setup & Installation on a Clean Machine
1. Open your terminal or command prompt and navigate into the `analysis_tool` folder.
2. Install the required dependency if you haven't already:
   ```bash
   pip install pandas
Ensure that the following three files reside together in this folder:

vireo_tool.py

tickets.csv

agents.csv

Running the Tool
Execute the following command in your terminal:

Bash
python vireo_tool.py
Outputs
The tool will automatically output:

Financial Waste Metric: Total internal team transfers and historical cost impact calculated at ₹305 per transfer (per Support Policy §4).

Weekly Complaint Digest: Grouped weekly category counts highlighting primary customer friction points (e.g., Delivery & Shipping, Billing & Payments).

Agent Leaderboard: Cleanly filtered Tier-1 frontline agent performance rankings based on total tickets closed, avoiding mixed-tier distortions.