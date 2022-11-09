'''
    api.py
    Jeff Ondich, 25 April 2016
    Updated 8 November 2021

    Tiny Flask API to support the tiny books web application.
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)

@api.route('/movies/')
def get_movies():
    query = '''SELECT id, movie_title, release_year FROM movies ORDER BY '''

    sort_argument = flask.request.args.get('sort')
    if sort_argument == 'id':
        query += 'id'
    else:
        query += 'release_year'

    movie_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            movie = {'id':row[0],
                      'movie_title':row[1],
                      'release_year':row[2],
                      'genre_id':row[3],
                      'overview':row[4],
                      'popularity':row[5],
                      'image_id':row[6],
                      'review_id':row[7]
                    }
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(movie_list)

