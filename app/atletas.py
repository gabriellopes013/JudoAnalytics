import streamlit as st

from app.database import insert_atleta, check_atleta_exists

def register_athletes():
    st.title('Cadastro de Atletas')

    nome = st.text_input('Nome Completo:')
    genero = st.selectbox('Gênero:', ['Masculino', 'Feminino'])
    ctg_idade = st.selectbox("Categoria de Idade:", ["sub-18", "sub-21", "Sênior"])

    if genero == 'Masculino':
        categorias_peso = {
            "sub-18": ["-55", "-60", "-66", "-73", "-81", "-90", "+90"],
            "sub-21": ["-60", "-66", "-73", "-81", "-90", "-100","+100"],
            "Sênior": ["-60", "-66", "-73", "-81", "-90", "-100","+100"]
        }
    elif genero == 'Feminino':
        categorias_peso = {
            "sub-18": ["-44", "-48", "-52", "-57", "-63", "-70", "+70"],
            "sub-21": ["-48", "-52", "-57", "-63", "-70", "-78","+78"],
            "Sênior": ["-48", "-52", "-57", "-63", "-70", "-78","+78"]
        }

    ctg_peso = st.selectbox("Escolha sua categoria de Peso:", categorias_peso[ctg_idade])
    clube = st.text_input('Clube:')

    if st.button('Cadastrar Atleta'):
        if all([genero, nome, ctg_idade, clube, ctg_peso]):
            if check_atleta_exists(nome, ctg_idade, ctg_peso, clube):
                st.warning(f"Atleta '{nome}' já existe no banco de dados.")
            else:
                insert_atleta(genero, nome, ctg_idade, ctg_peso, clube)
                st.success('Atleta cadastrado com sucesso!')
        else:
            st.error('Por favor, preencha todos os campos obrigatórios.')
    else:
        st.error('Por favor, preencha todos os campos obrigatórios.')