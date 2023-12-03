import streamlit as st
from utils.config import set_config, defaults
from utils.state import *
from components.footer import sidebar_footer
from components.header import default_header
from components.plots import category_by_year_bar_plot, category_by_year_box_plot
from components.tables import get_winners_df, get_demoters_df
from streamlit_extras.colored_header import colored_header 

set_config('Futebol Stats')
set_states()

with st.sidebar:
    # FILTRO
    # Selecionar anos
    sidebar_footer()

default_header()

selected_teams = defaults['selected_teams']
year = defaults['year']

melted_df = session_state['melted_df'].copy(deep=True)
base_df = session_state['base_df'].copy(deep=True)


st.write('''

''')

col1, col2, col3, col4 = st.columns(4)

col1.metric(label='Jogos', value=len(base_df))
col2.metric(label='Equipes', value=base_df['time_mandante'].nunique())
col3.metric(label='Técnicos', value=base_df['tecnico_visitante'].nunique())
col4.metric(label='Estádios', value=base_df['estadio'].nunique())

st.write('#### Distribuição de pontos por ano')
st.write('Na distribuição abaixo podemos acompanhar a disparidade de pontuação entre os times na última rodada do ano em questão. Podemos notar anos onde houve uma grande disparidade de pontuações como em 2019 ou anos onde a disputa foi acirrada, como em 2021. Além disso, podemos ver *outliers* no topo e na base da tabela.')
category_by_year_box_plot(melted_df[melted_df['rodada'] == 38], 'cum_pontos')

st.write('#### Média de gols por jogo')
category_by_year_bar_plot(base_df, 'gols_totais')

st.write('#### Vencedores de cada ano')
st.write('A tabela abaixo mostra os resultados do vencedor do Brasileirão em cada ano.')
st.dataframe(get_winners_df(melted_df), hide_index=True, height=600)

st.write('#### Corte de rebaixamento de cada ano')
st.write('A tabela abaixo mostra os resultados alcançados pela equipe que ficou em 17º lugar no Brasileirão em cada ano, sendo a equipe com maior pontuação que foi rebaixada. É interessante comparar com o gráfico abaixo a ideia de que uma equipe com 45 pontos dificilmente será rebaixada.')
st.dataframe(
    get_demoters_df(melted_df),
    use_container_width=True,
    hide_index=True,
    height=600
)

# Média de público por ano
# Média de valor da equipe titular por ano
# Média de idade da equipe titular por ano

# Média de gols por ano
# Média de escanteios por ano
# Média de faltas por ano
# Média de defesas por ano
# Média de chutes de bola parada por ano
# Média de chutes por ano
# Média de impedimentos por ano

# Top 5 clubes que mais ganharam
# Top 5 técnicos que mais ganharam
# Top 5 árbitros com mais jogos
# Top 5 clubes que mais ficaram no G4
