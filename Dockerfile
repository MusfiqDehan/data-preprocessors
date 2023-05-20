FROM python:3.8-alpine
RUN apk add --no-cache musl-dev gcc
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "data-preprocessors/__init__.py"]
LABEL org.opencontainers.image.source https://github.com/musfiqdehan/data-preprocessors