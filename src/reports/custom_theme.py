import streamlit as st

def set_custom_theme():
    """
        Define e injeta CSS customizado no app Streamlit.
    """
    
    
    # ----- Definição das Cores -----
    card_bg_color = "#262730"
    text_color = "#FAFAFA"
    gold_color = "#E1C16E"
    dark_text = "#1E1E1E"
    
    # ----- Bloco CSS -----
    css = f"""
    <style>

        /* --- Aumentar Altura Mínima dos Filtros Multiselect --- */
        /* [data-testid="stMultiSelect"]... : É um seletor CSS complexo que "mira" 
           exatamente na caixa interna do widget multiselect da sidebar. */
        [data-testid="stMultiSelect"] div[data-baseweb="select"] > div:first-child {{
            min-height: 100px !important;  /* Define uma altura mínima de 100px */
            overflow-y: auto !important;   /* Adiciona scroll vertical se os itens estourarem */
        }}
    
        /* --- Estilização dos Cards de KPI --- */
        /* Define a aparência da classe 'metric-card' (usada no Bloco 6) */
        .metric-card {{
            background-color: {card_bg_color};
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #444;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.3); /* Sombra sutil */
            text-align: center;
            margin-bottom: 10px; /* Espaçamento inferior */
        }}

        /* Estilo do subtítulo do card (ex: "Receita Total") */
        .metric-card h3 {{
            margin: 0;
            font-size: 1.2rem;
            color: #AAA; /* Cinza claro */
            font-weight: normal;
        }}

        /* Estilo do valor principal do card (ex: "R$ 1.500.000") */
        .metric-card h2 {{
            margin: 10px 0 0 0;
            font-size: 2rem;
            color: {text_color};
            font-weight: bold;
        }}

        /* Estilo do texto 'delta' (ex: "+5.0% vs meta") */
        .metric-card .delta {{
            font-size: 0.9rem;
            color: #4CAF50; /* Verde (padrão) */
            margin-top: 5px;
        }}
                
        /* --- Estilização dos Itens de Filtro Selecionados (Bege-Ouro) --- */
        /* [data-baseweb="tag"]: Mira nas "pílulas" dos itens selecionados
           dentro da caixa do multiselect. */
        [data-baseweb="tag"] {{
            background-color: {gold_color} !important;
            color: {dark_text} !important;
            border-radius: 4px !important;
        }}
        
        /* Mira no ícone 'X' dentro da pílula bege-ouro */
        [data-baseweb="tag"] svg {{
            color: {dark_text} !important;
        }}
        
        /* Muda a cor do 'X' para vermelho ao passar o mouse, indicando "excluir" */
        [data-baseweb="tag"] svg:hover {{
            color: #FF0000 !important; 
        }}
        
    </style>
    """
    
    # ----- Injeção do CSS -----
    st.markdown(css, unsafe_allow_html = True)
    
    
    