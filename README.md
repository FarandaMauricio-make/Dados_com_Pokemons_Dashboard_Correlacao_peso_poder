# 🧬 Pokémon Peso x Poder: ML Analytics

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite3-green)

> **Dashboard de Data Science** que aplica técnicas de Machine Learning (Clustering e Regressão) para analisar se o físico de um Pokémon influencia seus status de batalha e para identificar arquétipos ocultos de poder.

## 📋 Sobre o Projeto

Este projeto vai além da análise descritiva básica. Ele utiliza o banco de dados `pokemon_dw.db` (Data Warehouse) para responder perguntas complexas através de estatística e algoritmos não supervisionados.

O objetivo é investigar a filosofia de design dos jogos: **"Será que Pokémon maiores são necessariamente mais fortes?"** e **"Quais são os grupos táticos (arquétipos) que existem matematicamente no jogo?"**

---

## 🚀 Funcionalidades de Data Science

### 1. 🧠 Machine Learning (Clustering)
- **K-Means:** Agrupamento automático dos Pokémon em clusters baseados em seus 6 status base.
- **PCA (Principal Component Analysis):** Redução de dimensionalidade para visualizar dados complexos (6 dimensões) em um gráfico 2D interativo.
- **Identificação de Arquétipos:** O algoritmo rotula automaticamente os grupos como:
    - 🛡️ **Tanques:** Alta defesa/HP.
    - ⚔️ **Atacantes:** Foco em dano físico ou especial.
    - ⚡ **Velozes:** Foco em velocidade (Speedsters).
    - ⚖️ **Balanceados:** Status equilibrados.

### 2. 📈 Análise de Regressão
- **Regressão Linear:** Modela a relação entre Peso (kg) e HP (Health Points) para testar a hipótese de que "tamanho é documento".
- **Cálculo de R²:** Exibe estatisticamente o quanto uma variável explica a outra.

### 3. 📊 Correlação Estatística
- **Matriz de Spearman:** Mapa de calor (Heatmap) que cruza dados físicos (Altura/Peso) com dados de combate para encontrar correlações lineares e não-lineares.

### 4. 📝 Data Storytelling
- **Narrativa Guiada:** O dashboard não apenas joga números, ele guia o usuário por uma história, concluindo com insights sobre o metagame (ex: o jogo privilegia ofensiva sobre defesa).

---

## 🛠️ Tecnologias Utilizadas

* **[Streamlit](https://streamlit.io/):** Front-end interativo.
* **[Scikit-learn](https://scikit-learn.org/):** Biblioteca de Machine Learning (KMeans, PCA, LinearRegression, StandardScaler).
* **[Pandas](https://pandas.pydata.org/):** Manipulação de DataFrames e SQL.
* **[Plotly Express](https://plotly.com/python/):** Visualizações de dados ricas e interativas.
* **[SQLite3](https://www.sqlite.org/):** Banco de dados relacional (Fonte dos dados).

---

## 📦 Como Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o arquivo `pokemon_dw.db` na mesma pasta (gerado pelo seu script de ETL anterior).

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/pokemon-ml-analytics.git](https://github.com/SEU-USUARIO/pokemon-ml-analytics.git)
    cd pokemon-ml-analytics
    ```

2.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install streamlit pandas plotly scikit-learn
    ```

4.  **Execute o Dashboard:**
    ```bash
    streamlit run Pokemon_peso_poder.py
    ```

---

## 📂 Estrutura de Arquivos

---

## 🧠 Insights do Projeto

Ao rodar este dashboard, os dados revelam padrões interessantes sobre o equilíbrio do jogo:
1.  **Peso ≠ HP:** Ao contrário do senso comum, ser pesado não garante HP alto (R² baixo).
2.  **Metagame Ofensivo:** O algoritmo de clusterização mostra que a grande maioria dos Pokémon cai na categoria "Atacante" ou "Veloz", com poucos "Tanques" puros.

---

## 🤝 Contribuição

Quer testar outros algoritmos de clusterização (como DBSCAN) ou adicionar novas variáveis?

1.  Faça um Fork.
2.  Crie sua Feature Branch (`git checkout -b feature/NewAlgo`).
3.  Commit suas mudanças.
4.  Push para a Branch.
5.  Abra um Pull Request.

---

**Science, I Choose You!** 🧪

Você pode acessar o Dashboard a partir do link: [Peso x Poder: Explorando Arquétipos Pokémon](https://dados-com-pokemons-correlacao-peso-poder.onrender.com)

