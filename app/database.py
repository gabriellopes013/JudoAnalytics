import duckdb

# Conectar ao banco de dados DuckDB
con = duckdb.connect('judo_app.db')

# Função para criar a tabela se não existir
def create_table():
    con.execute("""
        CREATE TABLE IF NOT EXISTS atletas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genero VARCHAR,
            nome VARCHAR,
            sobrenome VARCHAR,
            ctg_idade VARCHAR,
            ctg_peso VARCHAR,
            clube VARCHAR
        )
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS lutas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_atleta INTEGER,
            adversario VARCHAR,
            minuto_luta VARCHAR,
            dir_golpe VARCHAR,
            postura VARCHAR,
            FOREIGN KEY (id_atleta) REFERENCES atletas(id)
        )
    """)
create_table()

# Função para inserir dados
def insert_atleta(genero, nome, sobrenome, ctg_idade, ctg_peso, clube):
    con.execute("""
        INSERT INTO atletas (genero, nome, sobrenome, ctg_idade, ctg_peso, clube) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (genero, nome, sobrenome, ctg_idade, ctg_peso, clube))

def insert_luta(id_atleta, adversario, minuto_luta, dir_golpe, postura):
    con.execute("""
        INSERT INTO lutas (id_atleta, adversario, minuto_luta, dir_golpe, postura) 
        VALUES (?, ?, ?, ?, ?)
    """, (id_atleta, adversario, minuto_luta, dir_golpe, postura))

# Função para obter todos os dados
def get_atletas():
    return con.execute("SELECT * FROM atletas").fetchdf()

def check_existing_atleta(atleta_id):
    result = con.execute("SELECT * FROM atletas WHERE id = ?", (atleta_id,)).fetchall()
    return len(result) > 0

def get_lutas():
    return con.execute("SELECT * FROM lutas").fetchdf()
