---
---
---

# W02 — Weekly Research Progress Report

**Project:** Advanced Chooser Option Pricing Model with Real-World Data & Machine Learning\
**Reporting period:** October 15–21, 2026\
**Stage:** Data Cleaning, Alignment & Feature Engineering\
**Status:** Completed; notebook restart-and-run-all and saved-file checks passed

## 1. Executive Summary

Week 2 converted the Week 1 raw market data into an aligned daily dataset and a preliminary feature dataset. The work produced **10 financial features**, resolved **13 missing Treasury-rate observations** using a documented forward-fill rule, and passed basic data-integrity and reproducibility checks.

## 2. Data Cleaning & Alignment

| Step | Method | Result |
|------------------------|------------------------|------------------------|
| Source inspection | Loaded JPM, VIX, DGS1, and DGS6MO CSVs | JPM/VIX: 1,761 rows each; FRED series: 1,827 rows each |
| Date standardization | Converted source dates to `datetime` | Common trading-date format |
| Treasury cleaning | Converted `"."` to `NaN`; yields from percent to decimal | 77 original missing observations in each FRED series |
| Alignment | Left-joined VIX and Treasury series on JPM trading dates | 1,761 aligned rows; no duplicate dates |
| Missing rates | Forward-filled 13 missing trading-day rates; added `rate_ffilled` indicator | No remaining missing DGS1/DGS6MO values |

**Calendar observation:** The 13 missing rate dates are consistent with differences between U.S. equity trading and Treasury observation calendars. The filled values are **carried-forward estimates, not newly observed rates**. Raw source files were not modified.

## 3. Feature Engineering

| Feature | Definition / purpose |
|------------------------------------|------------------------------------|
| `return_1d` | 1-day simple return from adjusted close |
| `log_return_1d` | 1-day log return from adjusted close |
| `return_5d` | 5-trading-day cumulative return |
| `return_20d` | 20-trading-day cumulative return |
| `volatility_5d` | 5-day rolling standard deviation of log returns, annualized by `sqrt(252)` |
| `volatility_20d` | 20-day rolling log-return volatility, annualized by `sqrt(252)` |
| `ma_5` | 5-day moving average of adjusted close |
| `ma_20` | 20-day moving average of adjusted close |
| `volume_ratio` | Daily volume divided by its 20-day rolling mean |
| `term_spread` | One-year minus six-month Treasury yield (`DGS1 - DGS6MO`) |

All features are preliminary **end-of-day** descriptors; their timing and lag structure will be reviewed before predictive modeling to prevent look-ahead bias.

## 4. Validation Results

| Check | Verified result |
|------------------------------------|------------------------------------|
| Aligned dataset | **1,761 rows × 13 columns** |
| Rows with incomplete rolling features | **20** initial trading days |
| Complete feature dataset | **1,741 rows × 23 columns** |
| Feature dataset coverage | **2018-01-31 to 2024-12-31** |
| Number of engineered features | **10** |
| Missing values across the 10 final features | **0** |
| Infinite feature values | **0** |
| Duplicate dates | **0** |
| Forward-filled Treasury dates | **13**, tracked by `rate_ffilled` |
| Reproducibility | CSV read-back checks and Jupyter kernel restart / run-all **passed** |

## 5. Deliverables

| File | Location |
|------------------------------------|------------------------------------|
| Preprocessing and feature-engineering notebook | `03_Code/notebooks/W02_Data_Preprocessing.ipynb` |
| Aligned market dataset | `02_Data/processed/W02_Aligned_Market_Data.csv` |
| Complete feature dataset | `02_Data/processed/W02_Feature_Dataset.csv` |
| Weekly report | `04_Reports/weekly/W02_Weekly_Report.md` |

## 6. Limitations & W03 Plan

**Open points:** Validate information-availability timing before forecasting; retain the original missing-rate flags; investigate previously flagged Nasdaq/Yahoo Finance discrepancies if those records are used. The present feature dataset is a preprocessing milestone, **not yet a leakage-tested ML training set**.

**Week 3 — BSM Chooser Baseline:** Implement and document the BSM call/put valuations, select the higher **continuation value at the choice date** (`T1`), and calculate the initial chooser value using consistent risk-neutral assumptions and discounting. Keep model-generated prices distinct from observed market transaction prices.
