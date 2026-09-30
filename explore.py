import pandas as pd

# Load tickets
print("Loading tickets.csv...")
df = pd.read_csv('../cded5ec7-cd54-40e6-ba66-7b3e581319c7-tickets.csv')

print(f"Total Tickets: {len(df)}")
print(f"Columns: {list(df.columns)}")

# Check status distribution
print("\n--- Ticket Status ---")
print(df['status'].value_counts())

# Check total refunds
if 'refund_amount_inr' in df.columns:
    # Convert to numeric, filling NaNs with 0
    df['refund_amount_inr'] = pd.to_numeric(df['refund_amount_inr'], errors='coerce').fillna(0)
    total_refunds = df['refund_amount_inr'].sum()
    print(f"\nTotal Refunds Issued: ₹{total_refunds:,.2f}")

# Check top refund reason codes if present
if 'refund_reason_code' in df.columns:
    print("\n--- Top Refund Reason Codes ---")
    print(df['refund_reason_code'].value_counts().head(10))