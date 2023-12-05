#!/usr/bin/env bash

set -eu

unzip csg5-chatacademico-deployment.zip
cd csg5-chatacademico-deployment
touch .env
sudo docker-compose up