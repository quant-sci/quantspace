import pandas as pd
import sys
sys.path.append("./")
from quantspace.risk import sharpe_ratio, sortino_ratio, value_at_risk, conditional_value_at_risk, beta

def summary_risk(returns, market_returns=None, risk_free_rate=0.05, alpha=0.95):
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
        'Sortino Ratio': sortino_ratio(returns, risk_free_rate),
        'Value at Risk': value_at_risk(returns, alpha),
        'Conditional Value at Risk': conditional_value_at_risk(returns, alpha),
        'Beta': beta(returns, market_returns),
    }
    table = pd.DataFrame()
    for metric in METRICS:
        table[metric] = [METRICS[metric]]

    return table.T.rename(columns={0: 'Risk Metrics'})
    
    

