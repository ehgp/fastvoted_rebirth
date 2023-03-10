"""Get Liquor Lottery Market Data.

Pull MOCO lottery file and put table data into a dataframe to compare against Google Shopping data to get a multiplier for the price of the liquor so we can choose the liquor that will profit the most if lottery is won."""

import os
import random
import re
import time
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = ''
title = 'moco_lottery_liquor'
path = Path(os.getcwd())


def save_html_to_file(response, title):
    """Save response to response.html."""
    with open(
        Path(path, f"{title}.html"),
        "w",
        encoding="utf-8",
    ) as fp:
        fp.write(response)


if __name__ == "__main__":
    if Path.is_file(Path(path, f"{title}.html")):
        print("File exists")
        with open(
            Path(path, f"{title}.html"),
            "r",
            encoding="utf-8",
        ) as fp:
            soup = BeautifulSoup(fp, 'lxml')
            titles = soup.find_all('p', {'class': 'well'})
            tables = soup.find_all('table', {'width': '100%'})
            for i in range(len(tables)):
                title = titles[i].text.split('\n\n', 1)[0]
                # print(title)
                table = pd.read_html(str(tables[i]))
                table[0].reset_index(drop=True)
                # print(table[0])
                # print('-------------------------------------')
                prices_sorted_filtered_list = []
                multipliers_list = []
                for i in range(len(table[0].Description)):
                    # print(description.replace(' (HAL)', ''))
                    time.sleep(random.randint(3, 5))
                    response = requests.get(
                        f'https://www.google.com/search?q=%22{table[0].Description[i].replace(" (HAL)", "")}%22&hl=en&tbm=shop&tbs=p_ord:r',
                        headers={
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "accept-encoding": "gzip, deflate, br",
                            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                            "origin": "https://www.google.com",
                        },
                        # proxies={"https": "https://"},
                    )
                    soup = BeautifulSoup(response.content, "lxml")
                    prices = re.findall(
                        r"\$[0-9]+\.[0-9][0-9]?",
                        soup.text,
                    )
                    print(prices)
                    prices_sorted = sorted(
                        [
                            float("".join(c for c in price if c != '$' and c != ','))
                            for price in prices
                        ],
                        key=float,
                    )
                    lottery_price = float(
                        "".join(c for c in table[0].Price[i] if c != '$' and c != ',')
                    )
                    prices_sorted_filtered = [
                        x for x in prices_sorted if x >= lottery_price
                    ]
                    multipliers = [x / lottery_price for x in prices_sorted_filtered]
                    print(prices_sorted_filtered)
                    print(lottery_price)
                    print(multipliers)
                    prices_sorted_filtered_list.append(prices_sorted_filtered)
                    multipliers_list.append(multipliers)
                table[0].assign(
                    MarketPrices=prices_sorted_filtered_list,
                    Multipliers=multipliers_list,
                )
                table[0].to_csv(Path(path, f"{title}.csv"), index=False)
    else:
        page = requests.get(url)
        save_html_to_file(page.text, title)
