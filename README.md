# Recipe Finder App

## Description
This is a Flask web app that lets users search for recipes and save their favourites using a database.

## Features
Search recipes using TheMealDB API
View ingredients and instructions
Save recipes to database
View saved recipes
Docker support
CI/CD with GitHub Actions

## Tech Stack
Python (Flask)
Docker
Supabase (PostgreSQL)
GitHub Actions
HTML/CSS

## How to Run

docker build -t flaskproject6 .
docker run --env-file .env -p 5050:5000 flaskproject6

Open:
http://localhost:5050

## API Endpoints
/ → Main page
/health → Check if app + database is working
/status → Shows database connection + saved count
/recipes → Basic API route

## Environment Variables
Create a .env file:

DATABASE_URL=your_database_connection_string

## Notes
.env is not uploaded to GitHub for security
Each user must create their own .env file