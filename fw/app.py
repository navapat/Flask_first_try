from flask import Flask, request, make_response, redirect
app = Flask(__name__)

# @app.route('/')
# def index():
#     response = make_response('<h1> this doc is response</h1>')
#     # return 'BAD request', 400
#     response.set_cookie('answer', '42')
#     return response

@app.route('/')
def index():
    return redirect('https://droidsans.com/')

@app.route('/user/<string:param>')
def home(param):
    return '<h1>Hello, {}!</h1>'.format(param)

if __name__ == '__main__':
    app.run(debug=True)