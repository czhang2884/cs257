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

# Movies to display on results page
@api.route('/movies/<movie_string>')
def get_movies(movie_string):
    # QUERY WILL INCLUDE MORE DATA (average_reviews, genres?)
    query = '''SELECT movies.id, movies.movie_title, movies.release_year, images.image_link 
               FROM movies, images 
               WHERE movies.movie_title ILIKE CONCAT('%%', %s, '%%') 
               AND movies.id = images.movie_id 
               ORDER BY movies.popularity DESC;'''
    movie_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_string,))
        for row in cursor:
            movie = {'id':int(row[0]),
                      'movie_title':row[1],
                      'release_year':row[2],
                      'image_link':row[3]
                    }
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(movie_list)

# Specific database for dropdown menu (title and picture)
# HAS NOT BEEN TESTED
@api.route('/movies_dropdown/<movie_string>')
def get_movies_dropdown(movie_string):
    query = '''SELECT movies.id movies.movie_title, movies.release_year, images.image_link 
               FROM movies, images 
               WHERE movies.movie_title ILIKE CONCAT('%%', %s, '%%') 
               AND movies.id = images.movie_id 
               ORDER BY movies.popularity LIMIT 5;'''
    movie_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_string,))
        for row in cursor:
            movie = {'id':int(row[0]),
                      'movie_title':row[1],
                      'release_year':row[2],
                      'image_link':row[3]
                    }
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(movie_list)

# Get movie review for a specific movie (for popup from results page and movie bios)
# THIS HAS NOT BEEN TESTED
@api.route('/overview/<movie_id>')
def get_overview(movie_id):
    query = '''SELECT movies.overview 
               FROM movies 
               WHERE movies.id = %s;'''
    overview_string = ''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_id,))
        for row in cursor:
            overview = {'overview':row[0]}
            overview_string.append(overview)
        if overview_string == '':
            overview_string = 'There is no overview for this movie!'
        cursor.close()
        connection.close()
        print(overview_string)
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(overview_string)

# Gets movie review info
@api.route('/reviews/<movie_id>')
def get_review(movie_id): 
    query = '''SELECT reviews.review_score reviews.review_comment reviews.users_name FROM reviews, movies WHERE reviews.movie_id = movies.id'''


