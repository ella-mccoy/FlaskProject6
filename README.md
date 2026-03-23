# Recipe Finder App

This is a Flask web application that allows users to search for recipes using an external API (TheMealDB).

## Features
- Search for recipes
- View ingredients and instructions
- Docker container support
- CI/CD with GitHub Actions

## How to Run

docker build -t flaskproject6 .
docker run -p 5050:5000 flaskproject6

Then open:

http://localhost:5050