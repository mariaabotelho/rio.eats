import streamlit as st
import pandas as pd
import folium  # cria o mapa
from folium.plugins import MarkerCluster  # restaurantes no mapa
from streamlit_folium import st_folium
from streamlit_custom_notification_box import custom_notification_box  # notificação da propaganda 

def set_style():
    st.markdown(
        """
        <style>
        .stApp {
            background: url('fundo.jpeg') no-repeat center center fixed;
            background-size: cover;
        }
        .css-1d391kg {
            background-color: rgba(255, 255, 255, 0.8);
        }
        h1, h2, h3, h4, h5, p, div, span {
            font-family: 'Times New Roman', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(page_title="Rio Eats", page_icon="🍽️", initial_sidebar_state="expanded")

# Aplicar o estilo definido
set_style()

profile_image_url = "matheuss.jpg"
logo_url = "rio eats.jpg"
app_logo = "logo rio eats.jpg"  # Caminho da sua logo

if 'captured_images' not in st.session_state:  # para armazenar foto tirada pelo usuário
    st.session_state.captured_images = []

def mostrar_perfil():
    container = st.container(border=True)
    col_pic, col_name = container.columns([1, 3])
    col_pic.image(profile_image_url, width=140)
    col_name.header('Teteu Pestana')
    col_name.caption('@Teteu_Pestana')
    col_name.caption('Rio de Janeiro - Brasil')
    container.write("""
        Professor de Ciência de Dados durante o dia, explorador de butecos durante a noite. Entre algoritmos e cervejas geladas, eu desvendo os mistérios dos dados e dos petiscos de boteco. Se você quer discutir sobre machine learning ou descobrir o melhor pastel de feira, sou a pessoa certa! No meu tempo livre, estou sempre em busca do próximo buteco perfeito, onde a comida é boa, a cerveja é gelada e a conversa é animada. Vamos juntos nessa jornada gastronômica?
    """)
    
    tab1, tab2, tab3 = st.tabs(["Fotos de Pratos", "Top 5 Restaurantes", "Interações"])
    
    with tab1:
        st.subheader("Fotos de Pratos")
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.expander("@Teteu_Pestana", expanded=True):
                st.image("paris 6.jpg", use_column_width=True)
                st.markdown('**Paris 6**')
                st.write('Crevettes à Bruno Gagliasso')
                st.caption('👍🏼 151 curtidas')
        with col2:
            with st.expander('@Teteu_Pestana', expanded=True):
                st.image("iraja.jpg", use_column_width=True)
                st.markdown('**Irajá Redux**')
                st.write('Bife de chorizo com creme de espinafre, redux fries e farofa')
                st.caption('👍🏼 392 curtidas')
        with col3:
            with st.expander('@Teteu_Pestana', expanded=True):
                st.image("mocelin.jpg", use_column_width=True)
                st.markdown('**Mocellin Steakhouse**')
                st.write('Shoulder steak com pastelzinho 🙏🏻')
                st.caption('👍🏼 205 curtidas')
        col4, col5 = st.columns(2)
        with col4:
            with st.expander('@Teteu_Pestana', expanded=True):
                st.image("gurume.jpg", use_column_width=True)
                st.markdown('**Gurumê**')
                st.write('Usuzukuri 3 peixes')
                st.caption('👍🏼 509 curtidas')
        with col5:
            with st.expander('@Teteu_Pestana', expanded=True):
                st.image("casa tua cocina.jpg", use_column_width=True)
                st.markdown('**Casa Tua Cocina**')
                st.write('Gnocchi com batata, camarões e vieiras')
                st.caption('👍🏼 442 curtidas')
        
        # widget capturar imagem da webcam
        picture = st.camera_input("Hmm parece estar gostoso.. Tire uma foto da sua comida para registrar!")
        
        # botão pra salvar a imagem capturada
        if picture:
            st.download_button("Salvar imagem", data=picture, file_name="imagem_comida.png", mime="image/png")
        
        if st.session_state.captured_images:
            st.subheader("Imagens Capturadas")
            for img in st.session_state.captured_images:
                st.image(img)
    
    with tab2:
        container = st.container(border=True)
        col_name = container.columns([1, 3])
        container.subheader('Top 5 Restaurantes')
        container.write("""1. Irajá Redux""")
        container.write("""2. Gurumê""")
        container.write("""3. Mocellin Steakhouse""")
        container.write("""4. Casa Tua Cocina""")
        container.write("""5. Paris 6""")
    
    with tab3:
        st.subheader("Interações")
        interacoes = [
            "@Eurico_Comilão te adicionou como amigo",
            "@Doctor_jojo curtiu sua publicação",
            "@Vanessinha salvou sua publicação",
            "@LapaFaminto te adicionou como amigo",
            "@Cat.docinhos acabou de visitar um restaurante perto de você! Confira a avaliação dela :)"
        ]
        for interacao in interacoes:
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; padding: 10px; margin: 5px 0; border-radius: 5px; background-color: #f9f9f9;">
                    {interacao}
                </div>
                """,
                unsafe_allow_html=True
            )

# função da notificação da propaganda
def exibir_notificacao():
    styles = {
        'material-icons': {'color': 'red'},
        'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
        'notification-text': {'': ''},
        'close-button': {'': ''},
        'link': {'': ''}
    }
    custom_notification_box(
        icon='info',
        textDisplay='O Bar do Bigode está a 800 metros de você. Já pensou em conhecer?',
        externalLink='',
        url='#',
        styles=styles,
        key="notificacao_bigode"
    )

with st.sidebar:
    pagina = st.selectbox("Navegação", ["Mapa", "Perfil"])
    st.image(logo_url, use_column_width=True)
    st.header('Rio Eats')
    st.write('O site que conecta amantes da gastronomia de forma moderna e interativa. Encontre restaurantes próximos, registre suas visitas, compartilhe experiências e descubra novos lugares recomendados pela comunidade. Transforme cada refeição em uma aventura gastronômica personalizada.')
    st.caption('Criado por Maria Botelho, Julia Frazão e Luana Pinheiro')

if pagina == "Perfil":
    mostrar_perfil()
else:
    # Substituindo o título por uma imagem na página do mapa
    st.image(app_logo, use_column_width=True)
    exibir_notificacao()

    data = pd.read_csv('restaurantes_final_limpo_com_estrelas.csv')
    # filtro com os tipos de culinária
    opcoes_culinaria = data['CULINARIA'].unique()
    culinaria_selecionada = st.multiselect('Selecione Tipos de Culinária', opcoes_culinaria, default=opcoes_culinaria[:3])
    
    if not culinaria_selecionada:
        st.warning('Você precisa escolher pelo menos uma opção.')
    else:
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
                          
        st_folium(m, width=700, height=500)
        # info dos restaurantes
        st.subheader('Restaurantes encontrados:')
        for idx, row in dados_filtrados.iterrows():
            with st.expander(row['NOME']):
                st.caption(f"**Culinária**: {row['CULINARIA']}")
                st.markdown(f"**Endereço**: {row['ENDERECO']}")
                st.markdown(f"**Estrelas**: {'⭐' * row['estrelas']}")
