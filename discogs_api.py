import discogs_client

class DiscogsApi:
  def __init__(self, user_token):
    self.connection = discogs_client.Client("streamcogs/0.1", user_token = user_token)

  def releases_by_artist(self):
    by_artist = {}

    for item in self.__releases():
      release = item.release
      artist_name = release.artists[0].name
      if artist_name not in by_artist.keys(): by_artist[artist_name] = []
      by_artist[artist_name].append(release.title)

    return by_artist

  def __releases(self):
    return self.connection.identity().collection_folders[0].releases

