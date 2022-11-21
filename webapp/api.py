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
@api.route('/movies/<movie_string>/<int:page>')
def get_movies(movie_string, page):
    # QUERY WILL INCLUDE MORE DATA (average_reviews, genres?)
    offset = page * 50
    query = '''SELECT movies.id, movies.movie_title, movies.release_year, images.image_link, movies.overview 
               FROM movies, images 
               WHERE movies.movie_title ILIKE CONCAT('%%', %s, '%%') 
               AND movies.id = images.movie_id 
               ORDER BY movies.popularity DESC
               OFFSET %s;'''
    movie_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_string, offset))
        for row in cursor:
            movie = {'id':int(row[0]),
                      'movie_title':row[1],
                      'release_year':row[2],
                      'image_link':row[3],
                      'overview':row[4]
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

# Get movie info for a specific movie (for popup from results page and movie bios)
# THIS HAS NOT BEEN TESTED
@api.route('/movie_bio/<movie_id>')
def get_movie_bio_info(movie_id):
    # genre, average_reviews
    query = '''SELECT movies.movie_title, movies.release_year, images.image_link, movies.overview, movies.mubi_url, movies.title_lang, movies.orig_lang, movies.runtime, movies.adult, profit.budget, profit.revenue, movies.director_id
               FROM movies, images, profit 
               WHERE movies.id = %s
               AND movies.id = images.movie_id
               AND movies.id = profit.movie_id;'''
    movie_bio_string = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_id,))
        for row in cursor:
            movie_bio = {'movie_title':row[0],
                         'release_year':row[1],
                         'image_link':row[2],
                         'overview':row[3],
                         'mubi_url':row[4],
                         'title_lang':row[5],
                         'orig_lang':row[6],
                         'runtime':row[7],
                         'adult':row[8],
                         'budget':int(row[9]),
                         'revenue':int(row[10])
                        }
            movie_bio_string.append(movie_bio)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(movie_bio_string)

@api.route('directors/<int:director_id>')
def get_director(director_id):
    query = '''SELECT directors.name, directors.director_url
               FROM directors
               WHERE directors.id = %s;'''
    director_array = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (director_id,))
        for row in cursor:
            directors = {'name':row[0],
                         'director_url':row[1]
                        }
            director_array.append(directors)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    print("HOWDCQEOQWCJQCNJBEIOJCWHJEIJCQWBHWOEICRWFHJROIWHJ")
    return json.dumps(director_array)