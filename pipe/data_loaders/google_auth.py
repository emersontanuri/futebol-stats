from google.cloud import bigquery
from os import environ
from dotenv import load_dotenv

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def google_cloud_auth(*args, **kwargs):
    load_dotenv()

    client = bigquery.Client()

    return client
