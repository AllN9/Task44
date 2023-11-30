import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

print('Полученный DataFrame, который состоит всего из 1 столбца:')
print(data, '\n')

new_data = pd.get_dummies(data, dtype=int)

print('One hot вид данной таблицы:')
print(new_data, '\n')

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None

print('One hot вид данной таблицы без использования get_dummies:')
print(data)