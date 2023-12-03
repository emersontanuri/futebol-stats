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
    df_2 = df.melt(
        id_vars=['ano_campeonato', 'rodada','data', 'estadio', 'arbitro', 'publico', 'publico_max'], 
        var_name=['mandato_campo'],
        value_vars=['time_mandante', 'time_visitante'], 
        value_name='time'
    )

    rename_visitante_cols = { col: col.replace('mandante', 'adversario').replace('_visitante', '') for col in [c for c in df if 'mandante' in c or 'visitante' in c] }
    rename_mandante_cols = { col: col.replace('visitante', 'adversario').replace('_mandante', '') for col in [c for c in df if 'visitante' in c or 'mandante' in c] }

    df_mandante = df_2.merge(
        df, 
        left_on=['ano_campeonato', 'data', 'rodada', 'estadio', 'arbitro', 'publico', 'publico_max', 'time'], 
        right_on=['ano_campeonato', 'data', 'rodada', 'estadio', 'arbitro', 'publico', 'publico_max', 'time_mandante'],
        how='inner'
    )

    df_visitante = df_2.merge(
        df, 
        left_on=['ano_campeonato', 'data', 'rodada', 'estadio', 'arbitro', 'publico', 'publico_max', 'time'], 
        right_on=['ano_campeonato', 'data', 'rodada', 'estadio', 'arbitro', 'publico', 'publico_max', 'time_visitante'], 
        how='inner'
    )

    df_mandante.drop(columns='time_mandante', inplace=True)
    df_visitante.drop(columns='time_visitante', inplace=True)

    df_mandante = df_mandante.rename(columns=rename_mandante_cols)
    df_visitante = df_visitante.rename(columns=rename_visitante_cols)

    df_main = pd.concat([df_mandante, df_visitante]).sort_values('rodada')

    return df_main.reset_index()


@test
def test_output(output, *args) -> pd.DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert output is not pd.DataFrame, 'The output is undefined'