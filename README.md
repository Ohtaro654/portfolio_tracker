# Portfolio Tracker

## Overview

This is a CLI application in which we can track and analyse a simple investment portfolio. This application allows user to:

- Add assets: ticker, sector, asset class, quantity and purchase price. Also keeps asking for ticker until a valid ticker is put in.
- Shows the current price and historical price (past 5 days) of the specified ticker from Yahoo Finance.
- Shows a graph of historical data over the years for one or more tickers. This can be seen for 1 month, 3 months, half a year, 1 year, 3 years or 5 years.
- View current portfolio with ticker, sector, asset class, quantity, purchase price, current price, transaction value and current value in a nicely formatted table.
- Compute portfolio weights for each asset, for each asset class or for each sector.
- Perform a Monte Carlo simulation over next 15 years for 100000 paths, and get summary statistics from this. Also able to plot a histogram to see the distribution for future portfolio value.

## Architecture

The project follows the Model-View-Controller (MVC) design pattern:

- Model: Handles the calculations, simulations and data handling.
- View: Handles the visualisations like the graphs and the input/output.
- Controller: Connects the model and the view to make the whole project flow.

## Installation
Clone the repository:
git clone https://github.com/Ohtaro654/portfolio_tracker
cd portfolio_tracker


pip install -r requirements.txt
python main.py

## How to run

python main.py






