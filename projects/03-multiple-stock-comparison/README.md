# Multiple Stock Comparison

## Project Overview

This project compares the historical performance of multiple stocks and a market benchmark using Python.

## Assets Analaysed

- AAPL
- MSFT
- GOOGL
- SPY

## Tools Used

- Python
- pandas
- NumPy
- matplotlib
- yfinance

## Key Concepts

### Normalised Price

Normalised prices allow different assets to be compared from the same starting point.

### Daily Return

The percentage change in price from one trading day to the next.

### Cumulative Return

Cumulative return shows how the value of an initial investment changes over time.

### Correlation

Correlation measures how similarly different assets move.

## Results

### Normalized Prices

![Normalized Prices](figures/normalized_prices.png)

### Cumulative Returns

![Cumulative Returns](figures/cumulative_returns.png)

### Daily Returns Distribution

![Daily Returns Distribution](figures/daily_returns_distribution.png)

### Correlation Matrix

![Correlation Matrix](figures/correlation_matrix.png)

### Risk-Return Scatter

![Risk Return Scatter](figures/risk_return_scatter.png)

## What I Learned

- How to use pandas DataFrames with multiple columns

## Limitations

- It does not predict future returns
- It ignores dividendsl, transaction costs, and taxes
- Sharpe ratio is calculated using a simplified risk-free rate of 0
