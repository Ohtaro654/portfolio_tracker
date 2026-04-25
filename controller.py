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

            elif choice == "4":
                # Function is from model, generating portfolio data
                portfolio_data = self.model.get_portfolio()
                self.view.view_current_portfolio(portfolio_data)
            
            elif choice == "7":
                print("done")
                break
                
            else:
                print("Not implemented yet")

            
            '''
            elif choice == "2":
                price_choice = self.view.ask_current_and_historical_prices()
                # Put this chosen option into function in model

            elif choice == "3":
                graph_choice = self.view.ask_graph_choice()
                # Pass this graph choice into function in model

            elif choice == "5":
                portfolio_info_choice = self.view.ask_calculation_choice()

            elif choice == "6":
                simulation_results = self.model.function()
                self.view.show_simulation(simulation_results)

            '''


            
