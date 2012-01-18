from xml.sax.saxutils import unescape as xunescape

def htmlunescape(string):
    return xunescape(string, entities={'&quot;': '"'})
