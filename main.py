# Strategic Solvency Assessment: Altman Z-Score Analysis
# Target Entity: Tesla Inc. (TSLA)
# Prepared by: Maher Al-Momani, CMA Candidate

def calculate_z_score(company_name, working_capital, retained_earnings, ebit, market_cap, total_liabilities, sales, total_assets):
    # Analyzing core financial pillars: Liquidity, Cumulative Profitability, and Asset Efficiency
    X1 = working_capital / total_assets  # Working Capital efficiency
    X2 = retained_earnings / total_assets # Historical profitability retention
    X3 = ebit / total_assets              # Operating productivity (Return on Assets)
    X4 = market_cap / total_liabilities    # Market value vs. Debt burden (Leverage)
    X5 = sales / total_assets             # Asset turnover / Revenue generation
    
    # Applying the Altman Z-Score formula specifically for public manufacturing firms
    # Formula: Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5
    z_score = (1.2 * X1) + (1.4 * X2) + (3.3 * X3) + (0.6 * X4) + (1.0 * X5)
    
    # Risk Classification based on standard Altman thresholds
    if z_score > 2.99:
        status = "Safe Zone (Financial Stability Confirmed)"
    elif 1.81 <= z_score <= 2.99:
        status = "Grey Zone (Incipient Stress - Monitor Closely)"
    else:
        status = "Distress Zone (High Probability of Insolvency)"
        
    return z_score, status

# Tesla Inc. Financial Data (FY 2024 Estimates - Billions USD)
# Source: Estimated data for solvency testing
tesla_stats = {
    "company_name": "Tesla Inc.",
    "working_capital": 20.0,
    "retained_earnings": 28.0,
    "ebit": 9.0,
    "market_cap": 600.0,
    "total_liabilities": 43.0,
    "sales": 97.0,
    "total_assets": 106.0
}

score, zone = calculate_z_score(**tesla_stats)

# Professional Reporting Output
print(f"--- Investment-Grade Solvency Report for {tesla_stats['company_name']} ---")
print(f"Final Quantitative Z-Score: {score:.2f}")
print(f"Assessed Risk Condition: {zone}")
