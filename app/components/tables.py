import pandas as pd
from streamlit import session_state

# Vencedores de cada ano
def get_winners_df(df):
    winners_columns = ['ano_str', 'time', 'cum_pontos', 'vitorias', 'empates', 'derrotas', 'cum_gols', 'cum_gols_adversario']
    winners_df = df[(df['rodada'] == 38) & (df['colocacao'] == 1)].sort_values('ano_str', ascending=False)[winners_columns]

    winners_df['Aproveitamento'] = round(winners_df['cum_pontos'] / (38 * 3) * 100, 2)
    winners_df['Aproveitamento'] = winners_df['Aproveitamento'].apply(lambda x: f'{x}%')
    winners_df['Saldo de Gols'] = winners_df['cum_gols'] - winners_df['cum_gols_adversario']

    winners_df.drop(columns=['cum_gols', 'cum_gols_adversario'], inplace=True)

    winners_df = winners_df.rename(
        columns={
            'ano_str': 'Ano',
            'time': 'Equipe',
            'cum_pontos': 'Pontuação final',
            'vitorias': 'Vitórias',
            'empates': 'Empates',
            'derrotas': 'Derrotas'
        }
    )
    return winners_df

# Vencedores de cada ano
def get_greatest_home_or_away_df(df, home_away):
    greatest_df = pd.DataFrame(
        df[
            (df['mandato_campo'] == home_away) & \
            (df['pontos'] == 3)
        ].groupby(['ano_str', 'time']).agg(victories=('rodada', 'count')).to_records()
    ).sort_values(['ano_str', 'victories'], ascending=False)

    greatest_df['max'] = greatest_df.groupby('ano_str')['victories'].transform('max')
    greatest_df = greatest_df[greatest_df['max'] == greatest_df['victories']]

    concat_str = lambda x: ', '.join(x)
    greatest_df = greatest_df.groupby(['ano_str', 'victories']).agg(time=('time', concat_str))
    greatest_df = pd.DataFrame(greatest_df.to_records()).sort_values(['ano_str'], ascending=False)

    greatest_df = greatest_df.rename(
        columns={
            'ano_str': 'Ano',
            'time': 'Equipe',
            'victories': 'Vitórias',
        }
    )
    
    return greatest_df[['Ano', 'Equipe', 'Vitórias']]

# Maior pontuação do time rebaixado por ano
def get_demoters_df(df):
    demoters_columns = ['ano_str', 'time', 'cum_pontos', 'vitorias', 'empates', 'derrotas', 'cum_gols', 'cum_gols_adversario']
    demoters_df = df[(df['rodada'] == 38) & (df['colocacao'] == 17)].sort_values('ano_str', ascending=False)[demoters_columns]

    demoters_df['Aproveitamento'] = round(demoters_df['cum_pontos'] / (38 * 3) * 100, 2)
    demoters_df['Aproveitamento'] = demoters_df['Aproveitamento'].apply(lambda x: f'{x}%')
    demoters_df['Saldo de Gols'] = round(demoters_df['cum_gols'] - demoters_df['cum_gols_adversario'])

    demoters_df.drop(columns=['cum_gols', 'cum_gols_adversario'], inplace=True)

    demoters_df = demoters_df.rename(
        columns={
            'ano_str': 'Ano',
            'time': 'Equipe',
            'cum_pontos': 'Pontuação final',
            'vitorias': 'Vitórias',
            'empates': 'Empates',
            'derrotas': 'Derrotas'
        }
    )

    return demoters_df

def get_year_g4_df(df, year_last_round, columns):

    g4_df = df[
        (df['rodada'] == year_last_round) & \
        (df['colocacao'] <= 4) & \
        (df['ano_campeonato'] == session_state['selected_year'])
    ][columns].sort_values('colocacao')
    
    g4_df['Aproveitamento'] = round(g4_df['cum_pontos'] / (38 * 3) * 100, 2)
    g4_df['Aproveitamento'] = g4_df['Aproveitamento'].apply(lambda x: f'{x}%')
    
    g4_df = g4_df.rename(
        columns={
            'colocacao': 'Colocação',
            'time': 'Equipe',
            'cum_pontos': 'Pontuação final',
            'vitorias': 'Vitórias',
            'empates': 'Empates',
            'derrotas': 'Derrotas'
        }
    )

    return g4_df

def get_year_demoters_df(df, year_last_round, columns):

    demoters_df = df[
        (df['rodada'] == year_last_round) & \
        (df['colocacao'] >= 17) & \
        (df['ano_campeonato'] == session_state['selected_year'])
    ][columns].sort_values('colocacao')

    demoters_df['Aproveitamento'] = round(demoters_df['cum_pontos'] / (38 * 3) * 100, 2)
    demoters_df['Aproveitamento'] = demoters_df['Aproveitamento'].apply(lambda x: f'{x}%')

    demoters_df = demoters_df.rename(
        columns={
            'colocacao': 'Colocação',
            'time': 'Equipe',
            'cum_pontos': 'Pontuação final',
            'vitorias': 'Vitórias',
            'empates': 'Empates',
            'derrotas': 'Derrotas'
        }
    )

    return demoters_df