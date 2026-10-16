# Predictive Forecasting of Care Load and Placement Demand

## Project Overview
This project analyses historical Unaccompanied Alien Children (UAC)
programme data to study care-load forecasting, discharge demand,
and operational planning.

## Objectives
- Analyse historical care-load and discharge patterns.
- Compare baseline, statistical, and machine-learning models.
- Evaluate forecasts on held-out observations.
- Visualise future forecasts and forecast uncertainty.
- Explore scenario-based operational planning.

## Tools and Technologies
- Microsoft Excel
- MySQL
- Python
- Pandas and NumPy
- Scikit-learn
- Statsmodels
- Matplotlib
- Streamlit

## Main Deliverables
- Data validation and exploratory analysis
- Forecasting model comparisons
- Forecast validation metrics
- Future forecast results
- Forecast uncertainty estimates
- Streamlit dashboard
- Research paper draft
- Executive summary

## Important Limitations
The dataset contains missing calendar dates. Missing dates should not
automatically be treated as zero observations.

Lag and rolling features may refer to previous observed records rather
than exact calendar-day intervals.

One-step-ahead validation does not guarantee the same accuracy for
multi-day recursive forecasts.

Residual-based forecast bands are empirical uncertainty estimates,
not guaranteed confidence intervals.

Capacity breach probabilities require suitable capacity data and a
validated probabilistic approach.

## Run the Dashboard
Install the dependencies in requirements.txt, then run:

python -m streamlit run 16_main_dashboard.py

## Responsible Use
Forecasts are analytical estimates and should be validated before
being used for real-world operational decisions.