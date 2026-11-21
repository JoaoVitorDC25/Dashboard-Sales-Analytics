import pandas as pd
import streamlit as st

from database.connection import connect_db
from database.schema import init_db

@st.cache_data(ttl=600)
def get_data_from_db():
     """
        Função para carregar dados
     """
     
     conn = connect_db()
     
     init_db(conn)  
     
     df = pd.read_sql_query("SELECT * FROM tb_vendas", conn, parse_dates = ["dates"])
     
     conn.close()
     
     return df