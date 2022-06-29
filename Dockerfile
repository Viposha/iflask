FROM python:3.8-slim-buster
WORKDIR /iflask
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "iflask.py"]

