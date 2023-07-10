import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression

# Dados simulados de logística
origens = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador"]
destinos = ["Curitiba", "Porto Alegre", "Fortaleza", "Manaus", "Curitiba"]
tempos_entrega = [1, 2, 3, 4, 5]
condicoes_estradas = [0.8, 0.6, 0.7, 0.9, 0.5]
trafegos = [0.3, 0.2, 0.4, 0.1, 0.5]
rotas = ["São Paulo -> Curitiba", "Rio de Janeiro -> Fortaleza", "Belo Horizonte -> Porto Alegre",
         "Brasília -> Manaus", "Salvador -> Curitiba"]

# Preparação dos dados
enc = OneHotEncoder(sparse=False, handle_unknown="ignore")
origens_encoded = enc.fit_transform(np.array(origens).reshape(-1, 1))
destinos_encoded = enc.transform(np.array(destinos).reshape(-1, 1))
X = np.column_stack((origens_encoded, destinos_encoded, tempos_entrega, condicoes_estradas, trafegos))
y = rotas

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinamento do modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Avaliação do modelo
accuracy = model.score(X_test, y_test)
print(f"Acurácia do modelo: {accuracy}")

# Exemplo de previsão
#Salvador -> Curitiba
#exemplo = np.array([[0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 4, 0.5, 0.5]])
#Salvador -> Curitiba
exemplo = np.array([[1, 0, 2, 1, 0, 0, 0, 1, 0, 1, 4, 0.9, 0.3]])
previsao = model.predict(exemplo)
print(f"Previsão de rota: {previsao}")

# Gráfico de Barras - Origens
plt.bar(origens, tempos_entrega)
plt.xlabel("Origens")
plt.ylabel("Tempo de Entrega")
plt.title("Tempo de Entrega por Origem")
plt.show()

# Gráfico de Barras - Destinos
plt.bar(destinos, tempos_entrega)
plt.xlabel("Destinos")
plt.ylabel("Tempo de Entrega")
plt.title("Tempo de Entrega por Destino")
plt.show()

# Gráfico de Dispersão - Condições das Estradas x Trafegos
plt.scatter(condicoes_estradas, trafegos, c=tempos_entrega)
plt.colorbar(label="Tempo de Entrega")
plt.xlabel("Condições das Estradas")
plt.ylabel("Tráfegos")
plt.title("Condições das Estradas x Tráfegos")
plt.show()

# Gráfico de Pizza - Distribuição das Origens
plt.pie([origens.count(origem) for origem in set(origens)], labels=set(origens), autopct="%1.1f%%")
plt.title("Distribuição das Origens")
plt.show()
