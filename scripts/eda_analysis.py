import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")

# ====================================
# PATHS
# ====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")
CHART_DIR = os.path.join(OUTPUT_DIR, "charts")

os.makedirs(CHART_DIR, exist_ok=True)

# ====================================
# LOAD DATA
# ====================================

aum = pd.read_csv(
    os.path.join(OUTPUT_DIR, "aum_data_clean.csv")
)

sip = pd.read_csv(
    os.path.join(OUTPUT_DIR, "sip_data_clean.csv")
)

category = pd.read_csv(
    os.path.join(OUTPUT_DIR, "category_inflows_clean.csv")
)

folio = pd.read_csv(
    os.path.join(OUTPUT_DIR, "folio_count_clean.csv")
)

performance = pd.read_csv(
    os.path.join(OUTPUT_DIR, "scheme_performance_clean.csv")
)

transactions = pd.read_csv(
    os.path.join(OUTPUT_DIR, "transactions_clean.csv")
)

portfolio = pd.read_csv(
    os.path.join(OUTPUT_DIR, "portfolio_clean.csv")
)

benchmark = pd.read_csv(
    os.path.join(OUTPUT_DIR, "benchmark_clean.csv")
)

print("Datasets Loaded Successfully")

# ====================================
# CHART 1
# TOP FUND HOUSES
# ====================================

top_aum = (
    aum.groupby("fund_house")["aum_crore"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
top_aum.plot(kind="bar")

plt.title("Top Fund Houses by AUM")
plt.ylabel("AUM (Crore)")
plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "01_top_fund_houses.png"
    )
)

plt.close()

# ====================================
# CHART 2
# SIP TREND
# ====================================

plt.figure(figsize=(12,6))

plt.plot(
    sip["month"],
    sip["sip_inflow_crore"],
    marker="o"
)

plt.title("Monthly SIP Inflows")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "02_sip_trend.png"
    )
)

plt.close()

# ====================================
# CHART 3
# CATEGORY INFLOWS
# ====================================

category_group = (
    category.groupby("category")
    ["net_inflow_crore"]
    .sum()
)

plt.figure(figsize=(8,8))

category_group.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Category Inflows")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "03_category_inflows.png"
    )
)

plt.close()

# ====================================
# CHART 4
# FOLIO GROWTH
# ====================================

plt.figure(figsize=(12,6))

plt.plot(
    folio["month"],
    folio["total_folios_crore"]
)

plt.title("Industry Folio Growth")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "04_folio_growth.png"
    )
)

plt.close()

# ====================================
# CHART 5
# TOP RETURN FUNDS
# ====================================

top_returns = (
    performance.sort_values(
        "return_5yr_pct",
        ascending=False
    )
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    data=top_returns,
    x="return_5yr_pct",
    y="scheme_name"
)

plt.title("Top Funds by 5 Year Return")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "05_top_returns.png"
    )
)

plt.close()

# ====================================
# CHART 6
# ALPHA VS BETA
# ====================================

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=performance,
    x="beta",
    y="alpha"
)

plt.title("Alpha vs Beta")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "06_alpha_beta.png"
    )
)

plt.close()

# ====================================
# CHART 7
# TRANSACTION TYPES
# ====================================

plt.figure(figsize=(8,8))

transactions[
    "transaction_type"
].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Transaction Distribution")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "07_transaction_types.png"
    )
)

plt.close()

# ====================================
# CHART 8
# STATE ANALYSIS
# ====================================

top_states = (
    transactions["state"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12,6))

top_states.plot(kind="bar")

plt.title("Top States by Transactions")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "08_top_states.png"
    )
)

plt.close()

# ====================================
# CHART 9
# SECTOR ALLOCATION
# ====================================

sector_alloc = (
    portfolio.groupby("sector")
    ["weight_pct"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

sector_alloc.plot(
    kind="bar"
)

plt.title("Sector Allocation")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "09_sector_allocation.png"
    )
)

plt.close()

# ====================================
# CHART 10
# BENCHMARK TREND
# ====================================

nifty = benchmark[
    benchmark["index_name"]
    == benchmark["index_name"].iloc[0]
]

plt.figure(figsize=(12,6))

plt.plot(
    nifty["close_value"]
)

plt.title("Benchmark Trend")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHART_DIR,
        "10_benchmark_trend.png"
    )
)

plt.close()

print("\nAll Charts Generated Successfully")