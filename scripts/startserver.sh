#!/bin/bash
clear && \
PYTHONPATH=. FLASK_DEBUG=1 ENV_NAME=development python ./app/main.py