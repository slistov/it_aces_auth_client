from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from yaml import safe_load

import app.core.config as config
import logging

from log import setupLogging

from oauthlib.oauth2 import WebApplicationClient

app = FastAPI()

@app.post(config.GET_USER_TOKEN)
def get_oauth_user_token():
    return {"client_id": os.getenv('CLIENT_ID')}


if os.__name__ == "__main__":
    logger = logging.getLogger(__name__)
    setupLogging()

    client = WebApplicationClient(client_id=os.getenv('CLIENT_ID'))