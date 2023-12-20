class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title


class RecommendationSystem:
    def __init__(self, movies_file, viewing_history_file):
        self.movies = self.load_movies(movies_file)
        self.viewing_history = self.load_viewing_history(viewing_history_file)

    def load_movies(self, movies_file):
        movies = {}
        with open(movies_file, 'r', encoding='utf-8') as file:
            for line in file:
                movie_id, title = line.strip().split(',')
                movies[int(movie_id)] = Movie(int(movie_id), title)
        return movies

    def load_viewing_history(self, viewing_history_file):
        viewing_history = []
        with open(viewing_history_file, 'r', encoding='utf-8') as file:
            for line in file:
                viewed_movies = [int(movie_id) for movie_id in line.strip().split(',')]
                viewing_history.append(viewed_movies)
        return viewing_history

    def recommend_movie(self, user_viewed_movies):
        max_views = 0
        recommended_movie = None

        for viewed_movies in self.viewing_history:
            common_movies = set(user_viewed_movies) & set(viewed_movies)
            if len(common_movies) >= len(user_viewed_movies) / 2:
                unique_movies = set(viewed_movies) - set(user_viewed_movies)
                for movie_id in unique_movies:
                    views = viewed_movies.count(movie_id)
                    if views > max_views:
                        max_views = views
                        recommended_movie = self.movies.get(movie_id)

        return recommended_movie.title if recommended_movie else "No recommendation"

if __name__ == "__main__":
    movies_file = "movies.txt"  # Путь к файлу с фильмами
    viewing_history_file = "viewing_history.txt"  # Путь к файлу с историей просмотров

    system = RecommendationSystem(movies_file, viewing_history_file)

    user_viewed_movies = input("Введите номера просмотренных фильмов пользователя через запятую: ")
    user_viewed_movies = [int(movie_id) for movie_id in user_viewed_movies.split(',')]

    recommendation = system.recommend_movie(user_viewed_movies)

    print(f"Рекомендация: {recommendation}")