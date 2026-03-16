# GitHub Setup Guide

## Prerequisites
- Git installed on your machine
- GitHub account

## Steps to Push to GitHub

### 1. Create a New Repository
1. Go to https://github.com/new
2. Repository name: `aine-movies-hd`
3. Choose Public or Private
4. Click "Create repository"

### 2. Initialize Git and Push Code
Run these commands in your project folder:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit - Aine Movies HD"

# Add GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/aine-movies-hd.git

# Push to GitHub
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Connect to Heroku from GitHub (Recommended)

### 1. Push code to GitHub (done above)

### 2. Connect Heroku to GitHub
1. Go to your Heroku dashboard
2. Select your app
3. Go to **Deploy** tab
4. Click **Connect to GitHub**
5. Search for your repository
6. Click **Connect**

### 3. Enable Automatic Deploys
1. In the same Deploy tab
2. Choose a branch to deploy (main)
3. Click **Enable Automatic Deploys**

Now every push to GitHub will automatically deploy to Heroku!

## GitHub Desktop Alternative
1. Download GitHub Desktop from https://desktop.github.com/
2. Add your local repository
3. Click "Publish repository"
4. Done!

## Useful Git Commands
```bash
# Check status
git status

# View changes
git diff

# Add specific file
git add filename.py

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push

# Pull latest changes
git pull
```

## .gitignore
The project already has a .gitignore that excludes:
- venv/ (virtual environment)
- __pycache__/ (Python cache)
- *.pyc (compiled Python)
- *.log (log files)
- config.json (personal config)
- app.log (application logs)
