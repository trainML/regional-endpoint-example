#!/bin/bash

uvicorn api:app --host 0.0.0.0 --port 8080 &
envsubst '${TRAINML_MODEL_PATH} ${PORT}' < $TRAINML_MODEL_PATH/nginx.template > /etc/nginx/nginx.conf
nginx