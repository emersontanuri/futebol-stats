from datetime import datetime
import streamlit as st
from utils.config import set_config, defaults
from components.plots import classification_line_plot
from utils.state import *
from components.footer import sidebar_footer
from components.header import default_header
from components.tables import get_year_g4_df, get_year_demoters_df
from streamlit_extras.colored_header import colored_header 

set_config('Análise por ano - Futebol Stats')
default_header()
set_states()

with st.sidebar:
    # FILTRO
    st.write('#### Filtros')
    # Selecionar anos
    session_state['selected_year'] = st.selectbox(
        'Selecione o ano de análise', 
        session_state['years_options']
    )

    st.write('Ano selecionado:', session_state['selected_year'])

    session_state['selected_teams'] = st.multiselect(
        'Selecione as equipes que deseja comparar',
        session_state['teams_options'],
        session_state['selected_teams']
    ) 
    st.divider()
    sidebar_footer()


df = session_state['melted_df'].copy(deep=True)
df['ano_str'] = df['ano_campeonato'].astype('str')

columns = ['colocacao', 'time', 'cum_pontos', 'vitorias', 'empates', 'derrotas']

year_last_round = df[
    (df['ano_campeonato'] == session_state['selected_year']) & \
    (df['colocacao'] == 1)
]['rodada'].max()

win_points = int((df[
    (df['rodada'] == year_last_round) & \
    (df['colocacao'] == 1) & \
    (df['ano_campeonato'] == session_state['selected_year'])
]['cum_pontos'].unique())[0])

year_winner = (df[
    (df['rodada'] == year_last_round) & \
    (df['colocacao'] == 1) & \
    (df['ano_campeonato'] == session_state['selected_year'])
]['time'].unique())[0]

g4_points = int((df[
    (df['rodada'] == year_last_round) & \
    (df['colocacao'] == 4) & \
    (df['ano_campeonato'] == session_state['selected_year'])
]['cum_pontos'].unique())[0])

escape_demote_points = int((df[
    (df['rodada'] == year_last_round) & \
    (df['colocacao'] == 17) & \
    (df['ano_campeonato'] == session_state['selected_year'])
]['cum_pontos'].unique())[0])

g4_df = get_year_g4_df(df, year_last_round, columns)
demoters_df = get_year_demoters_df(df, year_last_round, columns)

if not datetime.today().year == session_state['selected_year']:

    st.write(
    f"""
    ## 🏆 :red[{win_points + 1} pontos]
    ##### É o que o seu time precisaria alcançar para ser campeão em {session_state['selected_year']}.
    """)
    st.write(f"O campeão desse ano foi o **{year_winner}** com {win_points} pontos.")

    st.write(
    f"""
    ## 🥈 :red[{g4_points + 1} pontos]
    ##### É o que o seu time precisaria alcançar para estar no G4 em {session_state['selected_year']}.
    """)
    st.dataframe(g4_df, hide_index=True, use_container_width=True)

    st.write(
    f"""
    ## 😰 :red[{escape_demote_points + 1} pontos]
    ##### É o que o seu time precisaria alcançar para escapar do rebaixamento em {session_state['selected_year']}.
    """)

    st.dataframe(demoters_df, hide_index=True, use_container_width=True)

else:
    st.write(
    f"""
    ## 🏆 :red[{win_points + 1} pontos]
    ##### É o que o seu time precisaria alcançar para estar em primeiro lugar em {session_state['selected_year']}.
    """)
    st.write(f"O **{year_winner}** está em primeiro lugar com {win_points} pontos.")

    st.write(
    f"""
    ## 🥈 :red[{g4_points + 1} pontos]
    ##### É o que o seu time precisaria alcançar para estar no G4 em {session_state['selected_year']}.
    """)
    st.dataframe(g4_df, hide_index=True, use_container_width=True)

    st.write(
    f"""
    ## 😰 :red[{escape_demote_points + 1} pontos]
    ##### É o que o seu time precisaria alcançar para estar fora do rebaixamento em {session_state['selected_year']}.
    """)

    st.dataframe(demoters_df, hide_index=True, use_container_width=True)


# Colocacão dos times no ano
st.write('')

colored_header(
    label=f'Colocação ao longo das rodadas em {session_state["selected_year"]}',
    description='',
    color_name="red-70",
)
classification_df = df[
    (df['ano_campeonato'] == session_state['selected_year']) & \
    (df['time'].isin(session_state['selected_teams'] if len(session_state['selected_teams']) > 0 else session_state['default_teams']))
].reset_index()

classification_line_plot(classification_df)

