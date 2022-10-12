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