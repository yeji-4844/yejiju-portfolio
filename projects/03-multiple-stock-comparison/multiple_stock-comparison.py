import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def download_prices(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)

    prices = data["Close"]

    if isinstance(prices, pd.Series):
        prices = prices.to_frame()

    return prices

def calculate_daily_returns(prices):
    daily_returns = prices / prices.shift(1) - 1
    return daily_returns

def calculate_cumulative_returns(daily_returns):
    cumulative_returns = (1 + daily_returns).cumprod()
    return cumulative_returns

def plot_normalized_prices(prices):
    normalized_prices = prices / prices.iloc[0]

    plt.figure(figsize=(12, 6))
    for ticker in normalized_prices.columns:
        plt.plot(normalized_prices[ticker], label=ticker)

    plt.title("Normalized Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Normalized Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("projects/03-multiple-stock-comparison/figures/normalized_prices.png")
    plt.show()

def plot_cumulative_returns(cumulative_returns):
    plt.figure(figsize=(12, 6))
    for ticker in cumulative_returns.columns:
        plt.plot(cumulative_returns.index, cumulative_returns[ticker], label=ticker)

    plt.title("Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("projects/03-multiple-stock-comparison/figures/cumulative_returns.png")
    plt.show()

def plot_returns_distribution(daily_returns):
    plt.figure(figsize=(12, 6))

    for ticker in daily_returns.columns:
        plt.hist(daily_returns[ticker], bins=50, alpha=0.5, label=ticker)

    plt.title("Daily Returns Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("projects/03-multiple-stock-comparison/figures/daily_returns_distribution.png")
    plt.show()

def plot_correlation_matrix(daily_returns):
    correlation = daily_returns.corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(correlation, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar(label="Correlation")

    plt.xticks(range(len(correlation.columns)), correlation.columns)
    plt.yticks(range(len(correlation.columns)), correlation.columns)

    for i in range(len(correlation.columns)):
        for j in range(len(correlation.columns)):
            plt.text(j, i, f"{correlation.iloc[i, j]:.2f}",
                     ha='center', va='center', color='black')

    plt.title("Correlation Matrix of Daily Returns")
    plt.tight_layout()
    plt.savefig("projects/03-multiple-stock-comparison/figures/correlation_matrix.png")
    plt.show()

def plot_risk_return_scatter(daily_returns):
    mean_daily_returns = daily_returns.mean()
    daily_volatility = daily_returns.std()

    annualized_returns = mean_daily_returns * 252
    annualized_volatility = daily_volatility * np.sqrt(252)

    plt.figure(figsize=(8, 6))

    for ticker in daily_returns.columns:
        plt.scatter(annualized_volatility[ticker], annualized_returns[ticker], label=ticker, s=100)
        plt.text(annualized_volatility[ticker], annualized_returns[ticker], ticker, fontsize=10, ha='right')


    plt.title("Risk-Return Comparison")
    plt.xlabel("Annualized Volatility")
    plt.ylabel("Annualized Returns")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("projects/03-multiple-stock-comparison/figures/risk_return_scatter.png")
    plt.show()

def print_summary_statistics(daily_returns):
    mean_daily_returns = daily_returns.mean()
    daily_volatility = daily_returns.std()

    annualized_returns = mean_daily_returns * 252
    annualized_volatility = daily_volatility * np.sqrt(252)

    summary = pd.DataFrame({
        "Annualized Return": annualized_returns,
        "Annualized Volatility": annualized_volatility,
        "Sharpe Ratio": annualized_returns / annualized_volatility
    })

    print("Summary Statistics:")
    print(summary)

def main():
    tickers = ["AAPL", "MSFT", "GOOGL", "SPY"]
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    prices = download_prices(tickers, start_date, end_date)
    daily_returns = calculate_daily_returns(prices)
    cumulative_returns = calculate_cumulative_returns(daily_returns)

    print(prices.head())
    print()
    print_summary_statistics(daily_returns)

    plot_normalized_prices(prices)
    plot_cumulative_returns(cumulative_returns)
    plot_returns_distribution(daily_returns)
    plot_correlation_matrix(daily_returns)
    plot_risk_return_scatter(daily_returns)

if __name__ == "__main__":
    main()
