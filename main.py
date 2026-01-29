import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Strategic Solvency Analysis: Altman Z-Score Model ---
# Analyst: Maher Al-Momani, CMA Candidate
# Focus: Assessing Tesla Inc. (TSLA) Financial Health & Bankruptcy Risk

def analyze_solvency(working_capital, retained_earnings, ebit, market_cap, total_liabilities, sales, total_assets):
    # Standard Financial Ratios for Public Manufacturing Entities
    x1 = working_capital / total_assets  # Liquidity Ratio
    x2 = retained_earnings / total_assets # Profitability / Cumulative Leverage
    x3 = ebit / total_assets              # Operating Efficiency (ROA)
    x4 = market_cap / total_liabilities    # Market Value of Equity / Total Debt
    x5 = sales / total_assets             # Asset Turnover

    # Altman Z-Score Formula
    z_score = (1.2 * x1) + (1.4 * x2) + (3.3 * x3) + (0.6 * x4) + (1.0 * x5)
    
    return z_score, [x1, x2, x3, x4, x5]

# Dashboard UI Settings
st.set_page_config(page_title="Tesla Solvency Analysis", page_icon="⚖️", layout="wide")

st.title("📊 Tesla Inc. Financial Health Assessment")
st.markdown("### Model: Altman Z-Score for Public Manufacturing Companies")
st.write("---")

# Tesla Estimates (FY 2024 - B USD)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 Input Metrics (Estimates)")
    assets = st.number_input("Total Assets", value=106.0)
    wc = st.number_input("Working Capital", value=20.0)
    re = st.number_input("Retained Earnings", value=28.0)
    ebit = st.number_input("EBIT", value=9.0)
    m_cap = st.number_input("Market Cap", value=600.0)
    liab = st.number_input("Total Liabilities", value=43.0)
    sales = st.number_input("Total Sales", value=97.0)

score, ratios = analyze_solvency(wc, re, ebit, m_cap, liab, sales, assets)

with col2:
    st.subheader("🎯 Solvency Verdict")
    
    # Display Score with conditional coloring
    if score > 2.99:
        st.success(f"Z-Score: {score:.2f} | SAFE ZONE")
        st.info("Tesla shows a strong financial position with minimal bankruptcy risk.")
    elif 1.81 <= score <= 2.99:
        st.warning(f"Z-Score: {score:.2f} | GREY ZONE")
        st.write("Monitor closely. Financial health is stable but under pressure.")
    else:
        st.error(f"Z-Score: {score:.2f} | DISTRESS ZONE")
        st.write("High financial distress risk detected.")

    # Visualization of Ratios
    fig = go.Figure(go.Bar(
        x=['Liquidity (X1)', 'Profitability (X2)', 'Efficiency (X3)', 'Market (X4)', 'Turnover (X5)'],
        y=ratios,
        marker_color='#FF4B4B'
    ))
    fig.update_layout(title="Financial Ratio Weights", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
