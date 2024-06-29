import streamlit as st
from app.database import insert_luta,get_atletas_nomes,get_id_atleta_by_nome_sobrenome

direcao_nomes = ['Frente', 'Tras']
postura_nomes = ['Ai-Yotsu', 'Kenka-Yotsu']

def register_combat():
    st.title("Cadastro de Lutas")
     # Busca os nomes dos atletas para o selectbox
    nomes_atletas = get_atletas_nomes()

    # Selectbox para escolher o nome do atleta
    nome_atleta = st.selectbox('Selecione o Atleta', nomes_atletas,index=None, placeholder='Selecione o Atleta')
    evento = st.text_input('Insira o nome do evento')
    data = st.date_input('Data do evento',format="YYYY/MM/DD")

    adversario = st.text_input('Insira o Nome do adversario:')
    minuto_luta = st.time_input('Insira o Minuto da luta:')
    dir_golpe = st.radio('Direcao do golpe', direcao_nomes)

    postura = st.radio('Postura',postura_nomes)
    id_atleta = get_id_atleta_by_nome_sobrenome(nome_atleta)
    st.warning(id_atleta)
    st.warning(nome_atleta)

    if st.button('Cadastrar Atleta'):
        insert_luta(id_atleta, evento, data, adversario, minuto_luta, dir_golpe, postura)