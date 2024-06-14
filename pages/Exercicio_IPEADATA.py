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

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic

####
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))")
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))")
fig, ax = plt.subplots()
ip.plot(ax=ax)
st.pyplot(fig)
