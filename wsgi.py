from flask import Flask,request
import urllib
import json

app = Flask(__name__)


def fetch_fortune():
    url = "https://meigen.doodlenote.net/api/json.php"
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    if content and len(content) == 1:
       return f"{content[0].get('meigen')} by {content[0].get('auther')}"


@app.route('/')
def show_fortune():
    return fetch_fortune()


@app.route('/', methods=['POST'])
def hello():
    content_body_dict = json.loads(request.data)
    content_body_status = str(content_body_dict['status']) #ok
    content_body_events = content_body_dict["events"]
    content_body_text = unicode((content_body_events[0]["message"])["text"])
    #content_body_text = str(content_body_dict['events']['event_id']) #!fortune
    if(content_body_status == 'ok' and content_body_text == '!fortune'):
        return fetch_fortune()
    else:
        return ""
