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
        print("7. Remove asset")
        print("8. Show risk metrics portfolio")
        print("9. Exit")
    
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
        
        print(f"Last 5 closing prices for {ticker}:")

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
        tickers = input("Enter tickers separated by commas: ")
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
        plt.xlabel("Date")
        plt.ylabel("Closing Prices")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    
    # Option 4 
    def view_current_portfolio(self, portfolio_data):
        if not portfolio_data:
            print("Empty portfolio")
            return
        
        print(f"{'No.':<5} {'Ticker':<10} {'Sector':<15} {'Asset Class':<15}"
              f"{'Quantity':>10} {'Purchase price':>15} {'Current Price':>15}"
              f"{'Transaction Value':>20} {'Current Value':>20}")
        # Loop over every dictionary inside list
        for i, asset in enumerate(portfolio_data):
            current_price = asset["current_price"]
            current_value = asset["current_value"]

            # For safety if somehow we can not get data from yfinance
            current_price_text = "N/A" if current_price is None else f"{current_price:.2f}"
            current_value_text = "N/A" if current_value is None else f"{current_value:.2f}"


            print(f"{i:<5} {asset['ticker']:<10} {asset['sector']:<15} {asset['asset_class']:<15}"
                  f"{asset['quantity']:>10.2f} {asset['purchase_price']:>15.2f} {current_price_text:>15}"
                  f"{asset['transaction_value']:>20.2f} {current_value_text:>20}")

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
    def ask_simulation(self, results):
        if results is None:
            print("Simulation could not be performed")
            return
        
        print("1. Show the statistics")
        print("2. Show histogram for the simulations")
        print("3. Back to main menu")

        return input("Choose an option: ")

    def show_statistics_simulation(self, results):
        print("15 year Monte Carlo simulation with 100000 paths")
        print(f"Initial portfolio value: {results['initial value']:.2f}")
        print(f"Mean final value: {results['mean final value']:.2f}")
        print(f"Median final value: {results['median final value']:.2f}")
        print(f"5th percentile: {results['5_percentile']}")
        print(f"95th percentile: {results['95_percentile']:.2f}")

    
    def show_graph_simulation(self, results):
        final_values = results["final values"]
        initial_value = results["initial value"]
        mean = results["mean final value"]
        median = results["median final value"]
        p5 = results["5_percentile"]
        p95 = results["95_percentile"]

        plt.figure(figsize = (12, 6))
        plt.hist(final_values, bins = 100)

        plt.axvline(initial_value, linestyle = "dashed", label = "Initial Value", color = "red")
        plt.axvline(mean, linestyle = "dashed", label = "Mean")
        plt.axvline(median, linestyle = "dashed", label = "Median")
        plt.axvline(p5, linestyle = "dashed", label = "5th percentile")
        plt.axvline(p95, linestyle = "dashed", label = "95th percentile")

        plt.title("Distribution of final portfolio value")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

        plt.legend()
        plt.grid(True)

        plt.show()

    # Point 7
    def ask_remove_index(self):
        return input("Which asset do you want to remove (enter the index): ")
    
    def show_remove_success(self):
        print("Asset removed successfully!")

    def show_remove_error(self):
        print("Invalid asset number.")

    
    # Point 8

    def show_risk_metrics(self, metrics):
        if metrics is None:
            print("Risk metrics could not be calculated.")
            return
        
        print("Portfolio risk metrics:")
        print(f"Annualised return: {metrics["annual return"]:.2%}")
        print(f"Annualised volatility: {metrics["annual volatility"]:.2%}")

        if metrics is None:
            print("Sharpe ratio is not computable.")
        else:
            print(f"Sharpe ratio: {metrics["sharpe ratio"]:.2f}")
        
        print(f"95% daily value at risk: {metrics["95% VaR"]:.2%}")



        # Function such that program does not immediately go to the main menu, cleaner
    def pause(self):
        input("\nPress Enter to return the main menu: ")



        


  
