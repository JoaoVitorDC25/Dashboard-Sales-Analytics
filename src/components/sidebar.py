import streamlit as st

def filtros_sidebar(df):
    """
        Cria todos os widgets da sidebar
    """ 
    
    # ----- Banner Sidebar -----
    st.sidebar.markdown(
        """
            <div style= "background-color: #00CC96; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 15px;">
                <h3 style= "color: white; margin: 0; font-weight: bold;">Filtros</h3>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.header("Selecione os filtros desejados:")
    
    # ----- Filtro de Data -----
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    
    date_range = st.sidebar.date_input(
        "Selecione o intervalo de datas:",
        (min_date, max_date),
        min_value = min_date,
        max_value= max_date
    )
    
    # ----- Filtro Multiselect -----
    all_regioes = sorted(df["regiao"].unique())
    selected_regioes = st.sidebar.multiselect("Regiões", all_regioes, default = all_regioes)
    
    all_categorias = sorted(df["categoria"].unique())
    selected_categorias = st.sidebar.multiselect("Categorias", all_categorias, default = all_categorias)
    
    all_produtos = sorted(df["produto"].unique())
    selected_produtos = st.sidebar.multiselect("Produtos", all_produtos, default = all_produtos)
    
    # ----- Aplicação dos Filtros -----
    if len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = min_date, max_date
        
    df_filtrado = df[
        
        (df["date"].dt.date >= start_date) &
        (df["date"].dt.date <= end_date) &
        
        (df["regiao"].isin(selected_regioes)) &
        (df["categoria"].isin(selected_categorias)) &
        (df["produto"].isin(selected_produtos))
        
    ].copy() #Cria um novo Dataframe
    
    # ----- Footer -----
    st.sidebar.markdown("---")
    
    with st.sidebar.expander("Suporte / Fale conosco", expanded = False):
        st.write("Se tiver dúvidas, envie mensagem")
    
    st.sidebar.caption("Dashboard Desenvidas no Mini-Projetodo Curso de Python")
    
    return df_filtrado