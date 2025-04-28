# py-ytmusic-api

thanks [ytmusicapi](https://github.com/sigma67/ytmusicapi) lib for ytmusic client/api and [fastapi](https://github.com/fastapi/fastapi) lib for api builder!

## API Documentation

- first, run the server by following setup steps

- visit [localhost:8000/docs](localhost:8000/docs) for API documentation. :)

## Setup

- create a virtual environment (optional)

- install python and pip

- install requirements: `pip install -r requirements.txt`

## run

- `default port: 8000`, `default host: 0.0.0.0`

- run the development server: `fastapi dev ./src/main.py`

- run the production server: `uvicorn src.main:app --host <specific-host> --port <specific-port>`

### run with gunicorn

- install gunicorn: `pip install gunicorn`

- run gunicorn: `gunicorn --bind <specific-host>:<specific-port>./src/main:app`

- or run with workers: `gunicorn -k uvicorn.workers.UvicornWorker src.main:app --bind 0.0.0.0:8000 --workers 4`

### for docker

- build the docker image: `docker build -t yt_music_api:latest .`
- run the docker container: `docker run -p 8000:8000 yt_music_api:latest`

## Usage

- API endpoints:
  - `/search/<query>`: search for a song, album, or artist.
  - `/lyrics/<videoid>`: get lyrics from video.
  - `/top_tracks?limit=<limit>`: get top tracks.
  - etc. **( More information in [localhost:8000/docs](localhost:8000/docs) )**