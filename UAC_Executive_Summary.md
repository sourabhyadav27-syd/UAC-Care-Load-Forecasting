# Executive Summary
## UAC Care Load and Placement Demand Forecasting

### Purpose

This project explores forecasting approaches for historical care load
and discharge demand. Its purpose is to evaluate whether forecasting
methods can provide useful planning signals for further review.

### Analytical Approach

The workflow includes data-quality checks, exploratory analysis,
baseline comparisons, statistical forecasting, machine-learning
models, held-out evaluation, and a Streamlit dashboard.

### Data Profile

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

### Model Evaluation

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


### Potential Planning Use

Forecasts may help analysts explore possible changes in care load and
discharge demand. They should be reviewed alongside operational
information and domain expertise.

### Limitations and Safeguards

- Forecasts are estimates and are not guarantees.
- Irregular historical dates limit calendar-day interpretation.
- Empirical error bands are not formal confidence intervals.
- Scenario adjustments are hypothetical.
- Capacity-breach probability should not be reported without a
  validated probability method and verified capacity threshold.
- Forecast outputs should not independently determine placement
  or resource-allocation decisions.

### Recommended Next Steps

1. Validate model performance on additional time periods.
2. Compare against appropriate baseline forecasts.
3. Verify data definitions and calendar coverage.
4. Obtain a defensible operational capacity threshold.
5. Review findings with subject-matter experts before implementation.
