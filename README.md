# Portfolio Tracker

## Overview

This is a CLI application in which we can track and analyse a simple investment portfolio. This application allows the user to:

1. Add assets: ticker, sector, asset class, quantity and purchase price. The application keeps asking for a ticker until a valid ticker is entered.
2. Show the current price and historical price (past 5 days) of the specified ticker from Yahoo Finance.
3. Show a graph of historical data over the years for one or more tickers. This can be shown for 1 month, 3 months, half a year, 1 year, 3 years or 5 years. I chose predefined options instead of free input because the user might not be familiar with syntax like `1mo` or `1y`.
4. View the current portfolio with ticker, sector, asset class, quantity, purchase price, current price, transaction value and current value in a nicely formatted table.
5. Compute portfolio weights for each asset, asset class or sector.
6. Perform a Monte Carlo simulation over the next 15 years with 100,000 paths, including summary statistics and a histogram of the final portfolio value distribution.
7. Remove assets.
8. Show risk metrics such as VaR and Sharpe ratio.
9. Calculate a correlation matrix to see which assets move together, giving information about portfolio diversification.

## Architecture

The project follows the Model-View-Controller (MVC) design pattern:

- Model: Handles the calculations, simulations and data handling.
- View: Handles the visualisations, graphs and input/output.
- Controller: Connects the Model and View to manage the application flow.

## Installation

Python 3.10–3.12 recommended.

### Mac

git clone https://github.com/Ohtaro654/portfolio_tracker
cd portfolio_tracker

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python main.py

### Windows

git clone https://github.com/Ohtaro654/portfolio_tracker
cd portfolio_tracker

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python main.py