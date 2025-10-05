# installer streamlit si pas encore fait
# pip install streamlit plotly pandas

import streamlit as st
import pandas as pd
import plotly.express as px

# Charger le dataset nettoyé


import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Charger dataset nettoyé
df = pd.read_csv(r"C:\Users\Pc\Desktop\GIT\Netflix project\data\processed\netflix_cleaned.csv")

# Nettoyage simple
df['country'] = df['country'].fillna('Unknown').str.split(',').explode('country').str.strip()
df['listed_in'] = df['listed_in'].fillna('Unknown').str.split(',').explode('listed_in').str.strip()
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Sidebar - Filtres
st.sidebar.title("Filtres")
countries = st.sidebar.multiselect("Pays", df['country'].unique(), default=["United States"])
types = st.sidebar.multiselect("Type", df['type'].unique(), default=df['type'].unique())
years = st.sidebar.slider("Année de sortie", int(df['release_year'].min()), int(df['release_year'].max()),
                          (2010, 2023))
genres = st.sidebar.multiselect("Genres", df['listed_in'].unique(), default=[])

# Filtrer dataset
df_filtered = df[df['country'].isin(countries) & df['type'].isin(types)]
df_filtered = df_filtered[df_filtered['release_year'].between(years[0], years[1])]
if genres:
    df_filtered = df_filtered[df_filtered['listed_in'].isin(genres)]

# Afficher métriques clés
st.title("Netflix Dashboard Avancé")
st.metric("Total Titles", len(df_filtered))
st.metric("Unique Genres", df_filtered['listed_in'].nunique())
st.metric("Average Duration", round(df_filtered['duration_value'].mean(), 1))

# Top genres
top_genres = df_filtered.groupby('listed_in').size().reset_index(name='count').sort_values('count', ascending=False).head(10)
fig1 = px.bar(top_genres, x='listed_in', y='count', color='count', title="Top Genres")
st.plotly_chart(fig1)

# Evolution par année
year_count = df_filtered.groupby('release_year').size().reset_index(name='count')
fig2 = px.line(year_count, x='release_year', y='count', title="Titles per Year")
st.plotly_chart(fig2)

# Durée moyenne par type
avg_duration = df_filtered.groupby('type')['duration_value'].mean().reset_index()
fig3 = px.bar(avg_duration, x='type', y='duration_value', title="Average Duration by Type")
st.plotly_chart(fig3)

# Heatmap pays vs genres
pivot = df_filtered.pivot_table(index='country', columns='listed_in', aggfunc='size', fill_value=0)
plt.figure(figsize=(20,10))
sns.heatmap(pivot, cmap="YlGnBu")
plt.title("Heatmap Countries vs Genres")
st.pyplot(plt)
