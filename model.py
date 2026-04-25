class PortfolioModel:
    def __init__(self):
        self.assets = []


    def add_asset(self, asset_data):
        asset = {
            "ticker": asset_data["ticker"].upper(),
            "sector": asset_data["sector"],
            "asset_class": asset_data["asset_class"],
            "quantity": float(asset_data["quantity"]),
            "purchase_price": float(asset_data["purchase_price"])
        }

        self.assets.append(asset)

    def get_portfolio(self):
        return self.assets