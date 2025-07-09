# Binance Futures CLI Trading Bot

📽️ **[Watch CLI Demo Video Here](https://drive.google.com/file/d/1-cli-demo-video-link/view?usp=sharing)**  
*(Replace the above link with your actual uploaded video link)*

A Command-Line Interface (CLI) trading bot for Binance Futures Testnet.  
This tool allows users to place various types of crypto orders directly from the terminal using Python — including Market, Limit, Stop-Market, OCO (One Cancels the Other), TWAP (Time Weighted Average Price), and Grid Strategy orders.

---

## Developer Information

**Name:** Tarun Mawri  
**Email:** tarunmawri2005@gmail.com

---

## Objective

This project provides an interactive shell to perform futures trading on the Binance Testnet using simple commands. It is ideal for developers and traders looking to automate and experiment with trading strategies in a safe sandbox environment.

---

## Features Implemented

- Market Orders
- Limit Orders
- Stop-Market Orders
- OCO (Take-Profit + Stop-Loss) Orders
- TWAP Orders (Time-Weighted Average Price)
- Grid Strategy Orders
- Logging of each order
- CLI with help commands
- Formatted JSON and table-style output

---

## How to Set Up & Run (Step-by-Step)

1. **Download the code**  
   Clone this repo or extract the ZIP file into your local machine.

   ```bash
   git clone <your-repo-url>
   cd binance_bot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the environment**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the bot**

   ```bash
   python cli_shell.py
   ```

---

## How to Configure Binance Testnet API (Step-by-Step)

1. **Go to Binance Testnet**  
   Open [https://testnet.binancefuture.com](https://testnet.binancefuture.com) and sign in.

2. **Get your API credentials**  
   - Navigate to the API Management section  
   - Create a new API key (e.g., name it "CLI Bot")  
   - Copy the **API Key** and **API Secret**

3. **Add credentials to `.env`**

   Open the `.env` file and paste your keys like this:

   ```python
   BINANCE_API_KEY = "your_testnet_api_key"
   BINANCE_API_SECRET = "your_testnet_api_secret"
   ```

4. **Verify connection**  
   Run any order from the CLI (e.g., a market order) to ensure it connects successfully.

---

## Command Usage (Inside the Shell)

Once the CLI shell starts, use the following commands:

- **Market Order**
  ```
  market <symbol> <side> <quantity>
  Example: market BTCUSDT BUY 0.01
  ```

- **Limit Order**
  ```
  limit <symbol> <side> <quantity> <price>
  Example: limit BTCUSDT SELL 0.01 58000
  ```

- **Stop-Market Order**
  ```
  stoplimit <symbol> <side> <quantity> <stop_price> <0>
  Example: stoplimit BTCUSDT BUY 0.01 59000 0
  ```

- **OCO Order (Take-Profit & Stop-Loss)**
  ```
  oco <symbol> <side> <quantity> <tp_price> <sl_price>
  Example: oco BTCUSDT BUY 0.01 60000 55000
  ```

- **TWAP Order**
  ```
  twap <symbol> <side> <total_quantity> <chunks>
  Example: twap BTCUSDT BUY 0.05 5
  ```

- **Grid Strategy Order**
  ```
  grid <symbol> <base_price> <grid_size> <gap_percent> <quantity>
  Example: grid BTCUSDT 58000 3 1 0.01
  ```

- **General Commands**
  ```
  help       # List all commands
  clear      # Clear the terminal (banner remains visible)
  exit       # Exit the CLI
  ```

---

## Explanation of Each Order Type

- **Market Order:** Executes immediately at the current market price.
- **Limit Order:** Executes only when a specific target price is met.
- **Stop-Market Order:** Executes a market order once the stop price is reached.
- **OCO Order:** Places two linked orders — a take-profit and a stop-loss.
- **TWAP Order:** Splits a large order into smaller timed chunks to reduce slippage.
- **Grid Order:** Places multiple buy/sell limit orders above and below a base price for range trading.

---

## Dependencies

Main dependencies include:

- `python-binance`
- `tabulate`
- `colorama`
- `prettytable` (optional for CLI formatting)
- `dotenv` (optional if using `.env`)

---