from flask import Flask, make_response, request, render_template
import requests 

app = Flask(__name__)

@app.route('/')
def index():
    hi = 'hello world'

    cookieval = request.cookies.get('auth_service')
    print( f'auth_service cookie : {cookieval}' )

    URL = 'http://kubeflow-host/api/blahblah'
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    cookies = {'auth_service': cookieval}
    response = requests.get(URL, headers=headers, cookies=cookies)
 
    print( f'request to {URL}, status : {response.status_code}, val : {response.text} ' )

    return hi

if __name__ == '__main__':
    app.run(debug=True)

