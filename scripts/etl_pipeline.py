import pandas as pd
import os

print("=" * 60)
print("BLUESTOCK MUTUAL FUND ETL PIPELINE")
print("=" * 60)

# ---------------------------------------------------
# PATH CONFIGURATION
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------
# LOAD DATASETS
# ---------------------------------------------------

try:

    fund_master = pd.read_csv(
        os.path.join(DATA_DIR, "01_fund_master.csv")
    )

    nav_history = pd.read_csv(
        os.path.join(DATA_DIR, "02_nav_history.csv")
    )

    aum_data = pd.read_csv(
        os.path.join(DATA_DIR, "03_aum_by_fund_house.csv")
    )

    sip_data = pd.read_csv(
        os.path.join(DATA_DIR, "04_monthly_sip_inflows.csv")
    )

    category_inflows = pd.read_csv(
        os.path.join(DATA_DIR, "05_category_inflows.csv")
    )

    folio_count = pd.read_csv(
        os.path.join(DATA_DIR, "06_industry_folio_count.csv")
    )

    scheme_perf = pd.read_csv(
        os.path.join(DATA_DIR, "07_scheme_performance.csv")
    )

    transactions = pd.read_csv(
        os.path.join(DATA_DIR, "08_investor_transactions.csv")
    )

    portfolio = pd.read_csv(
        os.path.join(DATA_DIR, "09_portfolio_holdings.csv")
    )

    benchmark = pd.read_csv(
        os.path.join(DATA_DIR, "10_benchmark_indices.csv")
    )

    print("\nAll datasets loaded successfully!")

except Exception as e:

    print("\nDataset Loading Error:")
    print(e)

    exit()

# ---------------------------------------------------
# DATASET DICTIONARY
# ---------------------------------------------------

datasets = {
    "fund_master": fund_master,
    "nav_history": nav_history,
    "aum_data": aum_data,
    "sip_data": sip_data,
    "category_inflows": category_inflows,
    "folio_count": folio_count,
    "scheme_perf": scheme_perf,
    "transactions": transactions,
    "portfolio": portfolio,
    "benchmark": benchmark
}

# ---------------------------------------------------
# DATA PROFILING
# ---------------------------------------------------

print("\n" + "=" * 60)
print("DATASET PROFILING")
print("=" * 60)

summary_rows = []

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    print("-" * 40)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    missing = df.isnull().sum().sum()

    print(f"Missing Values: {missing}")

    duplicates = df.duplicated().sum()

    print(f"Duplicate Rows: {duplicates}")

    summary_rows.append({
        "dataset": name,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": missing,
        "duplicate_rows": duplicates
    })

# ---------------------------------------------------
# CLEANING
# ---------------------------------------------------

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

for name, df in datasets.items():

    before = len(df)

    df.drop_duplicates(inplace=True)

    after = len(df)

    print(
        f"{name}: Removed {before - after} duplicate rows"
    )

# ---------------------------------------------------
# SAVE CLEAN DATA
# ---------------------------------------------------

print("\n" + "=" * 60)
print("SAVING CLEAN FILES")
print("=" * 60)

fund_master.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "fund_master_clean.csv"
    ),
    index=False
)

nav_history.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "nav_history_clean.csv"
    ),
    index=False
)

aum_data.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "aum_data_clean.csv"
    ),
    index=False
)

sip_data.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "sip_data_clean.csv"
    ),
    index=False
)

category_inflows.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "category_inflows_clean.csv"
    ),
    index=False
)

folio_count.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "folio_count_clean.csv"
    ),
    index=False
)

scheme_perf.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "scheme_performance_clean.csv"
    ),
    index=False
)

transactions.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "transactions_clean.csv"
    ),
    index=False
)

portfolio.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "portfolio_clean.csv"
    ),
    index=False
)

benchmark.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "benchmark_clean.csv"
    ),
    index=False
)

# ---------------------------------------------------
# SAVE ETL REPORT
# ---------------------------------------------------

summary_df = pd.DataFrame(summary_rows)

summary_df.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "etl_summary_report.csv"
    ),
    index=False
)

# ---------------------------------------------------
# FINISH
# ---------------------------------------------------

print("\n" + "=" * 60)
print("ETL PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Files:")

for file in os.listdir(OUTPUT_DIR):
    print("✓", file)

print("\nOutput Folder:")
print(OUTPUT_DIR)