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