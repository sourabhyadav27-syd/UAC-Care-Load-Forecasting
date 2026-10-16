# Forecasting Care Load and Discharge Demand in the UAC Program

## Abstract

This project examines the use of historical time-series and machine
learning methods to forecast care load and discharge demand in the
Unaccompanied Alien Children (UAC) program. The analysis includes
data validation, baseline forecasting, statistical models, machine
learning models, held-out evaluation, and an interactive dashboard.

Final quantitative conclusions should be added only after reviewing
the verified evaluation results.

## 1. Introduction

Operational planning requires timely information about care load,
transfers, and discharges. Forecasting can provide estimates that
support further analysis of potential resource pressure. Forecasts
should be treated as decision-support estimates rather than guaranteed
future outcomes.

## 2. Project Objectives

- Analyze historical care-load and discharge patterns.
- Compare baseline, statistical, and machine-learning approaches.
- Evaluate forecasts on a held-out test period.
- Present forecast estimates and uncertainty transparently.
- Explore hypothetical planning scenarios.

## 3. Dataset and Data Quality

The following profile was generated from the project dataset.

UAC FORECASTING PROJECT: DATASET PROFILE
==================================================
Total rows: 720
Total columns: 15
Duplicate rows: 0
Invalid dates: 0
First date: 2023-01-12 00:00:00
Last date: 2025-12-21 00:00:00
Unique dates: 720
Calendar days in date range: 1075
Missing calendar dates: 355

COLUMN DATA TYPES
Date                  datetime64[us]
HHS_Care                       int64
Apprehended                    int64
CBP_Custody                    int64
Transfers                      int64
Discharged                     int64
Net_Pressure                   int64
Lag_1                        float64
Lag_7                        float64
Lag_14                       float64
7_Day_Rolling_Avg            float64
14_Day_Rolling_Avg           float64
Day_Of_Week                    int64
Month_Number                   int64
Data_Split                       str
dtype: object

MISSING VALUES BY COLUMN
Date                   0
HHS_Care               0
Apprehended            0
CBP_Custody            0
Transfers              0
Discharged             0
Net_Pressure           0
Lag_1                  2
Lag_7                  8
Lag_14                15
7_Day_Rolling_Avg      7
14_Day_Rolling_Avg    14
Day_Of_Week            0
Month_Number           0
Data_Split             0
dtype: int64

NUMERICAL SUMMARY
       HHS_Care  Apprehended  CBP_Custody  Transfers  Discharged  Net_Pressure     Lag_1     Lag_7    Lag_14  7_Day_Rolling_Avg  14_Day_Rolling_Avg  Day_Of_Week  Month_Number
count    720.00       720.00       720.00     720.00      720.00        720.00    718.00    712.00    705.00             713.00              706.00       720.00        720.00
mean    6061.28        93.52       171.49     128.67      173.41        -44.74   6071.26   6101.69   6138.21            6077.06             6087.47         3.06          6.53
std     2833.07        72.65       126.35      97.32      125.70         95.86   2830.68   2823.01   2812.96            2828.51             2819.81         1.40          3.39
min     1972.00         0.00         7.00       0.00        0.00       -465.00   1972.00   1972.00   1972.00            1981.00             1987.00         1.00          1.00
25%     2467.75        12.00        36.00      14.00       19.75        -94.25   2467.25   2472.25   2503.00            2461.00             2457.00         2.00          4.00
50%     6406.50        99.00       193.00     157.00      181.00        -11.50   6409.00   6451.00   6468.00            6373.00             6344.00         3.00          7.00
75%     8010.25       147.25       263.25     199.25      267.00          5.25   8014.75   8027.75   8042.00            8036.00             8047.25         4.00          9.00
max    11516.00       333.00       531.00     440.00      505.00        206.00  11516.00  11516.00  11516.00           11283.00            11186.00         6.00         12.00

## 4. Methodology

The project uses chronological train/test separation, lag features,
rolling averages, calendar features, baseline models, ARIMA/SARIMA
models, Random Forest, and Gradient Boosting where applicable.

The evaluation scripts use one-step-ahead predictions based on
previous observed target values. This differs from a fully recursive
multi-step forecast.

The dataset contains irregular observation dates. Observation-based
lags must therefore not automatically be interpreted as exact
calendar-day lags.

## 5. Model Evaluation

The validation summary below is generated from the held-out test
evaluation.

UAC FORECASTING: MODEL VALIDATION SUMMARY
==================================================

Lower MAE and RMSE generally indicate smaller errors.
Results apply to the evaluation method and test period used.
They should not be interpreted as proof of future performance.

Target: Discharged
    Target             Model  Train_Rows  Test_Rows     MAE      RMSE  MAPE_Percent
Discharged     Random_Forest         562        144 4.72364  6.451171     45.221959
Discharged Gradient_Boosting         562        144 9.17213 11.098694    109.869590

Target: HHS_Care
  Target             Model  Train_Rows  Test_Rows       MAE       RMSE  MAPE_Percent
HHS_Care     Random_Forest         562        144 64.983013  86.731040      2.993710
HHS_Care Gradient_Boosting         562        144 92.092545 113.878819      4.284827


## 6. Forecasting Dashboard

The Streamlit dashboard presents future care-load estimates, discharge
forecasts, model comparisons, empirical error bands, and hypothetical
scenario analysis.

The empirical error bands are not formal statistical confidence
intervals. Scenario adjustments are assumptions, not model-generated
probabilities.

## 7. Limitations

- Historical patterns may not continue into the future.
- Irregular observation dates complicate calendar-day interpretation.
- Recursive forecasts can accumulate errors.
- Model performance can vary across time periods.
- Operational capacity thresholds require independent verification.
- Forecasts do not establish causal relationships.

## 8. Recommendations

Review forecast performance against appropriate baselines, monitor
forecast errors over time, validate the forecasting horizon, and
consult domain experts before using forecasts for operational decisions.

## 9. Conclusion

This project provides a prototype workflow for analyzing historical
care load and discharge demand. Final claims about the best model,
operational benefits, or forecast reliability should be made only
after comprehensive validation.

## 10. References

Add verified dataset documentation, project instructions, and
methodological references here before final submission.
