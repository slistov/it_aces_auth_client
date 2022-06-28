import os
from fastapi import FastAPI
from yaml import safe_load

import app.core.config
import logging

from log import setupLogging

def config_safe_load(file):
    try:
        config = safe_load("config.yaml")
    except Exception:
        logger.exception("Couldn't load config.yaml")
    return config


app = FastAPI()


#@app.post()


if os.__name__ == "__main__":
    logger = logging.getLogger(__name__)
    setupLogging()

