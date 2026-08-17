import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def download_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Download historical stock price data using yfinance.
    """
    df = yf.download(ticker, start=start, end=end)

    if df.empty:
        raise ValueError("No data download. Check the ticker symbol or date range.")

    return df

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add useful financial features to the stock price DataFrame.
    """
    df = df.copy()

    df["Daily Return"] = df["Close"].pct_change()

    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()

    df["Cumulative Return"] = (1 + df["Daily Return"]).cumprod()

    df["Running Max"] = df["Cumulative Return"].cummax()
    df["Drawdown"] = df["Cumulative Return"] / df["Running Max"] - 1

    return df

def print_summary_statistics(df: pd.DataFrame, ticker: str) -> None:
    """
    Print basic summary statistics.
    """
    daily_returns = df["Daily Return"].dropna()

    mean_daily_return = daily_returns.mean()
    daily_volatility = daily_returns.std()

    annualized_return = mean_daily_return * 252
    annualized_volatility = daily_volatility * np.sqrt(252)

    cumulative_return = df["Cumulative Return"].iloc[-1] - 1
    max_drawdown = df["Drawdown"].min()

    print(f"===== {ticker} Stock Analysis =====")
    print(f"Mean daily return: {mean_daily_return:.4%}")
    print(f"Daily volatility: {daily_volatility:.4%}")
    print(f"Annualized return: {annualized_return:.4%}")
    print(f"Annualized volatility: {annualized_volatility:.4%}")
    print(f"Cumulative return: {cumulative_return:.4%}")
    print(f"Maximum drawdown: {max_drawdown:.4%}")

def plot_price_and_moving_averages(df: pd.DataFrame, ticker: str) -> None:
    """
    Plot closing price with moving averages.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close Price")
    plt.plot(df.index, df["MA20"], label="20-Day Moving Average")
    plt.plot(df.index, df["MA50"], label="50-Day Moving Average")

    plt.title(f"{ticker} Price and Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("projects/02-stock-price-analysis/figures/price_and_moving_averages.png")
    plt.show()


def plot_daily_returns_distribution(df: pd.DataFrame, ticker: str) -> None:
    """
    Plot histogram of daily returns.
    """
    plt.figure(figsize=(10, 5))
    plt.hist(df["Daily Return"].dropna(), bins=50, edgecolor="black")

    plt.title(f"{ticker} Daily Returns Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("projects/02-stock-price-analysis/figures/daily_returns_distribution.png")
    plt.show()

def plot_cumulative_return(df: pd.DataFrame, ticker: str) -> None:
    """
    Plot cumulative return over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Cumulative Return"])

    plt.title(f"{ticker} Cumulative Return")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("projects/02-stock-price-analysis/figures/cumulative_return.png")
    plt.show()

def plot_drawdown(df: pd.DataFrame, ticker: str) -> None:
    """
    Plot drawdown over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Drawdown"], color="red")

    plt.title(f"{ticker} Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("projects/02-stock-price-analysis/figures/drawdown.png")
    plt.show()


def main():
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    df = download_stock_data(ticker, start_date, end_date)
    df = add_features(df)

    print(df.head())
    print()
    print_summary_statistics(df, ticker)

    plot_price_and_moving_averages(df, ticker)
    plot_daily_returns_distribution(df, ticker)
    plot_cumulative_return(df, ticker)
    plot_drawdown(df, ticker)


if __name__ == "__main__":
    main()
