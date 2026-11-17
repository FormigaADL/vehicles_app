import pandas as pd
import plotly.express as px
import streamlit as st

venda = pd.read_csv('vehicles_us.csv')

st.title('Venda de Veículos')

build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')

    fig = px.histogram(venda, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão para a coluna odometer')

    fig = px.scatter(venda, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
