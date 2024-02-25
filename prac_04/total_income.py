"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))
    get_income(incomes, months)
    print("\nIncome Report\n-------------")
    print_report(incomes, months)


def print_report(incomes, months):
    """Print report"""
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def get_income(incomes, months):
    """Get user income"""
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month} "))
        incomes.append(income)


main()
