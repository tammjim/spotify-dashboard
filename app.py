import streamlit as st
import pandas as pd

df = pd.read_csv("spotify_user_behavior_realistic_50000_rows.csv")

st.set_page_config(page_title="Spotify User Dashboard", page_icon="🎵", layout="wide")
st.title("🎵 Spotify · Análisis de usuarios")
st.caption(f"Dataset: {df.shape[0]:,} usuarios · {df.shape[1]} columnas")

paises = sorted(df['country'].unique().tolist())
pais_sel = st.sidebar.selectbox("🌍 Filtrar por país", ["Todos"] + paises)

if pais_sel != "Todos":
    df = df[df['country'] == pais_sel]

col1, col2, col3 = st.columns(3)
col1.metric("👤 Total usuarios", f"{len(df):,}")
col2.metric("🎧 Horas promedio/semana", f"{df['avg_listening_hours_per_week'].mean():.1f} hrs")
col3.metric("⭐ Rating promedio", f"{df['music_suggestion_rating_1_to_5'].mean():.2f} / 5")

st.divider()

st.subheader("Usuarios por tipo de suscripción")
subs = df['subscription_type'].value_counts()
st.bar_chart(subs)

st.subheader("Géneros musicales más populares")
generos = df['favorite_genre'].value_counts().head(10)
st.bar_chart(generos)

premium = df[df['subscription_type'] != 'Free']['avg_listening_hours_per_week'].mean()
free = df[df['subscription_type'] == 'Free']['avg_listening_hours_per_week'].mean()

st.info(f"""
📊 **Insight:** Los usuarios Premium escuchan en promedio **{premium:.1f} hrs/semana**,
mientras que los usuarios Free escuchan **{free:.1f} hrs/semana**.
Esto sugiere que mayor tiempo de escucha está asociado con suscripciones de pago.
""")
