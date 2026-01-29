import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Strategic Solvency Analysis: Altman Z-Score Model ---
# Analyst: Maher Al-Momani, CMA Candidate
# Focus: Assessing Tesla Inc. (TSLA) Financial Health & Bankruptcy Risk

def analyze_solvency(working_capital, retained_earnings, ebit, market_cap, total_liabilities, sales, total_assets):
    # Standard Financial Ratios for Public Manufacturing Entities
    x1 = working_capital / total_assets  # Liquidity Ratio: Measures ability to cover short-term debt
    x2 = retained_earnings / total_assets # Cumulative Profitability: Measures historical reinvested earnings
    x3 = ebit / total_assets              # Operating Efficiency: Measures asset productivity (ROA)
    x4 = market_cap / total_liabilities    # Market Leverage: Measures equity value vs total debt load
    x5 = sales / total_assets             # Asset Turnover: Measures sales generation efficiency

    # Altman Z-Score Multivariate Formula
    z_score = (1.2 * x1) + (1.4 * x2) + (3.3 * x3) + (0.6 * x4) + (1.0 * x5)
    
    return z_score, [x1, x2, x3, x4, x5]

# Dashboard Configuration
st.set_page_config(page_title="Tesla Solvency Analysis", page_icon="⚖️", layout="wide")

st.title("📊 Tesla Inc. Financial Health Assessment")
st.markdown("### Methodology: Altman Z-Score for Public Manufacturing Companies")
st.write("---")

# Tesla Financial Estimates (FY 2024 - In Billions USD)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 Core Financial Metrics")
    assets = st.number_input("Total Assets", value=106.0, help="Total resources controlled by the entity")
    wc = st.number_input("Working Capital", value=20.0, help="Current Assets - Current Liabilities")
    re = st.number_input("Retained Earnings", value=28.0, help="Accumulated net income not distributed to shareholders")
    ebit = st.number_input("EBIT", value=9.0, help="Earnings Before Interest and Taxes")
    m_cap = st.number_input("Market Cap", value=600.0, help="Market value of outstanding shares")
    liab = st.number_input("Total Liabilities", value=43.0, help="Total debt and obligations")
    sales = st.number_input("Total Revenue", value=97.0, help="Top-line sales performance")

# Execute Analysis
score, ratios = analyze_solvency(wc, re, ebit, m_cap, liab, sales, assets)

with col2:
    st.subheader("🎯 Solvency Verdict & Analysis")
    
    # Conditional logic for visual output
    if score > 2.99:
        st.success(f"Final Z-Score: {score:.2f} | SAFE ZONE")
        st.info("The model confirms a strong financial position with minimal bankruptcy risk.")
    elif 1.81 <= score <= 2.99:
        st.warning(f"Final Z-Score: {score:.2f} | GREY ZONE")
        st.write("Caution advised. Financial health is stable but requires close monitoring.")
    else:
        st.error(f"Final Z-Score: {score:.2f} | DISTRESS ZONE")
        st.write("High financial distress risk detected. Significant insolvency probability.")

    # Visualization of Individual Ratio Weights
    fig = go.Figure(go.Bar(
        x=['Liquidity (X1)', 'Profitability (X2)', 'Efficiency (X3)', 'Market Value (X4)', 'Turnover (X5)'],
        y=ratios,
        marker_color='#FF4B4B'
    ))
    fig.update_layout(
        title="Key Financial Drivers (Ratio Contribution)",
        template="plotly_dark",
        yaxis_title="Ratio Value"
    )
    st.plotly_chart(fig, use_container_width=True)

st.write("---")
st.caption("Developed by Maher Al-Momani | Accounting & Data Analysis Student")
