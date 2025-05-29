monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
annual_interest_rate = 0.05
savings_before_interest = monthly_savings * 12
projected_savings = savings_before_interest + (savings_before_interest * annual_interest_rate)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")