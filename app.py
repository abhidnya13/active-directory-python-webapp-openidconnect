from flask import Flask
from flask import Response
from adal import AuthenticationContext
import urllib.parse
import flask
import logging
import uuid
import requests
import config

#call this function to turn on logging
def turn_on_logging():
    logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

SESSION = requests.Session()
PORT = 5000 # A flask app by default runs on PORT 5000
AUTHORITY_URL =  config.AUTHORITY_HOST_URL + '/' + config.TENANT
REDIRECT_URI = 'http://localhost:{}/getAToken'.format(PORT)

@app.route("/")
def main():
    login_url = 'http://localhost:{}/login'.format(PORT)
    resp = Response(status= 307)
    resp.headers['location'] = login_url
    return resp

@app.route("/login")
def login():
    auth_state = str(uuid.uuid4())
    SESSION.auth_state = auth_state

    params = urllib.parse.urlencode({'response_type': 'code',
                                     'client_id': config.CLIENT_ID,
                                     'redirect_uri': REDIRECT_URI,
                                     'state': auth_state,
                                     'resource': config.RESOURCE})
    authorization_url =AUTHORITY_URL + '/oauth2/authorize?' + params
    resp = Response(status=307)
    resp.headers['location']= authorization_url
    return resp

@app.route("/getAToken")
def main_logic():
    code = flask.request.args['code']
    state = flask.request.args['state']
    if state != SESSION.auth_state:
        raise ValueError("State does not match")
    auth_context = AuthenticationContext(AUTHORITY_URL, api_version=None)
    token_response = auth_context.acquire_token_with_authorization_code(code,REDIRECT_URI,config.RESOURCE, config.CLIENT_ID, config.CLIENT_SECRET)
    SESSION.headers.update({'Authorization': f"Bearer {token_response['accessToken']}",
                            'User-Agent': 'adal-python-sample',
                            'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            'return-client-request-id': 'true'})
    return flask.redirect('/graphcall')

@app.route('/graphcall')
def graphcall():
    endpoint = config.RESOURCE+ '/' + config.API_VERSION + '/me'
    http_headers = {'client-request-id': str(uuid.uuid4())}
    graph_data = SESSION.get(endpoint,headers = http_headers, stream=False).json()
    return flask.render_template('display_graph_info.html', graph_data = graph_data)

if __name__ == "__main__":
    app.run()