# W01 — Data Requirement Specification

**Project:** Advanced Chooser Option Pricing Model with Real-World Data & Machine Learning  
**Version:** 1.1 — organized October 13, 2026 from the Week 1 learning record  
**Initial underlying:** JPM  
**Target period:** January 1, 2018–December 31, 2024

## Objective

Establish a reproducible, configurable data foundation for BSM replication, subsequent Heston Monte Carlo valuation and machine-learning research. Changing ticker, series and date arguments should not require rewriting retrieval functions.

## Requirements

| Dataset | Required fields | Source | Frequency / units | Use |
| --- | --- | --- | --- | --- |
| JPM | Open, High, Low, Close, Adj Close, Volume | Yahoo Finance | Daily; USD and shares | Pricing inputs and return estimation |
| Corporate actions | Dividends, Stock Splits | Yahoo Finance, embedded in JPM CSV | Event information within daily rows | Adjustments and dividend research |
| Treasury rates | DGS6MO, DGS1 | FRED | Daily observations; percent; `.` indicates unavailable | Candidate rate inputs matched to option tenor |
| Market volatility | VIX Close | Yahoo Finance | Daily index level | Market-wide volatility feature |
| Independent JPM history | OHLC, Volume | Nasdaq | Daily; USD and shares | Cross-source validation |
| API connectivity sample | Recent JPM daily prices and volume | Alpha Vantage | 100 saved daily observations | Connectivity only, outside target period |

## Source Selection and Parameters

Yahoo Finance is the primary stock and VIX source. FRED supplies six-month and one-year Treasury yields. Nasdaq replaces the tested Alpha Vantage compact response as the historical comparison source because that response does not cover 2018–2024. The original learning record retains the earlier source plan for historical context.

| Parameter | Initial setting |
| --- | --- |
| ticker | `JPM`; `^VIX` for market context |
| start_date | `2018-01-01` |
| Yahoo end_date | `2025-01-01` (exclusive) |
| FRED end_date | `2024-12-31` (inclusive) |
| series_id | `DGS6MO`, `DGS1` |
| stock retrieval | `auto_adjust=False`, `actions=True` |

Credentials remain local environment configuration and are excluded from deliverables.

## Storage and Quality Rules

The six existing CSV files under `02_Data/raw/` retain their names and contents. JPM already includes dividends; separate dividend and combined Treasury files are not required to demonstrate initial collection.

Validate coverage, uniqueness, missing observations, numeric types, OHLC consistency and comparable provider fields. The initial cross-source comparison uses absolute price differences greater than $0.01. Treasury holiday markers remain unchanged in raw files. Date normalization, percent-to-decimal conversion, any further rate convention conversion, alignment and feature engineering belong in processed outputs.

VIX is market-wide and must not be labeled JPM implied volatility. Adjusted close and unadjusted close have distinct uses. Data cleaning and dividend treatment must be documented before pricing or historical-volatility estimation.

## Implementation Status

Raw inputs, executed notebook evidence, two reusable retrieval functions and preliminary validation exist. AAPL switching and a complete fresh end-to-end run remain unverified. See [weekly report](W01_Weekly_Report.md) and [validation findings](../../06_Research_Notes/W01_Cross_Source_Validation.md) for counts and remaining work.
