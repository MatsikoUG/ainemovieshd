from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from core.downloader import AineDownloader
from utils.config_manager import ConfigManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, async_mode='eventlet')

config = ConfigManager()
downloader = AineDownloader(config, socketio)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    if query:
        results = downloader.search_movies(query)
        return jsonify(results)
    return jsonify([])

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    query = data.get('query')
    quality = data.get('quality', '720p')
    save_path = data.get('save_path', config.get('download_path'))
    if query:
        downloader.add_to_queue(query, quality, save_path)
        return jsonify({'status': 'added'})
    return jsonify({'status': 'error'})

@app.route('/popular')
def get_popular():
    movies = downloader.get_popular_movies()
    return jsonify(movies)

@app.route('/top_rated')
def get_top_rated():
    movies = downloader.get_top_rated_movies()
    return jsonify(movies)

@app.route('/upcoming')
def get_upcoming():
    movies = downloader.get_upcoming_movies()
    return jsonify(movies)

@app.route('/movie/<int:movie_id>')
def get_movie_details(movie_id):
    details = downloader.get_movie_details(movie_id)
    return jsonify(details)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    downloader.start_download_worker()
    socketio.run(app, debug=True)