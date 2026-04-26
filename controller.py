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
                asset_data = self.view.ask_asset_input()
                self.model.add_asset(asset_data)

            
            elif choice == "2":
                price_choice = self.view.ask_current_and_historical_prices()
                
                if price_choice == "1":
                    ticker = self.view.ask_ticker()
                    current_price = self.model.get_current_price(ticker)
                    self.view.show_current_price(ticker, current_price)

                elif price_choice == "2":
                    ticker = self.view.ask_ticker()
                    historical_price = self.model.get_historical_price(ticker, "1y")

                    self.view.show_historical_price(ticker, historical_price)

                else:
                    continue

            elif choice == "3":
                graph_choice = self.view.ask_graph_choice()
                
                if graph_choice == "1":
                    tickers = self.view.ask_tickers()
                    period = self.view.ask_period()
                    historical_prices_per_ticker = self.model.multiple_historical_prices(tickers, period)
                    graph = self.view.plot_graph(historical_prices_per_ticker)

                else:
                    continue


            elif choice == "4":
                # Function is from model, generating portfolio data
                portfolio_data = self.model.get_portfolio()
                self.view.view_current_portfolio(portfolio_data)

            
            elif choice == "5":
                weight_choice = self.view.ask_calculation_choice()

                if weight_choice == "1":
                    total_value = self.model.total_portfolio_value()
                    self.view.show_total_value(total_value)

                elif weight_choice == "2":
                    weight_per_asset = self.model.weight_calculation("ticker")
                    self.view.show_weight(weight_per_asset)

                elif weight_choice == "3":
                    weight_per_class = self.model.weight_calculation("asset_class")
                    self.view.show_weight(weight_per_class)

                elif weight_choice == "4":
                    weight_per_sector = self.model.weight_calculation("sector")
                    self.view.show_weight(weight_per_sector)
                
                elif weight_choice == "5":
                    continue
            
            elif choice == "7":
                print("done")
                break
                
            else:
                print("Not implemented yet")

            
            '''


            elif choice == "6":
                simulation_results = self.model.function()
                self.view.show_simulation(simulation_results)

            '''


            
