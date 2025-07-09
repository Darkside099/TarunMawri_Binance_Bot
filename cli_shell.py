import os
import sys
import cmd
import json

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.stop_limit import place_stop_limit_order
from advanced.oco import place_oco_order
from advanced.twap import place_twap_order
from advanced.grid_strategy import place_grid_orders
from tabulate import tabulate

BANNER = r"""
  ____  _                            __       _             _             
 |  _ \(_)                          / _|     | |           | |            
 | |_) |_ _ __   __ _  ___ ___ ___| |_ ___  | | ___   __ _| |_ ___  _ __ 
 |  _ <| | '_ \ / _` |/ __/ __/ _ \  _/ _ \ | |/ _ \ / _` | __/ _ \| '__|
 | |_) | | | | | (_| | (_| (_|  __/ ||  __/ | | (_) | (_| | || (_) | |   
 |____/|_|_| |_|\__,_|\___\___\___|_| \___| |_|\___/ \__,_|\__\___/|_|   

             C L I   T R A D I N G   B O T   (BINANCE FUTURES)
"""



def print_response(response):
    if isinstance(response, dict):
        print("\nOrder Executed:")
        # Flatten nested dictionaries (e.g., OCO orders)
        if 'take_profit' in response and 'stop_loss' in response:
            print("\n[Take Profit Order]")
            tp_data = [(k, v) for k, v in response['take_profit'].items()]
            print(tabulate(tp_data, headers=["Field", "Value"], tablefmt="grid"))

            print("\n[Stop Loss Order]")
            sl_data = [(k, v) for k, v in response['stop_loss'].items()]
            print(tabulate(sl_data, headers=["Field", "Value"], tablefmt="grid"))
        else:
            data = [(k, v) for k, v in response.items()]
            print(tabulate(data, headers=["Field", "Value"], tablefmt="grid"))

    elif isinstance(response, str):
        print("\n" + response)
    else:
        print("\nDone.")



class BinanceShell(cmd.Cmd):
    intro = BANNER + "\nWelcome to the Binance Futures CLI Bot Shell. Type 'help' or '?' to list commands.\n"
    prompt = "binance > "

    def do_market(self, line: str):
        """Place a Market Order: market <symbol> <side> <quantity>
Example: market BTCUSDT BUY 0.01"""
        try:
            symbol, side, qty = line.split()
            response = place_market_order(symbol, side, qty)
            print_response(response)
        except ValueError:
            print("Usage: market <symbol> <side> <quantity>\nExample: market BTCUSDT BUY 0.01")

    def do_limit(self, line: str):
        """Place a Limit Order: limit <symbol> <side> <quantity> <price>
Example: limit BTCUSDT SELL 0.01 58000"""
        try:
            symbol, side, qty, price = line.split()
            response = place_limit_order(symbol, side, qty, price)
            print_response(response)
        except ValueError:
            print("Usage: limit <symbol> <side> <quantity> <price>\nExample: limit BTCUSDT SELL 0.01 58000")

    def do_stoplimit(self, line: str):
        """Place a Stop-Market Order: stoplimit <symbol> <side> <quantity> <stop_price> <0>
Example: stoplimit BTCUSDT BUY 0.01 58000 0"""
        try:
            symbol, side, qty, stop_price, limit_price = line.split()
            response = place_stop_limit_order(symbol, side, qty, stop_price, limit_price)
            print_response(response)
        except ValueError:
            print("Usage: stoplimit <symbol> <side> <quantity> <stop_price> <limit_price>\nExample: stoplimit BTCUSDT BUY 0.01 58000 0")

    def do_oco(self, line: str):
        """Place OCO-style TP & SL: oco <symbol> <side> <quantity> <tp_price> <sl_price>
Example: oco BTCUSDT BUY 0.01 60000 55000"""
        try:
            symbol, side, qty, tp_price, sl_price = line.split()
            response = place_oco_order(symbol, side, qty, tp_price, sl_price)
            print_response(response)
        except ValueError:
            print("Usage: oco <symbol> <side> <quantity> <tp_price> <sl_price>\nExample: oco BTCUSDT BUY 0.01 60000 55000")

    def do_twap(self, line: str):
        """Place TWAP Order: twap <symbol> <side> <total_quantity> <chunks>
Example: twap BTCUSDT BUY 0.05 5"""
        try:
            symbol, side, qty, chunks = line.split()
            response = place_twap_order(symbol, side, qty, int(chunks))
            print_response(response)
        except ValueError:
            print("Usage: twap <symbol> <side> <total_quantity> <chunks>\nExample: twap BTCUSDT BUY 0.05 5")

    def do_grid(self, line: str):
        """Place Grid Orders: grid <symbol> <base_price> <grid_size> <gap_percent> <quantity>
Example: grid BTCUSDT 58000 3 1 0.01"""
        try:
            symbol, base_price, grid_size, gap, qty = line.split()
            response = place_grid_orders(symbol, float(base_price), int(grid_size), float(gap), qty)
            print_response(response)
        except ValueError:
            print("Usage: grid <symbol> <base_price> <grid_size> <gap_percent> <quantity>\nExample: grid BTCUSDT 58000 3 1 0.01")

    def do_clear(self, _: str):
        """Clear the screen (but keep the banner)"""
        os.system("cls" if os.name == "nt" else "clear")
        print(BANNER)
        print("Welcome to the Binance Futures CLI Bot Shell. Type 'help' or '?' to list commands.\n")


    def do_exit(self, _: str):
        """Exit the bot"""
        print("Exiting Binance CLI Shell.")
        return True

    def default(self, line: str):
        print(f"Unknown command: {line}. Type 'help' to see available commands.")


if __name__ == "__main__":
    BinanceShell().cmdloop()
