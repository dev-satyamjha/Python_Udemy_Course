import matplotlib.pyplot as plt

monthly_income: float = 100000
rent: float = 10000
food: float = 5000
tax_rate: float = 0.22
taxes: float = monthly_income * tax_rate
other_expenses: float = 20000

yearly_income : float = monthly_income * 12
yearly_expenses: float = sum([rent,food,taxes,other_expenses]) * 12
yearly_savings: float = yearly_income - yearly_expenses

monthly_categories: list[str] = ['Income', 'Rent', 'Food', 'Taxes', 'Others']
monthly_amounts: list[float] = [monthly_income, rent, food, taxes, other_expenses]
monthly_indicators: list[str] = ['green', 'red', 'yellow', 'brown', 'orange']

yearly_categories: list[str] = ['Income', 'Expenses', 'Savings']
yearly_amounts: list[float] = [yearly_income, yearly_expenses, yearly_savings]
yearly_indicators: list[str] = ['green', 'red', 'blue']

fig, axes = plt.subplots(1, 2, figsize=(10,6))

axes[0].bar(monthly_categories, monthly_amounts, color=monthly_indicators)
axes[0].set_title('Monthly Expenditure Overview')
axes[0].set_ylabel('Amount in (₹)')
axes[0].tick_params(axis='x', rotation=45)

axes[1].bar(yearly_categories, yearly_amounts, color=yearly_indicators)
axes[1].set_title('Yearly Expenditure Overview')
axes[1].set_ylabel('Amount in (₹)')
axes[1].ticklabel_format(style='plain', axis='y') # Disable scientific notation

plt.tight_layout()
plt.show()
