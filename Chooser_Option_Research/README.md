# Chooser Option Research

Advanced Chooser Option Pricing Model with Real-World Data & Machine Learning.

The project starts with a BSM pricing benchmark, then plans Heston Monte Carlo simulation, ML volatility forecasting and direct model-price prediction. Initial market data covers JPM, VIX and Treasury yields for 2018–2024.

## Week 1 deliverables

| Deliverable | File |
| --- | --- |
| Weekly research report | [W01_Weekly_Report.md](04_Reports/weekly/W01_Weekly_Report.md) |
| Data requirement specification | [W01_Data_Requirement_Specification.md](04_Reports/weekly/W01_Data_Requirement_Specification.md) |
| API connection tests and preliminary validation | [W01_API_Connection_Test.ipynb](03_Code/W01_API_Connection_Test.ipynb) |
| Reusable data retrieval functions | [W01_data_extraction.py](03_Code/src/W01_data_extraction.py) |
| Cross-source findings | [W01_Cross_Source_Validation.md](06_Research_Notes/W01_Cross_Source_Validation.md) |
| Initial raw datasets | [02_Data/raw](02_Data/raw/) |
| Reference documents | [01_References](01_References/) |

No separate Week_01_Submission directory is used. Word documents are intentionally excluded from this repository. References to the private Word learning record in research documents are historical; that file is not published here.

## Data and validation status

Six original CSV files are preserved without edits. JPM and VIX each contain 1,761 observations. DGS1 and DGS6MO each contain 1,827 observations, including 77 missing-value markers. Nasdaq supplies independent historical comparison data; the Alpha Vantage sample contains 100 recent observations outside the target period. Dividend events are included in the JPM CSV.

Read-only comparison matched 1,761 dates and found one opening-price discrepancy, one high-price discrepancy, and 1,684 volume discrepancies. No raw observations were corrected. Offline comparison and module import checks passed; a complete fresh online notebook run remains pending. Existing notebook outputs are historical execution evidence.

## Running the notebook

Use Python with pandas, numpy, yfinance, requests, python-dotenv and JupyterLab. Start Jupyter inside this project and open `03_Code/W01_API_Connection_Test.ipynb`. Paths resolve relative to the project root. Existing raw files are preserved by the export helper.

For live API requests, configure `FRED_API_KEY` and `ALPHAVANTAGE_API_KEY` locally through environment variables or an ignored `.env` file. Credentials are not included in the repository. Do not print request URLs or credential values into notebook outputs.

The reusable module is `03_Code/src/W01_data_extraction.py`. With `03_Code` on Python's import path, import `stock_data` and `fred_data` from `src.W01_data_extraction`.

## Next stage

Week 2 covers cleaning, date alignment, anomaly investigation and feature engineering in processed outputs. Day 1's note template, the separate AAPL switching test and a fresh end-to-end run remain to be completed. BSM, Heston and ML implementations are later research stages.
