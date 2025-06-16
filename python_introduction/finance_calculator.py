monthly_income=int(input('Enter your monthly income: '))
total_monthly_expenses=int(input('Enter your total monthly expenses: '))
Monthly_Savings=monthly_income-total_monthly_expenses
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print(Monthly_Savings)
print(Projected_Savings)
