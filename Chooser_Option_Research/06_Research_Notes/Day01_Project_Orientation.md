# Day 01 — Project Orientation

**Date:** October 8, 2026  
**Estimated time:** 2 hours  
**Actual time:** ___  
**Status:** In progress — paper reading and research notes are for you to complete.

## 1. Project objectives

- Understand and reproduce the BSM-based chooser option pricing model in the assigned paper.
- Prepare real-world JPM, VIX and Treasury yield data (2018–2024 initially).
- Build a Heston stochastic-volatility Monte Carlo simulation benchmark in Week 4; consider market frictions separately.
- Compare BSM and ML-enhanced approaches and develop a configurable pricing tool.

## 2. Key financial concepts reviewed

**Call (看涨期权):** Right, not obligation, to buy at strike `K`.

**Put (看跌期权):** Right, not obligation, to sell at strike `K`.

**Intrinsic value (内在价值):**
- Call: `max(S − K, 0)`
- Put: `max(K − S, 0)`

**Option value vs. premium:** Under the illustrative assumption that the option's transaction price equals its value:  
`Option value = intrinsic value + time value`.  
Premium is the price paid when **buying** the option, not a separate third component.

**Payoff (到期收益):**
- Long call at expiry: `max(S_T − K, 0)`
- Long put at expiry: `max(K − S_T, 0)`

**Profit (简化利润):** `payoff − initial premium` (ignoring interest, transaction costs and contract multiplier).

**Chooser option (选择型期权):** Pay its premium at time `t=0`, then at choice date `T1` select call or put without paying an additional premium for the chosen leg. The choice is based on option **values** at `T1`: `V(T1) = max(C(T1), P(T1))`. The selected leg expires at `T2`. Its value on the choice date is not an additional amount to pay.

**Worked practice from our discussion:**
- Ordinary put: `K=150`, premium `$20`, expiry stock price `$110` → payoff `$40`, simplified profit `$20`.
- Chooser: initial premium `$20`; select put at `T1` when put value is `$35` vs call `$5`; if final price is `$100` with `K=150`, payoff `$50`, simplified profit `$30`.

## 3. Assigned paper — reading notes (fill in while reading)

Paper: Huang, Wang & Wan (2021), *Exploration of JPMorgan Chooser Option Pricing*.

### Abstract / Introduction — research motivation

_Write here:_

### Chooser option construction and assumptions

_Write here:_

### Method: BSM pricing / key equations

_Write here:_

### Parameters reported in original paper (Table 2; verify while reading)

| Parameter | Symbol | Reported value |
| --- | --- | --- |
| Initial JPM price | S₀ | $156.70 |
| Strike price | K | $150 |
| Risk-free rate | r | 0.15% |
| Volatility | σ | 28.2% |
| Dividend yield | q | 2.33% |
| Choice date | T₁ | 0.5 years |
| Final maturity | T₂ | 1 year |

### Results and limitations

_Write here:_

### Questions / unfamiliar terms

- 

## 4. Day 1 task log

- [ ] Read project overview.
- [x] Review basic long call/put and chooser-option definitions (from today's conversation).
- [ ] Read assigned paper's abstract, introduction and parameter section.
- [x] Set up folder structure.
- [ ] Record reading notes and questions.

## 5. Tomorrow's planned next step

Draft Week 1 data requirement specification: data fields, source, frequency, date coverage, units, intended usage, configurable parameters and known limitations.
