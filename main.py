import requests  # getting the data from a URL
# Parsing the data and  extracting things we need.
from bs4 import BeautifulSoup
import time


# Link to the Crypto Currency that you want to track.
all_coins = ["https://cryptocurrencyprices.stockmaster.in/cryptocurrencylive/ADA/cardano/INR/",
             "https://cryptocurrencyprices.stockmaster.in/cryptocurrencylive/MATIC/matic-network/INR/", "https://cryptocurrencyprices.stockmaster.in/cryptocurrencylive/VET/vechain/INR/"]

# Add the name of the crypto and the price at which you bought it.
bought_prices = {"ADA": 110.00, "VET": 8.00, "MATIC": 120.00}

# storing the coin price, coin code and coin Name. This list just stores for now.
coins_prices = []
coins_prices_dict = {}  # storing the current coin prices


def get_prices():
    for i in all_coins:
        val = requests.get(i)  # Getting data from each link in the list
        # Making the text HTML
        soup = BeautifulSoup(val.content, "html.parser")

        # Get the entry-title and get only the price
        current_price = float(
            soup.find('h1', class_="entry-title").get_text().split(" ")[-1][1:-1])
        # Get the Name and ID of the Coin, Splitting using ( instead of space because some coins have names that are two words

        temp = soup.find(
            'div', class_='cmc-logo-style1').findChild("h2").get_text().split("(")
        # Ex "Internet Computer (ICP)" we split using "(" so we get " Internet Computer " and "ICP)"

        # " Internet Computer "  -> "Internet Computer"
        coin_name = temp[0].strip()
        coin_code = temp[1][0:-1]  # "ICP)" -> "ICP"

        # Adding the price coin price, coin code and coin Name to the list
        coins_prices.append([current_price, coin_name, coin_code])

        # useful to see if things are working correctly. Comment out.
        print(current_price, coin_name, coin_code)
        coins_prices_dict[coin_code] = current_price
        # Sending multiple requests all at the same time isnt good.
        time.sleep(2.5)

    print()
    for i in bought_prices.keys():
        # Print out the values based on the crypto code
        print("You bought {} at {} now it is {}".format(
            i, bought_prices[i], coins_prices_dict[i]))


get_prices()
