import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt
from utils.config import defaults

def classification_line_plot(df):
    plt.gca().invert_yaxis()
    # sns.set_style('darkgrid')
    # sns.set_theme()
    # sns.set_style('darkgrid', {'grid.color': '.6', 'grid.linestyle': ':'})
    plot = sns.lineplot(df, x='rodada', y='colocacao', hue='time', markers=True)

    plot.set_xticks([x + 1 for x in range(38)], [x + 1 for x in range(38)])
    plot.set_yticks([y + 1 for y in range(20)], [y + 1 for y in range(20)])

    plot.set_ylim([21, 0])
    plot.set_xlim([0, 39])

    plot.set_xlabel('Rodada')
    plot.set_ylabel('Colocação')

    plot.figure.set_figwidth(14)
    plot.figure.set_figheight(8)

    for i in range(df.shape[0]):
        plot.annotate(
            df.loc[i, 'colocacao'] if df.loc[i, 'rodada'] % 2 > 0 else None,
            (df.loc[i, 'rodada'] - 0.2, df.loc[i, 'colocacao'] - 0.3), 
            fontsize=12
        )
    plot.grid()

    st.pyplot(plot.figure)


def category_by_year_bar_plot(df, category):
    plot = sns.barplot(
        x="ano_campeonato",
        y=category,
        data=df,
        color=defaults['primary_color']
    )

    plot.set_xlabel('Ano')
    plot.set_ylabel(' '.join(category.split('_')).capitalize())

    plot.figure.set_figwidth(12)

    # Show plot
    st.pyplot(plot.figure, clear_figure=True)

def category_by_year_box_plot(df, category):
    plot = sns.boxplot(df, x='ano_campeonato', y=category, color=defaults['primary_color'])
    
    plot.set_xlabel('Ano')
    plot.set_ylabel(' '.join(category.split('_')).capitalize())

    plot.figure.set_figwidth(12)

    # Show plot
    st.pyplot(plot.figure, clear_figure=True)

    