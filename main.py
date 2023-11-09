
import pandas as pd
# read drinks.csv into a DataFrame called 'drinks'
drinks = pd.read_table('drinks.csv', sep=',')
drinks = pd.read_csv('drinks.csv')              # assumes separator is comma
print(drinks)


print('\n\n\n\88888888888888888       head tail  8888888888888888888888888888888888888888888888888888888888888888888')
# print the head and the tail
print(drinks.head())
print(drinks.tail())
print('\n\n\n\888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(drinks.index)
print(drinks.dtypes)
print(drinks.shape)

print('\n\n\n\888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
drinks['beer_servings']
print(drinks.beer_servings)
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(drinks.beer_servings.mean())
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(drinks.continent.value_counts())
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
drinks.continent
drinks.continent=='EU'
print(drinks[drinks.continent=='EU'])



print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
#ufo = pd.read_table('ufo.csv', sep=',')
ufo = pd.read_csv('ufo.csv')
print(ufo)
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(ufo.describe())
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(ufo[ufo.State=='VA'].City.value_counts().head(1))

print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True))
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(ufo.City.value_counts())
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
print(ufo.dropna().shape[0])
print('\n\n\n888888888888888888888888888888888888888888888888888888888888888888888888888888888888')




















