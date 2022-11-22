FROM alpine:latest
WORKDIR /time
RUN apk add python3-dev gcc htop git curl screen nano libffi-dev libc-dev
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY . . 
RUN /root/.local/bin/poetry install
RUN cat Dockerfile
CMD /root/.local/bin/poetry run python3 time/main.py
