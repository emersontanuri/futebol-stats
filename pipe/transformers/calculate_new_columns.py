if 'pd' not in globals():
    import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df_main: pd.DataFrame, *args, **kwargs):
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
    def count_win(x):
        return (x == 3).cumsum()

    def count_tie(x):
        return (x == 1).cumsum()

    def count_loss(x):
        return (x == 0).cumsum()

    df_main['mandato_campo'] = df_main['mandato_campo'].apply(lambda x: x.split('_')[1])
    
    df_main['cum_pontos'] = df_main.groupby(['ano_campeonato', 'time'])['pontos'].transform('cumsum')
    df_main['cum_gols'] = df_main.groupby(['ano_campeonato', 'time'])['gols'].transform('cumsum')
    df_main['cum_gols_adversario'] = df_main.groupby(['ano_campeonato', 'time'])['gols_adversario'].transform('cumsum')
    df_main['vitorias'] = df_main.groupby(['ano_campeonato', 'time'])['pontos'].transform(count_win)
    df_main['empates'] = df_main.groupby(['ano_campeonato', 'time'])['pontos'].transform(count_tie)
    df_main['derrotas'] = df_main.groupby(['ano_campeonato', 'time'])['pontos'].transform(count_loss)

    return df_main


@test
def test_output(output, *args) -> pd.DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert output is not pd.DataFrame, 'The output is undefined'