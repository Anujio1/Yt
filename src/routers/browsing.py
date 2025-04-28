from typing import Literal
from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/home")
async def get_home(
  limit: int = 3
):
  ytmusic = YTMusic()
  search_results = ytmusic.get_home(limit)

  return {
    "message": "OK",
    "limit": limit,
    "result": search_results
  }

@router.get("/artist/{channelId}")
async def get_artist(
  channelId: str
):
  ytmusic = YTMusic()
  search_results = ytmusic.get_artist(channelId)

  if not search_results:
    raise HTTPException(status_code=404, detail="Artist not found")

  return {
    "message": "OK",
    "query": channelId,
    "result": search_results
  }

@router.get("/artist_videos/{channelId}")
async def get_artist_videos(
  channelId: str
):
  ytmusic = YTMusic()
  artist_results = ytmusic.get_artist(channelId)

  if not artist_results:
    raise HTTPException(status_code=404, detail="Artist not found")
  
  browseId = artist_results["videos"]["browseId"]
  videos = ytmusic.get_playlist(browseId)

  return {
    "message": "OK",
    "query": channelId,
    "result": videos
  }

@router.get("/artist_albums/{channelId}")
async def get_artist_albums(
  channelId: str,
  params: str,
  limit: int | None = 100,
  order: Literal['Recency', 'Popularity', 'Alphabetical order'] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_artist_albums(
    channelId=channelId,
    params=params,
    limit=limit,
    order=order
  )

  return {
    "message": "OK",
    "query": channelId,
    "result": results
  }

@router.get("/album/{browseId}")
async def get_album(
  browseId: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_album(browseId)

  if not results:
    raise HTTPException(status_code=404, detail="Album not found")

  return {
    "message": "OK",
    "query": browseId,
    "result": results
  }

@router.get("/album_browse_id/{audioPlaylistId}")
async def get_album_browse_id(
  audioPlaylistId: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_album_browse_id(audioPlaylistId)

  return {
    "message": "OK",
    "query": audioPlaylistId,
    "result": results
  }

@router.get("/user/{channelId}")
async def get_user(
    channelId: str
):
    ytmusic = YTMusic()
    try:
        results = ytmusic.get_user(channelId)
        if not results:
            raise HTTPException(status_code=404, detail="User not found")
    except KeyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected response structure: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )

    return {
        "message": "OK",
        "query": channelId,
        "result": results
    }

@router.get("/user_playlists/{channelId}")
async def get_user_playlists(
  channelId: str
):
  ytmusic = YTMusic()
  channel = ytmusic.get_user(channelId)
  if not channel:
    raise HTTPException(status_code=404, detail="User not found")
  params = channel["videos"]["params"]
  results = ytmusic.get_user_playlists(channelId, params)

  return {
    "message": "OK",
    "query": channelId,
    "result": results
  }

@router.get("/user_videos/{channelId}")
async def get_user_videos(
  channelId: str
):
  ytmusic = YTMusic()
  channel = ytmusic.get_user(channelId)
  if not channel:
    raise HTTPException(status_code=404, detail="User not found")
  params = channel["videos"]["params"]
  results = ytmusic.get_user_videos(channelId, params)

  return {
    "message": "OK",
    "query": channelId,
    "result": results
  }

@router.get("/song/{videoId}")
async def get_song(
  videoId: str,
  signatureTimestamp: int | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.get_song(videoId, signatureTimestamp)

  if not results:
    raise HTTPException(status_code=404, detail="Song not found")

  return {
    "message": "OK",
    "query": videoId,
    "result": results
  }

@router.get("/related/{browseId}")
async def get_related_by_browse_id(
  browseId: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_song_related(browseId)

  return {
    "message": "OK",
    "query": browseId,
    "result": results
  }

@router.get("/song_related/{songId}")
async def get_song_related_by_song_id(
  songId: str
):
  ytmusic = YTMusic()
  watch_playlist = ytmusic.get_watch_playlist(songId)
  if not watch_playlist or not watch_playlist["related"]:
    raise HTTPException(status_code=404, detail="Song not found")
  
  results = ytmusic.get_song_related(watch_playlist["related"])

  return {
    "message": "OK",
    "query": songId,
    "result": {
      "playlist": watch_playlist,
      "related": results
    }
  }

@router.get("/lyrics/{browseId}")
async def get_lyrics(
  browseId: str,
  timestamps: bool | None = False
):
  ytmusic = YTMusic()
  results = ytmusic.get_lyrics(browseId, timestamps)

  if not results:
    raise HTTPException(status_code=404, detail="Lyrics not found")

  return {
    "message": "OK",
    "query": browseId,
    "result": results
  }

@router.get("/tasteprofile")
async def get_tasteprofile():
  ytmusic = YTMusic()
  results = ytmusic.get_tasteprofile()

  return {
    "message": "OK",
    "result": results
  }

@router.post("/tasteprofile")
async def set_tasteprofile(
  artists: list[str],
  taste_profile: dict | None = None
):
  try:
    ytmusic = YTMusic()
    ytmusic.set_tasteprofile(artists, taste_profile)

    return {
      "message": "OK",
      "query": artists
    }
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))