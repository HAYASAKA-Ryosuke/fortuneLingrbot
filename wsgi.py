from flask import Flask,request
import urllib
import json

app = Flask(__name__)

@app.route('/')
def show_fortune():
    return ""

def escape(t):
    return t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&#39;", "'").replace("&quot;", '"')
        
@app.route('/', methods=['POST'])
def hello():
    content_body_dict = json.loads(request.data)
    content_body_status = str(content_body_dict['status']) #ok
    content_body_events = content_body_dict["events"]
    content_body_text = unicode((content_body_events[0]["message"])["text"])
    #content_body_text = str(content_body_dict['events']['event_id']) #!fortune
    if(content_body_status == 'ok' and content_body_text == '!fortune'):
        url = "http://www.iheartquotes.com/api/v1/random"
        htmldata = urllib.request.urlopen(url)
        fortune = escape(unicode(htmldata.read(),"utf-8"))
        htmldata.close()
        return fortune
    else:
        return ""
