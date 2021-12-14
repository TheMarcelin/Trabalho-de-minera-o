import pandas as pd
import matplotlib.pyplot as plt
bebidas = pd.read_csv('drinks.csv') 

bebidas.rename(columns={"country": "País", "beer_servings":"Cervejas", "spirit_servings": "Licor", "wine_servings" : "Vinho", "total_litres_of_pure_alcohol":"Litros de Álcool Puro"}, inplace=True)

auxbebidas = bebidas.loc[bebidas['Litros de Álcool Puro']>=10.0]
print(auxbebidas)

plt.bar(auxbebidas["País"],auxbebidas["Litros de Álcool Puro"])
plt.xlabel("País")
plt.ylabel("Litros de Álcool Puro")
plt.xticks(rotation = 90)
plt.show()

 