import streamlit as st
st.title("rio eats")

import pandas as pd
import folium #mapa
from folium.plugins import MarkerCluster #marcadores
from streamlit_folium import st_folium


try:
    data1 = pd.read_excel('OFICIAL GEO LULU E JULIA.xlsx')
    data2 = pd.read_excel('OFICIAL GEO DUO GOURMET.xlsx')
except FileNotFoundError as e:
    st.error(f"Erro ao carregar os arquivos: {e}")
    st.stop()
except ImportError as e:
    st.error(f"Erro de importação: {e}. Certifique-se de que o pacote 'openpyxl' está instalado.")
    st.stop()

# pra deixar padrão
data1.columns = ['NOME', 'BAIRRO', 'ENDERECO', 'CULINARIA', 'endereco_completo', 'latitude', 'longitude']
data2.columns = ['NOME', 'ENDERECO', 'BAIRRO', 'CULINARIA', 'endereco_completo', 'latitude', 'longitude']

# juntar os dois df
data = pd.concat([data1, data2], ignore_index=True)

# substituir vírgulas por pontos nas colunas de latitude e longitude
data['latitude'] = data['latitude'].astype(str).str.replace(',', '.').astype(float)
data['longitude'] = data['longitude'].astype(str).str.replace(',', '.').astype(float)

# criar um filtro para o tipo de culinária
opcoes_culinaria = data['CULINARIA'].unique()
culinaria_selecionada = st.multiselect('Selecione Tipos de Culinária', opcoes_culinaria, default=opcoes_culinaria)

# filtrar dados com base nos tipos de culinária selecionados
dados_filtrados = data[data['CULINARIA'].isin(culinaria_selecionada)]

# criar mapa
m = folium.Map(location=[dados_filtrados['latitude'].mean(), dados_filtrados['longitude'].mean()], zoom_start=12)
marker_cluster = MarkerCluster().add_to(m)

# adicionar marcadores ao mapa
for idx, row in dados_filtrados.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],
                  popup=f"{row['NOME']} - {row['CULINARIA']}",
                  icon=folium.Icon(color="blue", icon="info-sign")).add_to(marker_cluster)

# exibir mapa
st_folium(m, width=700, height=500)
