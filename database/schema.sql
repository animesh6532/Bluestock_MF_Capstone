DROP TABLE IF EXISTS dim_fund;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS fact_performance;
DROP TABLE IF EXISTS fact_portfolio;
DROP TABLE IF EXISTS fact_aum;
DROP TABLE IF EXISTS fact_sip_industry;

---------------------------------------------------
-- FUND DIMENSION
---------------------------------------------------

CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_level TEXT
);

---------------------------------------------------
-- DATE DIMENSION
---------------------------------------------------

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);

---------------------------------------------------
-- NAV FACT
---------------------------------------------------

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    nav_date DATE,
    nav REAL
);

---------------------------------------------------
-- PERFORMANCE FACT
---------------------------------------------------

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL
);

---------------------------------------------------
-- AUM FACT
---------------------------------------------------

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    report_date DATE,
    aum REAL
);

---------------------------------------------------
-- SIP FACT
---------------------------------------------------

CREATE TABLE fact_sip_industry (
    sip_id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_month DATE,
    sip_amount REAL
);

---------------------------------------------------
-- TRANSACTIONS FACT
---------------------------------------------------

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id INTEGER,
    scheme_code INTEGER,
    transaction_type TEXT,
    amount REAL,
    transaction_date DATE
);

---------------------------------------------------
-- PORTFOLIO FACT
---------------------------------------------------

CREATE TABLE fact_portfolio (
    holding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    stock_name TEXT,
    sector TEXT,
    allocation_percent REAL
);