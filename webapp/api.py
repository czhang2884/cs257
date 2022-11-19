'''
    api.py
    Adapted from api.py by Jeff Ondich
    Authors: Carl Zhang and Alex Falk
    9 Nov 2022

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

@api.route('/movies/<movie_string>')
def get_movies(movie_string):
    query = '''SELECT movies.id, movies.movie_title, movies.release_year FROM movies WHERE movie_title ILIKE CONCAT('%%', %s, '%%'); '''
    movie_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_string,))
        for row in cursor:
            movie = {'id':int(row[0]),
                      'movie_title':row[1],
                      'release_year':row[2],
                    }
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(movie_list)

# Specific database for dropdown menu (title and picture)
@api.route('/movies_dropdown/<movie_string>')
def get_movies_dropdown(movie_string):
    query = '''SELECT movies.movie_title, images.image_link, movies.release_year FROM movies, images WHERE movies.movie_title ILIKE CONCAT('%%', %s, '%%') AND movies.id = images.movie_id ORDER BY movies.popularity LIMIT 5;'''
    movie_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_string,))
        for row in cursor:
            movie = {'movie_title':row[0],
                      'image_link':row[1],
                      'release_year':row[2]
                    }
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(movie_list)

# @api.route('/movies/<movie_id>')
# def get_movie_info(movie_id):
#    return
