'''
    api.py
    Adapted from api.py by Jeff Ondich
    Authors: Carl Zhang and Alex Falk
    20 Nov 2022

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
    print("HELLLLLLLLLOOOO1")
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
        print("length:" + str(len(movie_list)))
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    print("HELLLLLLLLLOOOO2")

    return json.dumps(movie_list)

# Get movie info for a specific movie
@api.route('/movie_bio/<movie_id>')
def get_movie_bio_info(movie_id):
    print("HELLLLLLLLLOOOO3")
    query = '''SELECT movies.movie_title, movies.release_year, images.image_link, movies.overview, movies.mubi_url, movies.title_lang, movies.orig_lang, movies.runtime, movies.adult, profit.budget, profit.revenue, movies.director_id, movies.genre
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
                         'revenue':int(row[10]),
                         'director_id':row[11],
                         'genre':eval(row[12])
                        }
            movie_bio_string.append(movie_bio)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    print("HELLLLLLLLLOOOO4")

    return json.dumps(movie_bio_string)

# Get director given ID
@api.route('directors/<int:director_id>')
def get_director(director_id):
    print("HELLLLLLLLLOOOO5")
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
        print(director_array)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    print("HELLLLLLLLLOOOO6")    
    
    return json.dumps(director_array)

@api.route('/movies/<movie_string>/<int:start_year>/<int:end_year>/<genres>/<int:page>')
def get_movies_filters(movie_string, start_year, end_year, genres, page):
    print("HELLLLLLLLLOOOO7")
    # QUERY WILL INCLUDE MORE DATA (average_reviews, genres?)
    offset = page * 50
    query = '''SELECT movies.id, movies.movie_title, movies.release_year, images.image_link, movies.overview, movies.genre
               FROM movies, images
               WHERE movies.movie_title ILIKE CONCAT('%%', %s, '%%') 
               AND movies.genre ILIKE CONCAT('%%', %s, '%%') 
               AND movies.release_year >= %s
               AND movies.release_year <= %s
               AND movies.id = images.movie_id
               ORDER BY movies.popularity DESC
               OFFSET %s;'''
    movie_list = []
    print(type(movie_string))
    print(type(start_year))
    print(type(end_year))
    print(type(genres))
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_string, genres, start_year, end_year, offset))
        for row in cursor:
            movie = {'id':int(row[0]),
                      'movie_title':row[1],
                      'release_year':row[2],
                      'image_link':row[3],
                      'overview':row[4],
                      'genres':row[5]
                    }
            movie_list.append(movie)
        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)
    
    print("HELLLLLLLLLOOOO8")

    return json.dumps(movie_list)

