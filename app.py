import streamlit as st
from app.atletas import register_athletes
# from register_fights import register_fights

st.sidebar.title('Navegação')
page = st.sidebar.radio('Ir para', ['Registrar Atletas', 'Registrar Lutas'])

if page == 'Registrar Atletas':
    register_athletes()
# elif page == 'Registrar Lutas':
#     register_fights()
