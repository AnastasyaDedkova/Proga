import unittest
from src.lab4.r_sys import *

class R_sysTestCase(unittest.TestCase):

    def setUp(self):
        self.movies_file = "movies.txt"
        self.viewing_history_file = "viewing_history.txt"

    def test_recommend_movie(self):
        system = RecommendationSystem(self.movies_file, self.viewing_history_file)

        # Assuming that Movie objects are created with IDs 1, 2, 3 for simplicity
        user_viewed_movies = [1, 2]
        recommendation = system.recommend_movie(user_viewed_movies)

        self.assertEqual(recommendation, "Дюна")

if __name__ == 'main':
    unittest.main()

