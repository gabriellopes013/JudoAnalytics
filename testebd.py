import os
import psycopg2
from psycopg2 import OperationalError

DATABASE_URL = 'postgresql://neondb_owner:MDBbntz1xGy2@ep-proud-sea-a5pjm2xm.us-east-2.aws.neon.tech/neondb?sslmode=require'

def create_connection(db_url):
    try:
        conn = psycopg2.connect(db_url, sslmode='require')
        print("Conexão estabelecida com sucesso!")
        return conn
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_table(conn):
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL
    );
    '''
    try:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()
            print("Tabela 'test_table' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")

def insert_data(conn):
    insert_query = '''
    INSERT INTO test_table (name, age)
    VALUES
        ('Alice', 30),
        ('Bob', 25),
        ('Charlie', 35)
    RETURNING id;
    '''
    try:
        with conn.cursor() as cursor:
            cursor.execute(insert_query)
            conn.commit()
            print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def fetch_data(conn):
    fetch_query = '''
    SELECT * FROM test_table;
    '''
    try:
        with conn.cursor() as cursor:
            cursor.execute(fetch_query)
            rows = cursor.fetchall()
            print("Dados recuperados com sucesso!")
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")

def main():
    conn = create_connection(DATABASE_URL)
    if conn:
        create_table(conn)
        insert_data(conn)
        fetch_data(conn)
        conn.close()
        print("Conexão ao banco de dados encerrada.")

if __name__ == '__main__':
    main()