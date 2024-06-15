import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt

# Exercício IPEADATA
st.set_page_config(
page_title="Exercício IPEADATA",
page_icon="📆", 
)

ip.list_series('Selic')

#####
st.subheader("Resultados para o indicador Taxa de juros - Over / Selic - acumulada no mês na base da IPEADATA")
selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic

####
st.subheader("Apenas nos anos de 2022 e 2023:")
fig, ax = plt.subplots()
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))")
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))",ax=ax)
st.pyplot(fig)
