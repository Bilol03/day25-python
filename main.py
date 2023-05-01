import pandas as pd

df = pd.read_csv('./weather_data.csv')

print(df['temp'])

data_dict = df.to_dict()
print(data_dict)

data_list = df['temp'].to_list()

print(data_list)

avr = df['temp'].mean()

print(avr)

max_value = df['temp'].max()

print(max_value)


