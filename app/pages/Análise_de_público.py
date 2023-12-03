import streamlit as st
import pandas as pd
from utils.config import defaults, set_config
from utils.state import *
from components.footer import sidebar_footer
from components.header import default_header
from components.plots import category_by_year_bar_plot, category_by_year_box_plot

set_config('Análise de Público - Futebol Stats')
set_states()

with st.sidebar:
    sidebar_footer()

default_header()

selected_teams = defaults['selected_teams']
year = defaults['year']

melted_df = session_state['melted_df'].copy(deep=True)
base_df = session_state['base_df'].copy(deep=True)


st.write('''

''')
audience_df = pd.DataFrame(base_df.groupby(['ano_campeonato']).agg(publico=('publico', 'mean')).to_records())

year_with_biggest_audience = audience_df.sort_values('publico', ascending=False).head(1)

columns = ['ano_str', 'time_mandante', 'time_visitante', 'estadio', 'publico']
top_five_most_audience_games = base_df.sort_values('publico', ascending=False).head()[columns]


st.write(
    f"""
    ## ✨ :red[{year_with_biggest_audience["ano_campeonato"].unique()[0]}]
    ##### Foi o ano com maior média de público.
    """)

st.write(
    f"""
    ## 👨‍👩‍👧‍👧 :red[{top_five_most_audience_games["ano_str"].unique()[0]} - {top_five_most_audience_games["time_mandante"].unique()[0]} x {top_five_most_audience_games["time_visitante"].unique()[0]}]
    ##### Foi o jogo com maior público já registrado no campeonato.
    """)


st.write('#### Média de público por jogo')
st.write('Podemos notar claramente o efeito da pandemia da Covid-19 no público dos estádios, mas que a evolução que se apresentava nos anos anteriores voltou com forte crescimento no ano atual, sendo o recorde de média de público. A competição vem evoluindo a cada ano e se tornando um produto cada vez mais forte, o que se reflete nesse resultado de público nas partidas.')
category_by_year_bar_plot(base_df, 'publico')