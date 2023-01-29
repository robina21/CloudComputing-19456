FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install uszipcode
# RUN pip install -r requirements.txt

EXPOSE 8000


CMD ["python", "service1.py"]
