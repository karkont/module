import requests

url = 'https://www.speedtest.net/'

response = requests.get(url)

if response.status_code == 200:

    print("Данные получены успешно:")
    print(response.text)
else:
    print(f"Ошибка при запросе данных: {response.status_code}")

import pandas as pd


file_path = 'data.csv'
data = pd.read_csv(file_path)


average_age = data['Age'].mean()
average_salary = data['Salary'].mean()


highest_salary_person = data.loc[data['Salary'].idxmax()]


print("Средний возраст:", average_age)
print("Средняя зарплата:", average_salary)
print("Человек с самой высокой зарплатой:",
      highest_salary_person['Name'], "с зарплатой", highest_salary_person['Salary'])


import numpy as np


arr = np.array([1, 2, 3, 4, 5])


print("Исходный массив:")
print(arr)


arr_add = arr + 10
print("\nПосле сложения каждого элемента на 10:")
print(arr_add)


arr_sub = arr - 2
print("\nПосле вычитания 2 из каждого элемента:")
print(arr_sub)


arr_mul = arr * 3
print("\nПосле умножения каждого элемента на 3:")
print(arr_mul)


arr_div = arr / 2
print("\nПосле деления каждого элемента на 2:")
print(arr_div)


arr_pow = arr ** 2
print("\nКаждый элемент возведён в степень 2:")
print(arr_pow)


