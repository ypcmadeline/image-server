FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /workdir
COPY . /workdir

ENTRYPOINT [ "bash" ]