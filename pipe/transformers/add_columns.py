if 'pd' not in globals():
    import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data: pd.DataFrame, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    columns_to_add = [
        'idade_media_titular', 
        'gols', 
        'gols_1_tempo',
        'escanteios', 
        'faltas', 
        'chutes_bola_parada',
        'defesas', 
        'impedimentos', 
        'chutes',
        'chutes_fora'
    ]

    for col in columns_to_add:
        data[col + '_totais'] = data[col + '_mandante'] + data[col + '_visitante']

    return data


@test
def test_output(output, *args) -> pd.DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert output is not pd.DataFrame, 'The output is undefined'