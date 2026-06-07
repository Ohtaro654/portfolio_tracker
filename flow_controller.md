## Flow controller

### Initialisation

- Call the model and the view to use in the entire flow.

### The main loop

- Call the show_menu function(view) to show the options, and then call the ask_choice function (view) to ask for which option you want to choose. 
 
 #### Option 1 (add assets)

 - Begin with while true loop, do this to ensure that the user provides valid input. We call the ask_asset_input function (view) such that user can put in the ticker, sector, asset_class, quantity and price which is put in dictionary.

 - First check if the price and quantity can be converted to float (so no strings like ten). Then look if the ticker is valid, to do this turn the ticker in upper and call the get_current_price function (model) to look if we can even get a price (if it is not a valid ticker, then returns None). If this price is not none, then add this to the list with dictionaries (where each dictionary is an asset) using add_asset function (model). Note that asset_data["ticker"] = ticker is technically redundant.

 #### Option 2 (Current and historical prices)

- We have three choices, ask these and ask for input using ask_current_and_historical_prices (view).

##### Option 1 (Current price)

- 