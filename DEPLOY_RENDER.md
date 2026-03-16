# Render Deployment Guide

## Quick Deploy (Automatic)
1. Go to https://render.com and sign up with GitHub
2. Click "New +" → "Web Service"
3. Connect to your GitHub repository: `MatsikoUG/ainemovieshd`
4. Render will auto-detect the configuration

## Settings
- **Name**: aine-movies-hd
- **Environment**: Python
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn src.main:app --worker-class eventlet`

## Deploy
Click "Create Web Service" and wait for deployment.

## Access Your App
Your app will be live at: `https://aine-movies-hd.onrender.com`

## Note
Free tier services spin down after 15 minutes of inactivity. For persistent service, upgrade to a paid plan.
