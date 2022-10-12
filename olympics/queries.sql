/*
List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. 
    These entities, by the way, are mostly equivalent to countries. 
    But in some cases, you might find that a portion of a country participated in a particular games 
    (e.g. one guy from Newfoundland in 1904) or some other oddball situation.

List the names of all the athletes from Jamaica. If your database design allows it, sort the athletes by last name.

List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.

List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
*/

'''
    queries.sql
    Carl Zhang, 12 Oct 2022
'''

SELECT athletes.noc
FROM athletes
ORDER BY athletes.noc

SELECT athletes.fullname
FROM athletes
WHERE athletes.team = 'Jamaica'

SELECT event_results.medal, events.event, games.game, games_traits.year
FROM athletes, event_results, events, games_traits
WHERE athletes.name = 'Gregory Efthimios "Greg" Louganis'
AND event_results.event_id = events.id
AND event_results.game_id = games.id
AND event_results.game_id = games_traits.id
ORDER BY games_traits.year

SELECT medal_counts.noc_name, medal_counts.gold
FROM medal_counts
ORDER BY medal_counts.gold

/*
t
*/