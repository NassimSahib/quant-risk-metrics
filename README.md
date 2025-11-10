# Quant Risk Metrics

Python library for core risk measures — **duration**, **convexity**, and **Value-at-Risk (VaR)** via analytical and Monte Carlo methods.

## Features
- Macaulay/modified duration & convexity (bonds/portfolios)
- Parametric / historical / Monte Carlo VaR
- Modular `src/` layout, config via YAML, logging

### Layer 2
- ES (Expected Shortfall)
- Stress testing
- Greeks & scenarios

## Quickstart
```bash
python -m src.quant-risk-metrics.main
