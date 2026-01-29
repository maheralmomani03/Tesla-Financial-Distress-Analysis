# Project: Financial Distress Prediction (Altman Z-Score)
# Analyst: Maher Al-Momani

def calculate_z_score(company_name, working_capital, retained_earnings, ebit, market_cap, total_liabilities, sales, total_assets):
    # 1. Financial Ratios Calculation
    X1 = working_capital / total_assets
    X2 = retained_earnings / total_assets
    X3 = ebit / total_assets
    X4 = market_cap / total_liabilities
    X5 = sales / total_assets
    
    # 2. Altman Z-Score Formula for Public Manufacturing Companies
    z_score = (1.2 * X1) + (1.4 * X2) + (3.3 * X3) + (0.6 * X4) + (1.0 * X5)
    
    # 3. Decision Logic (Standard Zones)
    if z_score > 2.99:
        status = "Safe Zone (Strong Financial Position)"
    elif 1.81 <= z_score <= 2.99:
        status = "Grey Zone (Monitor Closely)"
    else:
        status = "Distress Zone (High Bankruptcy Risk)"
        
    return z_score, status

# Tesla Inc. Financial Data (FY 2024 Estimates in Billions USD)
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

print(f"--- Financial Analysis for {tesla_stats['company_name']} ---")
print(f"Final Z-Score: {score:.2f}")
print(f"Current Condition: {zone}")
