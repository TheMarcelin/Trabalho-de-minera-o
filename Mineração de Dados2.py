import pandas as pd
import matplotlib.pyplot as plt
bebidas = pd.read_csv('drinks.csv') 

bebidas.rename(columns={"country": "País", "beer_servings":"Cervejas", "spirit_servings": "Licor", "wine_servings" : "Vinho", "total_litres_of_pure_alcohol":"Litros de Álcool Puro"}, inplace=True)

aux = bebidas.sort_values("Cervejas")
aux = aux[164:194]
plt.bar(aux["País"],aux["Cervejas"])
plt.xlabel("País")
plt.ylabel("Cervejas")
plt.xticks(rotation = 90)
plt.show()