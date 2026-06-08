from fastapi import FastAPI

from backend.routes.analyze import router

app = FastAPI(
    title="AI Webinar Moderation API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():

    return {
        "message": "AI Webinar Moderation API Running"
    }