import pandas as pd

# Считываем данные из файлов
doc1 = pd.read_excel('ActiveLoans_2024.xlsx')
doc2 = pd.read_excel('Сегмент.xlsx')

# Сверка данных
doc1['Сегмент'] = doc1['Кредитный продукт'].map(doc2.set_index('Кредитный продукт')['Сегмент'])

# Обновление данных
doc1.loc[doc1['Сегмент'].notna(), 'Сегмент'] = doc1['Сегмент']

# Сохранение результата
doc1.to_excel('ActiveLoans_2024_updated.xlsx', index=False)










