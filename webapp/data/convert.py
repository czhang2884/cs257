'''
    convert.py
    Carl Zhang, 12 Oct 2022

    The data was accessed here:
    https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
    To run this code, type python3 convert.py in terminal
    with the above dataset (athlete_events.csv) in your 
    working directory
    
    Once running this file, there will be multiple csv files
    saved to your working directory. You will use these csv's
    copying their data to the database tables listed in the
    'olympics-schema.sql'.

    Once this has been done, go to the 'queries.sql' file to
    see the next steps.
'''

import csv
import os
import json
import re

# CREATE TABLE movies (
#     id integer,
#     movie_title text,
#     release_year float,
#     genre_id integer,
#     overview text,
#     popularity integer,
#     image_id integer
# );

movie = {}
with open('movies_joined_info.csv') as original_data_file,\
        open('movies.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[1]
        title = row[0]
        genre_list = []
        genre = eval(row[11])
        for dict in genre:
            genre_list.append(dict['id'])
        print(genre_list)
        overiew = row[12]
        popularity = row[13]
        image_url = row[6]

        if movie_id not in movie:
            movie[movie_id] = title
            writer.writerow([movie_id, title, genre, overiew, popularity, image_url])

# CREATE TABLE reviews (
#     id integer,
#     movie_id integer,
#     review_score integer,
#     review_comment text,
#     users_name text
# );

review = {}
with open('mubi_ratings_data.csv') as original_data_file,\
        open('reviews.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader)
    for row in reader:
        rating_id = row[1]
        movie_id = row[0]
        score = row[3]
        comment = row[5]
        user_id = row[8]

        if rating_id not in review:
            review[rating_id] = title
            writer.writerow([rating_id, movie_id, score, comment, user_id])

# CREATE TABLE average_reviews (
#     movie_id integer,
#     average_review float
# );

avg_ratings = {}
with open('mubi_ratings_data.csv') as original_data_file,\
        open('reviews.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[0]
        score = row[3]

        if movie_id not in avg_ratings:
            avg_ratings[movie_id] = [0,0]
            avg_ratings[movie_id][0] += 1
            avg_ratings[movie_id][1] += score
        else:
            avg_ratings[movie_id][0] += 1
            avg_ratings[movie_id][1] += score

    for key in avg_ratings:
        writer.writerow([key, avg_ratings[key][1]/avg_ratings[key][0]])

# CREATE TABLE genres (
#     id serial,
#     genre text
# );

genres = {}
with open('movies_joined_info.csv') as original_data_file,\
        open('genres.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader)
    for row in reader:
        genre = eval(row[11])
        for dict in genre:
            if dict['id'] not in genres:
                genres[dict['id']] = dict['name']
    for key in genres:
        writer.writerow([key, genres[key]])
    

# CREATE TABLE images (
#     movie_id integer,
#     image_link text
# );

movie_images = {}
with open('movies_joined_info.csv') as original_data_file,\
        open('movie_images.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[0]
        movie_image_url = row[6]
        print(movie_image_url)

        if movie_id not in movie_images:
            movie_images[movie_id] = movie_image_url
    
    for key in movie_images:
        writer.writerow([key, movie_images[key]])

    

