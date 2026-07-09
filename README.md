# 📈 Stock Portfolio Tracker

A console-based tool that lets users build a mock stock portfolio using a hardcoded set of stock prices, calculates the total value of their holdings, and optionally saves a summary to a text file.

## Features
- Lets users add shares of predefined stocks (AAPL, TSLA, GOOGL, MSFT, AMZN) to a portfolio
- Handles repeated entries by accumulating share counts for the same stock
- Calculates and displays the value of each holding and the total portfolio value
- Optionally exports the portfolio summary to `saved_portfolio.txt`

## Concepts Demonstrated
- Dictionaries for storing prices and portfolio data
- `while` loops for continuous input
- Basic arithmetic operations
- Type conversion (`float()`)
- File handling (`open()`, `.write()`, `.close()`)

## How to Run
```bash
python tracker.py
```

## Example Interaction
```
Welcome to my Stock Tracker!
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

Enter a stock name (or type 'exit' to stop): AAPL
How many shares do you have? 10
Okay, added 10.0 shares of AAPL
```

## Possible Improvements
- Accept "y" as a shorthand for "yes" when prompted to save
- Use `with open(...)` instead of manual `open()`/`close()` for safer file handling
- Pull live stock prices from an API instead of using hardcoded values
