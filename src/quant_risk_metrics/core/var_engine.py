import numpy as np
from scipy.stats import norm


class VaREngine:
    """
    Value-at-Risk engine supporting:
    - Parametric (Gaussian) VaR
    - Historical VaR
    - Monte Carlo VaR
    """

    def __init__(self, returns):
        self.returns = np.asarray(returns)

        if self.returns.ndim != 1:
            raise ValueError("Returns must be a 1D array")
        
        self.mu = self.returns.mean()
        self.sigma = self.returns.std(ddof=1)
    
    


