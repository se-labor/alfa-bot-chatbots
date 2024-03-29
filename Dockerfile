##
#  bot: general | dockerfile
#  Project: ALFA-Bot
#
#  Created by Simon on 24.12.2023
#  Copyright © 2023 Fachhochschule Münster. All rights reserved.
##

# Generate a custom rasa docker container
# Start from python 3.9 environment
FROM python:3.10.10-slim

# Versionsnummern python 3.8 und pip upgrade prüfen!
USER root
# Install Rasa version 3.2.8
RUN /usr/local/bin/python3 -m pip install pip==23.2.1
RUN python3 -m pip install rasa==3.4.6
RUN python3 -m pip install websockets==10.0

WORKDIR /app
ENV HOME=/app

COPY . .

# Set User to run, don't run as root
RUN chgrp -R 0 /app && chmod -R g=u /app && chmod o+wr /app
USER 1001

# Set entrypoint for interactive shells
ENTRYPOINT ["rasa"]

# command to run when the container is called to run
CMD ["run", "--enable-api", "--port", "5005"]