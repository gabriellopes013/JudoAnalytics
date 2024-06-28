import streamlit as st
# from app.atletas import register_athletes
# from app.database import df_teste
# from register_fights import register_fights
def main():
    st.sidebar.title('Navegação')
    page = st.sidebar.radio('Ir para', ['Registrar Atletas', 'Registrar Lutas'])
    st.write("Deu certo")

    # if page == 'Registrar Atletas':
    #     register_athletes()
    # # elif page == 'Registrar Lutas':
    # #     register_fights()
    # df_atletas = df_teste()

    # st.table(df_atletas)
if __name__ == '__main__':
    main()
