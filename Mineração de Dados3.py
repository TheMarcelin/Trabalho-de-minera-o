import pandas as pd
import matplotlib.pyplot as plt
bebidas = pd.read_csv('drinks.csv') 

bebidas.rename(columns={"country": "País", "beer_servings":"Cervejas", "spirit_servings": "Licor", "wine_servings" : "Vinho", "total_litres_of_pure_alcohol":"Litros de Álcool Puro"}, inplace=True)

aux = bebidas.sort_values("Litros de Álcool Puro")
aux = aux[0:30]
plt.bar(aux["País"],aux["Litros de Álcool Puro"])
plt.xlabel("País")
plt.ylabel("Litros de Álcool Puro")
plt.xticks(rotation = 90)
plt.show()