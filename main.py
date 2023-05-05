import pandas as pd


# df = pd.read_csv('./weather_data.csv')
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



# data_dict = {
#     "students": ["Bilol", "Elyor", "Shahzod"],
#     "scores": [20, 22, 25]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv('new_data.csv')


central_park = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray = 0
cinnamon = 0
black = 0
nan = 0
for i in central_park['Primary Fur Color']:
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        cinnamon += 1
    elif i == "Black":
        black += 1
    elif i == "nan":
        nan += 1


all = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Counts": [gray, cinnamon, black]
}

df = pd.DataFrame(all)
df.to_csv("count_result.csv")
# print(f"""
#     Grays are: {gray},
#     Cinnamons are: {cinnamon},
#     Blacks are: {black}
# """)