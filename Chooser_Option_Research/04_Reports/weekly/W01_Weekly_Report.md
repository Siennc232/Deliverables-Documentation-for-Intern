# Week 1 Research Progress Report

**Project:** Advanced Chooser Option Pricing Model with Real-World Data & Machine Learning  
**Reporting period:** October 8–14, 2026  
**Research stage:** W01 — Project Orientation, Data Specification, API Setup & Initial Data Collection  
**Status:** Core research tasks completed; submission packaging and final reproducibility check pending.

## 1. Executive Summary

The first week focused on building the conceptual, computational, and data foundations for a chooser option pricing study. Work included understanding chooser option payoffs and pricing, reviewing a reference pricing approach, specifying market and macroeconomic data requirements, creating a dedicated Python research environment, testing financial data sources, and collecting historical observations for JPMorgan Chase (JPM), the VIX, and U.S. Treasury yields.

A preliminary cross-source validation compared Yahoo Finance and Nasdaq prices over **1,761 matched JPM trading days (2018–2024)**. Two price discrepancies exceeding **$0.01** were identified: an opening-price difference of approximately **$3.87** on **January 24, 2023**, and a high-price difference of approximately **$0.80** on **June 5, 2023**. On the latter date, the Nasdaq-reported high was lower than its reported open, violating an internal OHLC consistency condition. Daily trading volumes differed on **1,684** matched dates. Original source files were preserved without correction.

Reusable retrieval functions were developed and tested for Yahoo Finance and FRED. The resulting materials form a foundation for W02 preprocessing, date alignment, feature engineering, and the later BSM, Heston Monte Carlo, and machine learning pricing stages.

## 2. Project Orientation and Theoretical Foundation

### 2.1 Research objective

A **chooser option** grants its holder the right, at a specified choice date \(T_1\), to decide whether the contract will become a call or a put. The selected option expires at \(T_2\). The flexibility to defer this decision provides value under market uncertainty but does not guarantee a positive payoff or eliminate market risk.

The project will investigate three related approaches:

| Approach | Method | Intended role |
|---|---|---|
| BSM-based baseline | Classical option pricing and chooser valuation | Establish a theoretical benchmark |
| Heston Monte Carlo | Simulate underlying prices with stochastic variance | Examine pricing under stochastic volatility and selected market-friction scenarios |
| Machine learning | (i) Forecast volatility for use in a pricing model; (ii) predict chooser prices directly | Compare data-driven approaches with model-based benchmarks |

The study will distinguish between **market-observed prices**, **model-generated option values**, and **simulated training or evaluation targets**. Accessible historical transaction prices for chooser options have not yet been established.

### 2.2 Basic valuation concepts

For European options with strike \(K\) and underlying stock price \(S_T\) at maturity:

\[
\text{Call payoff}=\max(S_T-K,0), \qquad
\text{Put payoff}=\max(K-S_T,0).
\]

Option value reflects intrinsic value and time value. A contract's net profit is not the same as its payoff: the initial premium must also be considered when calculating profit.

For a standard chooser contract, the option premium is paid at initiation, not again when the call/put choice is made. At \(T_1\), the rational exercise of the choice feature compares the **continuation values** of the remaining call and put:

\[
\max\bigl(C(T_1),P(T_1)\bigr).
\]

For a simple European chooser with the same strike \(K\) and expiry \(T_2\) for both choices, put–call parity gives

\[
C(T_1)-P(T_1)=S_{T_1}e^{-q(T_2-T_1)}-Ke^{-r(T_2-T_1)},
\]

where \(q\) represents continuous dividend yield and \(r\) the applicable risk-free rate under the model's assumptions. Thus the decision is based on relative option values; the simple rule \(S_{T_1}>K\) is not universally appropriate when rates, dividends, and remaining maturity matter.

### 2.3 Reference paper review

The initial reading examined the reference paper's chooser pricing method, especially Section 3.3. It models lognormal stock prices and divides the horizon into a first period ending at the choice date and a second period ending at expiration. The reading identified points for investigation rather than treating them as verified flaws in every implementation:

| Dimension | Initial paper-reading observation | Planned treatment |
|---|---|---|
| Choice rule | A stock-price-versus-strike rule is used in the discussed simulation | Compare call and put continuation values at \(T_1\) |
| Payoff versus price | Simulated terminal payoffs are central to the presentation | Explicitly calculate the discounted risk-neutral expectation for a theoretical initial value |
| Volatility | Constant-volatility assumptions | Introduce stochastic variance and volatility forecasts |
| Evaluation | Simulated pricing examples | Compare model outputs and robustness under consistent inputs and assumptions |

Under idealized BSM assumptions, pricing follows **no-arbitrage and risk-neutral valuation** rather than a direct forecast of the stock's physical expected return. The drift adjustment in geometric Brownian motion and the \(\sqrt{T}\) scaling of Brownian shocks were reviewed as part of the theoretical preparation.

## 3. W01 Data Requirement Specification

### 3.1 Initial scope

- **Underlying asset:** JPMorgan Chase & Co. (`JPM`)
- **Research period:** January 1, 2018–December 31, 2024
- **Frequency:** Daily observations, with event-based corporate actions
- **Extension requirement:** Configurable ticker, data-series identifiers, and date ranges

| Dataset | Required fields or series | Selected source | Purpose |
|---|---|---|---|
| JPM stock history | Open, High, Low, Close, Adj Close, Volume | Yahoo Finance | Returns, historical volatility, underlying market inputs |
| JPM corporate actions | Dividends, Stock Splits | Yahoo Finance | Dividend-related adjustments and features |
| Treasury yields | `DGS6MO`, `DGS1` | FRED | Risk-free rate proxies and maturity matching |
| Broader-market volatility | `^VIX` | Yahoo Finance | Market-wide volatility environment and potential ML feature |
| Independent JPM historical quotes | Date, Open, High, Low, Close/Last, Volume | Nasdaq | Cross-source consistency checks |
| Alternative API connection | Daily OHLCV, most recent observations | Alpha Vantage (testing only) | Document API availability and free-tier historical limits |

**Rate maturity matching.** The risk-free rate input should reflect the option horizon rather than being selected arbitrarily from a long-term Treasury series. The six-month and one-year yields provide initial references; their suitability will be evaluated with the contract's remaining maturity.

**Volatility distinctions.** JPM historical volatility is estimated from past JPM returns. The VIX is a market-wide, forward-looking measure derived from S&P 500 options, not JPM-specific implied volatility.

### 3.2 Data provider decisions

Yahoo Finance was selected for the primary JPM and VIX historical retrieval; FRED was selected for Treasury yields. Alpha Vantage API connectivity was tested, but its available free-tier daily endpoint returned approximately **100 recent trading days**, which did not satisfy the full 2018–2024 coverage requirement. Following the mentor's suggestion, Nasdaq historical JPM quotes were downloaded as a separate historical source and used in the validation exercise. Alpha Vantage is therefore **not** represented as a complete historical dataset in this project.

The initial data specification is a W01 document. Its earlier draft should be updated to reflect the actual source selection above and to list only the CSV files that were genuinely saved.

## 4. Environment, API Testing, and Data Acquisition

### 4.1 Computational environment

A project-specific Conda environment named `chooser_option` was created using Python 3.12. JupyterLab was used for interactive testing and validation. Key packages included `pandas`, `numpy`, `yfinance`, `requests`, `matplotlib`, and `python-dotenv`.

The working project structure separates references, raw and processed datasets, notebooks, reusable source code, weekly and final reports, models, and research notes. API credentials are stored separately in a local `.env` file; `.env` is intended to remain excluded from version control via `.gitignore`.

### 4.2 Initial retrieval and tests

| Data or test | Period / coverage | Result |
|---|---|---|
| JPM history via Yahoo Finance | 2018–2024 | **1,761** daily records, saved as CSV |
| VIX via Yahoo Finance | 2018–2024 | Historical data downloaded and saved as CSV |
| FRED `DGS1` | 2018–2024 | **1,827** dated observations returned |
| FRED `DGS6MO` | 2018–2024 | **1,827** dated observations returned |
| JPM via Nasdaq | Downloaded historical file spanning approximately 2016–2026 | **2,513** records in full downloaded history |
| Alpha Vantage daily JPM | Latest available free-tier window | **100** recent trading days returned; connection verified |

Source conventions were documented during testing:

- Yahoo Finance `end` is **exclusive**; an end value of `2025-01-01` was used for history through December 2024.
- FRED `observation_end` is **inclusive**.
- FRED uses the text marker `"."` for missing yield observations, including market holidays; returned yield values such as `1.83` represent **1.83%** rather than `1.83` in decimal-rate units.
- Yahoo Finance dates can carry timezone information, whereas Nasdaq dates are formatted differently and its price fields can contain `$` characters.
- Raw files have been preserved. Alignment, rate conversion, missing-value handling, and corporate-action treatment belong to W02 preprocessing.

### 4.3 Reusable code

A parameterized Yahoo Finance function was developed:

```python
def stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(
        start=start_date,
        end=end_date,
        auto_adjust=False,
        actions=True
    )
    return data
```

A corresponding `fred_data(series_id, start_date, end_date)` function was developed using the FRED observations endpoint, `requests.get`, and an API key loaded from the environment. Tests returned the expected data frames for both `DGS1` and `DGS6MO`. The Yahoo Finance function was also tested on JPM January 2024 data (**21 rows, 8 columns**).

The functions demonstrate basic reuse without editing their internals. Packaging and import checks for a standalone source module remain part of the **final submission/reproducibility check** unless confirmed by rerunning the saved project files.

## 5. Preliminary Cross-source Validation: Yahoo Finance vs Nasdaq

### 5.1 Methodology

The comparison covered **1,761 matched JPM trading dates** from 2018 through 2024. The two datasets were loaded from CSV, date fields were converted to a common representation, Nasdaq prices were converted to numeric values, and the records were joined by date using `pandas.merge()`.

For OHLC prices, dates were flagged when the **absolute difference exceeded $0.01**. This threshold is a screening convention, **not** a proof that a quotation is erroneous. For volume, the initial test counted all nonzero share-count differences.

### 5.2 OHLC results

| Field | Number of dates with difference > $0.01 | Flagged date |
|---|---:|---|
| Open | **1** | January 24, 2023 |
| High | **1** | June 5, 2023 |
| Low | **0** | None above threshold |
| Close | **0** | None above threshold |

**January 24, 2023 — Opening-price discrepancy.** Yahoo Finance reports an open of approximately **$136.42** and Nasdaq reports **$140.29**, an absolute difference of approximately **$3.87**. Both sources report a high of approximately **$140.29**, low of **$135.00**, and close of **$138.45**. Nasdaq's open equals its high, which is possible and does not itself violate OHLC constraints. The discrepancy remains unresolved. A reported NYSE opening-auction technical incident on the same date is a potential research lead, but has **not** been established as the cause of this specific JPM difference.

**June 5, 2023 — High-price inconsistency.** Yahoo Finance reports both an open and high of approximately **$140.11**, while Nasdaq reports an open of **$140.11** and a high of **$139.31**. The high-price difference is approximately **$0.80**. The Nasdaq row violates

\[
\mathrm{High}\geq\max(\mathrm{Open},\mathrm{Close}),
\]

providing evidence of an **internal OHLC inconsistency** in that source's record. The underlying raw file was not altered.

### 5.3 Volume results

Trading volumes were not identical on **1,684 of 1,761 matched dates**. The five largest absolute differences were:

| Date | Yahoo Finance volume | Nasdaq volume | Absolute difference (shares) |
|---|---:|---:|---:|
| 2019-10-15 | 23,379,000 | 30,522,340 | **7,143,340** |
| 2018-06-12 | 15,294,100 | 10,822,240 | **4,471,860** |
| 2021-05-05 | 10,506,700 | 6,938,197 | **3,568,503** |
| 2019-01-14 | 21,258,500 | 19,161,430 | **2,097,070** |
| 2018-12-14 | 19,879,500 | 18,159,340 | **1,720,160** |

The causes have not yet been verified. Possible differences in vendor data definitions, reporting, aggregation, or revisions should be investigated before treating these as incorrect observations.

### 5.4 Validation conclusion

At the chosen price-difference threshold, the two sources show strong agreement for JPM closing prices, but display two notable OHLC differences and frequent volume differences. The distinction between an **inter-vendor discrepancy** and a demonstrable **within-record inconsistency** will guide the W02 data quality log. All raw datasets should remain unchanged, with any exclusions or corrections documented in the processed-data workflow.

## 6. Challenges, Limitations, and Decisions

| Issue | W01 observation | Action or next step |
|---|---|---|
| Alpha Vantage historical coverage | Free-tier daily output was limited to ~100 recent sessions | Retain evidence of successful testing; rely on Yahoo Finance and Nasdaq for long history |
| Provider-specific date formats | Timezone-aware Yahoo timestamps vs Nasdaq date strings | Standardize during preprocessing and retain original source columns |
| Missing Treasury observations | FRED uses `"."` for missing data | Convert to missing numeric values during W02; document alignment rules |
| Different price and volume values | Two significant OHLC differences; 1,684 nonidentical volume dates | Investigate exceptions before selecting final series |
| Chooser transaction prices | Actual comparable transaction-price history not yet established | Label all simulated or modeled option values explicitly |
| Reproducibility | Functions tested interactively, source-file packaging still requires verification | Check notebook top-to-bottom execution, module imports, and directory-relative paths |

## 7. W02 Plan — Data Cleaning, Alignment & Feature Engineering

**Target:** Produce a documented and reproducible dataset suitable for baseline pricing and future ML feature development.

| Workstream | Planned action | Expected output |
|---|---|---|
| Data cleaning | Standardize dates, price fields, types, and missing-value markers | Cleaned provider-specific datasets |
| Quality checks | Log and investigate identified OHLC and volume discrepancies | Data quality report / issue log |
| Cross-source alignment | Align JPM market days with VIX and Treasury observations; define missing-market-day handling | Integrated daily research table |
| Rates and corporate actions | Document percent-to-decimal conversion, maturity considerations, and adjusted-price choice | Modeling-ready rate and return inputs |
| Feature engineering | Build at least 10 interpretable preliminary features, with careful timing to avoid look-ahead leakage | Feature table and definitions |
| Reproducibility | Parameterize processing and validate saves/loads | Runnable preprocessing pipeline and W02 notes |

## 8. Overall Assessment and Deliverable Inventory

The Week 1 research goals—conceptual orientation, historical data requirements, API availability testing, initial data collection, and first-pass validation—have been achieved. The most important technical outcome is a data foundation with documented limitations and preliminary evidence of vendor-specific inconsistencies. The project is ready to move toward W02 preprocessing rather than expanding the W01 API scope.

**Core deliverables for submission:**

1. `W01_Weekly_Report.md` (this report).
2. `W01_Data_Requirement_Specification` (finalize the existing draft, updating Nasdaq/Alpha Vantage decisions; preserve its actual extension).
3. `W01_API_Connection_Test.ipynb` (retain functioning API and validation demonstrations).
4. Existing historical CSVs under `02_Data/raw/` (**keep the raw filenames unchanged**).

**Supporting material:** A reusable source module, W01 research notes, and a concise data-validation note may accompany the core deliverables once their saved files and import paths have been verified. `.env` and other credentials must **not** be included in submissions or repository commits.

*Preparation note: This report reflects the user-provided Day 1–5 research log and test outputs. It is not a claim that each referenced local file was inspected or that the entire saved notebook was re-executed.*
