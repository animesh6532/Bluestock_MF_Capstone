import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")

CLEANED_DIR = os.path.join(
    OUTPUT_DIR,
    "Cleaned_Data"
)

REPORT_DIR = os.path.join(
    OUTPUT_DIR,
    "reports"
)

os.makedirs(REPORT_DIR, exist_ok=True)

performance = pd.read_csv(
    os.path.join(
        CLEANED_DIR,
        "scheme_performance_clean.csv"
    )
)

print("Performance Dataset Loaded Successfully")

# ==========================================
# FUND SCORE
# ==========================================

performance["fund_score"] = (
      performance["return_5yr_pct"] * 0.35
    + performance["sharpe_ratio"] * 0.25
    + performance["alpha"] * 0.20
    - performance["beta"] * 0.10
    - performance["max_drawdown_pct"] * 0.10
)

# ==========================================
# RISK CATEGORY
# ==========================================

def risk_label(beta):

    if beta < 0.8:
        return "Low Risk"

    elif beta < 1.2:
        return "Moderate Risk"

    else:
        return "High Risk"

performance["risk_profile"] = (
    performance["beta"]
    .apply(risk_label)
)

# ==========================================
# RANK FUNDS
# ==========================================

ranked = (
    performance
    .sort_values(
        "fund_score",
        ascending=False
    )
)

ranked["rank"] = (
    range(
        1,
        len(ranked)+1
    )
)

# ==========================================
# TOP 20 FUNDS
# ==========================================

top20 = ranked[
    [
        "rank",
        "scheme_name",
        "fund_house",
        "category",
        "return_5yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "max_drawdown_pct",
        "fund_score",
        "risk_profile"
    ]
].head(20)

top20.to_csv(
    os.path.join(
        REPORT_DIR,
        "top20_funds.csv"
    ),
    index=False
)

# ==========================================
# LOW RISK
# ==========================================

low_risk = ranked[
    ranked["risk_profile"]
    == "Low Risk"
]

low_risk.head(10).to_csv(
    os.path.join(
        REPORT_DIR,
        "low_risk_funds.csv"
    ),
    index=False
)

# ==========================================
# MODERATE RISK
# ==========================================

moderate_risk = ranked[
    ranked["risk_profile"]
    == "Moderate Risk"
]

moderate_risk.head(10).to_csv(
    os.path.join(
        REPORT_DIR,
        "moderate_risk_funds.csv"
    ),
    index=False
)

# ==========================================
# HIGH RISK
# ==========================================

high_risk = ranked[
    ranked["risk_profile"]
    == "High Risk"
]

high_risk.head(10).to_csv(
    os.path.join(
        REPORT_DIR,
        "high_risk_funds.csv"
    ),
    index=False
)

# ==========================================
# SUMMARY REPORT
# ==========================================

summary = pd.DataFrame({

    "Metric":[
        "Average Alpha",
        "Average Beta",
        "Average Sharpe",
        "Average Sortino",
        "Average Drawdown"
    ],

    "Value":[

        performance["alpha"].mean(),

        performance["beta"].mean(),

        performance["sharpe_ratio"].mean(),

        performance["sortino_ratio"].mean(),

        performance["max_drawdown_pct"].mean()

    ]

})

summary.to_csv(
    os.path.join(
        REPORT_DIR,
        "risk_summary.csv"
    ),
    index=False
)

print("\nRisk Analytics Completed")
print("\nGenerated Reports:")
print("- top20_funds.csv")
print("- low_risk_funds.csv")
print("- moderate_risk_funds.csv")
print("- high_risk_funds.csv")
print("- risk_summary.csv")