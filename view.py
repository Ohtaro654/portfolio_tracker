class portfolioview:
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

        return {
            "ticker": asset_ticker,
            "sector": sector,
            "class": asset_class,
            "quantity": quantity,
            "price": purchase_price
        }
    
    # Option 2
    def ask_current_and_historical_prices(self):
        print("Price options")
        print("1. Current price")
        print("2. Historical price")
        print("3. Back to main menu")

        return input("Choose an option: ")
    
    # Option 3
    def ask_graph_choice(self):
        print("1. Create graph")
        print("2. Back to main menu")

        return input("Choose an option")
    
    # Option 4 Needs data to create table
    def view_current_portfolio(self, portfolio_data):
        if not portfolio_data:
            print("Empty portfolio")
            return
        
        # Still need table
        print(portfolio_data)
        
    # Option 5
    def ask_calculation_choice(self):
        print("1. Total portfolio value")
        print("2. Weights per asset")
        print("3. Weights per asset class")
        print("4. Weights per sector")
        print("5. Back to main menu")

        return input("Choose an option")

    # Option 6
    def show_simulation(self, results):
        print("Simulation over the upcoming 15 years for the porfolio")
        print(results)


  
