from python:3.11.5-slim

RUN useradd -m user

WORKDIR /app

COPY *py /app/

COPY run.sh /app/

RUN chmod 777 /app -R

USER user

CMD "/app/run.sh"
