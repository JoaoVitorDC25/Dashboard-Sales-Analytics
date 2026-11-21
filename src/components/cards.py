import numpy as np
import streamlit as st

def render_cards_kpis(df):
    
    
    # ----- Calculos -----'
    total_faturamento = df["faturamento"].sum()
    total_qty = df["quantidade"].sum()
    
    avg_ticket = total_faturamento / total_qty if total_qty > 0 else 0
    
    delta_rev = np.random.uniform(-5,15)
    
    # ----- Layout -----
    c1, c2, c3, c4 = st.columns(4) #Quatro colunas com container
    
    # ----- Render Cards ----
    with c1:
        st.markdown(f"""
        <div class = "metric-card">
            <h3>Receita Total</h3>
            <h2>R$ {total_faturamento: ,.0f}</h2>
            <div class = "delta" style = "color: {'#4CAF50' if delta_rev > 0 else '#FF5252'}">
                {delta_rev:+.1f}% vs meta
            </div>  
        </div>            
        """, unsafe_allow_html=True
        )
    with c2:
            st.markdown(f"""
            <div class = "metric-card">
                <h3>Vendas (QTD)</h3>
                <h2>{total_qty: ,.0f}</h2>
                <div class = "delta">Unidades Vendidas
                </div>  
            </div>            
            """, unsafe_allow_html=True
            )
            
    with c3:
            st.markdown(f"""
            <div class = "metric-card">
                <h3>Ticket Médio</h3>
                <h2>R$ {avg_ticket: ,.2f}</h2>
                <div class = "delta">Por transações
                </div>  
            </div>            
            """, unsafe_allow_html=True
            )
    with c4:
            transactions = df.shape[0]
            st.markdown(f"""
            <div class = "metric-card">
                <h3>Transações</h3>
                <h2>{transactions}</h2>
                <div class = "delta"> Volume total
                </div>  
            </div>            
            """, unsafe_allow_html=True
            )
    
    return total_faturamento, total_qty, avg_ticket