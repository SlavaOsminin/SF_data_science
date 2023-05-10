income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

import pandas as pd
def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
        'Income': income,
        'Expenses': expenses
        },
        index = years
    )
    return df
print(create_companyDF(income, expenses, years))

