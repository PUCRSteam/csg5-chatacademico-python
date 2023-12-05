#!/usr/bin/env bash

set -eu

cd csg5-chatacademico-deployment
touch .env
sudo docker-compose up