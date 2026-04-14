# Recipe Finder
A web application that allows users to search for recipes, save their favourites, and view them anytime.
The project combines a live web app, database integration, and deployment.
## Live Demo
https://flaskproject6.onrender.com
## GitHub URL Acess
https://github.com/ella-mccoy/FlaskProject6
## Features
Search for recipes
Save recipes to a database
View saved recipes anytime
## Technologies Used
Python (Flask)
PostgreSQL (Supabase)
Docker
Render (deployment)
## How to Use
1. Open the live link above  
2. Search for a recipe  
3. Click "Save Recipe"  
4. View it in the "Saved Recipes" section  
## Notes
The application is fully deployed on Render  
The database is hosted on Supabase  
No setup is required — simply use the live link
## Release
Version 1.0.0 was published on GitHub after deployment.
## Team Members
Ella McCoy 124307196  
Maggie O'Brien 124307173  
Seán Harrington 124416512  
Mia Cronin 124339831  
## Environment Variables
Create a `.env` file based on `.env.example`:

DATABASE_URL=your_supabase_connection_string

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Homepage, search and view saved recipes |
| /save | POST | Save a recipe to the database |
| /health | GET | Check database connectivity |
| /status | GET | View runtime info and DB connection state |

## CI/CD
GitHub Actions runs on every push to main:
- Lints code with ruff
- Runs tests with pytest
- Builds Docker image
- Publishes image to GHCR
- Render auto-deploys on every push to main
Final version submitted for assignment. 
