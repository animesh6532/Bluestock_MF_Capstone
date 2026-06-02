import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

CLEANED_DIR = os.path.join(
    PROJECT_ROOT,
    "outputs",
    "Cleaned_Data"
)

REPORT_DIR = os.path.join(
    PROJECT_ROOT,
    "outputs",
    "reports"
)

os.makedirs(REPORT_DIR, exist_ok=True)

df = pd.read_csv(
    os.path.join(
        CLEANED_DIR,
        "scheme_performance_clean.csv"
    )
)

# Conservative Investor
conservative = df[
    (df["beta"] < 0.8) &
    (df["sharpe_ratio"] > 1)
]

# Moderate Investor
moderate = df[
    (df["beta"] >= 0.8) &
    (df["beta"] <= 1.2)
]

# Aggressive Investor
aggressive = df[
    (df["return_5yr_pct"] > df["return_5yr_pct"].median())
]

conservative.sort_values(
    "sharpe_ratio",
    ascending=False
).head(10).to_csv(
    os.path.join(
        REPORT_DIR,
        "recommended_conservative.csv"
    ),
    index=False
)

moderate.sort_values(
    "return_5yr_pct",
    ascending=False
).head(10).to_csv(
    os.path.join(
        REPORT_DIR,
        "recommended_moderate.csv"
    ),
    index=False
)

aggressive.sort_values(
    "return_5yr_pct",
    ascending=False
).head(10).to_csv(
    os.path.join(
        REPORT_DIR,
        "recommended_aggressive.csv"
    ),
    index=False
)

print("Recommendation Engine Completed")