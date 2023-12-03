from google.cloud import bigquery
from os import environ
from dotenv import load_dotenv

if 'pd' not in globals():
    import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_big_query(*args, **kwargs) -> pd.DataFrame:
    load_dotenv()

    GOOGLE_CLOUD_PROJECT = environ['GOOGLE_CLOUD_PROJECT']
    client = bigquery.Client(GOOGLE_CLOUD_PROJECT)

    query = """
    SELECT *
    FROM `basedosdados.mundo_transfermarkt_competicoes.brasileirao_serie_a`
    """
    query_job = client.query(query)
    query_job.result()

    # Para carregar o dado direto no pandas
    df = pd.read_gbq(query, project_id=GOOGLE_CLOUD_PROJECT)

    df['data'] = pd.to_datetime(df['data'])

    return df


@test
def test_output(output, *args) -> pd.DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert output is not pd.DataFrame, 'The output is undefined'
