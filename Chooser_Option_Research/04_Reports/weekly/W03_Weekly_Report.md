# W03 — Weekly Research Progress Report

**Project:** Advanced Chooser Option Pricing Model with Real-World Data & Machine Learning\
**Reporting period:** October 22–28, 2026\
**Stage:** Dividend-adjusted BSM Chooser Option Baseline\
**Status:** Completed; documented model checks passed

## 1. Executive Summary

Implemented a **European Simple Chooser Option** baseline for JPM using dividend-adjusted Black–Scholes–Merton (BSM) pricing and put–call parity decomposition. The estimated theoretical chooser value is **$29.8290** as of December 31, 2024. Tested the choice rule, pricing consistency, and sensitivity to five model inputs.

## 2. Inputs & Method

| Input | Value / method |
|---|---|
| Underlying / valuation date | JPM / 2024-12-31 |
| Spot price / strike | **$239.71 / $239.71** (at the money) |
| Choice date / final expiry | **0.5 / 1.0 years** |
| Annualized volatility | **18.67%**, trailing 20-day historical estimate |
| Dividend yield | **1.919%**, $4.60 trailing annual dividends / $239.71 spot |
| Risk-free yield proxies | **4.24% (6M)** / **4.16% (1Y)** |
| Implied 6M–1Y forward-rate proxy | **4.08%** |

**Pricing method:** Dividend-adjusted BSM European call and put, followed by the simple chooser decomposition:

\[
V_0 = C(S_0,K,T_2) + P\!\left(S_0 e^{-q(T_2-T_1)},\;K e^{-f(T_2-T_1)},\;T_1\right).
\]

The adjusted put uses the 6M discount-rate proxy; the European call uses the 1Y proxy. At the choice date, the holder selects the **higher continuation value**, not the larger realized payoff at final expiry.

## 3. Pricing & Validation

| Theoretical component | Price |
|---|---:|
| European call (1Y) | **$20.0223** |
| European put (1Y) | **$14.8111** |
| Additional choice value | **$9.8067** |
| **Simple chooser option** | **$29.8290** |

**Passed checks:** BSM put–call parity (error: **0.0**); expected dividend sensitivity; chooser value ≥ individual call/put; two equivalent chooser decompositions (both **$29.829018**); call–put equality at the critical choice price (**$237.1339**); and the near-expiry choice-date limit toward the European straddle (**$34.8335**).

These are **internal consistency checks**, not validation against traded chooser prices.

## 4. Sensitivity Analysis

![W03 Chooser Option Sensitivity Analysis](figures/W03_Chooser_Sensitivity.png)

Five one-at-a-time scenarios were evaluated: **volatility, dividend yield, parallel risk-free yield shifts, choice date, and strike/spot ratio**.

| Scenario | Chooser theoretical price | Interpretation |
|---|---|---|
| Baseline: volatility **18.67%** | **$29.8290** | Historical-volatility reference |
| Volatility increased to **25%** | **$39.7354** | Strong sensitivity to volatility assumptions |
| Choice date delayed from **0.5 to 0.95 years** | **$34.4001** | Later choice increases flexibility value |
| Dividend yield **0% → 5%** | **$30.8567 → $29.1178** | Net dividend sensitivity over the tested range |
| Strike/spot **80% / 100% / 120%** | **$53.2405 / $29.8290 / $47.7700** | Nonlinear moneyness response |

**Implication:** Volatility input quality is especially consequential, motivating later ML-based volatility forecasting and comparison with stochastic-volatility models.

## 5. Assumptions & Limitations

- **BSM assumptions:** Constant volatility, deterministic rates, and continuous dividend yield. The 1.919% yield is a *trailing-dividend proxy*, not a known forward dividend schedule.
- **Rate matching:** 6M/1Y Treasury constant-maturity yields are **proxies**, not a bootstrapped zero-coupon discount curve; intermediate choice dates use interpolation of cumulative rates.
- **Scope of evidence:** Prices are **model-generated**, not observed chooser-option market quotes. Sensitivity figures vary one input at a time and do not establish predictive superiority.

## 6. W04 — Heston Monte Carlo Plan

- Simulate **correlated price and stochastic-variance paths**, using a positivity-aware discretization scheme.
- Price the chooser using **information available at the choice date**, without looking ahead to final payoffs.
- Evaluate **simulation convergence and uncertainty**, and distinguish stochastic volatility from additional market frictions (e.g., transaction costs or bid–ask spreads).
- Produce **clearly labeled synthetic pricing benchmarks** for subsequent ML experiments.

**Deliverables:** `03_Code/W03_BSM_Chooser_Option_Pricing.ipynb`, `W03_Chooser_Sensitivity.png`, and this weekly report.
