import streamlit as st
from app.database import insert_luta,get_atletas_nomes

direcao_nomes = ['Frente', 'Tras']
postura_nomes = ['Ai-Yotsu', 'Kenka-Yotsu']

def register_combat():
    st.title("Cadastro de Lutas")
     # Busca os nomes dos atletas para o selectbox
    nomes_atletas = get_atletas_nomes()

    # Selectbox para escolher o nome do atleta
    nome_atleta = st.selectbox('Selecione o Atleta:', nomes_atletas)

    adversario = st.text('Insira o Nome do adversario:')
    minuto_luta = st.time_input('Insira o Minuto da luta')
    dir_golpe = st.radio('Direcao do golpe', direcao_nomes)
    
    postura = st.radio('Postura',postura_nomes)

    if st.button('Cadastrar Atleta'):          
            insert_luta(adversario,minuto_luta,dir_golpe,postura)
            st.success('Atleta cadastrado com sucesso!')