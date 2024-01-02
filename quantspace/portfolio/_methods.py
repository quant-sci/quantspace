import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers

# using cvxopt [https://cvxopt.org/index.html] to solve quadratic programming problems

solvers.options['show_progress'] = False

plt.style.use('dark_background')

class MarkowitzFrontier:
    def __init__(self, returns, stds, means):
        self.returns = returns
        self.stds = stds
        self.means = means
    
    def optimal_portfolio(self):
        n = len(self.returns)
        self.returns = np.asmatrix(self.returns)
        
        N = 100
        mus = [10**(5.0 * t/N - 1.0) for t in range(N)]
        
        # Convert to cvxopt matrices
        S = opt.matrix(np.cov(self.returns))
        pbar = opt.matrix(np.mean(self.returns, axis=1))
        
        # Create constraint matrices
        G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
        h = opt.matrix(0.0, (n ,1))
        A = opt.matrix(1.0, (1, n))
        b = opt.matrix(1.0)
        
        # Calculate efficient frontier weights using quadratic programming
        portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x'] 
                    for mu in mus]
        
        self.returns = [blas.dot(pbar, x) for x in portfolios]
        risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
        
        m1 = np.polyfit(self.returns, risks, 2)
        x1 = np.sqrt(m1[2] / m1[0])
        
        wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
        return np.asarray(wt), self.returns, risks
    
    def plot_frontier(self, figsize=(8, 5)):
        weights, returns, risks = self.optimal_portfolio()
        fig = plt.figure(figsize=figsize)
        plt.plot(self.stds, self.means, 'o')
        plt.ylabel('Mean Return')
        plt.xlabel('Standard Deviation')
        plt.plot(risks, returns, 'y-o', )
        plt.title('Markowitz Efficient Frontier')
        plt.legend(['Assets', 'Efficient Frontier'], loc='upper left', bbox_to_anchor=(1, 1))
        plt.tight_layout()
        
        
        
        