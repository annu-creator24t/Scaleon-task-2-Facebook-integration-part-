from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse

from services.facebook_service import FacebookService
from models.facebook_models import FacebookPostRequest

router = APIRouter()

facebook = FacebookService()


@router.get("/login")
def facebook_login():
    return RedirectResponse(
        url=facebook.get_login_url()
    )


@router.get("/callback")
def callback(code: str):
    return facebook.exchange_code_for_token(code)


@router.get("/pages")
def pages(access_token: str = Query(...)):
    return facebook.get_pages(access_token)


@router.post("/post")
def create_post(request: FacebookPostRequest):
    return facebook.create_post(
        request.page_id,
        request.page_access_token,
        request.message
    )