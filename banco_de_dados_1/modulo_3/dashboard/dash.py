import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


df = pd.read_csv(r'.\experimento.csv')


df['TEMPERATURA'] = df['TEMPERATURA'].astype(float)
df['CONDUTIVIDADE'] = df['CONDUTIVIDADE'].astype(float)
df['ALCALINIDADE TOTAL'] = df['ALCALINIDADE TOTAL'].astype(float)


df['ACIDEZ'] = pd.to_numeric(df['ACIDEZ'], errors='coerce')
df['LATITUDE'] = df['LATITUDE'] / 1000  
df['LONGITUDE'] = df['LONGITUDE'] / 1000  


fig_map = px.scatter_geo(
    df, lat='LATITUDE', lon='LONGITUDE',
    hover_name='NOME', hover_data=['LOCAL', 'TEMPERATURA'],
    title='Localização das Amostras de Água',
    projection="natural earth"
)
fig_map.update_geos(fitbounds="locations")  

temperature_counts = df['TEMPERATURA'].value_counts().reset_index()
temperature_counts.columns = ['TEMPERATURA', 'CONTAGEM']

fig_pizza = px.pie(
    temperature_counts, names='TEMPERATURA', values='CONTAGEM',
    title='Distribuição das Temperaturas das Amostras'
)

fig_condutividade = px.bar(
    df, x='NOME', y='CONDUTIVIDADE',
    title='Distribuição de Condutividade nas Amostras',
    labels={'CONDUTIVIDADE': 'Condutividade (µS/cm)', 'NOME': 'Amostra'}
)


fig_dual_axis = go.Figure()

fig_dual_axis.add_trace(go.Scatter(
    x=df['NOME'], y=df['ALCALINIDADE TOTAL'], mode='lines', name='Alcalinidade Total',
    line=dict(color='blue'), yaxis='y1'
))

fig_dual_axis.add_trace(go.Scatter(
    x=df['NOME'], y=df['ACIDEZ'], mode='lines', name='Acidez',
    line=dict(color='red'), yaxis='y2'
))

fig_dual_axis.update_layout(
    title='Evolução da Alcalinidade Total e Acidez nas Amostras',
    xaxis=dict(title='Amostra'),
    yaxis=dict(title='Alcalinidade Total (mg/L)', side='left', showgrid=True),
    yaxis2=dict(title='Acidez (mg/L)', side='right', overlaying='y', showgrid=False),
    legend=dict(x=0.1, y=0.9),
    template='plotly_white'
)


min_temp = df['TEMPERATURA'].min()
max_temp = df['TEMPERATURA'].max()

temp_filter = st.slider('Selecione a faixa de Temperaturas', float(min_temp), float(max_temp), (float(min_temp), float(max_temp)))


df_filtered = df[(df['TEMPERATURA'] >= temp_filter[0]) & (df['TEMPERATURA'] <= temp_filter[1])]


fig_map_filtered = px.scatter_geo(
    df_filtered, lat='LATITUDE', lon='LONGITUDE',
    hover_name='NOME', hover_data=['LOCAL', 'TEMPERATURA'],
    title=f'Localização das Amostras de Água ({temp_filter[0]}°C a {temp_filter[1]}°C)',
    projection="natural earth"
)
fig_map_filtered.update_geos(fitbounds="locations") 

temperature_counts_filtered = df_filtered['TEMPERATURA'].value_counts().reset_index()
temperature_counts_filtered.columns = ['TEMPERATURA', 'CONTAGEM']

fig_pizza_filtered = px.pie(
    temperature_counts_filtered, names='TEMPERATURA', values='CONTAGEM',
    title=f'Distribuição das Temperaturas ({temp_filter[0]}°C a {temp_filter[1]}°C)'
)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Localização das Amostras de Água')
    st.plotly_chart(fig_map_filtered)

with col2:
    st.subheader('Distribuição das Temperaturas')
    st.plotly_chart(fig_pizza_filtered)

st.subheader('Distribuição de Condutividade nas Amostras')
st.plotly_chart(fig_condutividade)
st.subheader('Evolução da Alcalinidade Total e Acidez nas Amostras')
st.plotly_chart(fig_dual_axis)
