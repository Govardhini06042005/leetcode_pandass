import pandas as pd

#def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
 #   ddd=employee['salary'].drop_duplicates().sort_values(ascending=False)
  #  if len(ddd)<N:
   #     return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    #return pd.DataFrame({f'getNthHighestSalary({N})':[ddd.iloc[N-1]]})

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = f'getNthHighestSalary({N})'

    # 🔴 IMPORTANT CHECK
    if N <= 0:
        return pd.DataFrame({col: [None]})

    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(salaries) < N:
        return pd.DataFrame({col: [None]})

    return pd.DataFrame({col: [salaries.iloc[N-1]]})
