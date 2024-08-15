# Cryptocurrency Data Fetcher
![coinmarketcap.jpg]

This project provides Python scripts to fetch and process historical cryptocurrency data (Bitcoin and Ethereum) using the CoinMarketCap API. The data includes hourly price, market cap, and volume information and can be saved to CSV files.

## Features

- Fetches historical hourly cryptocurrency data for the last 365 days.
- Fetches data for the last 24 hours.
- Saves the fetched data to CSV files.
- Supports both Bitcoin (BTC) and Ethereum (ETH).

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `requests`
  - `datetime`

You can install the required libraries using pip:

```bash
pip install pandas requests
```

## Setup

- Clone the repository:

```bash 
git clone https://github.com/your-username/cryptocurrency-data-fetcher.git
cd cryptocurrency-data-fetcher
```

- Replace the placeholder API key with your own CoinMarketCap API key in the script:

```bash 
apikey = 'your_api_key_here'
```

## Usage
# Fetch Historical Data

- Use the get_historical_data function to fetch historical data for the past year.

```bash
get_historical_data(coin, api_key)
```

# Fetch Last 24 Hours Data

- Use the get_last_24_hours_data function to fetch data for the last 24 hours.
```bash
get_last_24_hours_data(coin, api_key)
```

## License

- This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

- Contributions are welcome! Please feel free to submit a Pull Request.

You can customize this `README.md` file further according to your project specifics.
