import numpy as np

def sharpe_ratio(returns, risk_free_rate):
    """
    Calculate the Sharpe ratio of an investment.

    Parameters:
    returns (array-like): An array or list of investment returns.
    risk_free_rate (float): The risk-free rate of return.

    Returns:
    float: The Sharpe ratio of the investment.
    """
    mean_return = np.mean(returns)
    std_deviation = np.std(returns)
    
    excess_return = mean_return - risk_free_rate
    sharpe_ratio = excess_return / std_deviation
    
    return sharpe_ratio

def sortino_ratio(returns, risk_free_rate):
    """
    Calculate the Sortino ratio of an investment.

    Parameters:
    returns (array-like): An array or list of investment returns.
    risk_free_rate (float): The risk-free rate of return.

    Returns:
    float: The Sortino ratio of the investment.
    """
    mean_return = np.mean(returns)
    downside_returns = [ret - risk_free_rate for ret in returns if ret < risk_free_rate]
    
    downside_std_dev = np.std(downside_returns)
    
    sortino_ratio = (mean_return - risk_free_rate) / downside_std_dev if downside_std_dev != 0 else np.nan
    
    return sortino_ratio


def value_at_risk(returns, alpha=0.95):
    """
    Calculate the value at risk (VaR) of an investment.

    Parameters:

    returns (array-like): An array or list of investment returns.
    alpha (float): The confidence level.

    Returns:
    float: The VaR of the investment.
    """
    var = -np.percentile(returns, alpha * 100)
    return var


def conditional_value_at_risk(returns, alpha=0.95):
    """
    Calculate the conditional value at risk (CVaR) of an investment.

    Parameters:
    returns (array-like): An array or list of investment returns.
    alpha (float): The confidence level.

    Returns:
    float: The CVaR of the investment.
    """
    var = value_at_risk(returns, alpha)
    cvar = -np.mean([ret for ret in returns if ret < -var])
    return cvar

def beta(asset_returns, market_returns=None):
    """
    Calculate the beta of an investment.

    Parameters:
    asset_returns (array-like): An array or list of asset returns.
    market_returns (array-like): An array or list of market returns.

    Returns:
    float: The beta of the investment.
    """

    if market_returns is None:
        market_returns = asset_returns
        print("Info (beta metric): Market returns not provided. Using asset returns as market returns.")
    covar = np.cov(asset_returns, market_returns)[0, 1]
    market_variance = np.var(market_returns)
    
    beta = covar / market_variance if market_variance != 0 else np.nan
    
    return beta
