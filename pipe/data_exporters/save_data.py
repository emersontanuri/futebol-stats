from google.cloud import bigquery
from dotenv import load_dotenv
from google.cloud import storage
from os import path, environ

if 'pd' not in globals():
    import pandas as pd
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: pd.DataFrame, df_2: pd.DataFrame, **kwargs) -> None:
    load_dotenv()

    GOOGLE_CLOUD_PROJECT = environ['GOOGLE_CLOUD_PROJECT']
    GOOGLE_CLOUD_BUCKET = environ['GOOGLE_CLOUD_BUCKET']

    parquet_file = df.to_parquet(index=False, compression='gzip')
    parquet_file_main = df_2.to_parquet(index=False, compression='gzip')

    # Create a Storage client object
    client = storage.Client(GOOGLE_CLOUD_PROJECT)

    # Get a reference to the bucket
    bucket = client.get_bucket(GOOGLE_CLOUD_BUCKET)

    # Create a blob object
    blob = bucket.blob('futebol-stats.parquet.gzip')

    blob_main = bucket.blob('futebol-stats-main.parquet.gzip')

    # Upload the CSV string to the blob
    blob.upload_from_string(parquet_file)

    blob_main.upload_from_string(parquet_file_main)
