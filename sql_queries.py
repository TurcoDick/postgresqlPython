# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id serial , \
                                                                 start_time varchar NOT NULL, \
                                                                 user_id varchar, \
                                                                 level varchar, \
                                                                 song_id varchar, \
                                                                 artist_id varchar , \
                                                                 session_id varchar , \
                                                                 location varchar, \
                                                                 user_agent varchar , \
                                                                 PRIMARY KEY (songplay_id));""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id varchar , \
                                                         first_name varchar, \
                                                         last_name varchar, \
                                                         gender varchar, \
                                                         level varchar, \
                                                         PRIMARY KEY(user_id));""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar, \
                                                         song varchar NOT NULL, \
                                                         artist_id varchar, \
                                                         year int, \
                                                         duration numeric, \
                                                         PRIMARY KEY(song_id) ,\
                                                         CONSTRAINT fk_artist_id \
                                                             FOREIGN KEY(artist_id) \
                                                             REFERENCES artists(artist_id) \
                                                             ON DELETE CASCADE);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar , \
                                                             artist_name varchar NOT NULL, \
                                                             artist_location varchar, \
                                                             artist_latitude varchar, \
                                                             artist_longitude varchar, \
                                                             PRIMARY KEY(artist_id));""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(time_id serial, \
                                                        start_time varchar NOT NULL,\
                                                        hour varchar, \
                                                        day varchar, \
                                                        week varchar, \
                                                        month varchar, \
                                                        year varchar, \
                                                        weekday varchar, \
                                                        PRIMARY KEY(time_id));""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)\
                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)\
                     VALUES(%s, %s, %s, %s, %s) \
                     ON CONFLICT(user_id) DO UPDATE \
                         SET first_name = excluded.first_name, \
                             last_name = excluded.last_name, \
                             gender = excluded.gender, \
                             level = excluded.level;""")

song_table_insert = ("""INSERT INTO songs(song_id, song, artist_id, year, duration)\
                     VALUES(%s, %s, %s, %s, %s) \
                     ON CONFLICT(song_id) DO UPDATE \
                         SET song = excluded.song, \
                             artist_id = excluded.artist_id, \
                             year = excluded.year, \
                             duration = excluded.duration;""")

artist_table_insert = ("""INSERT INTO artists(artist_id, artist_name, artist_location, artist_latitude, artist_longitude)\
                       VALUES(%s, %s, %s, %s, %s) \
                       ON CONFLICT(artist_id) DO UPDATE \
                           SET artist_name = excluded.artist_name, \
                               artist_location = excluded.artist_location, \
                               artist_latitude = excluded.artist_latitude, \
                               artist_longitude = excluded.artist_longitude;""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)\
                                  VALUES(%s, %s, %s, %s, %s, %s, %s)""")


# FIND SONGS

song_select = ("""SELECT songs.artist_id, artists.artist_name
                  FROM songs JOIN artists 
                  ON songs.artist_id = artists.artist_id
                  WHERE songs.song = %s 
                  AND artists.artist_name = %s 
                  AND songs.duration = %s;""")

# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]