FROM python:3.9-slim-bookworm

# instalar ping
RUN apt-get update && apt-get install -y iputils-ping


WORKDIR /app

COPY . .

# RUN pip install -r requirements.txt

CMD ["python", "main.py"]