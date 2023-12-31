if 'pd' not in globals():
    import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df: pd.DataFrame, *args, **kwargs):
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
    df.loc[df['gols_mandante'] > df['gols_visitante'], ['pontos_mandante', 'pontos_visitante']] = [3, 0]
    df.loc[df['gols_mandante'] == df['gols_visitante'], ['pontos_mandante', 'pontos_visitante']] = [1, 1]
    df.loc[df['gols_mandante'] < df['gols_visitante'], ['pontos_mandante', 'pontos_visitante']] = [0, 3]

    return df


@test
def test_output(output, *args) -> pd.DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert output is not pd.DataFrame, 'The output is undefined'