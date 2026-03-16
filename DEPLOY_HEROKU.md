# Heroku Deployment Guide

## Prerequisites
- Heroku account (Sign up at https://heroku.com/)
- Git installed
- Heroku CLI installed

## Steps to Deploy

### 1. Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### 2. Login to Heroku
```bash
heroku login
```

### 3. Create a New Heroku App
```bash
heroku create aine-movies-hd
```
(Replace `aine-movies-hd` with your preferred app name)

### 4. Add Required Buildpacks
```bash
heroku buildpacks:add heroku/python
```

### 5. Push to Heroku
```bash
git init
git add .
git commit -m "Initial commit"
heroku git:remote -a aine-movies-hd
git push heroku main
```

### 6. Scale the Web Dyno
```bash
heroku ps:scale web=1
```

### 7. Open Your App
```bash
heroku open
```

Your app will be live at: `https://aine-movies-hd.herokuapp.com/`

## Important Notes

### Free Tier Limitations
- Dynos sleep after 30 minutes of inactivity
- 550 hours of free dyno hours per month
- No background jobs (downloads won't work in background)
- App sleeps and needs to wake up

### For Full Functionality
Heroku's free tier has limitations. For production with downloads:
- Upgrade to Heroku Hobby ($7/month) for persistent dynos
- Use Heroku Postgres for data storage
- Consider using external services for downloads

## Troubleshooting

### Check Logs
```bash
heroku logs --tail
```

### Common Issues
1. **Build failed**: Check that all dependencies are in requirements.txt
2. **Application error**: Check logs for Python errors
3. **Static files not loading**: Flask needs configuration for production

## Alternative: Use GitHub Integration
1. Push code to GitHub
2. Connect Heroku to your GitHub repository
3. Enable automatic deployments from main branch
