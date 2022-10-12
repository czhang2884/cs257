'''
    convert.py
    Carl Zhang, 12 Oct 2022
'''

import csv
import sys

# Strategy:
# (1) Create a dictionary that maps athlete IDs to athlete names
#       and then save the results in athletes.csv
# (2) Create a dictionary that maps event names to event IDs
#       and then save the results in events.csv
# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
#
# NOTE: I'm doing these three things in three different passes through
# the athlete_events.csv files. This is not necessary--you can do it all
# in a single pass.


# CREATE TABLE athletes (
#     id INTEGER,
#     fullname TEXT,
#     sex TEXT,
#     team TEXT,
#     noc TEXT,
#     sport TEXT
# );

# (1) Create a dictionary that maps athlete_id -> athlete_name
#       and then save the results in athletes.csv
athletes = {}
with open('athlete_events.csv') as original_data_file,\
        open('athletes.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        fullname = row[1]
        athlete_sex = row[2]
        team = row[6]
        noc = row[7]
        sport = row[12]
        if athlete_id not in athletes:
            athletes[athlete_id] = fullname
            writer.writerow([athlete_id, fullname, athlete_sex, team, noc, sport])

#  CREATE TABLE events (
#      id SERIAL,
#      event TEXT
#  );

# (2) Create a dictionary that maps event_name -> event_id
#       and then save the results in events.csv
events = {}
with open('athlete_events.csv') as original_data_file,\
        open('events.csv', 'w') as events_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(events_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        event_name = row[13]
        if event_name not in events:
            event_id = len(events) + 1
            events[event_name] = event_id
            writer.writerow([event_id, event_name])

#  CREATE TABLE games (
#      id SERIAL,
#      game TEXT
#  );

games = {}
with open('athlete_events.csv') as original_data_file,\
        open('games.csv', 'w') as games_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(games_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        game_name = row[8]
        if game_name not in games:
            game_id = len(games) + 1
            games[game_name] = game_id
            writer.writerow([game_id, game_name])

#  CREATE TABLE event_results (
#      athlete_id INTEGER,
#      game_id INTEGER,
#      event_id INTEGER,
#      medal TEXT
#  );

# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
with open('athlete_events.csv') as original_data_file,\
        open('event_results.csv', 'w') as event_results_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(event_results_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        game_id = games[row[8]]
        event_id = events[row[13]]
        medal = row[14]

        # event_id = events[event_name] # this is guaranteed to work by section (2)
        writer.writerow([athlete_id, game_id, event_id, medal])


#  CREATE TABLE games_traits (
#      game_id INTEGER,
#      year INTEGER,
#      season TEXT,
#      city TEXT
#  );

# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
with open('athlete_events.csv') as original_data_file,\
        open('game_traits.csv', 'w') as games_traits_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(games_traits_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        game_id = games[row[8]]
        year = row[9]
        season = row[10]
        city = row[11]
        writer.writerow([game_id, year, season, city])

#  CREATE TABLE medal_count (
#      noc_id integer
#      gold integer
#      silver integer
#      bronze integer
#  );

# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
nocs = {}
with open('athlete_events.csv') as original_data_file,\
        open('medal_counts.csv', 'w') as medal_counts_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(medal_counts_file)
    heading_row = next(reader)
    for row in reader:
        if row[0] == 20:
            sys.exit()
        print(row)
        noc_name = row[7]
        print(noc_name)
        print(row[14])
        if noc_name not in nocs:
            # first index for gold
            # second index for silver
            # third index for bronze
            # fourth index for id
            noc_medals = [0,0,0,0]
            nocs[noc_name] = noc_medals
            nocs[noc_name][3] = len(nocs)
        elif noc_name in nocs:
            if row[14].lower() == 'gold':
                nocs[noc_name][0] += 1
                print(nocs[noc_name][0])
            elif row[14].lower() == 'silver':
                nocs[noc_name][1] += 1
                print(nocs[noc_name][1])
            elif row[14].lower() == 'bronze':
                nocs[noc_name][2] += 1
                print(nocs[noc_name][2])
    for key in nocs:
        writer.writerow([key, nocs[key][3], nocs[key][0], nocs[key][1], nocs[key][2]])