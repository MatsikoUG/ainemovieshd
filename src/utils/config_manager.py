import json
import os

class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.defaults = {
            'download_path': os.path.expanduser('~/Downloads'),
            'max_concurrent_downloads': 3,
            'theme': 'light',
            'auto_retry': True,
            'retry_attempts': 3,
            'search_history': []
        }
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return {**self.defaults, **json.load(f)}
        return self.defaults.copy()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get(self, key):
        return self.config.get(key, self.defaults.get(key))

    def set(self, key, value):
        self.config[key] = value
        self.save_config()