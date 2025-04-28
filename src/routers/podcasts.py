from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/channel/{channelId}")
async def get_channel(
  channelId: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_channel(channelId)

  if not results:
    raise HTTPException(status_code=404, detail="Channel not found")

  return {
    "message": "OK",
    "query": channelId,
    "result": results
  }

@router.get("/channel_episodes/{channelId}")
async def get_channel_episodes(
  channelId: str,
  params: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_channel_episodes(channelId, params)

  if not results:
    raise HTTPException(status_code=404, detail="Channel not found")

  return {
    "message": "OK",
    "query": channelId,
    "result": results
  }

@router.get("/podcast/{playlistId}")
async def get_podcast(
  playlistId: str,
  limit: int | None = 100
):
  ytmusic = YTMusic()
  results = ytmusic.get_podcast(playlistId, limit)

  if not results:
    raise HTTPException(status_code=404, detail="Podcast not found")

  return {
    "message": "OK",
    "query": playlistId,
    "result": results
  }

@router.get("/episode/{videoId}")
async def get_episode(
  videoId: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_episode(videoId)

  if not results:
    raise HTTPException(status_code=404, detail="Episode not found")

  return {
    "message": "OK",
    "query": videoId,
    "result": results
  }

@router.get("/episodes_playlist/{playlist_id}")
async def get_episodes_playlist(
  playlist_id: str = 'RDPN'
):
  ytmusic = YTMusic()
  results = ytmusic.get_episodes_playlist(playlist_id)

  if not results:
    raise HTTPException(status_code=404, detail="episodes_playlist not found")

  return {
    "message": "OK",
    "query": playlist_id,
    "result": results
  }