import gcsfs
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from utils.auth import generate_auth
load_dotenv()


@st.cache_data(show_spinner='Carregando dados...', ttl='1d')
def get_data_from_cloud_storage(file):
    generate_auth()

    fs = gcsfs.GCSFileSystem(
        token=os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

    df = pd.read_parquet(fs.open(file))

    df['ano_str'] = df['ano_campeonato'].astype('str')

    return df
