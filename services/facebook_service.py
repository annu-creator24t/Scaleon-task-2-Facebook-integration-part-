import os
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv

load_dotenv()


class FacebookService:

    def get_login_url(self):
        params = {
            "client_id": os.getenv("FACEBOOK_APP_ID"),
            "redirect_uri": os.getenv("FACEBOOK_REDIRECT_URI"),
            "response_type": "code",
            "scope": ",".join([
                "public_profile",
                "pages_show_list",
                "pages_manage_posts",
                "pages_read_engagement",
                "pages_manage_engagement"
            ])
        }

        return (
            f"https://www.facebook.com/{os.getenv('GRAPH_API_VERSION')}/dialog/oauth?"
            + urlencode(params)
        )

    def exchange_code_for_token(self, code: str):
        url = f"https://graph.facebook.com/{os.getenv('GRAPH_API_VERSION')}/oauth/access_token"

        params = {
            "client_id": os.getenv("FACEBOOK_APP_ID"),
            "client_secret": os.getenv("FACEBOOK_APP_SECRET"),
            "redirect_uri": os.getenv("FACEBOOK_REDIRECT_URI"),
            "code": code
        }

        response = requests.get(url, params=params)
        return response.json()

    def get_pages(self, access_token: str):
        url = f"https://graph.facebook.com/{os.getenv('GRAPH_API_VERSION')}/me/accounts"

        params = {
            "access_token": access_token
        }

        response = requests.get(url, params=params)
        return response.json()

    def create_post(self, page_id: str, page_access_token: str, message: str):
        url = f"https://graph.facebook.com/{os.getenv('GRAPH_API_VERSION')}/{page_id}/feed"

        data = {
            "message": message,
            "access_token": page_access_token
        }

        response = requests.post(url, data=data)
        return response.json()

    def get_comments(self, post_id: str, page_access_token: str):
        url = f"https://graph.facebook.com/{os.getenv('GRAPH_API_VERSION')}/{post_id}/comments"

        params = {
            "access_token": page_access_token
        }

        response = requests.get(url, params=params)
        return response.json()

    def reply_to_comment(self, comment_id: str, page_access_token: str, message: str):
        url = f"https://graph.facebook.com/{os.getenv('GRAPH_API_VERSION')}/{comment_id}/comments"

        data = {
            "message": message,
            "access_token": page_access_token
        }

        response = requests.post(url, data=data)
        return response.json()