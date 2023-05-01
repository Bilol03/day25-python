import pandas
import pandas as pd
#
df = pd.read_csv('./weather_data.csv')
#
# print(df['temp'])
#
# data_dict = df.to_dict()
# print(data_dict)
#
# data_list = df['temp'].to_list()
#
# print(data_list)
#
# avr = df['temp'].mean()
#
# print(avr)
#
# max_value = df['temp'].max()
#
# print(max_value)
#


# Celsius to Fahrenheit

# celsius = df['temp']
#
# for i in celsius:
#     fahrenhit = (i * 9/5) + 32
#
#     print(fahrenhit)



data_dict = {
    "students": ["Bilol", "Elyor", "Shahzod"],
    "scores": [20, 22, 25]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv('new_data.csv')
