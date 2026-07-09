# 1. DICTIONARY: Setting up my hardcoded stock prices
prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 330.00,
    "AMZN": 130.00
}

# This dictionary will hold the stocks the user types in
my_portfolio = {}
total_money = 0.0

print("Welcome to my Stock Tracker!")
print("Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN")

# 2. INPUT/OUTPUT & LOOP: Keep asking until they type 'exit'
while True:
    stock_name = input("\nEnter a stock name (or type 'exit' to stop): ")
    # Make it uppercase just in case they typed lowercase
    stock_name = stock_name.upper()
    
    if stock_name == "EXIT":
        break
        
    # Check if the stock is in our dictionary
    if stock_name in prices:
        shares_input = input("How many shares do you have? ")
        shares = float(shares_input) # Converting their text into a decimal number
        
        # BASIC ARITHMETIC: Add it to their portfolio
        if stock_name in my_portfolio:
            # If they already have it, add to the old amount
            my_portfolio[stock_name] = my_portfolio[stock_name] + shares
        else:
            # If it is new, just set the amount
            my_portfolio[stock_name] = shares
            
        print("Okay, added " + str(shares) + " shares of " + stock_name)
    else:
        print("Error: Stock not in the list! Try again.")

# Output the final results
print("\n--- MY PORTFOLIO SUMMARY ---")

for stock in my_portfolio:
    shares = my_portfolio[stock]
    stock_price = prices[stock]
    
    # BASIC ARITHMETIC: multiply shares by the price
    value = shares * stock_price
    total_money = total_money + value
    
    print(stock + " -> " + str(shares) + " shares = $" + str(value))

print("----------------------------")
print("TOTAL MONEY: $" + str(total_money))

# 4. FILE HANDLING: Ask if they want to save
save = input("\nDo you want to save this to a file? (yes/no): ")

if save == "yes" or save == "y":
    # Open a file in write mode ("w")
    my_file = open("saved_portfolio.txt", "w")
    my_file.write("--- MY PORTFOLIO SUMMARY ---\n")
    
    # Loop through again to write into the file
    for stock in my_portfolio:
        shares = my_portfolio[stock]
        stock_price = prices[stock]
        value = shares * stock_price
        
        my_file.write(stock + " -> " + str(shares) + " shares = $" + str(value) + "\n")
        
    my_file.write("----------------------------\n")
    my_file.write("TOTAL MONEY: $" + str(total_money) + "\n")
    
    # Newbies always use file.close() instead of 'with open()'
    my_file.close() 
    print("Awesome! Saved to saved_portfolio.txt")