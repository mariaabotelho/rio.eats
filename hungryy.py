import streamlit as st
import pandas as pd
import folium  # Mapa
from folium.plugins import MarkerCluster  # Marcadores
from streamlit_folium import st_folium
import time

# URL direta para a imagem do Cristo no GitHub
image_url = "https://raw.githubusercontent.com/mariaabotelho/rio.eats/main/cristinho%202.jpg"
profile_image_url = "https://raw.githubusercontent.com/mariaabotelho/rio.eats/main/matheuss.jpg"

# Função para exibir o perfil fake
def mostrar_perfil():
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <h1 style="margin-right: 10px;">Teteu Pestana</h1>
            <img src="{profile_image_url}" width="100">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("""
        Professor de Ciência de Dados durante o dia, explorador de butecos durante a noite. Entre algoritmos e cervejas geladas, eu desvendo os mistérios dos dados e dos petiscos de boteco. Se você quer discutir sobre machine learning ou descobrir o melhor pastel de feira, sou a pessoa certa! No meu tempo livre, estou sempre em busca do próximo buteco perfeito, onde a comida é boa, a cerveja é gelada e a conversa é animada. Vamos juntos nessa jornada gastronômica?
    """)

    # Tabs para separar as seções
    tab1, tab2 = st.tabs(["Fotos de Pratos", "Top 5 Restaurantes"])
    
    with tab1:
        st.subheader("Fotos de Pratos")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("paris 6.jpg", use_column_width=True)
        with col2:
            st.image("iraja.jpg", use_column_width=True)
        with col3:
            st.image("mocelin.jpg", use_column_width=True)
        col4, col5 = st.columns(2)
        with col4:
            st.image("gurume.jpg", use_column_width=True)
        with col5:
            st.image("casa tua cocina.jpg", use_column_width=True)
    
    with tab2:
        st.subheader("Top 5 Restaurantes")
        st.write("1. Irajá Redux")
        st.write("2. Gurumê")
        st.write("3. Mocellin Steakhouse")
        st.write("4. Casa Tua Cocina")
        st.write("5. Paris 6")

# Barra lateral
with st.sidebar:
    st.header('Rio Eats')
    st.write('O site que vai ajudar a achar o restaurante mais pertinho de você')
    st.caption('Criado por Luaninha, Julinha e Mary')
    st.image('rio eats.jpg')
    
    # Link para a seção de perfil
    pagina = st.selectbox("Navegação", ["Mapa", "Perfil"])

if pagina == "Perfil":
    mostrar_perfil()
else:
    # Título com a imagem ao lado
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <h1 style="margin-right: 10px;">RIO EATS</h1>
            <img src="{image_url}" width="90">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write('O Rio Eats chegou para deixar mais fácil a sua escolha de restaurante na cidade maravilhosa!')

    # Carregar dados diretamente do CSV limpo com estrelas
    data = pd.read_csv('restaurantes_final_limpo_com_estrelas.csv')

    # Criar um filtro para o tipo de culinária
    opcoes_culinaria = data['CULINARIA'].unique()
    culinaria_selecionada = st.multiselect('Selecione Tipos de Culinária', opcoes_culinaria, default=opcoes_culinaria[:3])

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

    # Exibe info dos restaurantes
    for idx, row in dados_filtrados.iterrows():
        with st.expander(row['NOME']):
            st.markdown(f"**Endereço**: {row['ENDERECO']}")
            st.markdown(f"**Estrelas**: {'⭐' * row['estrelas']}")

# Exibir notificações temporárias
def exibir_notificacoes():
    placeholder = st.empty()

    with placeholder.container():
        st.info("Eurico Comilão te adicionou como amigo")
        time.sleep(3)
        placeholder.empty()

    with placeholder.container():
        st.success("Jojo curtiu sua publicação")
        time.sleep(3)
        placeholder.empty()

# Chama a função para exibir notificações
exibir_notificacoes()
