from wikipedia import wikipedia
from Reaction import react

def search(src_itm):
    try:
        page = wikipedia.page(src_itm)
        text = wikipedia.summary(src_itm, sentences=1)
        return text,page.url
    except:
        return  "Sorry i didn't understand your question",react.sad_react()