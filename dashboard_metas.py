"""
Dashboard Interativo – Acompanhamento de Metas de Vendas
Especialistas: Letícia, Claudete, Daniela, Jessica, Mandely
Execute com: streamlit run dashboard_metas.py
Dependências: pip install streamlit plotly pandas
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json

# ─────────────────────────────────────────────
# 0. CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard – Metas & Vendas",
    page_icon="📊",
    layout="wide",
)

# ─────────────────────────────────────────────
# 1. DADOS (JSON embutido)
# ─────────────────────────────────────────────
RAW_DATA = [
    # ── LETÍCIA ──────────────────────────────
    {"especialista": "Letícia",  "marca_ciclo": "OUI Ciclo BOT 6 EUDORA",
     "tipo_meta": "Financeiro",  "descricao": "Financeiro OUI ABRIL/26",
     "meta_valor": 156428.12,    "realizado_valor": 45394.53,
     "peso": 500, "porcentagem_alcancada": 29.0,
     "restante": 111033.53, "meta_dia_18_04": 12337.06, "meta_dia_salao": 6168.53},

    {"especialista": "Letícia",  "marca_ciclo": "OUI Ciclo BOT 6 EUDORA",
     "tipo_meta": "META VD",     "descricao": "META VD ABRIL/26",
     "meta_valor": 7006714.95,   "realizado_valor": 3658902.57,
     "peso": 300, "porcentagem_alcancada": 52.2,
     "restante": 3347812.38, "meta_dia_18_04": 371979.15, "meta_dia_salao": None},

    {"especialista": "Letícia",  "marca_ciclo": "OUI Ciclo BOT 6 EUDORA",
     "tipo_meta": "Penetração",  "descricao": "Penetração MULTIMARCAS CICLO 6",
     "meta_valor": 73.0, "realizado_valor": 68.0,
     "peso": 200, "porcentagem_alcancada": None,
     "restante": None, "meta_dia_18_04": None, "meta_dia_salao": None},

    # ── CLAUDETE ─────────────────────────────
    {"especialista": "Claudete", "marca_ciclo": "QDB EAM Ciclo 5",
     "tipo_meta": "Financeiro",  "descricao": "Financeiro QDB ABRIL/26",
     "meta_valor": 46416.16,     "realizado_valor": 54300.79,
     "peso": 500, "porcentagem_alcancada": 117.0,
     "restante": -7864.63, "meta_dia_18_04": -876.07, "meta_dia_salao": -438.04},

    {"especialista": "Claudete", "marca_ciclo": "QDB EAM Ciclo 5",
     "tipo_meta": "META VD",     "descricao": "META VD ABRIL/26",
     "meta_valor": 7006714.95,   "realizado_valor": 3658902.57,
     "peso": 300, "porcentagem_alcancada": 52.2,
     "restante": 3347812.38, "meta_dia_18_04": 371979.15, "meta_dia_salao": None},

    {"especialista": "Claudete", "marca_ciclo": "QDB EAM Ciclo 5",
     "tipo_meta": "Penetração",  "descricao": "Penetração EAM CICLO 6",
     "meta_valor": 38.0, "realizado_valor": 34.0,
     "peso": 200, "porcentagem_alcancada": None,
     "restante": None, "meta_dia_18_04": None, "meta_dia_salao": None},

    # ── DANIELA ──────────────────────────────
    {"especialista": "Daniela",  "marca_ciclo": "QDB Ciclo 5",
     "tipo_meta": "Financeiro",  "descricao": "Financeiro QDB ABRIL/26",
     "meta_valor": 5281912.67,   "realizado_valor": 2570588.01,
     "peso": 500, "porcentagem_alcancada": 48.7,
     "restante": 2711324.66, "meta_dia_18_04": 301258.30, "meta_dia_salao": 150629.15},

    {"especialista": "Daniela",  "marca_ciclo": "QDB Ciclo 5",
     "tipo_meta": "META VD",     "descricao": "META VD ABRIL/26",
     "meta_valor": 7006714.95,   "realizado_valor": 3658902.57,
     "peso": 300, "porcentagem_alcancada": 52.2,
     "restante": 3347812.38, "meta_dia_18_04": 371979.15, "meta_dia_salao": None},

    {"especialista": "Daniela",  "marca_ciclo": "QDB Ciclo 5",
     "tipo_meta": "Penetração",  "descricao": "Penetração CICLO 6 SKIN",
     "meta_valor": 10.0, "realizado_valor": 6.0,
     "peso": 200, "porcentagem_alcancada": None,
     "restante": None, "meta_dia_18_04": None, "meta_dia_salao": None},

    # ── JESSICA ──────────────────────────────
    {"especialista": "Jessica",  "marca_ciclo": "EUDORA Ciclo 5",
     "tipo_meta": "Financeiro",  "descricao": "Financeiro ABRIL/26",
     "meta_valor": 1521957.99,   "realizado_valor": 988619.18,
     "peso": 500, "porcentagem_alcancada": 65.0,
     "restante": 533338.81, "meta_dia_18_04": 59259.87, "meta_dia_salao": 29629.93},

    {"especialista": "Jessica",  "marca_ciclo": "EUDORA Ciclo 5",
     "tipo_meta": "META VD",     "descricao": "META VD ABRIL/26",
     "meta_valor": 7006714.95,   "realizado_valor": 3658902.57,
     "peso": 300, "porcentagem_alcancada": 52.2,
     "restante": 3347812.38, "meta_dia_18_04": 371979.15, "meta_dia_salao": None},

    {"especialista": "Jessica",  "marca_ciclo": "EUDORA Ciclo 5",
     "tipo_meta": "Penetração",  "descricao": "Penetração CABELOS CICLO 6",
     "meta_valor": 37.0, "realizado_valor": 30.0,
     "peso": 200, "porcentagem_alcancada": None,
     "restante": None, "meta_dia_18_04": None, "meta_dia_salao": None},

    {"especialista": "Jessica",  "marca_ciclo": "EUDORA Ciclo 5",
     "tipo_meta": "Penetração",  "descricao": "Penetração MULTIMARCAS CICLO 6",
     "meta_valor": 73.0, "realizado_valor": 68.0,
     "peso": 200, "porcentagem_alcancada": None,
     "restante": None, "meta_dia_18_04": None, "meta_dia_salao": None},

    # ── MANDELY ──────────────────────────────
    {"especialista": "Mandely",  "marca_ciclo": "MARCA BOTICÁRIO Ciclo 5",
     "tipo_meta": "Financeiro",  "descricao": "Financeiro perfumaria ABRIL/26",
     "meta_valor": 5281912.67,   "realizado_valor": 2570588.01,
     "peso": 500, "porcentagem_alcancada": 48.7,
     "restante": 2711324.66, "meta_dia_18_04": 301258.30, "meta_dia_salao": 150629.15},

    {"especialista": "Mandely",  "marca_ciclo": "MARCA BOTICÁRIO Ciclo 5",
     "tipo_meta": "META VD",     "descricao": "META VD ABRIL/26",
     "meta_valor": 7006714.95,   "realizado_valor": 3658902.57,
     "peso": 300, "porcentagem_alcancada": 52.2,
     "restante": 3347812.38, "meta_dia_18_04": 301258.30, "meta_dia_salao": None},

    {"especialista": "Mandely",  "marca_ciclo": "MARCA BOTICÁRIO Ciclo 5",
     "tipo_meta": "Penetração",  "descricao": "Penetração CICLO 6",
     "meta_valor": 73.0, "realizado_valor": 68.0,
     "peso": 200, "porcentagem_alcancada": None,
     "restante": None, "meta_dia_18_04": None, "meta_dia_salao": None},
]

# ─────────────────────────────────────────────
# 2. CARREGAMENTO E PRÉ-PROCESSAMENTO
# ─────────────────────────────────────────────
df = pd.DataFrame(RAW_DATA)

# Cores por especialista (identidade visual)
CORES = {
    "Letícia":  "#4e79a7",
    "Claudete": "#f28e2b",
    "Daniela":  "#e15759",
    "Jessica":  "#76b7b2",
    "Mandely":  "#59a14f",
}

# ─────────────────────────────────────────────
# 3. SIDEBAR – FILTROS
# ─────────────────────────────────────────────
st.sidebar.image("https://img.icons8.com/color/96/bar-chart.png", width=70)
st.sidebar.title("🔍 Filtros")
st.sidebar.markdown("---")

especialistas = sorted(df["especialista"].unique().tolist())
especialista_sel = st.sidebar.selectbox(
    "👤 Selecione a Especialista",
    options=["Todas"] + especialistas,
)

tipos_disponiveis = sorted(df["tipo_meta"].unique().tolist())
tipos_sel = st.sidebar.multiselect(
    "📋 Tipos de Meta",
    options=tipos_disponiveis,
    default=tipos_disponiveis,
)

st.sidebar.markdown("---")
st.sidebar.caption("📅 Referência: ABRIL/26  |  Ciclo atual")

# ─────────────────────────────────────────────
# 4. FILTROS APLICADOS AO DATAFRAME
# ─────────────────────────────────────────────
if especialista_sel == "Todas":
    df_filtrado = df[df["tipo_meta"].isin(tipos_sel)].copy()
else:
    df_filtrado = df[
        (df["especialista"] == especialista_sel) &
        (df["tipo_meta"].isin(tipos_sel))
    ].copy()

# Apenas registros financeiros/META VD para KPIs (têm valores monetários)
df_financeiro = df_filtrado[df_filtrado["tipo_meta"].isin(["Financeiro", "META VD"])]

# ─────────────────────────────────────────────
# 5. CABEÇALHO PRINCIPAL
# ─────────────────────────────────────────────
col_titulo, col_badge = st.columns([4, 1])
with col_titulo:
    nome_exib = especialista_sel if especialista_sel != "Todas" else "Todas as Especialistas"
    st.title(f"📊 Dashboard de Metas — {nome_exib}")
    st.caption("Acompanhamento de desempenho comercial | Ciclo Abril/2026")
with col_badge:
    st.markdown("<br>", unsafe_allow_html=True)
    # Badge de marca/ciclo se uma especialista selecionada
    if especialista_sel != "Todas":
        marca = df[df["especialista"] == especialista_sel]["marca_ciclo"].iloc[0]
        st.info(f"🏷️ {marca}")

st.markdown("---")

# ─────────────────────────────────────────────
# 6. KPI CARDS
# ─────────────────────────────────────────────
st.subheader("📌 Indicadores Principais")

# Calcula KPIs apenas para Financeiro (evita distorção da META VD geral compartilhada)
df_fin_only = df_filtrado[df_filtrado["tipo_meta"] == "Financeiro"]
df_metavd_only = df_filtrado[df_filtrado["tipo_meta"] == "META VD"]

total_meta_fin       = df_fin_only["meta_valor"].sum()
total_real_fin       = df_fin_only["realizado_valor"].sum()
pct_media            = df_fin_only["porcentagem_alcancada"].mean() if not df_fin_only.empty else 0
total_restante_fin   = df_fin_only["restante"].sum()

# Penetração média
df_pen = df_filtrado[df_filtrado["tipo_meta"] == "Penetração"]
pen_media_meta  = df_pen["meta_valor"].mean() if not df_pen.empty else 0
pen_media_real  = df_pen["realizado_valor"].mean() if not df_pen.empty else 0

k1, k2, k3, k4, k5 = st.columns(5)

def fmt_br(valor):
    """Formata número no padrão brasileiro."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

with k1:
    st.metric(
        label="💰 Meta Financeiro",
        value=fmt_br(total_meta_fin),
    )
with k2:
    delta_real = total_real_fin - total_meta_fin
    st.metric(
        label="✅ Realizado",
        value=fmt_br(total_real_fin),
        delta=fmt_br(delta_real) if delta_real != 0 else None,
        delta_color="normal",
    )
with k3:
    cor_pct = "🟢" if pct_media >= 100 else ("🟡" if pct_media >= 60 else "🔴")
    st.metric(
        label=f"{cor_pct} % Médio Atingido",
        value=f"{pct_media:.1f}%",
    )
with k4:
    st.metric(
        label="⏳ Restante (9 dias)",
        value=fmt_br(total_restante_fin),
    )
with k5:
    pct_pen = (pen_media_real / pen_media_meta * 100) if pen_media_meta > 0 else 0
    st.metric(
        label="🎯 Penetração Média",
        value=f"{pen_media_real:.0f}% / {pen_media_meta:.0f}%",
        delta=f"{pct_pen:.1f}% atingido",
        delta_color="normal" if pct_pen >= 80 else "inverse",
    )

st.markdown("---")

# ─────────────────────────────────────────────
# 7. GRÁFICO DE BARRAS – META vs REALIZADO
# ─────────────────────────────────────────────
st.subheader("📊 Meta vs. Realizado — Financeiro & META VD")

df_bar = df_filtrado[df_filtrado["tipo_meta"].isin(["Financeiro", "META VD"])].copy()

if not df_bar.empty:
    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        name="Meta",
        x=df_bar["descricao"],
        y=df_bar["meta_valor"],
        marker_color="#636efa",
        text=[fmt_br(v) for v in df_bar["meta_valor"]],
        textposition="outside",
        textfont=dict(size=10),
        opacity=0.85,
    ))

    fig_bar.add_trace(go.Bar(
        name="Realizado",
        x=df_bar["descricao"],
        y=df_bar["realizado_valor"],
        marker_color="#00cc96",
        text=[fmt_br(v) for v in df_bar["realizado_valor"]],
        textposition="outside",
        textfont=dict(size=10),
        opacity=0.85,
    ))

    fig_bar.update_layout(
        barmode="group",
        xaxis_tickangle=-30,
        height=430,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(gridcolor="#e0e0e0"),
        margin=dict(t=40, b=80),
    )
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.info("Nenhum dado disponível para os filtros selecionados.")

st.markdown("---")

# ─────────────────────────────────────────────
# 8. GAUGES – % DE ATINGIMENTO (FINANCEIRO)
# ─────────────────────────────────────────────
st.subheader("🔵 Velocímetros — Atingimento do Financeiro por Especialista")

# Usa apenas dados de Financeiro (1 registro por especialista)
df_gauge = df[df["tipo_meta"] == "Financeiro"].copy()

if especialista_sel != "Todas":
    df_gauge = df_gauge[df_gauge["especialista"] == especialista_sel]

n = len(df_gauge)
if n > 0:
    cols_gauge = st.columns(min(n, 5))
    for idx, row in enumerate(df_gauge.itertuples()):
        pct = row.porcentagem_alcancada or 0
        cor_agulha = CORES.get(row.especialista, "#636efa")

        # Define cor do arco baseado no %
        if pct >= 100:
            bar_color = "#00cc96"   # verde
        elif pct >= 70:
            bar_color = "#ffd166"   # amarelo
        else:
            bar_color = "#ef476f"   # vermelho

        fig_g = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=pct,
            number={"suffix": "%", "font": {"size": 28, "color": cor_agulha}},
            delta={"reference": 100, "increasing": {"color": "#00cc96"},
                   "decreasing": {"color": "#ef476f"}},
            title={"text": f"<b>{row.especialista}</b><br><sub>{row.marca_ciclo}</sub>",
                   "font": {"size": 13}},
            gauge={
                "axis": {"range": [0, 130], "tickwidth": 1, "tickcolor": "darkgray",
                         "tickvals": [0, 25, 50, 75, 100, 130]},
                "bar": {"color": bar_color},
                "bgcolor": "white",
                "borderwidth": 2,
                "bordercolor": "gray",
                "steps": [
                    {"range": [0, 50],   "color": "#fff0f0"},
                    {"range": [50, 100], "color": "#fff9e6"},
                    {"range": [100, 130],"color": "#e6fff5"},
                ],
                "threshold": {
                    "line": {"color": "red", "width": 3},
                    "thickness": 0.8,
                    "value": 100,
                },
            },
        ))
        fig_g.update_layout(
            height=260,
            margin=dict(t=60, b=20, l=20, r=20),
            paper_bgcolor="rgba(0,0,0,0)",
        )
        with cols_gauge[idx % 5]:
            st.plotly_chart(fig_g, use_container_width=True)

st.markdown("---")

# ─────────────────────────────────────────────
# 9. GRÁFICO DE PENETRAÇÃO (Barras horizontais)
# ─────────────────────────────────────────────
st.subheader("🎯 Penetração — Meta vs. Realizado (%)")

df_pen_all = df[df["tipo_meta"] == "Penetração"].copy()
if especialista_sel != "Todas":
    df_pen_all = df_pen_all[df_pen_all["especialista"] == especialista_sel]

if not df_pen_all.empty:
    fig_pen = go.Figure()
    fig_pen.add_trace(go.Bar(
        name="Meta %",
        y=df_pen_all["descricao"],
        x=df_pen_all["meta_valor"],
        orientation="h",
        marker_color="#636efa",
        opacity=0.7,
    ))
    fig_pen.add_trace(go.Bar(
        name="Realizado %",
        y=df_pen_all["descricao"],
        x=df_pen_all["realizado_valor"],
        orientation="h",
        marker_color="#00cc96",
        opacity=0.85,
    ))
    fig_pen.update_layout(
        barmode="overlay",
        height=max(200, len(df_pen_all) * 55),
        xaxis_title="Percentual (%)",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(gridcolor="#e0e0e0"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        margin=dict(t=30, b=30),
    )
    st.plotly_chart(fig_pen, use_container_width=True)

st.markdown("---")

# ─────────────────────────────────────────────
# 10. TABELA DE METAS DIÁRIAS
# ─────────────────────────────────────────────
st.subheader("📅 Metas Diárias — 18/04 e Meta Salão")

df_daily = df_filtrado[
    df_filtrado["tipo_meta"].isin(["Financeiro", "META VD"])
].copy()

df_daily = df_daily[[
    "especialista", "marca_ciclo", "descricao",
    "porcentagem_alcancada", "restante",
    "meta_dia_18_04", "meta_dia_salao"
]].rename(columns={
    "especialista":          "Especialista",
    "marca_ciclo":           "Marca / Ciclo",
    "descricao":             "Meta",
    "porcentagem_alcancada": "% Atingido",
    "restante":              "Restante (9 dias)",
    "meta_dia_18_04":        "Meta Dia 18/04",
    "meta_dia_salao":        "Meta Dia Salão",
})

# Formata colunas monetárias
def fmt_cell(v):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return "—"
    if isinstance(v, (int, float)):
        prefix = "-R$ " if v < 0 else "R$ "
        return f"{prefix}{abs(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return v

for col in ["Restante (9 dias)", "Meta Dia 18/04", "Meta Dia Salão"]:
    df_daily[col] = df_daily[col].apply(fmt_cell)

# Formata %
df_daily["% Atingido"] = df_daily["% Atingido"].apply(
    lambda v: f"{v:.1f}%" if pd.notna(v) else "—"
)

# Estiliza a tabela com cores condicionais via HTML
def highlight_pct(row):
    pct_str = row["% Atingido"]
    if pct_str == "—":
        return [""] * len(row)
    pct = float(pct_str.replace("%", ""))
    if pct >= 100:
        color = "background-color: #d4edda; color: #155724"
    elif pct >= 70:
        color = "background-color: #fff3cd; color: #856404"
    else:
        color = "background-color: #f8d7da; color: #721c24"
    return [color if col == "% Atingido" else "" for col in row.index]

styled = df_daily.style.apply(highlight_pct, axis=1)
st.dataframe(styled, use_container_width=True, hide_index=True)

st.markdown("---")

# ─────────────────────────────────────────────
# 11. RANKING GERAL (visão de todas as especialistas)
# ─────────────────────────────────────────────
st.subheader("🏆 Ranking — % de Atingimento do Financeiro")

df_rank = df[df["tipo_meta"] == "Financeiro"].sort_values(
    "porcentagem_alcancada", ascending=True
).copy()

cores_bar = [
    "#00cc96" if p >= 100 else ("#ffd166" if p >= 70 else "#ef476f")
    for p in df_rank["porcentagem_alcancada"]
]

fig_rank = go.Figure(go.Bar(
    x=df_rank["porcentagem_alcancada"],
    y=df_rank["especialista"],
    orientation="h",
    marker_color=cores_bar,
    text=[f"{p:.1f}%" for p in df_rank["porcentagem_alcancada"]],
    textposition="outside",
))

fig_rank.add_vline(
    x=100, line_dash="dash", line_color="red",
    annotation_text="Meta 100%", annotation_position="top right"
)

fig_rank.update_layout(
    height=300,
    xaxis_title="% Atingido",
    xaxis_range=[0, 140],
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(gridcolor="#e0e0e0"),
    margin=dict(t=30, b=30),
)
st.plotly_chart(fig_rank, use_container_width=True)

# ─────────────────────────────────────────────
# 12. RODAPÉ
# ─────────────────────────────────────────────
st.markdown("---")
st.caption(
    "📌 Dashboard gerado automaticamente a partir dos dados extraídos da planilha de metas — "
    "Ciclo ABRIL/2026 · 9 dias restantes no ciclo."
)
