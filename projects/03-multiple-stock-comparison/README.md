# Multiple Stock Comparison

This project compares the historical performance and risk of Apple (AAPL), Microsoft (MSFT), Alphabet (GOOGL), and the S&P 500 ETF (SPY).

## Analysis

- Downloads daily closing prices from Yahoo Finance for 2020-01-01 through 2025-01-01.
- Calculates daily and cumulative returns.
- Compares normalized price performance and daily return distributions.
- Measures correlations between each asset's daily returns.
- Reports annualized return, annualized volatility, and Sharpe ratio.

## Generated Figures

- `normalized_prices.png`: normalized price growth from a common starting value.
- `cumulative_returns.png`: growth of an initial $1 investment.
- `daily_returns_distribution.png`: distribution of daily returns for each asset.
- `correlation_matrix.png`: correlation between daily returns.
- `risk_return_scatter.png`: annualized risk-return comparison.

## Run

From the repository root, install the dependencies and run:

```bash
python projects/03-multiple-stock-comparison/multiple_stock-comparison.py
```

The script prints summary statistics and saves the figures in the `figures/` directory. An internet connection is required to download the market data.
