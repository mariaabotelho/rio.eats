import streamlit as st
st.title("Rio Eats")

import pandas as pd
import folium # Mapa
from folium.plugins import MarkerCluster # Marcadores
from streamlit_folium import st_folium

st.write("Iniciando a aplicação...")

# Carregar dados
try:
    st.write("Carregando dados...")
    data1 = pd.read_excel('OFICIAL GEO LULU E JULIA.xlsx')
    data2 = pd.read_excel('OFICIAL GEO DUO GOURMET.xlsx')
    st.write("Dados carregados com sucesso!")
except FileNotFoundError as e:
    st.error(f"Erro ao carregar os arquivos: {e}")
    st.stop()
except ImportError as e:
    st.error(f"Erro de importação: {e}. Certifique-se de que o pacote 'openpyxl' está instalado.")
    st.stop()

# Padronizar nomes das colunas
st.write("Padronizando nomes das colunas...")
data1.columns = ['NOME', 'BAIRRO', 'ENDERECO', 'CULINARIA', 'endereco_completo', 'latitude', 'longitude']
data2.columns = ['NOME', 'ENDERECO', 'BAIRRO', 'CULINARIA', 'endereco_completo', 'latitude', 'longitude']

# Combinar dados
st.write("Combinando dados...")
data = pd.concat([data1, data2], ignore_index=True)

# Substituir vírgulas por pontos nas colunas de latitude e longitude
st.write("Substituindo vírgulas por pontos nas coordenadas...")
data['latitude'] = data['latitude'].astype(str).str.replace(',', '.').astype(float)
data['longitude'] = data['longitude'].astype(str).str.replace(',', '.').astype(float)
st.write("Coordenadas corrigidas!")

# Remover linhas com NaN em latitude e longitude
st.write("Removendo linhas com NaN em latitude e longitude...")
data = data.dropna(subset=['latitude', 'longitude'])
st.write(f"Número de registros após remover NaNs: {len(data)}")

# Criar um filtro para o tipo de culinária
st.write("Criando filtro para tipos de culinária...")
opcoes_culinaria = data['CULINARIA'].unique()
culinaria_selecionada = st.multiselect('Selecione Tipos de Culinária', opcoes_culinaria, default= opcoes_culinaria[:3])

# Filtrar dados com base nos tipos de culinária selecionados
st.write("Filtrando dados com base nos tipos de culinária selecionados...")
dados_filtrados = data[data['CULINARIA'].isin(culinaria_selecionada)]
st.write(f"Número de restaurantes após o filtro: {len(dados_filtrados)}")

# Criar mapa
st.write("Criando o mapa...")
m = folium.Map(location=[dados_filtrados['latitude'].mean(), dados_filtrados['longitude'].mean()], zoom_start=12)
marker_cluster = MarkerCluster().add_to(m)

# Adicionar marcadores ao mapa
st.write("Adicionando marcadores ao mapa...")
for idx, row in dados_filtrados.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],
                  popup=f"{row['NOME']} - {row['CULINARIA']}",
                  icon=folium.Icon(color="blue", icon="info-sign")).add_to(marker_cluster)
st.write("Marcadores adicionados!")

# Exibir mapa
st.write("Exibindo o mapa...")
st_folium(m, width=700, height=500)
st.write("Mapa exibido com sucesso!")
