if 'pd' not in globals():
    import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
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
    data.loc[data['time_mandante'] == 'Atlético-PR', 'time_mandante'] = 'Athletico-PR'
    data.loc[data['time_visitante'] == 'Atlético-PR', 'time_visitante'] = 'Athletico-PR'

    data.loc[data['time_mandante'] == 'Santos', 'time_mandante'] = 'Santos FC'
    data.loc[data['time_visitante'] == 'Santos', 'time_visitante'] = 'Santos FC'

    data = data[data['ano_campeonato'] > 2006]

    data = data.sort_values('data', ascending=False)

    return data


@test
def test_output(output, *args) -> pd.DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert output is not pd.DataFrame, 'The output is undefined'
