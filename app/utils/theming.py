import streamlit.components.v1 as components

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """
    <script>
        var elements = window.parent.document.querySelectorAll('*'), i;
        for (i = 0; i < elements.length; ++i) { 
            console.log(|wgt_txt|)
            console.log(elements[i].innerText)
            if (elements[i].innerText.includes(|wgt_txt|)) 
                elements[i].style.color = ' """ + wch_colour + """ '; 
        } 
    </script>"""

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)