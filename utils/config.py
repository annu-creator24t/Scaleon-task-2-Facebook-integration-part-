import os
from dotenv import load_dotenv

load_dotenv()

FACEBOOK_APP_ID = os.getenv("FACEBOOK_APP_ID")
FACEBOOK_APP_SECRET = os.getenv("FACEBOOK_APP_SECRET")
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")

GRAPH_API_VERSION = os.getenv("GRAPH_API_VERSION")
GRAPH_API_BASE_URL = os.getenv("GRAPH_API_BASE_URL")