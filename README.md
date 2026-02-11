# 🐉 Peso x Poder: Explorando Arquétipos Pokémon

Este projeto é um **painel interativo em Streamlit** que analisa dados de Pokémon, revelando como atributos físicos (altura e peso) se relacionam com status de batalha (HP, ataque, defesa, velocidade) e como os Pokémon podem ser agrupados em **arquétipos** usando técnicas de Machine Learning.

---

## ✨ Funcionalidades

- 📊 **Correlação**: Heatmap interativo mostrando relações entre físico e status.  
- 📈 **Regressão Linear**: Análise de como o peso influencia o HP.  
- 🎨 **Clusters (KMeans)**: Agrupamento automático em arquétipos:  
  - Tanques 🛡️  
  - Atacantes ⚔️  
  - Velozes ⚡  
  - Balanceados ⚖️  
- 📚 **Storytelling**: Narrativa final que explica os padrões encontrados.  
- 📥 **Download**: Exportação dos resultados em CSV.  

---

## 🛠️ Tecnologias utilizadas

- [Streamlit](https://streamlit.io/) → Interface interativa.  
- [Pandas](https://pandas.pydata.org/) → Manipulação de dados.  
- [Plotly](https://plotly.com/python/) → Gráficos interativos.  
- [Scikit-learn](https://scikit-learn.org/) → Regressão, clustering e PCA.  
- [SQLite](https://www.sqlite.org/) → Banco de dados dos Pokémon.  

---

## 🚀 Como rodar localmente

Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/pokemon-peso-poder.git
   cd pokemon-peso-poder
  ```
Você pode acessar o o Dashboard a partir do link: [Dashboard_relação_peso_x_poder](https://dados-com-pokemons-correlacao-peso-poder.onrender.com)

