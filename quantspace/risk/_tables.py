import pandas as pd
import sys
sys.path.append("./")
from quantspace.risk import sharpe_ratio

def summary_risk(returns, risk_free_rate):
    """
    Calculate the Sharpe ratio of an investment.

    Parameters:
    returns (array-like): An array or list of investment returns.
    risk_free_rate (float): The risk-free rate of return.

    Returns:
    float: The Sharpe ratio of the investment.
    """
    METRICS = {
        'Sharpe Ratio': sharpe_ratio(returns, risk_free_rate),
    }
    table = pd.DataFrame()
    for metric in METRICS:
        table[metric] = [METRICS[metric]]

    return table
    
    

