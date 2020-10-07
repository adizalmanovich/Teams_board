FROM python:3-alpine

COPY . /mission_app

WORKDIR /mission_app

RUN  pip install -r requirments.txt


ENTRYPOINT ["python", "missions.py"]
