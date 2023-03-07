# Responder a pergunta: "Vamos invertir 75k em marketing, qual er o estoque enviado para a loja?"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importar a base de vendas
base = pd.read_excel("Investimento_x_Vendas.xlsx")

# Exibindo as 5 primeiras linhas
base.head()

# Visualizando de forma gráfica essas informaçõe
plt.scatter(base["Investimento em marketing"], base["Venda Qtd"])
plt.show()

# Traçando uma reta
plt.scatter(base["Investimento em marketing"], base["Venda Qtd"])
x0 = base["Investiment em marketing"][0]
y0 = base["Venda Qtd"][0]
x1 = base["Investimento em marketing"][6]
y1 = base["Venda Qtd"][6]
plt.plot([x0, x1], [y0, y1], "r")
plt.show()

# Usando a equação de reta para determinar a venda
def EncontrarY(x_reta, y_reta, x):
    a = (y_reta[1] - y_reta[0]) / (x_reta[1] - x_reta[0])
    b = y_reta[1] - a * x_reta[1]
    y = a * x + b
    return y

EncontrarY([x0, x1], [y0, y1], 75)

plt.scatter(base["Investimento em marketing"], base["Venda Qtd"])
plt.scatter(75, EncontrarY([x0, x1], [y0, y1], 75), color="k")
x0 = base["Investimento em marketing"], [0]
y0 = base["Venda qtd"][0]
x1 = base["Investimento em marketing"][6]
y1 = base["Venda Qtd"][6]
plt.plot([x0, x1], [y0, y1], "r")
plt.show()

# Descobrindo a venda usando Machine Learning
from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(base["Investimento em marketing"].value.reshape(-1, 1), base["Venda Qtd"])
reg.coef_
reg.intercept_

# Tipo de dado (Data Frame)
type(base)

# Visualizando o DataFrame
base.head()
coluna = base["Investimento em marketing"]

# Tipo de coluna (Series)
type(coluna)

# Visualizando a Series
coluna

# Pegando apenas valores
coluan.values

# Pegando apenas os Índices
coluna.index