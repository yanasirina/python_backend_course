# pull official base image
FROM python:3.8

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt ./
# --no-cache-dir
RUN pip install  -r requirements.txt

COPY . .

# CMD [ "python", "./web_app.py" ]
