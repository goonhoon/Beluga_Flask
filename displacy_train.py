import spacy
from spacy import displacy

nlp = spacy.load("models/model-best")


text_open = open("displacytest.txt", "r", encoding="utf8")
text = text_open.read()


doc = nlp(text)
doc.spans["sentences"]
options = {"spans_key": "sentences"}

text_open.close()
colors = {"Governing Law": "#92a8d1", "Assignment": "#99c9ff", "Parties": "#d0ff00", "Term": "#bc066a", "Pricing": "#f86749", "Notices": "#468468"}


options = {"spans_key": "sentences", "compact": True, "color": "yellow", "bg": "#09a3d5"}
template = "<span class='entity' style='background: {{bg}}; color: {{color}};' title='{{title}}'>{{get_span_text(span)}}&nbsp;</span>"

displacy.serve(doc, style="span", options=options)


#with open ("data.vis.html", "w") as f:
#f.write(html)


