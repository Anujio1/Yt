from typing import Literal
from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/library_upload_songs/{videoId}")
async def get_library_upload_songs(
  limit: int | None = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_upload_songs(
    limit,
    order=order
  )

  if not results:
    raise HTTPException(status_code=404, detail="library_upload_songs not found")

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_upload_artists/{videoId}")
async def get_library_upload_artists(
  limit: int | None = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_upload_artists(
    limit,
    order=order
  )

  if not results:
    raise HTTPException(status_code=404, detail="library_upload_artists not found")

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_upload_albums/{videoId}")
async def get_library_upload_albums(
  limit: int | None = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_upload_albums(
    limit,
    order=order
  )

  if not results:
    raise HTTPException(status_code=404, detail="library_upload_albums not found")

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_upload_artist/{browseId}")
async def get_library_upload_artist(
  browseId: str,
  limit: int = 25
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_upload_artist(
    browseId,
    limit
  )

  if not results:
    raise HTTPException(status_code=404, detail="library_upload_artist not found")

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_upload_album/{browseId}")
async def get_library_upload_album(
  browseId: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_upload_album(browseId)

  if not results:
    raise HTTPException(status_code=404, detail="library_upload_album not found")

  return {
    "message": "OK",
    "result": results
  }

@router.post("/upload_song/{filepath}")
async def upload_song(
  filepath: str
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.upload_song(filepath)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.delete("/upload_entity/{entityId}")
async def delete_upload_entity(
  entityId: str
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.delete_upload_entity(entityId)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))