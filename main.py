# MIT License
# 
# Copyright (c) 2024 Maaz Jamshaid
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pandas as pd
import requests
from datetime import datetime, timedelta

class CryptoDataFetcher:
    def __init__(self, api_key: str, coin: str):
        self.api_key = api_key
        self.coin = coin
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key
        }

    def _get_data(self, start_time: datetime, end_time: datetime):
        parameters = {
            'symbol': self.coin,
            'convert': 'USD',
            'time_start': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'time_end': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'interval': 'hourly'
        }

        response = requests.get(self.url, headers=self.headers, params=parameters)
        data = response.json()

        if 'data' in data and 'quotes' in data['data']:
            timestamps = [entry['timestamp'] for entry in data['data']['quotes']]
            prices = [entry['quote']['USD']['price'] for entry in data['data']['quotes']]
            market_caps = [entry['quote']['USD']['market_cap'] for entry in data['data']['quotes']]
            volumes = [entry['quote']['USD']['volume_24h'] for entry in data['data']['quotes']]

            df = pd.DataFrame({
                'Timestamp': pd.to_datetime(timestamps),
                'Price': prices,
                'Market Cap': market_caps,
                'Volume (24h)': volumes
            })

            return df
        else:
            print("No data found or an error occurred.")
            return pd.DataFrame()

    def fetch_historical_data(self, days: int = 365):
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)

        df = self._get_data(start_time, end_time)
        if not df.empty:
            df.to_csv(f'{self.coin}_hourly_data.csv', index=False)
            print(f"Data saved to {self.coin}_hourly_data.csv")

    def fetch_last_24_hours_data(self):
        end_time = datetime.now()
        start_time = end_time - timedelta(days=1)

        df = self._get_data(start_time, end_time)
        if not df.empty:
            df.to_csv(f'{self.coin}_last_24_hours.csv', index=False)
            print(f"Data saved to {self.coin}_last_24_hours.csv")

# Usage example
if __name__ == "__main__":
    api_key = "API KEY"
    coin = "BTC"

    fetcher = CryptoDataFetcher(api_key, coin)
    fetcher.fetch_historical_data()
    fetcher.fetch_last_24_hours_data()
