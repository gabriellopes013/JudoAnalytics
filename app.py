import streamlit as st
from app.atletas import register_athletes
from app.database import create_table_atletas, create_table_lutas
from app.lutas import register_combat
def main():
    st.sidebar.title('Navegação')
    page = st.sidebar.radio('Ir para', ['Registrar Atletas', 'Registrar Lutas'])


    if page == 'Registrar Atletas':
        register_athletes()
    
    if page == 'Registrar Lutas':
        register_combat()

if __name__ == '__main__':
    create_table_atletas()
    create_table_lutas()
    main()
