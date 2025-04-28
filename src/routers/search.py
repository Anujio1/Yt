from typing import Any
from fastapi import APIRouter, HTTPException, Query
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/search")
async def search(
  query: str = Query(..., description="Search query"),
  filter: str | None = None,
  ignore_spelling: bool = False,
  limit: int = 20,
  scope: str | None = None
):
  ytmusic = YTMusic()
  search_results = ytmusic.search(
    query=query,
    filter=filter,
    ignore_spelling=ignore_spelling,
    limit=limit,
    scope=scope
  )

  if not search_results:
    raise HTTPException(status_code=404, detail="No search result found")

  return {
    "message": "OK",
    "query": query,
    "result": search_results
  }

@router.get("/search_suggestions")
async def get_search_suggestions(
  query: str = Query(..., description="Search query"),
  detailed_runs: bool = False
):
  ytmusic = YTMusic()
  search_results = ytmusic.get_search_suggestions(
    query=query,
    detailed_runs=detailed_runs
  )
  
  if not search_results:
    raise HTTPException(status_code=404, detail="No search result found")

  return {
    "message": "OK",
    "query": query,
    "result": search_results
  }

@router.delete("/search_suggestions")
async def remove_search_suggestions(
  suggestions: list[dict[str, Any]],
  indices: list[int] | None = None
):
  ytmusic = YTMusic()
  results = ytmusic.remove_search_suggestions(
    suggestions=suggestions,
    indices=indices
  )

  return {
    "message": "OK",
    "query": suggestions,
    "result": results
  }