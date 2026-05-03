import yfinance as yf
from datetime import datetime
import pandas as pd

# Configuration
TICKER = 'CLM26.NYM'
CONTRACT_SIZE = 1000

# Fetch Data
df = yf.download(TICKER, start='2026-04-01', auto_adjust=True, progress=False)
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)
df = df.reset_index()[['Date', 'Close']].dropna()

# Initial Setup
entry_price = df['Close'].iloc[0]
initial_deposit = (entry_price * CONTRACT_SIZE) * 0.10
balance = initial_deposit
total_injected = 0
total_mtm_pnl = 0

print(f"Contract: {TICKER} | Entry: {entry_price:.2f} | Initial Deposit: {initial_deposit:.2f}\n")

# MTM Loop
for i in range(1, len(df)):
    date = df.loc[i, 'Date'].strftime('%Y-%m-%d')
    curr_price = df.loc[i, 'Close']
    prev_price = df.loc[i-1, 'Close']
    
    # Daily Calculations
    daily_pnl = (curr_price - prev_price) * CONTRACT_SIZE
    balance += daily_pnl
    total_mtm_pnl += daily_pnl
    
    maint_balance_req = (curr_price * CONTRACT_SIZE) * 0.08
    
    status = "OK"
    if balance < maint_balance_req:
        init_req = (curr_price * CONTRACT_SIZE) * 0.10
        top_up = init_req - balance
        balance += top_up
        total_injected += top_up
        status = f"CALL (Injected: {top_up:.2f})"

    print(f"{date} | Price: {curr_price:<7.2f} | Daily PnL: {daily_pnl:>8.2f} | Balance: {balance:>9.2f} | Maint: {maint_balance_req:>8.2f} | {status}")

# Final Summary Logic
exit_price = df['Close'].iloc[-1]
print("\n" + "="*30)
print("       FINAL SUMMARY")
print("="*30)
print(f"Total MTM Profit/Loss : {total_mtm_pnl:>12.2f}")
print(f"Total Capital Injected: {total_injected:>12.2f}")
print(f"Total Initial Deposit : {initial_deposit:>12.2f}")
print("-" * 30)
print(f"Final Account Value   : {balance:>12.2f}")
print("="*30)