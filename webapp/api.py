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
    query = '''SELECT movies.movie_title, movies.release_year, images.image_link, movies.overview
               FROM movies, images 
               WHERE movies.id = %s
               AND movies.id = images.movie_id;'''
    movie_bio_string = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_id,))
        for row in cursor:
            movie_bio = {'movie_title':row[0],
                         'release_year':row[1],
                         'image_link':row[2],
                         'overview':row[3]
                        }
            movie_bio_string.append(movie_bio)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(movie_bio_string)

# Gets movie review info
@api.route('/reviews/<movie_id>')
def get_review(movie_id): 
    query = '''SELECT reviews.review_score, reviews.review_comment, reviews.users_name 
               FROM reviews, movies 
               WHERE reviews.movie_id = movies.id 
               AND movies.id = %s;'''
    review_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (movie_id,))
        for row in cursor:
            review = {'review_score':row[0],
                      'review_comment':row[1],
                      'users_name':row[2],
                    }
            review_list.append(review)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(review_list)

