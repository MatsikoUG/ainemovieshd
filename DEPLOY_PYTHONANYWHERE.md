# PythonAnywhere Deployment Guide

## Prerequisites
- A PythonAnywhere account (Sign up at https://www.pythonanywhere.com/)

## Steps to Deploy

### 1. Upload Your Code
1. Log in to PythonAnywhere
2. Go to the **Files** tab
3. Create a new directory called `AineMoviesHD`
4. Upload your project files to this directory:
   - `src/` folder (with all subfolders)
   - `requirements.txt`
   - `setup_venv.bat` (optional)

### 2. Create a Virtual Environment
1. Go to **Consoles** → Start a new **Bash console**
2. Run:
```bash
cd AineMoviesHD
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure the Web App
1. Go to the **Web** tab
2. Click **Add a new web app**
3. Select **Manual configuration** (not Flask)
4. Choose your Python version (3.9 or 3.10)

### 4. Edit WSGI Configuration
Click on the **WSGI configuration file** link and replace the content with:

```python
import sys
path = '/home/YOUR_USERNAME/AineMoviesHD'
if path not in sys.path:
    sys.path.append(path)

from src.main import app as application
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

### 5. Set Environment Variables
In the Web tab, find **Environment variables** section and add:
- `FLASK_ENV`: `production`
- `SECRET_KEY`: (generate a random string)

### 6. Configure Static Files
In the Web tab, add a static file mapping:
- URL: `/static/`
- Path: `/home/YOUR_USERNAME/AineMoviesHD/src/templates/`

### 7. Reload the App
Click the **Reload** button in the Web tab.

### 8. Access Your App
Your app will be available at: `https://YOUR_USERNAME.pythonanywhere.com/`

## Important Notes
- PythonAnywhere's free tier has limitations (no background downloads)
- For the download feature to work, you'll need a paid plan or alternative hosting
- The TMDB API key is hardcoded - consider using environment variables for security

## Alternative: Use a Different Hosting for Downloads
If you need full download functionality, consider:
1. Hosting the UI on PythonAnywhere (free)
2. Running downloads locally on your machine

Or use a VPS like DigitalOcean ($4/month) or Railway for full functionality.
