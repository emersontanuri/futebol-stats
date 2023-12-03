from streamlit import title, write
from utils.config import defaults
from utils.theming import ColourWidgetText

def default_header():
    title("⚽ Futebol Stats")
    write('Os dados apresentados abaixo são referentes aos anos de 2007 até os dias atuais. \n pode haver um atraso de algumas rodadas nos dados para o campeonato do ano atual.')

    # ColourWidgetText('Futebol Stats', defaults['primary_color'])