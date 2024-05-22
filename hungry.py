import streamlit as st
st.title("rio eats")

import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Carregar dados
data1 = pd.read_excel('/mnt/data/OFICIAL GEO LULU E JULIA.xlsx')
data2 = pd.read_excel('/mnt/data/OFICIAL GEO DUO GOURMET.xlsx')

# Padronizar nomes das colunas
data1.columns = ['NOME', 'BAIRRO', 'ENDERECO', 'CULINARIA', 'endereco_completo', 'latitude', 'longitude']
data2.columns = ['NOME', 'ENDERECO', 'BAIRRO', 'CULINARIA', 'endereco_completo', 'latitude', 'longitude']

# Combinar dados
data = pd.concat([data1, data2], ignore_index=True)

# Criar um filtro para o tipo de culinária
opcoes_culinaria = data['CULINARIA'].unique()
culinaria_selecionada = st.multiselect('Selecione Tipos de Culinária', opcoes_culinaria, default=opcoes_culinaria)

# Filtrar dados com base nos tipos de culinária selecionados
dados_filtrados = data[data['CULINARIA'].isin(culinaria_selecionada)]

# Criar mapa
m = folium.Map(location=[dados_filtrados['latitude'].mean(), dados_filtrados['longitude'].mean()], zoom_start=12)
marker_cluster = MarkerCluster().add_to(m)

# Adicionar marcadores ao mapa
for idx, row in dados_filtrados.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],
                  popup=f"{row['NOME']} - {row['CULINARIA']}",
                  icon=folium.Icon(color="blue", icon="info-sign")).add_to(marker_cluster)

# Exibir mapa
st_folium(m, width=700, height=500)

