---

# Futures MTM & Margin Simulator

A Python-based risk management tool that simulates the daily **Mark-to-Market (MTM)** process and margin account mechanics for futures contracts using live market data.

## 📌 Overview
This project simulates how a professional margin account operates. Unlike a static calculator, this script tracks the lifecycle of a futures position over time, handling daily price fluctuations, calculating dynamic margin requirements, and triggering margin calls when equity falls below maintenance thresholds.

## 🚀 Features
*   **Live Market Integration:** Fetches historical daily closing prices using the `yfinance` API.
*   **Daily Mark-to-Market:** Calculates daily P&L and updates the account balance in real-time.
*   **Dynamic Margin Requirements:** 
    *   **Initial Margin (10%):** The capital required to open the position.
    *   **Maintenance Margin (8%):** The minimum "floor" balance required to keep the position open.
*   **Automated Margin Calls:** Simulates a broker's intervention by calculating the exact "top-up" amount needed to restore the account to the Initial Margin level upon a breach.
*   **Comprehensive Summary:** Provides a final breakdown of total MTM profit/loss, total capital injected, and final account value.

## 🛠️ Tech Stack
*   **Python 3.x**
*   **Pandas:** For data manipulation and structured logging.
*   **yfinance:** For fetching real-time financial market data.

## 📖 How It Works
1.  **Entry:** The script "buys" a contract at the first available price in the selected date range.
2.  **Daily Loop:** For every trading day, it calculates the gain or loss based on the settlement price.
3.  **Risk Check:** It compares the running balance against the **Maintenance Margin**.
4.  **Recovery:** If a breach occurs, it logs a margin call and "injects" capital to bring the balance back to the **Initial Margin** requirement.

## 🚦 Getting Started
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yasho1209/futures-mtm-simulator.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install yfinance pandas
    ```
3.  **Run the simulator:**
    ```bash
    python mtm_simulator.py
    ```

## 📊 Example Output
```text
2026-04-10 | Price: 85.50 | Daily PnL: -1500.00 | Balance: 7200.00 | Maint: 6840.00 | OK
2026-04-11 | Price: 83.20 | Daily PnL: -2300.00 | Balance: 4900.00 | Maint: 6656.00 | CALL (Injected: 3420.00)
```

---

### How to add this to your project:
1.  Create a new file in your folder named `README.md`.
2.  Paste the content above into the file.
3.  Run the following commands in your terminal:
    ```bash
    git add README.md
    git commit -m "Add professional README"
    git push
```
