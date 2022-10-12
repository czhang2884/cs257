'''
    queries.sql
    Carl Zhang, 12 Oct 2022

    These were the four tasks we were asked to do:

    List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. 
    These entities, by the way, are mostly equivalent to countries. But in some cases, you 
    might find that a portion of a country participated in a particular games (e.g. one guy 
    from Newfoundland in 1904) or some other oddball situation.

    List the names of all the athletes from Jamaica. If your database design allows it, sort 
    the athletes by last name.
    
    List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this 
    output that you think appropriate.
    
    List all the NOCs and the number of gold medals they have won, in decreasing order of the 
    number of gold medals.

    To do this, enter the olympics database and run the search queries below. Copying them 
    individually and entering them will get you a table output that solves the above tasks.
'''

SELECT noc_name
FROM nocs
ORDER BY noc_name;

SELECT athletes.fullname
FROM athletes
WHERE athletes.team = 'Jamaica';

SELECT DISTINCT athletes.fullname, event_results.medal, games_traits.year, events.event
FROM athletes, event_results, games_traits, events
WHERE athletes.fullname LIKE '%Gregory%'
AND athletes.fullname LIKE '%Louganis%'
AND event_results.athlete_id = athletes.athlete_id
AND event_results.game_id = games_traits.game_id
AND event_results.event_id = events.id
AND event_results.medal != 'NA'
ORDER BY games_traits.year;

SELECT medal_count.noc_name, medal_count.gold
FROM medal_count
ORDER BY medal_count.gold DESC;