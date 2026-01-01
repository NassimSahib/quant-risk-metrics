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

    



