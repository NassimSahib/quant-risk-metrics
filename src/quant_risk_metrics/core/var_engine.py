import numpy as np
from scipy.stats import norm


class VaREngine:
    """
    Market Risk Engine supporting tail risk measures.

    Measures: 
    - Value-at-Risk (VaR)
    - Expected Shortfall (ES)

    Methods:
    - Parametric (Gaussian)
    - Historical
    - Monte Carlo

    Convention:
    - Input: 1D array of returns
    - Output: positive number representing a loss
    """

    def __init__(self, returns):
        self.returns = np.asarray(returns)

        if self.returns.ndim != 1:
            raise ValueError("Returns must be a 1D array")
        
        self.mu = self.returns.mean()
        self.sigma = self.returns.std(ddof=1)
    
    # VaR

    def var_parametric(self, alpha: float = 0.99) -> float:
        """
        Gaussian parametric VaR.
        """
        z = norm.ppf(1 - alpha)
        return -(self.mu + self.sigma * z)
    
    def var_historical(self, alpha: float = 0.99) -> float:
        """
        Historical VaR based on empirical quantile.
        """
        return -np.quantile(self.returns, 1 - alpha)
    
    def var_monte_carlo(
            self,
            alpha: float = 0.99,
            n_sims: int = 100_000,
            random_state: int | None = None
    ) -> float:
        """
        Monte Carlo VaR assuming Gaussian returns.
        """
        rng = np.random.default_rng(random_state)
        simulated_returns = rng.normal(self.mu, self.sigma, size=n_sims)
        return -np.quantile(simulated_returns, 1 - alpha)
    
    # ES

    def es_parametric(self, alpha: float = 0.99) -> float:
        """
        Gaussian parametric Expected Shortfall.
        """
        z = norm.ppf(1 - alpha)
        return -(self.mu - self.sigma * norm.pdf(z) / (1 - alpha))
    
    def es_historical(self, alpha: float = 0.99) -> float:
        """
        Historical Expected Shortfall.
        """
        var_threshold = np.quantile(self.returns, 1 - alpha)
        tail_losses = self.returns[self.returns <= var_threshold]
        return -tail_losses.mean()
