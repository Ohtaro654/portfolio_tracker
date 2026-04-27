import yfinance as yf

class PortfolioModel:
    def __init__(self):
        # List with dictionaries as entries, evey dictionary is about the stock you purchased
        self.assets = []

    '''
    Maybe add removing asset
    '''
    # Point 1
    def add_asset(self, asset_data):
        asset = {
            "ticker": asset_data["ticker"].upper(),
            "sector": asset_data["sector"],
            "asset_class": asset_data["asset_class"],
            "quantity": float(asset_data["quantity"]),
            "purchase_price": float(asset_data["purchase_price"])
        }

        self.assets.append(asset)

    # Point 2
    # Get the current price
    def get_current_price(self, ticker):
        stock = yf.Ticker(ticker)
        data = stock.history(period = "1d")
        
        if data.empty:
            return None
        
        # Iloc for safety, probably not intraday so fine
        return data["Close"].iloc[-1]


    def get_historical_price(self, ticker, time_period):
        stock = yf.Ticker(ticker)
        data = stock.history(period = time_period)

        if data.empty:
            return None

        return data["Close"]

    
    # Point 3

    # Gives back dictionary, with each entry a ticker as key and historical prices as value
    def multiple_historical_prices(self, tickers, period):
        prices = {}

        for ticker in tickers:
            price = self.get_historical_price(ticker, period)

            if price is not None and not price.empty:
                prices[ticker] = price
        
        return prices
        
        
    # Option 4

    def get_portfolio(self):
        return self.assets
    
    def get_full_portfolio(self):
        # Need to add things to dictionary in list iteration
        full_assets = []

        for asset in self.assets:
            ticker = asset["ticker"]
            current_price = self.get_current_price(ticker)
            quantity = asset["quantity"]
            purchase_price = asset["purchase_price"]

            transaction_value = quantity * purchase_price

            if current_price is None:
                current_value = None
            else:
                current_value = quantity * current_price

            # Take a copy of dictionary, we do not want to change the original assets list
            # new_asset is a dictionary, and we will modify this instead of the original asset
            new_asset = asset.copy()

            new_asset["current_price"] = current_price
            new_asset["transaction_value"] = transaction_value
            new_asset["current_value"] = current_value
            full_assets.append(new_asset)

        return full_assets

    # Point 5
    def total_portfolio_value(self):
        total_value = sum(asset["quantity"] * asset["purchase_price"] for asset in self.assets)
        return total_value

    # Calculate the weights
    def weight_calculation(self, group):
        total_value = self.total_portfolio_value()
        if total_value == 0:
            return {}

        weights = {}

        for asset in self.assets:
            key = asset[group]
            value = asset["quantity"] * asset["purchase_price"]
            if key not in weights:
                weights[key] = 0
            
            weights[key] += value
        
        for key in weights:
            weights[key] /= total_value

        return weights
    

