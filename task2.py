import pandas as pd

file_path = 'dz.csv'
df = pd.read_csv(file_path)

average_salary_by_city = df.groupby('City')['Salary'].mean()

print("Средняя зарплата по городам:")
print(average_salary_by_city)