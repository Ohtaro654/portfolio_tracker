import yfinance as yf

class PortfolioModel:
    def __init__(self):
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


    def get_historical_price(self, ticker):
        stock = yf.Ticker(ticker)
        data = stock.history(period = "1mo")

        if data.empty:
            return None

        return data["Close"]


    def get_portfolio(self):
        return self.assets
    

    # Point 4
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
    

