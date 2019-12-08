from chalice import Chalice

import urllib.request


app = Chalice(app_name='lambda-ip-checker')

def get_json():
    response = urllib.request.urlopen('http://inet-ip.info/json')
    j = response.read().decode('utf-8')
    return j

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/hoge')
def hogehoge():
    return get_json()

@app.lambda_function(name='ip-checker')
def hoge2(handler, context):
    print(handler)
    print(context)
    j = get_json()
    print(j)
    return j


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
