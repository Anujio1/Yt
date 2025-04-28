from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/playlist/{playlistId}")
def get_playlist(
  playlistId: str,
  limit: int | None = 100,
  related: bool = False,
  suggestions_limit: int = 0
):
  ytmusic = YTMusic()
  results = ytmusic.get_playlist(
    playlistId,
    limit=limit,
    related=related,
    suggestions_limit=suggestions_limit
  )

  if not results:
    raise HTTPException(status_code=404, detail="Playlist not found")

  return {
    "message": "OK",
    "result": results
  }

@router.post("/playlist")
async def create_playlist(
  title: str,
  description: str,
  privacy_status: str = 'PRIVATE',
  video_ids: list | None = None,
  source_playlist: str | None = None
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.create_playlist(
      title,
      description,
      privacy_status=privacy_status,
      video_ids=video_ids,
      source_playlist=source_playlist
    )

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.patch("/playlist")
async def edit_playlist(
  playlistId: str,
  title: str | None = None,
  description: str | None = None,
  privacyStatus: str | None = None,
  moveItem: str | tuple[str, str] | None = None,
  addPlaylistId: str | None = None,
  addToTop: bool | None = None
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.edit_playlist(
      playlistId,
      title=title,
      description=description,
      privacyStatus=privacyStatus,
      moveItem=moveItem,
      addPlaylistId=addPlaylistId,
      addToTop=addToTop
    )

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.delete("/playlist/{playlistId}")
async def delete_playlist(
  playlistId: str
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.delete_playlist(playlistId)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.post("/playlist_items")
async def add_playlist_items(
  playlistId: str,
  videoIds: list[str] | None = None,
  source_playlist: str | None = None,
  duplicates: bool = False
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.add_playlist_items(
      playlistId,
      videoIds=videoIds,
      source_playlist=source_playlist,
      duplicates=duplicates
    )

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.delete("/playlist_items/{playlistId}")
async def remove_playlist_items(
  playlistId: str,
  videos: list[dict]
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.remove_playlist_items(playlistId, videos)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))