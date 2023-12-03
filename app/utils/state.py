from streamlit import session_state, cache_data
from utils.importer import get_data_from_cloud_storage

def set_states():
  if 'base_df' not in session_state:
    session_state['base_df'] = get_data_from_cloud_storage('futebol-stats/futebol-stats.parquet.gzip')

  if 'melted_df' not in session_state:
    session_state['melted_df'] = get_data_from_cloud_storage('futebol-stats/futebol-stats-main.parquet.gzip')

  if 'default_year' not in session_state:
    session_state['default_year'] = 2022

  if 'selected_year' not in session_state:  
    session_state['selected_year'] = session_state['default_year']

  if 'years_options' not in session_state:
    session_state['years_options'] = tuple(session_state['melted_df'].sort_values('ano_campeonato', ascending=False)['ano_campeonato'].unique())

  if 'default_teams' not in session_state:
    session_state['default_teams'] = ['Flamengo']

  if 'selected_teams' not in session_state:
    session_state['selected_teams'] = session_state['default_teams']

  if 'teams_options' not in session_state:
    session_state['teams_options'] = tuple(session_state['melted_df'][session_state['melted_df']['ano_campeonato'] == session_state['selected_year']].sort_values('time')['time'].unique())


