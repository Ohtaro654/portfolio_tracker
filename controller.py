'''
Controller will connect the view and the model, so we need to import both
'''

from model import PortfolioModel
from view import PortfolioView

class PortfolioController:
    def __init__(self):
        self.model = PortfolioModel()
        self.view = PortfolioView()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.ask_choice()

            if choice == "1":
                # Loop such that only valid tickers are allowed
                while True:
                    asset_data = self.view.ask_asset_input()

                    try:
                        asset_data["quantity"] = float(asset_data["quantity"])
                        asset_data["purchase_price"] = float(asset_data["purchase_price"])
                    except:
                        print("Quantity and purchase price must be numbers, try again.")
                        continue

                    ticker = asset_data["ticker"].upper()
                    current_price = self.model.get_current_price(ticker)

                    if current_price is not None:
                        asset_data["ticker"] = ticker
                        self.model.add_asset(asset_data)
                        break

                    print("Ticker is not valid, try again.")
                    

            
            elif choice == "2":
                price_choice = self.view.ask_current_and_historical_prices()
                
                if price_choice == "1":
                    ticker = self.ask_valid_ticker()
                    current_price = self.model.get_current_price(ticker)
                    self.view.show_current_price(ticker, current_price)
                    self.view.pause()

                elif price_choice == "2":
                    ticker = self.ask_valid_ticker()
                    historical_price = self.model.get_historical_price(ticker, "1y")
                    self.view.show_historical_price(ticker, historical_price)
                    self.view.pause()

                else:
                    continue

            elif choice == "3":
                graph_choice = self.view.ask_graph_choice()
                
                if graph_choice == "1":
                    tickers = self.view.ask_tickers()
                    valid_tickers = []
                    # Loop over every ticker to check if they are valid
                    for ticker in tickers:
                        if self.model.get_current_price(ticker) is not None:
                            valid_tickers.append(ticker)
                        else:
                            print(f"{ticker} is invalid so this will be skipped and not shown in the graph.")

                    period = self.view.ask_period()
                    historical_prices_per_ticker = self.model.multiple_historical_prices(valid_tickers, period)
                    graph = self.view.plot_graph(historical_prices_per_ticker)
                    self.view.pause()

                else:
                    continue

            elif choice == "4":
                # Function is from model, generating portfolio data
                portfolio_data = self.model.get_full_portfolio()
                self.view.view_current_portfolio(portfolio_data)
                self.view.pause()

            elif choice == "5":
                weight_choice = self.view.ask_calculation_choice()

                if weight_choice == "1":
                    total_value = self.model.total_portfolio_value()
                    self.view.show_total_value(total_value)
                    self.view.pause()

                elif weight_choice == "2":
                    weight_per_asset = self.model.weight_calculation("ticker")
                    self.view.show_weight(weight_per_asset)
                    self.view.pause()

                elif weight_choice == "3":
                    weight_per_class = self.model.weight_calculation("asset_class")
                    self.view.show_weight(weight_per_class)
                    self.view.pause()

                elif weight_choice == "4":
                    weight_per_sector = self.model.weight_calculation("sector")
                    self.view.show_weight(weight_per_sector)
                    self.view.pause()
                
                elif weight_choice == "5":
                    continue

            elif choice == "6":
                simulation_results = self.model.simulate_portfolio()
                simulation_choice = self.view.ask_simulation(simulation_results)

                if simulation_choice == "1":
                    self.view.show_statistics_simulation(simulation_results)
                    self.view.pause()

                if simulation_choice == "2":
                    self.view.show_graph_simulation(simulation_results)
                    self.view.pause()

                if simulation_choice == "3":
                    continue

            elif choice == "7":
                portfolio_data = self.model.get_full_portfolio()
                self.view.view_current_portfolio(portfolio_data)

                remove_index = self.view.ask_remove_index()

                try:
                    remove_index = int(remove_index)
                    success = self.model.remove_asset(remove_index)

                    if success:
                        self.view.show_remove_success()
                    else:
                        self.view.show_remove_error()

                except ValueError:
                    self.view.show_remove_error()

                self.view.pause()

            elif choice == "8":
                metrics = self.model.portfolio_risk_metrics()
                self.view.show_risk_metrics(metrics)
                self.view.pause()

            elif choice == "9":
                correlation_matrix = self.model.correlation_matrix()
                self.view.show_correlation(correlation_matrix)
                self.view.pause()

            elif choice == "10":
                print("done")
                break
                
            else:
                print("Not implemented yet")
                self.view.pause()


    # Function to keep asking ticker until you give right one
    # Check by seeing if ticker gives current price
    def ask_valid_ticker(self):
        while True:
            ticker = self.view.ask_ticker().upper()
            price = self.model.get_current_price(ticker)

            if price is not None:
                return ticker
        
            print("Ticker is not valid, try again.")