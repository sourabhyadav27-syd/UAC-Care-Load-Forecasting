from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ==================================================
# 1. CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="UAC Forecasting | Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent


# ==================================================
# 2. DATA LOADER
# ==================================================
@st.cache_data
def load_csv(filename):
    path = BASE_DIR / filename

    if not path.exists():
        return None

    try:
        return pd.read_csv(path)
    except Exception:
        return None


future = load_csv("future_forecast_results.csv")
validation = load_csv("forecast_validation_metrics.csv")
uncertainty = load_csv("forecast_uncertainty_results.csv")
care_comparison = load_csv("final_model_comparison.csv")
discharge_comparison = load_csv("discharge_model_comparison.csv")
combined = load_csv("combined_forecast_analysis.csv")


# ==================================================
# 3. HEADER
# ==================================================
st.title("UAC Care Load & Placement Demand Forecasting")
st.caption(
    "Integrated forecasting | Model validation | "
    "Uncertainty analysis | Scenario planning"
)

st.divider()


# ==================================================
# 4. SIDEBAR
# ==================================================
st.sidebar.title("Dashboard Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Executive Overview",
        "Care Load Forecast",
        "Discharge Demand",
        "Model Comparison",
        "Forecast Uncertainty",
        "Scenario Planning",
        "Data & Validation"
    ]
)


# ==================================================
# 5. HELPER FUNCTIONS
# ==================================================
def show_table(data, title):
    st.subheader(title)

    if data is None:
        st.warning("Required CSV file is not available.")
        return

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )


def draw_forecast(data, date_column, columns, title):
    if data is None or data.empty:
        st.warning("No forecast data available.")
        return

    if date_column not in data.columns:
        st.warning(f"Missing column: {date_column}")
        return

    view = data.copy()
    view[date_column] = pd.to_datetime(
        view[date_column],
        errors="coerce"
    )
    view = view.dropna(subset=[date_column])

    available_columns = [
        col for col in columns
        if col in view.columns
    ]

    if not available_columns:
        st.warning("No matching forecast columns found.")
        return

    fig, ax = plt.subplots(figsize=(12, 5))

    for col in available_columns:
        ax.plot(
            view[date_column],
            pd.to_numeric(view[col], errors="coerce"),
            marker="o",
            label=col.replace("_", " ")
        )

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Forecast value")
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.autofmt_xdate()
    st.pyplot(fig)
    plt.close(fig)


def get_column_mean(data, column):
    if data is None or column not in data.columns:
        return None

    values = pd.to_numeric(data[column], errors="coerce")
    return values.mean()


# ==================================================
# 6. EXECUTIVE OVERVIEW
# ==================================================
if page == "Executive Overview":

    st.header("Executive Overview")

    if future is None:
        st.error(
            "future_forecast_results.csv missing. "
            "Run Task 11 first."
        )
    else:
        horizon_max = min(
            30,
            int(future["Forecast_Step"].max())
        )

        horizon = st.slider(
            "Forecast Horizon (steps)",
            min_value=1,
            max_value=horizon_max,
            value=min(7, horizon_max)
        )

        view = future.head(horizon)

        care_col = "HHS_Care_Random_Forest_Forecast"
        discharge_col = "Discharged_Random_Forest_Forecast"

        care_mean = get_column_mean(view, care_col)
        discharge_mean = get_column_mean(view, discharge_col)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Forecast Care Load",
            f"{care_mean:,.1f}" if care_mean is not None else "N/A"
        )

        col2.metric(
            "Average Forecast Discharges",
            f"{discharge_mean:,.1f}"
            if discharge_mean is not None else "N/A"
        )

        col3.metric(
            "Forecast Steps",
            len(view)
        )

        st.info(
            "Forecasts are model estimates, not observed outcomes. "
            "The selected model is not necessarily the best-performing "
            "model on the held-out test period."
        )

        draw_forecast(
            view,
            "Forecast_Date",
            [
                "HHS_Care_Random_Forest_Forecast",
                "HHS_Care_Gradient_Boosting_Forecast"
            ],
            "Future Care Load Forecast"
        )

        draw_forecast(
            view,
            "Forecast_Date",
            [
                "Discharged_Random_Forest_Forecast",
                "Discharged_Gradient_Boosting_Forecast"
            ],
            "Future Discharge Demand"
        )


# ==================================================
# 7. CARE LOAD FORECAST
# ==================================================
elif page == "Care Load Forecast":

    st.header("Future Care Load Forecast")

    if future is None:
        st.warning("Future forecast file not available.")
    else:
        model_choice = st.selectbox(
            "Select Model",
            ["Random Forest", "Gradient Boosting", "Compare Both"]
        )

        horizon = st.slider(
            "Forecast Steps",
            1,
            min(30, int(future["Forecast_Step"].max())),
            min(7, int(future["Forecast_Step"].max()))
        )

        view = future.head(horizon)

        if model_choice == "Random Forest":
            cols = ["HHS_Care_Random_Forest_Forecast"]
        elif model_choice == "Gradient Boosting":
            cols = ["HHS_Care_Gradient_Boosting_Forecast"]
        else:
            cols = [
                "HHS_Care_Random_Forest_Forecast",
                "HHS_Care_Gradient_Boosting_Forecast"
            ]

        draw_forecast(
            view,
            "Forecast_Date",
            cols,
            "Care Load Forecast"
        )

        show_table(view, "Forecast Data")


# ==================================================
# 8. DISCHARGE DEMAND
# ==================================================
elif page == "Discharge Demand":

    st.header("Discharge Demand Forecast")

    if future is None:
        st.warning("Future forecast file not available.")
    else:
        horizon = st.slider(
            "Forecast Steps",
            1,
            min(30, int(future["Forecast_Step"].max())),
            min(7, int(future["Forecast_Step"].max()))
        )

        view = future.head(horizon)

        draw_forecast(
            view,
            "Forecast_Date",
            [
                "Discharged_Random_Forest_Forecast",
                "Discharged_Gradient_Boosting_Forecast"
            ],
            "Discharge Demand Forecast"
        )

        show_table(view, "Discharge Forecast Data")


# ==================================================
# 9. MODEL COMPARISON
# ==================================================
elif page == "Model Comparison":

    st.header("Model Comparison")

    show_table(
        care_comparison,
        "Care Load Model Comparison"
    )

    show_table(
        discharge_comparison,
        "Discharge Model Comparison"
    )

    show_table(
        validation,
        "Held-out Test Validation Metrics"
    )

    st.caption(
        "Compare RMSE, MAE and MAPE only when the target, "
        "test dates and evaluation procedure are comparable."
    )


# ==================================================
# 10. FORECAST UNCERTAINTY
# ==================================================
elif page == "Forecast Uncertainty":

    st.header("Forecast Uncertainty")

    if uncertainty is None:
        st.warning(
            "forecast_uncertainty_results.csv not available."
        )
    else:
        target = st.selectbox(
            "Target",
            ["HHS_Care", "Discharged"]
        )

        model = st.selectbox(
            "Model",
            ["Random_Forest", "Gradient_Boosting"]
        )

        view = uncertainty[
            (uncertainty["Target"] == target)
            & (uncertainty["Model"] == model)
        ].copy()

        if view.empty:
            st.warning("No uncertainty results for this selection.")
        else:
            view["Forecast_Date"] = pd.to_datetime(
                view["Forecast_Date"],
                errors="coerce"
            )

            fig, ax = plt.subplots(figsize=(12, 5))

            ax.plot(
                view["Forecast_Date"],
                view["Forecast"],
                label="Forecast"
            )

            ax.fill_between(
                view["Forecast_Date"],
                view["Empirical_Lower_Band"],
                view["Empirical_Upper_Band"],
                alpha=0.2,
                label="Empirical error band"
            )

            ax.set_title(f"{target} Forecast Uncertainty")
            ax.set_xlabel("Date")
            ax.set_ylabel("Forecast value")
            ax.legend()
            ax.grid(True, alpha=0.3)

            fig.autofmt_xdate()
            st.pyplot(fig)
            plt.close(fig)

            st.warning(
                "These are empirical bands based on historical test "
                "errors, not formal confidence intervals."
            )

            show_table(view, "Uncertainty Results")


# ==================================================
# 11. SCENARIO PLANNING
# ==================================================
elif page == "Scenario Planning":

    st.header("What-if Scenario Planning")

    if future is None:
        st.warning("Future forecast file not available.")
    else:
        horizon = st.slider(
            "Forecast Steps",
            1,
            min(30, int(future["Forecast_Step"].max())),
            min(7, int(future["Forecast_Step"].max()))
        )

        care_change = st.slider(
            "Hypothetical Care Load Change (%)",
            -50,
            100,
            0,
            step=5
        )

        discharge_change = st.slider(
            "Hypothetical Discharge Change (%)",
            -50,
            100,
            0,
            step=5
        )

        capacity = st.number_input(
            "Illustrative Capacity Threshold",
            min_value=1,
            value=1000,
            step=50
        )

        view = future.head(horizon).copy()

        view["Base_Care_Load"] = view[
            "HHS_Care_Random_Forest_Forecast"
        ]

        view["Scenario_Care_Load"] = (
            view["Base_Care_Load"] * (1 + care_change / 100)
        )

        view["Base_Discharges"] = view[
            "Discharged_Random_Forest_Forecast"
        ]

        view["Scenario_Discharges"] = (
            view["Base_Discharges"]
            * (1 + discharge_change / 100)
        )

        view["Above_Illustrative_Threshold"] = (
            view["Scenario_Care_Load"] > capacity
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Scenario Care Load",
            f"{view['Scenario_Care_Load'].mean():,.1f}"
        )

        col2.metric(
            "Average Scenario Discharges",
            f"{view['Scenario_Discharges'].mean():,.1f}"
        )

        col3.metric(
            "Steps Above Threshold",
            f"{view['Above_Illustrative_Threshold'].sum()} / {len(view)}"
        )

        draw_forecast(
            view,
            "Forecast_Date",
            ["Base_Care_Load", "Scenario_Care_Load"],
            "Base vs Scenario Care Load"
        )


# ==================================================
# 12. DATA AND VALIDATION
# ==================================================
elif page == "Data & Validation":

    st.header("Data & Validation")

    show_table(
        validation,
        "Forecast Validation Metrics"
    )

    show_table(
        combined,
        "Combined Historical Forecast Analysis"
    )


# ==================================================
# 13. FOOTER
# ==================================================
st.divider()

st.caption(
    "UAC Forecasting Project | Integrated research prototype | "
    "Forecasts require further validation before operational use."
)



