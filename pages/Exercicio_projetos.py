import streamlit as st
import pandas as pd  
import matplotlib.pyplot as plt

# Exercício Projetos
st.set_page_config(
page_title="Exercício Projetos",
page_icon="📊", 
)

st.header("Análise dos 5 projetos")
st.write("Os dados se referem aos valores futuros previstos para receita mensal de 5 projetos diferentes. A análise dos dados permitirá a decisão sobre o investitmento em um ou mais alternativas de projetos. Neste cenário, os dados futuros se referem ao período de 2022 e 2023, logo, a data referência da análise é de dezembro/2021") 

# Arquivo utilizado
arquivo = "https://raw.githubusercontent.com/PaolaRamina/Lista-de-Exercicios-4/main/projetos-1.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df)


# 1
#arquivo = "projetos.csv" 
#df = pd.read_csv(arquivo, sep=';') 
#df.head(23)

# 2
st.write("Foi adicionado uma linha ao final com os dados referentes ao mês de dezembro de 2023")         
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.write(df.tail())


# 3
st.subheader("Apresentação da soma dos valores de cada projeto agrupado por ano")
colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.write(df.groupby('ano')[colunas].sum())


# 4
st.write("Gráfico de dispersão cruzando os dados do Projeto1 e Projeto2")
fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

# 5
st.write("Gráfico do tipo histograma com os dados do Projeto 1 e Projeto4")
fig, ax = plt.subplots()
df["Projeto1"].plot(kind = 'hist')
df["Projeto4"].plot(kind = 'hist')
st.pyplot(fig)









