from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/mood_playlists/{query}")
async def search(
  query: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_mood_playlists(query)

  return {
    "message": "OK",
    "query": query,
    "result": results
  }

@router.get("/charts/{country}")
async def get_charts(
  country: str = 'ZZ'
):
  ytmusic = YTMusic()
  results = ytmusic.get_charts(country)

  return {
    "message": "OK",
    "query": country,
    "result": results
  }