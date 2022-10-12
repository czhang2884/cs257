'''
    convert.py
    Carl Zhang, 12 Oct 2022
'''

import csv

# CREATE TABLE athletes (
#     athlete_id INTEGER,
#     fullname TEXT,
#     sex TEXT,
#     team TEXT,
#     noc TEXT,
#     sport TEXT
# );

athletes = {}
with open('athlete_events.csv') as original_data_file,\
        open('athletes.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader)
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
    heading_row = next(reader)
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

with open('athlete_events.csv') as original_data_file,\
        open('event_results.csv', 'w') as event_results_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(event_results_file)
    heading_row = next(reader)
    for row in reader:
        athlete_id = row[0]
        game_id = games[row[8]]
        event_id = events[row[13]]
        medal = row[14]
        writer.writerow([athlete_id, game_id, event_id, medal])


#  CREATE TABLE games_traits (
#      game_id INTEGER,
#      year INTEGER,
#      season TEXT,
#      city TEXT
#  );

with open('athlete_events.csv') as original_data_file,\
        open('game_traits.csv', 'w') as games_traits_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(games_traits_file)
    heading_row = next(reader)
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

nocs = {}
with open('athlete_events.csv') as original_data_file,\
        open('medal_counts.csv', 'w') as medal_counts_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(medal_counts_file)
    heading_row = next(reader)
    for row in reader:
        noc_name = row[7]
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
            elif row[14].lower() == 'silver':
                nocs[noc_name][1] += 1
            elif row[14].lower() == 'bronze':
                nocs[noc_name][2] += 1
    for key in nocs:
        writer.writerow([key, nocs[key][3], nocs[key][0], nocs[key][1], nocs[key][2]])