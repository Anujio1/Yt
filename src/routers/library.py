from typing import Literal
from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/library_playlists")
async def get_library_playlists(
  limit: int | None = 25
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_playlists(limit)

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_songs")
async def get_library_songs(
  limit: int = 25,
  validate_responses: bool = False,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_songs(
    limit,
    validate_responses,
    order
  )

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_albums")
async def get_library_albums(
  limit: int = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_albums(
    limit,
    order
  )

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_artists")
async def get_library_artists(
  limit: int = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_artists(
    limit,
    order
  )

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_subscriptions")
async def get_library_subscriptions(
  limit: int = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_subscriptions(
    limit,
    order
  )

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_podcasts")
async def get_library_podcasts(
  limit: int = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_podcasts(
    limit,
    order
  )

  return {
    "message": "OK",
    "result": results
  }

@router.get("/library_channels")
async def get_library_channels(
  limit: int = 25,
  order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_library_channels(
    limit,
    order
  )

  return {
    "message": "OK",
    "result": results
  }

@router.get("/liked_songs")
async def get_liked_songs(
  limit: int = 100
):
  ytmusic = YTMusic()
  results = ytmusic.get_liked_songs(limit)

  return {
    "message": "OK",
    "result": results
  }

@router.get("/saved_episodes")
async def get_saved_episodes(
  limit: int = 100
):
  ytmusic = YTMusic()
  results = ytmusic.get_saved_episodes(limit)

  return {
    "message": "OK",
    "result": results
  }

@router.get("/history")
async def get_history():
  ytmusic = YTMusic()
  results = ytmusic.get_history()

  return {
    "message": "OK",
    "result": results
  }

@router.get("/account_info")
async def get_account_info():
  ytmusic = YTMusic()
  results = ytmusic.get_account_info()

  return {
    "message": "OK",
    "result": results
  }

@router.post("/history/{videoId}")
async def add_history_item(
  videoId: str
):
  try:
    ytmusic = YTMusic()
    song = ytmusic.get_song(videoId)
    results = ytmusic.add_history_item(song)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.delete("/history")
async def remove_history_items(
  feedbackTokens: list[str]
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.remove_history_items(feedbackTokens)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.post("/rate_song/{videoId}")
async def rate_song(
  videoId: str,
  rating: str = 'INDIFFERENT'
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.rate_song(videoId, rating)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.post("/rate_playlist/{playlistId}")
async def rate_playlist(
  playlistId: str,
  rating: str = 'INDIFFERENT'
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.rate_playlist(playlistId, rating)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.post("/subscribe_artists")
async def subscribe_artists(
  channelIds: list[str]
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.subscribe_artists(channelIds)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.delete("/subscribe_artists")
async def unsubscribe_artists(
  channelIds: list[str]
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.unsubscribe_artists(channelIds)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.patch("/song_library_status")
async def edit_song_library_status(
  feedbackTokens: list[str]
):
  try:
    ytmusic = YTMusic()
    results = ytmusic.edit_song_library_status(feedbackTokens)

    return {
      "message": "OK",
      "result": results
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))