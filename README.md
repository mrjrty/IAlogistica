Projeto de Logística - Modelo de Previsão de Rotas
Este é um projeto de logística que implementa um modelo de previsão de rotas com base em dados simulados. O modelo é criado utilizando a técnica de regressão logística e é capaz de aprender a rota mais provável entre origem e destino, levando em consideração informações como tempo de entrega, condições das estradas e tráfegos.

Funcionamento
O código principal está no arquivo logistica.py. A implementação do modelo de regressão logística é feita utilizando a biblioteca scikit-learn.

O fluxo do código é o seguinte:

Dados de logística:

origens: Uma lista contendo as origens das rotas simuladas.
destinos: Uma lista contendo os destinos correspondentes às origens.
tempos_entrega: Uma lista contendo os tempos de entrega simulados para cada rota.
condicoes_estradas: Uma lista contendo as condições das estradas simuladas para cada rota.
trafegos: Uma lista contendo os níveis de tráfego simulados para cada rota.
rotas: Uma lista contendo as rotas completas no formato "Origem -> Destino".
Preparação dos dados:

Os dados de origens e destinos são codificados utilizando a técnica One-Hot Encoding, transformando as variáveis categóricas em vetores binários.
As variáveis categóricas codificadas são combinadas com as variáveis numéricas (tempos de entrega, condições das estradas e tráfegos) para formar a matriz de entrada X.
As rotas completas são usadas como rótulos de saída y.
Divisão dos dados:

A matriz de entrada X e os rótulos y são divididos em conjuntos de treinamento e teste usando a função train_test_split da biblioteca scikit-learn.
Treinamento do modelo:

O modelo de regressão logística é criado e treinado utilizando o conjunto de treinamento.
Avaliação do modelo:

A acurácia do modelo é calculada utilizando o conjunto de teste.
Previsão de rota:

É feita uma previsão de rota utilizando um exemplo fornecido na forma de uma matriz.
Visualização dos dados:

São criados gráficos para visualizar os dados de logística, incluindo gráficos de barras para tempo de entrega por origem e destino, um gráfico de dispersão para visualizar as condições das estradas em relação ao tráfego, e um gráfico de pizza para mostrar a distribuição das origens.
Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o código:

NumPy
Matplotlib
scikit-learn
