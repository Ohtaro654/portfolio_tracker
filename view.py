import matplotlib.pyplot as plt

class PortfolioView:
    # Choices 
    def show_menu(self):
        print("Option choices")
        print("1. Add assets")
        print("2. current and historical prices")
        print("3. graphs for ticker")
        print("4. View current portfolio")
        print("5. Calculations total portfolio")
        print("6. Simulation over 15 years")
        print("7. Exit")
    
    # Ask for choice (number input) 
    def ask_choice(self):
        return input("Choose an option: ")
    
    # For option 1
    def ask_asset_input(self):
        asset_ticker = input("Asset ticker: ")
        sector = input("sector: ")
        asset_class = input("asset_class: ")
        quantity = input("quantity: ")
        purchase_price = input("purchase price: ")

        # Return a dictionary
        return {
            "ticker": asset_ticker,
            "sector": sector,
            "asset_class": asset_class,
            "quantity": quantity,
            "purchase_price": purchase_price
        }
    
    # Option 2
    def ask_current_and_historical_prices(self):
        print("Price options")
        print("1. Current price")
        print("2. Historical price")
        print("3. Back to main menu")

        return input("Choose an option: ")
    
    def ask_ticker(self):
        return input("For which stock do you want to see data: ")
    
    def show_current_price(self, ticker, price):
        if price is None:
            print("No data available")
            return
        
        print(f"The current price for {ticker} is {price:.2f}.")

    '''
    Maybe let the user manually input this
    '''
    def ask_period(self):
        print("Choose period: ")
        print("1. 1 month")
        print("2. 3 months")
        print("3. Half a year")
        print("4. 1 year")
        print("5. 3 years")
        print("6. 5 years")

        choice = input("Choose an option: ")
        if choice == "1":
            return "1mo"
        elif choice == "2":
            return "3mo"
        elif choice == "3":
            return "6mo"
        elif choice == "4":
            return "1y"
        elif choice == "5":
            return "3y"
        elif choice == "6":
            return "5y"
        else:
            return "1mo"

    def show_historical_price(self, ticker, prices):
        if prices is None:
            print("No data available")
            return
        
        print(f"Print the last 5 closing prices for {ticker}.")

        last_5_days = prices.tail(5)

        for date, value in last_5_days.items():
            print(f"{date.date()} | {value:.2f}")

    
    '''
    Maybe add log differences of stocks
    '''
    # Option 3
    def ask_graph_choice(self):
        print("1. Create graph")
        print("2. Back to main menu")

        return input("Choose an option: ")
    
    # Returns a list with tickers
    def ask_tickers(self):
        tickers = input("Enter tickers seperated by comma's: ")
        return [ticker.strip().upper() for ticker in tickers.split(",")]
    
    # Prices from the model, dictionary with ticker as key and series with date and closing price as value
    def plot_graph(self, prices):
        if not prices:
            print("No data available")
            return
        
        plt.figure(figsize = (12, 6))

        for ticker, price_series in prices.items():
            plt.plot(price_series.index, price_series.values, label = ticker)

        plt.title("Historical closing prices")
        plt.xlabel("Data")
        plt.ylabel("closing prices")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    
    # Option 4 
    def view_current_portfolio(self, portfolio_data):
        if not portfolio_data:
            print("Empty portfolio")
            return
        
        print("Ticker | Sector | Asset Class | Quantity | Purchase Price | current price | transaction value | current value")
        # Loop over every dictionary inside list
        for asset in portfolio_data:
            print(f"{asset['ticker']} | {asset['sector']} | {asset['asset_class']} | {asset['quantity']} | {asset['purchase_price']}, {asset['current_price']} | {asset['transaction_value']} | {asset['current_value']}")
        
    # Option 5
    def ask_calculation_choice(self):
        print("1. Total portfolio value")
        print("2. Weights per asset")
        print("3. Weights per asset class")
        print("4. Weights per sector")
        print("5. Back to main menu")

        return input("Choose an option: ")
    
    # Print total asset value
    def show_total_value(self, total_value):
        print(f"Total portfolio value: {total_value:.2f}")
    
    def show_weight(self, weights):
        if not weights:
            print("There are no weights")
            return
        
        for key, value in weights.items():
            print(f"{key}: {value:.2%}")

    # Option 6
    def show_simulation(self, results):
        print("Simulation over the upcoming 15 years for the porfolio")
        print(results)


  
