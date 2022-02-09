from discogs_api import DiscogsApi
from dotenv import load_dotenv
import os
import unittest
import vcr

load_dotenv()

class TestDiscogsApi(unittest.TestCase):
  @vcr.use_cassette(filter_query_parameters = ["token"])
  def test_releases_by_artist(self):
    """
    Test that the return is a dict of only the user's albums grouped by artist
    """
    result = DiscogsApi(os.getenv("DISCOGS_USER_TOKEN")).releases_by_artist()
    self.assertIn("The Ugly Organ", result["Cursive"])
    self.assertNotIn("Band user does not own an album from", result.keys())

if __name__ == "__main__":
  unittest.main()
