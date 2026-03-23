# Recipe Finder App

This is a Flask web application that allows users to search for recipes using an external API (TheMealDB).

## Features
- Search for recipes
- View ingredients and instructions
- Docker container support
- CI/CD with GitHub Actions

## How to Run

Run the following commands in the project folder:

```bash
docker build -t flaskproject6 .
docker run -p 5050:5000 flaskproject6
```

The application runs on port 5000 inside the Docker container, but is mapped to port 5050 on your local machine.

Open your browser and go to:

http://localhost:5050