#!/usr/bin/env bash
set -e

botname="finance-bot-model-latest"

source ./venv/bin/activate

# trains rasa model named learning-bot-model.tar-gz
# rasa train --fixed-model-name learning-bot-model-latest
rasa train --fixed-model-name $botname

curl -v -u ${DEPLOY_USER}:${DEPLOY_PASSWORD} --upload-file models/$botname.tar.gz https://nexus.beemo.eu/repository/raw-public/alfabot/
# curl -v -u ${DEPLOY_USER}:${DEPLOY_PASSWORD} --upload-file models/finance-bot-model-latest.tar.gz https://nexus.beemo.eu/repository/raw-public/alfabot/

#curl -v -u deploy:deploy4Nav1k1 --upload-file models/finance-bot-model-latest.tar.gz https://nexus.beemo.eu/repository/raw-public/alfabot/