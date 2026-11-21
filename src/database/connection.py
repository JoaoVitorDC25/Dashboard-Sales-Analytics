import sqlite3

def connect_db(db_path = "data/dsa_database.db"):
    """
    Conecta ao banco de dados SQLite
    
    Parâmetros:
    db_path (str): Caminho para o arquivo do banco de dados SQLite;
                    Padrao: 'src/database/sales.db'
                    
    """
    conn = sqlite3.connect(db_path, check_same_thread=False)
     
    return conn