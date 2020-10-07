FROM python:3-alpine

COPY . /teams_app

WORKDIR /teams_app

RUN  pip install -r requirments.txt


ENTRYPOINT ["python", "teams.py"]
