from threading import Thread
from queue import Queue
import time
from utils.logger import Logger
from tmdbv3api import TMDb, Movie

class AineDownloader:
    def __init__(self, config, socketio):
        self.config = config
        self.socketio = socketio
        self.logger = Logger()
        self.download_queue = Queue()
        self.active_downloads = []
        self.is_running = True
        self.max_concurrent = self.config.get('max_concurrent_downloads')
        self.tmdb = TMDb()
        self.tmdb.api_key = 'eefcc515ed0980a6aa4717c8080f9ccc'
        self.movie_api = Movie()

    def search_movies(self, query):
        """Search for movies using TMDB"""
        try:
            results = self.movie_api.search(query)
            movies = []
            for r in results:
                movies.append({
                    'title': r.title,
                    'year': r.release_date[:4] if r.release_date else 'N/A',
                    'poster': f"https://image.tmdb.org/t/p/w200{r.poster_path}" if r.poster_path else '',
                    'overview': r.overview,
                    'id': r.id
                })
            self.logger.info(f"TMDB search completed for '{query}': {len(movies)} results")
            return movies
        except Exception as e:
            self.logger.error(f"TMDB search failed for '{query}': {e}")
            return []

    def add_to_queue(self, query, quality="720p", save_path=None):
        """Add a movie to download queue"""
        self.download_queue.put({
            'query': query,
            'quality': quality,
            'save_path': save_path
        })

    def start_download_worker(self):
        """Background thread for processing downloads"""
        def worker():
            while self.is_running:
                if not self.download_queue.empty() and len(self.active_downloads) < self.max_concurrent:
                    task = self.download_queue.get()
                    Thread(target=self._download_movie, args=(task,), daemon=True).start()
                time.sleep(0.5)

        Thread(target=worker, daemon=True).start()

    def get_popular_movies(self):
        """Get popular movies from TMDB"""
        try:
            movies = self.movie_api.popular()
            return self._format_movies(movies)
        except Exception as e:
            self.logger.error(f"Popular movies error: {e}")
            return []

    def get_top_rated_movies(self):
        """Get top rated movies from TMDB"""
        try:
            movies = self.movie_api.top_rated()
            return self._format_movies(movies)
        except Exception as e:
            self.logger.error(f"Top rated movies error: {e}")
            return []

    def get_upcoming_movies(self):
        """Get upcoming movies from TMDB"""
        try:
            movies = self.movie_api.upcoming()
            return self._format_movies(movies)
        except Exception as e:
            self.logger.error(f"Upcoming movies error: {e}")
            return []

    def get_movie_details(self, movie_id):
        """Get detailed movie information"""
        try:
            movie = self.movie_api.details(movie_id)
            return {
                'title': movie.title,
                'overview': movie.overview,
                'poster': f"https://image.tmdb.org/t/p/w500{movie.poster_path}" if movie.poster_path else '',
                'backdrop': f"https://image.tmdb.org/t/p/w1280{movie.backdrop_path}" if movie.backdrop_path else '',
                'release_date': movie.release_date,
                'runtime': movie.runtime,
                'genres': [g.name for g in movie.genres],
                'cast': [{'name': c.name, 'character': c.character} for c in movie.casts.cast[:5]] if movie.casts else [],
                'videos': [{'key': v.key, 'name': v.name, 'type': v.type} for v in movie.videos.results[:3]] if movie.videos else [],
                'watch_providers': movie.watch_providers.results.get('US', {}).get('flatrate', []) if movie.watch_providers else []
            }
        except Exception as e:
            self.logger.error(f"Movie details error for {movie_id}: {e}")
            return {}

    def _format_movies(self, movies):
        """Format movie list for frontend"""
        return [{
            'id': m.id,
            'title': m.title,
            'year': m.release_date[:4] if m.release_date else 'N/A',
            'poster': f"https://image.tmdb.org/t/p/w200{m.poster_path}" if m.poster_path else '',
            'overview': m.overview
        } for m in movies]

    def _download_movie(self, task):
        """Handle movie downloads - shows streaming info instead"""
        query = task['query']
        quality = task['quality']
        save_path = task['save_path']

        self.active_downloads.append(query)
        self.socketio.emit('download_started', {'name': query})

        try:
            self.logger.info(f"Download requested for {query}")
            # On web deployment, show where to stream instead of downloading
            # Users can stream legally via the watch providers shown in movie details
            self.socketio.emit('download_completed', {'name': query, 'message': 'Streaming links available in movie details'})
            self.logger.info(f"Streaming info shown for {query}")
        except Exception as e:
            self.logger.error(f"Download error for {query}: {e}")
            self.socketio.emit('download_failed', {'name': query, 'error': str(e)})
        finally:
            self.active_downloads.remove(query)