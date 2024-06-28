import streamlit as st
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values

# Função para conectar ao banco de dados
url="postgresql://neondb_owner:MDBbntz1xGy2@ep-proud-sea-a5pjm2xm.us-east-2.aws.neon.tech/judo_app?sslmode=require"
@st.cache_resource()
def get_connection():
    conn = psycopg2.connect(url)
    return conn

# Função para criar a tabela atletas
@st.cache_data()
def create_table_atletas():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS atletas (
                id SERIAL PRIMARY KEY,
                genero VARCHAR,
                nome VARCHAR,
                sobrenome VARCHAR,
                ctg_idade VARCHAR,
                ctg_peso VARCHAR,
                clube VARCHAR
            )
        """)
        conn.commit()
        cur.close()
        print('Tabela atletas criado')
    except Exception as e:
        print(f"Erro ao criar a tabela atletas: {e}")

# Função para criar a tabela lutas
@st.cache_data()
def create_table_lutas():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lutas (
                id SERIAL PRIMARY KEY,
                id_atleta INTEGER,
                adversario VARCHAR,
                evento VARCHAR,
                data DATE,
                minuto_luta VARCHAR,
                dir_golpe VARCHAR,
                postura VARCHAR,
                FOREIGN KEY (id_atleta) REFERENCES atletas(id)
            )
        """)
        conn.commit()
        cur.close()
        print('Tabela lutas criado')
    except Exception as e:
        print(f"Erro ao criar a tabela lutas: {e}")

# Função para inserir dados na tabela atletas
def insert_atleta(genero, nome, sobrenome, ctg_idade, ctg_peso, clube):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO atletas (genero, nome, sobrenome, ctg_idade, ctg_peso, clube) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (genero, nome, sobrenome, ctg_idade, ctg_peso, clube))
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Erro ao inserir atleta: {e}")

def insert_luta(id_atleta,adversario,evento ,data,minuto_luta, dir_golpe, postura):
    try:
        id_atleta = get_id_atleta_by_nome_sobrenome(id_atleta)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO lutas (id_atleta,evento,data,dversario, minuto_luta, dir_golpe, postura) 
            VALUES (%s, %s, %s, %s, %s, %s,%s)
        """, (id_atleta,adversario, evento, data,minuto_luta, dir_golpe, postura))
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Erro ao inserir atleta: {e}")

def check_atleta_exists(nome, sobrenome, ctg_idade, ctg_peso, clube):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM atletas 
            WHERE nome = %s AND sobrenome = %s AND ctg_idade = %s AND ctg_peso = %s AND clube = %s
        """, (nome, sobrenome, ctg_idade, ctg_peso, clube))
        atleta = cur.fetchone()
        return atleta is not None
    except Exception as e:
        if conn is not None:
            conn.rollback()
        st.error(f"Erro ao verificar existência do atleta: {e}")
        return False
    
def get_id_atleta_by_nome_sobrenome(nome_completo):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id FROM atletas WHERE CONCAT(nome, ' ', sobrenome) = %s
        """, (nome_completo,))
        id_atleta = cur.fetchone()
        cur.close()
        return id_atleta[0] if id_atleta else None
    except Exception as e:
        print(f"Erro ao buscar ID do atleta: {e}")
        return None
    
def get_atletas_nomes():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT CONCAT(nome, ' ', sobrenome) FROM atletas
        """)
        nomes_atletas = cur.fetchall()
        cur.close()
        return [nome[0] for nome in nomes_atletas]
    except Exception as e:
        print(f"Erro ao buscar nomes dos atletas: {e}")
        return []