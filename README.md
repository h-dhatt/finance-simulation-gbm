
# Mathematical Finance & Risk Analysis — GBM & Monte Carlo Option Pricing

**Author:** You (B.Sc. (Honours) Math & Stats, McMaster)  
**Target Program:** York University — MA in Mathematics & Statistics

## Objectives
1. Simulate **Geometric Brownian Motion (GBM)** stock price paths.
2. Analyze distribution of terminal stock prices.
3. Use **Monte Carlo simulation** to estimate European call option prices under the risk-neutral measure.

## Key Results
- Simulated 20000 GBM stock price paths with drift μ=0.05, volatility σ=0.2.
- Distribution of terminal prices approximates lognormal.
- Monte Carlo option pricing converges to ≈ 10.544 for strike K=100, maturity T=1, risk-free rate r=0.05.

## Deliverables
- **gbm_samplepaths.csv** — sample stock price paths
- **option_pricing_convergence.csv** — estimated option prices vs number of simulations
- **fig_gbm_paths.png** — GBM stock price paths
- **fig_gbm_final_distribution.png** — terminal price histogram
- **fig_option_convergence.png** — option pricing convergence

## Admissions-Ready Highlights
- Implemented GBM, the **stochastic differential equation model** of stock prices, via discretized simulations.
- Applied **Monte Carlo methods** to price European options, demonstrating convergence.
- Bridged rigorous probability theory with **financial applications**.

## How to Run
```bash
pip install numpy pandas matplotlib
python analysis_script.py
```

## Talking Points
- GBM satisfies the **SDE**: dS = μS dt + σS dW. The solution is lognormal.
- Under **risk-neutral pricing**, drift becomes r, and option prices are discounted expected payoffs.
- Monte Carlo pricing shows **law of large numbers**: estimates converge as simulations increase.
