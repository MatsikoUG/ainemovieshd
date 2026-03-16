# Aine Movies HD

A Netflix-style web application for discovering, streaming info, and downloading movies, powered by TMDB API and fzmovies.

## Features

- **Netflix-style Interface**: Scrollable movie rows with categories
- **Rich Movie Information**: Posters, descriptions, cast, genres from TMDB
- **Legal Streaming Integration**: Shows where to watch legally via TMDB
- **Movie Details Modal**: Comprehensive movie information with watch providers
- **Advanced Search**: Find movies with TMDB-powered results
- **Download Functionality**: Offline viewing with quality selection
- **Real-time Updates**: WebSocket-powered download progress
- **Responsive Design**: Works on all devices
- **Background Processing**: Multi-threaded downloads
- **Configuration Management**: User preferences and settings

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup
1. Download or clone the project to your local machine.
2. Run `setup_venv.bat` to create a virtual environment and install dependencies.
3. Activate the virtual environment: `venv\Scripts\activate`
4. Run the application: `python src/main.py`
5. Open your browser and go to `http://localhost:5000`

## Usage

1. **Browse Movies**: Scroll through Popular, Top Rated, and Upcoming movies on homepage
2. **Search**: Use the search bar to find specific movies
3. **View Details**: Click any movie poster to see detailed information, cast, and where to watch legally
4. **Stream**: Click "Watch Now" to see available streaming providers
5. **Download**: Click "Download" for offline viewing with quality selection
6. **Monitor**: Track download progress in the sidebar queue

## Troubleshooting

### Application won't start
- Ensure Python is installed and added to PATH.
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Make sure port 5000 is not in use.

### Downloads fail
- Check internet connection.
- Ensure sufficient disk space.
- Verify download location permissions in config.json.

### WebSocket issues
- Ensure your browser supports WebSockets.
- Check firewall settings.

## Disclaimer

This application is for educational purposes only. Users are responsible for complying with copyright laws and website terms of service. The developers are not liable for any misuse.

## License

[Add license if applicable]