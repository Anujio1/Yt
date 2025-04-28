from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/mood_categories")
def get_mood_categories():
  ytmusic = YTMusic()
  results = ytmusic.get_mood_categories()

  return {
    "message": "OK",
    "result": results
  }

@router.get("/watch/{videoId}")
async def get_watch_playlist(
  videoId: str,
  playlistId: str | None = None,
  limit: int = 25,
  radio: bool = False,
  shuffle: bool = False
):
  ytmusic = YTMusic()
  results = ytmusic.get_watch_playlist(
    videoId=videoId,
    playlistId=playlistId,
    limit=limit,
    radio=radio,
    shuffle=shuffle
  )

  if not results:
    raise HTTPException(status_code=404, detail="Video not found")

  return {
    "message": "OK",
    "query": videoId,
    "result": results
  }