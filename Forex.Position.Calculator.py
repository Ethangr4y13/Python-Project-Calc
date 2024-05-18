import tkinter as tk
from tkinter import messagebox
import yfinance as yf


def submit():
    symbol = symbol_entry.get()
    account_balance = float(account_balance_entry.get())
    risk_tolerance = float(risk_tolerance_entry.get())
    stop_loss = float(stop_loss_entry.get())

    try:
        if symbol in ["GBPUSD", "EURUSD", "USDCHF", "USDCAD", "GBPCAD"]:
            p_value = 0.0001
            lots = ((account_balance * risk_tolerance) / (stop_loss * p_value)) / 10000000
            output_label.config(text=f"{lots} standard lots")
        elif symbol == "USDJPY":
            symbol_ticker = 'USDJPY=X'
            ticker = yf.Ticker(symbol_ticker)
            data = ticker.history(period='1d')
            ask_price = data['Close'].iloc[-1]
            lots = ((account_balance * (ask_price / stop_loss)) / 100000)
            output_label.config(text=f"Ask price for {symbol}: ${ask_price:.2f}\n{lots} standard lots")
        elif symbol == "GBPJPY":
            symbol_ticker = 'GBPJPY=X'
            ticker = yf.Ticker(symbol_ticker)
            data = ticker.history(period='1d')
            ask_price = data['Close'].iloc[-1]
            lots = ((account_balance * (ask_price / stop_loss)) / 100000)
            output_label.config(text=f"Ask price for {symbol}: ${ask_price:.2f}\n{lots} standard lots")
        else:
            output_label.config(text="Invalid Symbol")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Forex Position Size Calculator (Std Lots)")

root.configure(bg='black')

fields = [("Symbol: ", 0), ("Account Balance: ", 1), ("Risk Tolerance (%): ", 2), ("Stop loss (pips): ", 3)]
entries = {}

for field, row in fields:
    label = tk.Label(root, text=field, fg='white', bg='blue', font=('Arial', 12, 'bold',))
    label.grid(row=row, column=0, padx=10, pady=10, sticky='e')

    entry = tk.Entry(root, bg='blue', fg='white', font=('Arial', 12))
    entry.grid(row=row, column=1, padx=10, pady=10)
    entries[field] = entry

symbol_entry = entries["Symbol: "]
account_balance_entry = entries["Account Balance: "]
risk_tolerance_entry = entries["Risk Tolerance (%): "]
stop_loss_entry = entries["Stop loss (pips): "]

submit_button = tk.Button(root, text="Submit", command=submit, bg='green', fg='black', font=('Arial', 12, 'bold'))
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

output_label = tk.Label(root, text="", fg='white', bg='blue', font=('Arial', 14, 'bold'))
output_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()


