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
