import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Ingestão de Dados com Cache
@st.cache_data(ttl=3600)  # cache por 1 hora
def carregar_dados():
    conn = sqlite3.connect("pokemon_dw.db")
    pokemon = pd.read_sql_query("SELECT * FROM pokemon", conn)
    pokemon_stats = pd.read_sql_query("SELECT * FROM pokemon_stats", conn)
    conn.close()

    stats_pivot = pokemon_stats.pivot_table(index='pokemon_id',
                                            columns='stat_name',
                                            values='base_stat',
                                            aggfunc='first')
    df = pd.merge(pokemon, stats_pivot, left_on='id', right_on='pokemon_id')
    return df

df = carregar_dados()

# Introdução
st.title("Peso x Poder: Explorando Arquétipos Pokémon")
st.markdown("""
Este painel conta uma história sobre como os atributos físicos (altura e peso) e os status (HP, ataque, defesa, velocidade) 
se relacionam entre si. Depois, agrupamos os Pokémon em **clusters** — arquétipos — para revelar padrões escondidos.
""")

# Criar abas para organizar a narrativa
tab1, tab2, tab3, tab4 = st.tabs(["📊 Correlação", "📈 Regressão", "🎨 Clusters", "📚 Conclusão"])

# 2. Correlação
with tab1:
    st.header("Correlação entre físico e status")
    corr_cols = ['height', 'weight', 'hp', 'attack', 'defense', 'speed']
    corr_matrix = df[corr_cols].corr(method='spearman')

    fig_corr = px.imshow(corr_matrix,
                         text_auto=True,
                         color_continuous_scale="RdBu",
                         title="Correlação: Físico vs Status (Spearman)")
    st.plotly_chart(fig_corr, use_container_width=True)

    st.markdown("""
    🔎 O físico (altura/peso) pouco explica os status de batalha.  
    - Altura e peso estão fortemente correlacionados entre si.  
    - HP tem correlação fraca com físico.  
    - Velocidade não se relaciona com altura/peso.  
    """)

# 3. Regressão Linear (Peso -> HP)
with tab2:
    st.header("Peso influencia o HP?")
    X = df[['weight']]
    y = df['hp']
    reg = LinearRegression().fit(X, y)
    st.write(f"R² da Regressão: {reg.score(X, y):.4f} (quanto mais próximo de 1, mais forte a relação)")

    fig_reg = px.scatter(df, x="weight", y="hp",
                         trendline="ols",
                         title="Regressão Linear: Peso vs HP")
    st.plotly_chart(fig_reg, use_container_width=True)

    st.markdown("""
    📈 O peso não é um bom preditor de HP.  
    - Pokémon pesados podem ter pouco HP (ex.: Onix).  
    - Pokémon leves podem ter muito HP (ex.: Chansey).  
    """)

# 4. Clustering (KMeans)
with tab3:
    st.header("Clusters de Arquétipos Pokémon")
    features = ['hp', 'attack', 'defense', 'speed', 'special-attack', 'special-defense']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features].fillna(0))

    n_clusters = st.slider("Número de clusters (KMeans)", 2, 8, 4)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)

    # PCA para visualização
    pca = PCA(n_components=2)
    components = pca.fit_transform(X_scaled)
    df['pca1'] = components[:, 0]
    df['pca2'] = components[:, 1]

    # Nomear clusters automaticamente
    cluster_summary = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=features).round(1)
    cluster_labels = {}
    for c in cluster_summary.index:
        stats = cluster_summary.loc[c]
        dominant_attr = stats.idxmax()
        if dominant_attr in ['hp', 'defense']:
            cluster_labels[c] = "Tanques 🛡️"
        elif dominant_attr in ['attack', 'special-attack']:
            cluster_labels[c] = "Atacantes ⚔️"
        elif dominant_attr == 'speed':
            cluster_labels[c] = "Velozes ⚡"
        else:
            cluster_labels[c] = "Balanceados ⚖️"
    df['cluster_label'] = df['cluster'].map(cluster_labels)

    fig_pca = px.scatter(df, x="pca1", y="pca2",
                         color="cluster_label",
                         hover_data=["name","hp","attack","defense","speed"],
                         title="Clusters de Arquétipos Pokémon")
    st.plotly_chart(fig_pca, use_container_width=True)

    st.write(cluster_summary.assign(Perfil=cluster_summary.index.map(cluster_labels)))

    st.markdown("""
    🎨 **Insight:**  
    - A maioria dos Pokémon é **Atacante ⚔️**.  
    - Os mais poderosos e lendários tendem a ser **Velozes ⚡**.  
    - Os **Balanceados ⚖️** são raros, mas versáteis.  
    - Os **Tanques 🛡️** quase não aparecem, mostrando que o design privilegia ataque e velocidade.  
    """)

# 5. Conclusão
with tab4:
    st.header("Narrativa Final")
    st.markdown("""
    📚 **História que os dados contam:**

    - O físico (altura/peso) não determina poder de batalha.  
    - O peso não prediz HP de forma confiável.  
    - O ecossistema Pokémon é ofensivo e veloz: a maioria dos Pokémon é desenhada para atacar rápido ou forte.  
    - Poucos são defensivos puros, o que revela uma filosofia de design voltada para ofensiva.  

    👉 Em resumo: **o mundo Pokémon privilegia ofensiva e velocidade em vez de pura resistência.**
    """)

# Botão de download
st.header("Baixar resultados")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download dos resultados em CSV",
    data=csv,
    file_name="pokemon_clusters.csv",
    mime="text/csv"
)