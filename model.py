import yfinance as yf
import numpy as np
import pandas as pd

class PortfolioModel:
    def __init__(self):
        # List with dictionaries as entries, every dictionary is about the stock you purchased
        self.assets = []

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
        
        # iloc for safety, probably not intraday so fine
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
        total_value = sum(asset["quantity"] * self.get_current_price(asset["ticker"]) for asset in self.assets
                          if self.get_current_price(asset["ticker"]) is not None)
        return total_value

    # Calculate the weights
    def weight_calculation(self, group):
        total_value = self.total_portfolio_value()
        if total_value == 0:
            return {}

        weights = {}

        for asset in self.assets:
            key = asset[group]
            current_price = self.get_current_price(asset["ticker"])
            if current_price is None:
                continue


            value = asset["quantity"] * current_price
            if key not in weights:
                weights[key] = 0
            
            weights[key] += value
        
        for key in weights:
            weights[key] /= total_value

        return weights
    

    # Point 6
    # Function to calculate how much each ticker contributes to total portfolio, if we have 2 apple entries, then combine them
    def aggregated_weights(self):
        aggregated_values = {}

        for asset in self.assets:
            ticker = asset["ticker"]
            value = asset["quantity"] * asset["purchase_price"]

            if ticker not in aggregated_values:
                aggregated_values[ticker] = 0

            aggregated_values[ticker] += value

        total_value = sum(aggregated_values.values())

        if total_value == 0:
            return {}
        
        weights = {}

        for ticker, value in aggregated_values.items():
            weights[ticker] = value / total_value

        return weights


    def simulate_portfolio(self, years = 15, paths = 100000):
        if not self.assets:
            return None
        
        # Weights per ticker, if we have two same ticker they get combined
        weights = self.aggregated_weights()
        if not weights:
            return None
        
        tickers = list(weights.keys())
        # Dictionary, every key is ticker and values are the historical prices as series with dates
        historical_prices = {}

        # For every ticker get the 5 year historical prices
        for ticker in tickers:
            prices = self.get_historical_price(ticker, "5y")

            if prices is not None and not prices.empty:
                historical_prices[ticker] = prices

        if not historical_prices:
            return None
        
        # Keys become column names, and the values become the columns, while the dates stay that way.
        price_data = pd.DataFrame(historical_prices).dropna()

        if price_data.empty:
            return None
        
        # Convert dataframe with closing prices to daily returns, where we drop the first row
        daily_returns = price_data.pct_change().dropna()

        if daily_returns.empty:
            return None
        
        # For dot product turn it into np.array, and then reorder the weights vector such that it matches daily_returns
        weight_vector = np.array([weights[ticker] for ticker in price_data.columns])

        # Matrix vector multiplication, now each row is daily returns of all tickers adjusted by weight
        portfolio_returns = daily_returns.dot(weight_vector)

        # On internet, average trading days per year is 252. This gives average trading return and volatilty in a year
        annual_mean = portfolio_returns.mean() * 252
        annual_volatility = portfolio_returns.std() * np.sqrt(252)

        initial_portfolio_value = self.total_portfolio_value()

        # Generates 100000 x 15 matrix, every row is simulated future
        simulated_returns = np.random.normal(annual_mean, annual_volatility, size = (paths, years))

        # Multiply initial portfolio value with the entire row, this is still 100000 x 15 matrix, but we compound each time
        simulated_values = initial_portfolio_value * np.cumprod(1 + simulated_returns, axis = 1)

        # Only extract the last column
        final_values = simulated_values[:,-1]

        return{
            "initial value": initial_portfolio_value,
            "mean final value": np.mean(final_values),
            "median final value": np.median(final_values),
            "5_percentile": np.percentile(final_values, 5),
            "95_percentile": np.percentile(final_values, 95),
            "final values": final_values
        }
    
    # Point 7
    def remove_asset(self, index):
        if index < 0 or index >= len(self.assets):
            return False
        
        self.assets.pop(index)
        return True
    
    # Point 8
    def portfolio_risk_metrics(self):
        if not self.assets:
            return None
        
        weights = self.aggregated_weights()
        if not weights:
            return None
        
        tickers = list(weights.keys())
        historical_prices = {}

        for ticker in tickers:
            prices = self.get_historical_price(ticker, "5y")
            if prices is not None and not prices.empty:
                historical_prices[ticker] = prices

        if not historical_prices:
            return None
        
        price_data = pd.DataFrame(historical_prices).dropna()

        if price_data.empty:
            return None
        
        # Convert dataframe with closing prices to daily returns, where we drop the first row
        daily_returns = price_data.pct_change().dropna()

        if daily_returns.empty:
            return None
        
        weight_vector = np.array([weights[ticker] for ticker in price_data.columns])

        portfolio_returns = daily_returns.dot(weight_vector)

        annual_mean = portfolio_returns.mean() * 252
        annual_volatility = portfolio_returns.std() * np.sqrt(252)

        if annual_volatility == 0:
            sharpe_ratio = None
        else:
            sharpe_ratio = annual_mean / annual_volatility
        
        var_95 = np.percentile(portfolio_returns, 5)

        return{
            "annual return": annual_mean,
            "annual volatility": annual_volatility,
            "sharpe ratio": sharpe_ratio,
            "95% VaR": var_95
        }
    

    # Point 9
    def correlation_matrix(self):
        if not self.assets:
            return None
        
        # Extract all individual tickers
        tickers = list(set(asset["ticker"] for asset in self.assets))

        # Dictionary with ticker as key and series of historical prices as value
        historical_prices = self.multiple_historical_prices(tickers, "1y")

        # Dates on left, tickers as column names and series as columns
        prices = pd.DataFrame(historical_prices).dropna()

        if prices.empty:
            return None
        
        # Every row becomes difference
        returns = prices.pct_change().dropna()

        if returns.empty:
            return None
        
        # Correlation matrix, 5 tickers means 5x5 matrix
        correlation = returns.corr()
        return correlation