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
#     id numeric,
#     movie_title text,
#     release_year integer,
#     genre text,
#     overview text,
#     popularity numeric,
#     director_id text,
#     mubi_url text,
#     title_lang text,
#     orig_lang text,
#     runtime integer,
#     adult integer
# );

movie = {}
with open('../doc/datasets/movies_joined_info.csv') as original_data_file,\
        open('movies.csv', 'w') as movies_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(movies_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[1]
        title = row[2]
        release_year = row[3]
        genres = row[14]
        overiew = row[19]
        popularity = row[6]
        director_id = row[8]
        mubi_url = row[4]
        title_lang = row[5]
        orig_lang = row[18]
        runtime = row[26]
        if row[11]:
            adult = 1
        elif not row[11]:
            adult = 0

        if movie_id not in movie:
            movie[movie_id] = title
            writer.writerow([movie_id, title, release_year, genres, overiew, popularity, director_id, mubi_url, title_lang, orig_lang, runtime, adult])

# CREATE TABLE reviews (
#     id integer,
#     movie_id integer,
#     review_score integer,
#     review_comment text,
#     users_name text
# );

review = {}
with open('../doc/datasets/mubi_ratings_dataSHORT.csv') as original_data_file,\
        open('reviews.csv', 'w') as reviews_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(reviews_file)
    heading_row = next(reader)
    for row in reader:
        rating_id = row[2]
        movie_id = row[1]
        score = row[4]
        comment = row[6]
        user_id = row[9]
        timestamp = row[5]

        if rating_id not in review:
            review[rating_id] = movie_id
            writer.writerow([rating_id, movie_id, score, comment, user_id, timestamp])

# CREATE TABLE average_reviews (
#     movie_id integer,
#     average_review float,
#     num_reviews integer
# );

avg_ratings = {}
with open('../doc/datasets/mubi_ratings_data.csv') as original_data_file,\
        open('average_reviews', 'w') as average_reviews_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(average_reviews_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[1]
        score = row[4]

        if movie_id not in avg_ratings:
            avg_ratings[movie_id] = [0,0]
            avg_ratings[movie_id][0] += 1
            avg_ratings[movie_id][1] += score
        else:
            avg_ratings[movie_id][0] += 1
            avg_ratings[movie_id][1] += score

    for key in avg_ratings:
        writer.writerow([key, avg_ratings[key][1]/avg_ratings[key][0]])

# CREATE TABLE users (
#     user_id integer,
#     profile_pic text
# );

users = {}
with open('../doc/datasets/mubi_ratings_user_data.csv') as original_data_file,\
        open('users.csv', 'w') as users_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(users_file)
    heading_row = next(reader)
    for row in reader:
        user_id = row[1]
        pic = row[5]
        
        if user_id not in users:
            users[user_id] = 1
            writer.writerow([user_id, pic])

# CREATE TABLE profit (
#     movie_id integer,
#     budget numeric,
#     revenue numeric
# );

profit = {}
with open('../doc/datasets/movies_joined_info.csv') as original_data_file,\
        open('profit.csv', 'w') as profit_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(profit_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[1]
        budget = row[13]
        revenue = row[25]

        if movie_id not in profit:
            profit[movie_id] = 1
            writer.writerow([movie_id, budget, revenue])

# CREATE TABLE voting_average (
#     movie_id integer,
#     vote_avg float,
#     vote_count integer
# );

voting_average = {}
with open('../doc/datasets/movies_joined_info.csv') as original_data_file,\
        open('voting_average.csv', 'w') as voting_average_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(voting_average_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[1]
        vote_avg = row[32]
        vote_count = row[33]

        if movie_id not in voting_average:
            voting_average[movie_id] = 1
            writer.writerow([movie_id, vote_avg, vote_count])

# CREATE TABLE genres (
#     id serial,
#     genre text
# );

genres = {}
with open('../doc/datasets/movies_joined_info.csv') as original_data_file,\
        open('genres.csv', 'w') as genres_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(genres_file)
    heading_row = next(reader)
    for row in reader:
        genre = eval(row[14])
        for dict in genre:
            if dict['id'] not in genres:
                genres[dict['id']] = dict['name']
    for key in genres:
        writer.writerow([key, genres[key]])

# CREATE TABLE images (
#     movie_id integer,
#     image_link text
# );

images = {}
with open('../doc/datasets/movies_joined_info.csv') as original_data_file,\
        open('images.csv', 'w') as images_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(images_file)
    heading_row = next(reader)
    for row in reader:
        movie_id = row[1]
        url = row[7]

        if movie_id not in images:
            images[movie_id] = 1
            writer.writerow([movie_id, url])


# CREATE TABLE directors (
#     id serial,
#     name text,
#     director_url text
# );

directors = {}
with open('../doc/datasets/movies_joined_info.csv') as original_data_file,\
        open('directors.csv', 'w') as directors_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(directors_file)
    heading_row = next(reader)
    for row in reader:
        director_id = row[8].split(", ")
        name = row[9].split(", ")
        url = row[10].split(", ")

        for i in range(0,len(director_id)):
            if director_id[i] not in directors:
                directors[director_id[i]] = [name[i], url[i]]

    for key in directors:
        writer.writerow([key, directors[key][0], directors[key][1]])


########### OLDER VERSION ###########

# CREATE TABLE movies (
#     id integer,
#     movie_title text,
#     release_year float,
#     genre_id integer,
#     overview text,
#     popularity integer,
#     image_id integer
# );

# movie = {}
# with open('movies_joined_info.csv') as original_data_file,\
#         open('movies.csv', 'w') as athletes_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(athletes_file)
#     heading_row = next(reader)
#     for row in reader:
#         movie_id = row[1]
#         title = row[0]
#         genre_list = []
#         genre = eval(row[11])
#         for dict in genre:
#             genre_list.append(dict['id'])
#         print(genre_list)
#         overiew = row[12]
#         popularity = row[13]
#         image_url = row[6]

#         if movie_id not in movie:
#             movie[movie_id] = title
#             writer.writerow([movie_id, title, genre, overiew, popularity, image_url])

# # CREATE TABLE reviews (
# #     id integer,
# #     movie_id integer,
# #     review_score integer,
# #     review_comment text,
# #     users_name text
# # );

# review = {}
# with open('mubi_ratings_data.csv') as original_data_file,\
#         open('reviews.csv', 'w') as athletes_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(athletes_file)
#     heading_row = next(reader)
#     for row in reader:
#         rating_id = row[1]
#         movie_id = row[0]
#         score = row[3]
#         comment = row[5]
#         user_id = row[8]

#         if rating_id not in review:
#             review[rating_id] = title
#             writer.writerow([rating_id, movie_id, score, comment, user_id])

# # CREATE TABLE average_reviews (
# #     movie_id integer,
# #     average_review float
# # );

# avg_ratings = {}
# with open('mubi_ratings_data.csv') as original_data_file,\
#         open('reviews.csv', 'w') as athletes_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(athletes_file)
#     heading_row = next(reader)
#     for row in reader:
#         movie_id = row[0]
#         score = row[3]

#         if movie_id not in avg_ratings:
#             avg_ratings[movie_id] = [0,0]
#             avg_ratings[movie_id][0] += 1
#             avg_ratings[movie_id][1] += score
#         else:
#             avg_ratings[movie_id][0] += 1
#             avg_ratings[movie_id][1] += score

#     for key in avg_ratings:
#         writer.writerow([key, avg_ratings[key][1]/avg_ratings[key][0]])

# # CREATE TABLE genres (
# #     id serial,
# #     genre text
# # );

# genres = {}
# with open('movies_joined_info.csv') as original_data_file,\
#         open('genres.csv', 'w') as athletes_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(athletes_file)
#     heading_row = next(reader)
#     for row in reader:
#         genre = eval(row[11])
#         for dict in genre:
#             if dict['id'] not in genres:
#                 genres[dict['id']] = dict['name']
#     for key in genres:
#         writer.writerow([key, genres[key]])
    

# # CREATE TABLE images (
# #     movie_id integer,
# #     image_link text
# # );

# movie_images = {}
# with open('movies_joined_info.csv') as original_data_file,\
#         open('movie_images.csv', 'w') as athletes_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(athletes_file)
#     heading_row = next(reader)
#     for row in reader:
#         movie_id = row[0]
#         movie_image_url = row[6]
#         print(movie_image_url)

#         if movie_id not in movie_images:
#             movie_images[movie_id] = movie_image_url
    
#     for key in movie_images:
#         writer.writerow([key, movie_images[key]])

    

