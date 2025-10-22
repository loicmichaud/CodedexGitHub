from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
    return song[1] > 5

def minutes_to_seconds(song):
    return song[1] * 60

def add_duration(total, song_duration):
    return total + song_duration

long = filter(longer_than_five_minutes, playlist)
seconds = map(minutes_to_seconds, playlist)
add = reduce(add_duration, seconds, 0)
print(list(long))
print(list(seconds))
print(add)