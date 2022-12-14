'''
    app.py
    Adapted from app.py by Jeff Ondich
    Authors: Carl Zhang and Alex Falk

'''
import flask
import argparse
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/') 
def home():
    return flask.render_template('home.html')

@app.route('/bios/<int:movie_id>')
def bios(movie_id):
    return flask.render_template('bios.html')

@app.route('/api/help')
def help():
    return flask.render_template('help.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A movie application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)