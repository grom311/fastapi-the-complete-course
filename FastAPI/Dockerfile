FROM python:3.10.3-alpine
# RUN mkdir /app
# WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers make python3-dev openssl-dev libffi-dev 
COPY requirements.txt .
# RUN pip install -U setuptools pip
# docker overwrites the src location for editable packages so we pass in a --src path that doesnt get blatted
# https://stackoverflow.com/questions/29905909/pip-install-e-packages-dont-appear-in-docker
RUN pip install -r requirements.txt

COPY . .
# CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80"]
