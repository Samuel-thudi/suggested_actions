#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    #APP_ID = os.environ.get("MicrosoftAppId", "69033c7d-aa4d-47bc-91c6-6f194f2c100d")
    APP_ID = os.environ.get("MicrosoftAppId", "360bcbc8-339f-49d9-8da4-be9f8e345292")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "TSM8Q~_zkHcNtaRwicuYKo3lWqFulXyonC2GRbty")
