import json

import requests
from bs4 import BeautifulSoup

from config import Config


def get_current_exchange_rate(parse_url):
    currencies = []
    for route in ("TRY", "USD", "EUR"):
        url = f"{parse_url}{route}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "lxml")
        currency = soup.find_all('div', class_="finance-currency-plate__currency")[1].text.strip()
        currencies.append({
            "name": route,
            "value": currency
        })

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(currencies, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # url = 'https://finance.rambler.ru/currencies/'
    get_current_exchange_rate(Config.URL)
