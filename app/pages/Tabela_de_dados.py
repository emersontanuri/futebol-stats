import streamlit as st
from utils.state import *
from utils.config import set_config
from components.footer import sidebar_footer

set_config('Tabela de dados - Futebol Stats')
set_states()

st.title("⚽ Futebol Stats")
st.write('## Tabela de Dados')

with st.sidebar:
    sidebar_footer()

main_df = session_state['base_df']

st.write(main_df)
