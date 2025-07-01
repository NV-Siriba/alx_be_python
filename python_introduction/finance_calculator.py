monthly_income=int(input('Enter your monthly income: '))
monthly_expenses=int(input('Enter your total monthly expenses: '))
monthly_savings=float(monthly_income)-float(monthly_expenses) # Changed to monthly_savings
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) # Changed to monthly_savings
print(monthly_savings) # Changed to monthly_savings
print(Projected_Savings)
