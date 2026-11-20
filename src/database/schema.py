import sqlite3
import numpy as np
import pandas as pd

import plotly.express as px
import streamlit as st

from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime, date, timedelta

def init_db(conn):
    """
    Inicializa o banco de dados
    1. Cria a tabela 'tb_vendas' se ela não existir
    2. Verifica se a tabela está vazia
    3. Se estiver vazia, popula com 180 dias de dados fictícios
    """
    
    cursor = conn.cursor()
    
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS tb_vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                regiao TEXT,
                categoria TEXT,
                produto TEXT,
                faturamento REAL,
                quantidade INTEGER
            )   
        """)
    
    populate_db(conn, cursor)
    
    conn.commit()
    
def populate_db(conn, cursor):
    """
    Popula a tabela 'tb_vendas' com dados fictícios
    """
    
    cursor.execute("SELECT COUNT(*) FROM tb_vendas")
    count = cursor.fetchone()[0]
    
    if count == 0:
        
        np.random.seed(42)
        
        # Gera 180 dias de dados fictícios
        start_date = date(2026, 1, 1)
        datas = [start_date + timedelta(days=i) for i in range(180)]
        
        regioes = ['Norte', 'Sul', 'Leste', 'Oeste']
        categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Serviços']
        
        dict_produtos = {
            'Eletrônicos': {'Smartphone':1200, 'Notebook':3500, 'Tablet':800},
            'Roupas': {'Camiseta':50, 'Terno':150, 'Casaco':300},
            'Alimentos': {'Congelados':40, 'Bebidas':15, 'Limpeza':15},
            'Serviços': {'Consultoria':1000, 'Instalação':400, 'Suporte':200}
        }
        
        rows = []
        
        for d in datas:
            
            vendas_diarias = np.random.randint(5, 15)
            
            for _ in range(vendas_diarias):
                
                r = np.random.choice(regioes)
                c = np.random.choice(categorias)
                
                p = np.random.choice(list(dict_produtos[c].keys()))
                
                preco_base = dict_produtos[c][p]
                quantidade = np.random.randint(1, 25)
                base_faturamento = preco_base * quantidade
                noise = np.random.uniform(-0.20, 0.20)
                faturamento = base_faturamento * (1 + noise)
                
                faturamento = max(0, faturamento)
                
                rows.append((d.isoformat(), r, c, p, round(faturamento, 2), quantidade))
                
        cursor.executemany("""
            INSERT INTO tb_vendas (date, regiao, categoria, produto, faturamento, quantidade) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, rows)
            
        conn.commit()
    