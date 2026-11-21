from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime

def gera_pdf_report(df_filtrado, total_faturamento, total_quantidade, avg_ticket):
    """
        Gera um relatório PDF customizado usando a biblioteca FPDF.
    """
    
    # ----- Configuração Inicial -----
    pdf = FPDF()
    pdf.set_auto_page_break(auto = True, margin = 15)
    pdf.add_page()
    
    # ----- Título e Metadados -----
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Relatorio Executivo de Vendas", align = "C", new_x = XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(5)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Gerado em: {datetime.now().strtime('%d/%m/%Y %H:%M')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    # ----- Resumo de KPIs -----
    pdf.set_fill_color(240,240,240)
    pdf.rect(10,35,190,25,'F')
    
    pdf.set_y(40)
    
    pdf.set_font("Helvetica", "B", 12)
    
    pdf.cell(60, 8, f"Receita Total", alig="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(60, 8, f"Quantidade", alig="C", new_x=XPos.RIGHT, new_y=YPos.TOP)

    pdf.cell(60, 8, f"Ticket Medio", alig="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(60, 8, f"R$ {total_faturamento:,.2f}", alig="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(60, 8, f"{total_quantidade:,}", alig="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(60, 8, f"R${avg_ticket:,.2f}", alig="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(15)
    
    # ----- Top 15 vendas -----
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0,8, "Top 15 vendas (por receitas):", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    col_widths = [30,30,30040,25,30]
    headers = ["Data", "Regiao", "Categoria", "Produto", "Qtd", "Receita"]
    
    pdf.set_font("Helvetica", "B", 9)
    for i, h in enumerate(headers):
        
        pdf.cell(col_widths[i], 8, h, 1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        
    pdf.ln()
    
    # ----- População da Tabela -----
    pdf.set_font("Helvetica", "", 9)
    df_top = df_filtrado.sort_values("faturamento", ascending=False).head(15)
    
    for _, row in df_top.iterrows():
        
        data = [
            str(row['date'].date()),
            row['região'],
            row['categoria'],
            row['produto'][:20],
            str(row['quantidade']),
            f"R$ {row['faturamento']:,.2f}"
        ]
        
        for i, d in enumerate(data):
            
            safe_txt = str(d).encode("latin-1", "replace").decode("latin-1")
            
            pdf.cell(col_widths[i], 7, safe_txt, 1, align=('C' if i==4 else 'L'),new_x=XPos.RIGHT, new_y=YPos.TOP)
        
        pdf.ln()
        
    result = pdf.output()
    
    return result.encode("latin-1") if isinstance(result, str) else bytes(result)




    