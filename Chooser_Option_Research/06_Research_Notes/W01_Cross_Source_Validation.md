# W01 — Cross-Source Validation

**Asset:** JPM  
**Period:** 2018–2024  
**Audit date:** October 13, 2026  
**Inputs:** `02_Data/raw/JPM_daily_2018_2024.csv` and `02_Data/raw/JPM_Nasdaq_2016_2026.csv`

An independent read-only comparison reproduced 1,761 matched dates. Yahoo local calendar dates were taken from the first ten timestamp characters; Nasdaq dates were parsed as month/day/year. Dollar signs and thousands separators were removed in memory for numeric comparison. Raw files were not rewritten.

| Field | Absolute-difference threshold | Count |
| --- | --- | ---: |
| Open | > $0.01 | 1 |
| High | > $0.01 | 1 |
| Low | > $0.01 | 0 |
| Close | > $0.01 | 0 |
| Volume | > 0 shares | 1,684 |

- January 24, 2023: opening prices approximately $136.42 (Yahoo) versus $140.29 (Nasdaq), a $3.87 discrepancy. Cause unresolved.
- June 5, 2023: high approximately $140.11 (Yahoo) versus $139.31 (Nasdaq). Nasdaq's opening price is $140.11, exceeding its high; this is an internal OHLC inconsistency.
- Largest volume difference: October 15, 2019, Yahoo 23,379,000 versus Nasdaq 30,522,340 shares; absolute difference 7,143,340.

No corrections, provider selection or causal conclusions were applied. Investigate provider definitions and anomalies during Week 2 before constructing the modeling dataset.
