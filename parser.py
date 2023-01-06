import json

import requests
from bs4 import BeautifulSoup

from config import Config


def get_current_exchange_rate(parse_url):
    response = requests.get(parse_url).text
    soup = BeautifulSoup(response, "lxml")

    currency = soup.find_all('tr')
    need_cur = []
    # c = soup.find_all('a',
    #                   class_="finance-currency-table__tr"
    #                   )
    # l = len(c)
    for i in range(1, len(currency)):
        item = currency[i].text.strip().split('\n')[1:]
        cur_name = item[0]
        count = item[1]
        name = item[2]
        price = item[3]

        if cur_name in ("EUR", "USD", "TRY"):
            price = price.replace(",", ".")
            if count != "1":
                count = "1"
                price = float(price) / 10
            to_dict = {
                "currency": cur_name,
                "count": count,
                "name": name,
                "price": price
            }
            need_cur.append(to_dict)
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(need_cur, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # url = 'https://finance.rambler.ru/currencies/'
    get_current_exchange_rate(Config.URL)
