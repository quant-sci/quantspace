import sys
sys.path.append("./")

import numpy as np
from quantspace.risk import summary_risk

# Example usage:
investment_returns = [0.12, 0.08, 0.15, 0.10, 0.14]
risk_free_rate = 0.03

print(summary_risk(investment_returns, risk_free_rate))

