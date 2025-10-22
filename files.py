liked_songs = {
  'Last Song': 'StarrySky',
  'Squeezie': 'StarrySky',
  'Maliki': 'StarrySky'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as f:
        f.write("Liked Songs:\n")
        for song, artist in liked_songs.items():
            f.write(f'{song} by {artist}\n')

write_liked_songs_to_file(liked_songs, 'liked_songs.txt')