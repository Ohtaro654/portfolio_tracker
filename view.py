class Portfolioview:
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
            "Ticker": asset_ticker,
            "Sector": sector,
            "Class": asset_class,
            "quantity": quantity,
            "price": purchase_price
        }
    
    def ask_current_and_historical_prices(self):
        print("Price options")
        print("1. Current price")
        print("2. Historical price")
        print("Back to main menu")

        return input("Choose an option: ")
    
    def create_graph(self):
        print("1. Create graph")
        print("2. Back to main menu")

        return input("Choose an option")
    
    def view_current_portfolio(self):
        

  
