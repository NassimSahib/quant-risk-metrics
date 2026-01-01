import numpy as np
from quant_risk_metrics.core.var_engine import VaREngine


def test_parametric_var_is_positive():
    rng = np.random.default_rng(42)
    returns = rng.normal(0.0005, 0.015, size=5_000)

    engine = VaREngine(returns)
    var_99 = engine.var_parametric(alpha=0.99)

    assert var_99 > 0

def test_historical_var_is_positive():
    rng = np.random.default_rng(42)
    returns = rng.normal(0.0005, 0.015, size=5_000)

    engine = VaREngine(returns)
    var_99 = engine.var_historical(alpha=0.99)

    assert var_99 > 0

def test_monte_carlo_var_is_positive():
    rng = np.random.default_rng(42)
    returns = rng.normal(0.0005, 0.015, size=5_000)

    engine = VaREngine(returns)
    var_99 = engine.var_monte_carlo(alpha=0.99,n_sims=50_000, random_state=42)

    assert var_99 > 0
