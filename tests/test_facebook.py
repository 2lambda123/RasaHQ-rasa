import logging
from typing import Dict
from unittest.mock import patch, MagicMock

import pytest
from _pytest.monkeypatch import MonkeyPatch
from aiohttp import ClientTimeout
from aioresponses import aioresponses
from sanic import Sanic

import rasa.core.run
from rasa.core import utils
from rasa.core.channels import RasaChatInput, console
from rasa.core.channels.channel import UserMessage
from rasa.core.channels.rasa_chat import (
    JWT_USERNAME_KEY,
    CONVERSATION_ID_KEY,
    INTERACTIVE_LEARNING_PERMISSION,
)
from rasa.core.channels.telegram import TelegramOutput
from rasa.utils.endpoints import EndpointConfig
from tests.core import utilities

# this is needed so that the tests included as code examples look better
from tests.utilities import json_of_latest_request, latest_request

logger = logging.getLogger(__name__)

# USED FOR DOCS - don't rename without changing in the docs
def test_facebook_channel():
    # START DOC INCLUDE
    from rasa.core.channels.facebook import FacebookInput

    input_channel = FacebookInput(
        fb_verify="YOUR_FB_VERIFY",
        # you need tell facebook this token, to confirm your URL
        fb_secret="YOUR_FB_SECRET",  # your app secret
        fb_access_token="YOUR_FB_PAGE_ACCESS_TOKEN"
        # token for the page you subscribed to
    )

    s = rasa.core.run.configure_app([input_channel], port=5004)
    # END DOC INCLUDE
    # the above marker marks the end of the code snipped included
    # in the docs
    routes_list = utils.list_routes(s)

    assert routes_list["fb_webhook.health"].startswith("/webhooks/facebook")
    assert routes_list["fb_webhook.webhook"].startswith("/webhooks/facebook/webhook")


def test_facebook_send_custon_json_list():
    json_with_list = [["example text"]]
    json_with_list_else = [{"id": "example text"}]
    assert json_with_list.pop().pop() == "example text"
    assert json_with_list_else.pop().pop("id", None) == "example text"


def test_facebook_send_custon_json():
    json_without_list = {"sender": {"id": "example text"}}
    assert json_without_list.pop("sender", {}).pop("id", None) == "example text"
