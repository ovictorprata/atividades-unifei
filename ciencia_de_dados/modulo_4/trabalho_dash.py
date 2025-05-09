import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard TikTok", layout="wide")
st.title("📊 Dashboard TikTok - Análise de Hashtags Populares")

@st.cache_data
def carregar_dados():
    df = pd.read_csv("dataset_tiktok.csv")
    df["Order Date"] = pd.to_datetime(df["createTimeISO"], errors='coerce')
    return df.dropna(subset=["Order Date"])

df = carregar_dados()

anos = df["Order Date"].dt.year.dropna().unique()
ano_selecionado = st.selectbox("Selecione o ano", sorted(anos))
df_filtrado = df[df["Order Date"].dt.year == ano_selecionado]

# Tabela mais compacta
st.subheader("📋 Tabela de Dados Filtrados")
st.dataframe(
    df_filtrado[[
        "Order Date", "authorMeta/name", "searchHashtag/name", 
        "playCount", "shareCount", "videoMeta/duration"
    ]],
    height=200
)

# Dados para gráficos
df_resumo = df_filtrado[[
    "Order Date", "playCount", "shareCount", "videoMeta/duration", "searchHashtag/name"
]].copy()
df_resumo["Mes"] = df_resumo["Order Date"].dt.to_period("M").astype(str)

# Gráficos Linha + Barra
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Visualizações Totais por Mês")
    linha = df_resumo.groupby("Mes")["playCount"].sum()
    fig_linha, ax_linha = plt.subplots(figsize=(5.5, 1.8))
    linha.plot(marker='o', ax=ax_linha)
    ax_linha.set_xlabel("Mês", fontsize=8)
    ax_linha.set_ylabel("Visualizações", fontsize=8)
    ax_linha.tick_params(axis='both', labelsize=8, rotation=45)
    st.pyplot(fig_linha)

with col2:
    st.subheader("📊 Top 5 Hashtags por Visualizações")
    barra = df_resumo.groupby("searchHashtag/name")["playCount"].sum().nlargest(5)
    fig_bar, ax_bar = plt.subplots(figsize=(5.5, 1.8))
    barra.plot(kind="bar", ax=ax_bar)
    ax_bar.set_xlabel("Hashtag", fontsize=8)
    ax_bar.set_ylabel("Visualizações", fontsize=8)
    ax_bar.set_xticklabels(barra.index, rotation=30, fontsize=8)
    ax_bar.tick_params(axis='y', labelsize=8)
    st.pyplot(fig_bar)

# Dispersão + Pizza
col3, col4 = st.columns(2)

with col3:
    st.subheader("📎 Dispersão: Duração do Vídeo vs Visualizações")
    top_hashtags = df_resumo["searchHashtag/name"].value_counts().nlargest(6).index
    dispersao = df_resumo[df_resumo["searchHashtag/name"].isin(top_hashtags)]
    fig_disp, ax_disp = plt.subplots(figsize=(5.5, 1.8))
    sns.scatterplot(
        data=dispersao,
        x="videoMeta/duration",
        y="playCount",
        hue="searchHashtag/name",
        ax=ax_disp,
        legend=False
    )
    ax_disp.set_xlabel("Duração (s)", fontsize=8)
    ax_disp.set_ylabel("Visualizações", fontsize=8)
    ax_disp.tick_params(axis='both', labelsize=8)
    st.pyplot(fig_disp)

with col4:
    st.subheader("🥧 Compartilhamentos por Hashtag (Top 5)")
    pizza = df_resumo.groupby("searchHashtag/name")["shareCount"].sum().nlargest(5)
    fig_pie, ax_pie = plt.subplots(figsize=(5.5, 1.8))
    ax_pie.pie(pizza, labels=pizza.index, autopct="%1.1f%%", textprops={'fontsize': 8})
    ax_pie.axis("equal")
    st.pyplot(fig_pie)


st.markdown("Criado por Victor Prata | Dados: Kaggle | Ferramentas: Python, Streamlit, Pandas, Matplotlib, Seaborn")
