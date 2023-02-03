#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("28394784"))

API_HASH = os.environ.get("9544a3ad7d8660acbae0dcf553c808e5")

BOT_TOKEN = os.environ.get("5877942822:AAHNf46r8fFlnlmzbjdjfihuSIYK4UMdOmk")

DB_URI = os.environ.get("mongodb+srv://klaus:klausbot@cluster0.w1hv2ov.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQGxRSAAxJsBsqlUoUVFZUlBzmidN2NdMgZbwjJehIkoVmig2ERXdoISaNylfjPWHqkVSZb4GYfapBFpI2nXczCDlnLiOUeq2XFvu1pxLNxgcjILLwrUnNknsu2YOq_RWuMGn8nwYvSHbrbpiXrvsILQQF4_mhckIYpM4WZs4TnnQcOIgyMa_Cu-iuCQK8js2DYMvMmgvvy5swhrW3S4NhqmFMUtPLCcHQxosafhIJjcGRyXkMKWWZ3UJA3BoADFOGXAVPESfmGysHswII9PUmMkd0QWVayJjxVuGA9hLbmxSRgB5dOlFuafZWVH9edfxtLDNCIeO5PKmTUJE5UNUDux_jRrxwAAAAB1NIUZAA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
