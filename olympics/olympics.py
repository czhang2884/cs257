'''
    olympics.py
    Carl Zhang, 20 October 2022
    CS 257 Software Design class, Fall 2022.
'''

import sys
import psycopg2
import config

def get_connection():
    ''' Returns a database connection object with which you can create cursors,
        issue SQL queries, etc. This function is extremely aggressive about
        failed connections--it just prints an error message and kills the whole
        program. Sometimes that's the right choice, but it depends on your
        error-handling needs. '''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()


#if system inputted arguments too little
if len(sys.argv) < 2:
    sys.exit('wrong number of arguments, check help by typing "python3 olympics.py -help"')
else:
    subcommand = sys.argv[1]

if subcommand == 'noc_aths':

    try:
        search = sys.argv[2]
        print(search)
    except:
        sys.exit('specified noc of interest must be included, check help by typing "python3 olympics.py -help"')

    athletes = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''SELECT DISTINCT athletes.fullname FROM athletes WHERE athletes.noc = %s ORDER BY athletes.fullname'''
        cursor.execute(query, (search,))
        for row in cursor:
            fullname = row[0]
            athletes.append(fullname)
    
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()

    for athlete in athletes:
        print(athlete)
    print()

elif subcommand == 'game_num_gmedls':
    nocs = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = 'SELECT DISTINCT medal_count.noc_name, medal_count.gold FROM medal_count ORDER BY medal_count.gold DESC'
        cursor.execute(query)
        for row in cursor:
            noc = row[0]
            num_golds = row[1]
            nocs.append(f'{noc} {num_golds}')  
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()

    for noc in nocs:
        print(noc)
    print()

elif subcommand == 'game_city':

    try:
        search = sys.argv[2]
    except:
        sys.exit('specified game must be included, check help by typing "python3 olympics.py -help"')

    games = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = 'SELECT DISTINCT games.game, games_traits.city FROM games, games_traits WHERE games.id = games_traits.game_id AND games.game ILIKE %s'
        cursor.execute(query, (search,))
        for row in cursor:
            game = row[0]
            city = row[1]
            games.append(f'{game} {city}')
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    try:
        print(games[0])
    except Exception as e:
        sys.exit('not a valid year or season')

#help subcommandx
elif subcommand == '-h' or subcommand == '--help':
    with open('usage.txt', 'r') as f:
        print(f.read())
else:
    print('Uh-oh, check help by typing "python3 olympics.py --help"')
