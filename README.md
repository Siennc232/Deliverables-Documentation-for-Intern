# Chooser Option Research

**Project:** Advanced Chooser Option Pricing Model with Real-World Data & Machine Learning  
**Project start:** October 8, 2026  
**First weekly submission:** Wednesday, October 14, 2026  
**Planned duration:** 12 weeks, with adjustments based on mentor feedback.

## Research objective

Reproduce a Black–Scholes–Merton (BSM) chooser-option pricing model; use a Heston stochastic-volatility Monte Carlo framework to construct a simulation-based benchmark; investigate machine-learning volatility forecasting and direct option pricing; and build a configurable pricing tool.

The mentor requested that stock tickers and historical periods be changeable through parameters, rather than by rewriting the data-retrieval code.

## Folder guide

| Folder | Purpose |
| --- | --- |
| `01_References/` | Assigned project brief, research-paper links and PDFs you obtain. |
| `02_Data/raw/` | **Unmodified** downloaded historical market data; Week 1 collection starts here. |
| `02_Data/processed/` | Cleaned, aligned data and engineered features (primarily Week 2). |
| `03_Code/notebooks/` | Jupyter experiments, API connection tests and model validation notebooks. |
| `03_Code/src/` | Reusable Python scripts (API retrieval, preprocessing, pricing, ML). |
| `04_Reports/weekly/` | **Empty folder reserved for your own Wednesday weekly reports.** |
| `04_Reports/final/` | **Empty folder reserved for your final report.** |
| `05_Models/` | Trained model artifacts / saved parameters later in the project. |
| `06_Research_Notes/` | Your reading notes, definitions, research log and questions. |

## Day 1 checklist — October 8

- [ ] Read the project brief and clarify research goals.
- [ ] Review option basics: call/put, premium, intrinsic/time value, payoff/profit, chooser choice date.
- [ ] Start reading the original JPMorgan chooser option paper; record unanswered questions.
- [x] Create project folders and initial research note template.

See `06_Research_Notes/Day01_Project_Orientation.md`.

## Week 1 planned datasets — NOT YET DOWNLOADED

The `raw/` and `processed/` directories are intentionally empty. **No historical market prices have been fabricated or presented as already collected.**

Planned raw data:
- `JPM_daily_2018_2024.csv` — JPM stock prices.
- `VIX_daily_2018_2024.csv` — VIX index.
- `Treasury_Rates_2018_2024.csv` — U.S. Treasury yield series (choose tenor and document it).

Sources to test: Yahoo Finance (commonly via `yfinance`), Alpha Vantage and FRED. The stock and date parameters should be changeable (e.g., `ticker`, `start_date`, `end_date`). API keys should be provided using environment variables or local non-committed configuration; do not commit them to GitHub.

## Reference paper

The project paper was included from the conversation attachment. The original 2021 paper is **linked, not downloaded** here, because the publisher PDF could not be fetched in this environment. See `01_References/Reference_Papers_Links.md`; you can open the PDF link in a browser and save a copy into `01_References/`.

## How to use on Mac

1. Download and unzip `Chooser_Option_Research.zip`.
2. Drag the **whole** `Chooser_Option_Research` folder to your Desktop.
3. Open `06_Research_Notes/Day01_Project_Orientation.md` with VS Code, TextEdit or any Markdown editor.
4. Keep original datasets in `02_Data/raw/` and put cleaned files into `02_Data/processed/` only after processing.

Created for Week 1, Day 1. This is an **initial research workspace**, not a completed API/data deliverable.
