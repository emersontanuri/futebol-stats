import streamlit as st
from utils.config import defaults, set_config
from utils.state import *
from components.footer import sidebar_footer
from components.header import default_header
from components.tables import get_greatest_home_or_away_df

set_config('Análise de Mandantes e Visitantes - Futebol Stats')
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


st.write('#### Maiores vencedores mandantes e visitantes de cada ano')
col_1, col_2 = st.columns(2)
col_1.write('#### Maiores mandantes')
col_1.dataframe(get_greatest_home_or_away_df(melted_df, 'mandante'), hide_index=True, height=600, width=320)

col_2.write('#### Maiores visitantes')
col_2.dataframe(get_greatest_home_or_away_df(melted_df, 'visitante'), hide_index=True, height=600, width=320)