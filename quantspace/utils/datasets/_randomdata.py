import numpy as np

def rand_weights(n):
    """
    Produces n random weights that sum to 1

    Parameters
    ----------
    n : int
        Number of weights to produce

    Returns
    -------
    k : array
        Array of random weights that sum to 1
    """
    k = np.random.rand(n)
    return k / sum(k)

def random_portfolio(returns):
    """
    Returns the mean and standard deviation of returns for a random portfolio

    Parameters
    ----------
    returns : array
        Returns for each stock in the portfolio

    Returns
    -------
    mu : float
        Mean of random portfolio returns
    sigma : float
        Standard deviation of random portfolio returns
    """
    p = np.asmatrix(np.mean(returns, axis=1))
    w = np.asmatrix(rand_weights(returns.shape[0]))
    C = np.asmatrix(np.cov(returns))
    
    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)
    
    if sigma > 2:
        return random_portfolio(returns)
    return mu, sigma