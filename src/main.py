from fastapi import FastAPI
from fastapi.openapi.docs import (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
from src.routers import search, browsing, explore, watch, library, playlists, podcasts, uploads

app = FastAPI(docs_url=None, redoc_url=None, title="YT Music API")
app.include_router(search.router)
app.include_router(browsing.router)
app.include_router(explore.router)
app.include_router(watch.router)
app.include_router(library.router)
app.include_router(playlists.router)
app.include_router(podcasts.router)
app.include_router(uploads.router)

@app.get("/")
def root():
  return {"message": "Hello YT Music API!"}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
  )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
  )

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0")