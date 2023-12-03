import streamlit as st

def set_config(title='Futebol Stats'):
  return st.set_page_config(
    page_title=title,
    page_icon='app/static/img/bola.png'
  ) 
  
defaults = {
  'selected_teams': ['Flamengo'],
  'year': 2023,
  'primary_color': '#FF4B4B'
}