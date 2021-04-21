from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None



  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.


  def add_song(self, title):
    current_song = self.__first_song
    song =Song(title)
    song.set_title(title)


    if current_song == None:
      self.first_song = song
      return

    while current_song.get_next_song() != None:
      current_song = current_song.get_next_song()

      current_song.set_next_song(song)



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.



  def find_song(self, title):
    song_counter = 0
    current_song = self.__first_song

    while current_song.get_title() != title:
      song_counter += 1
      current_song = current_song.get_next_song()

      if current_song == None:
        return -1

    if current_song.get_title() == title:
      return song_counter



  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 



  def remove_song(self, title):
    previous_song = self.__first_song
    current_song = self.__first_song

    if current_song.get_title() == title:
      self.__first_song = self.__first_song.get_next_song()
      return f" {current_song.get_title()} has been removed from this playlist. "

    while current_song.get_title() != title:
      previous_song = current_song
      current_song = current_song.get_next_song()

      if current_song == None:
        return f" Unable to find this song. "

      if current_song.get_title() == title:
        next_song = current_song.get_next_song()
        previous_song.set_next_song(next_song)
        return f" {current_song.get_title()} has been removed from this playlist. "





  # TODO: Create a method called length, which returns the number of songs in the playlist.



  def length(self):
    song_counter = 0
    current_song = self.__first_song

    while current_song != None:
      song_counter += 1
      current_song = current_song.get_next_song()

    return song_counter




  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.


  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3



  def print_songs(self):
    song_counter = 1
    current_song = self.__first_song

    if current_song == None:
      print(f" This playlist is empty. ")
      return None

    while current_song.get_title() != None:
      print(f"{song_counter}. {current_song.get_title()}")
      song_counter += 1
      current_song = current_song.get_next_song()

      if current_song == None:
        break