from fastapi import FastAPI

from routers.facebook import router as facebook_router

app = FastAPI(
    title="Meta Integration API",
    version="1.0.0",
    description="Facebook Integration Service"
)

app.include_router(facebook_router, prefix="/facebook", tags=["Facebook"])


@app.get("/")
def home():
    return {
        "message": "Meta Integration API Running 🚀"
    }