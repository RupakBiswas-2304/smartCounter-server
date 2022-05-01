FROM python:3.8-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/
RUN cd /app 
RUN ls | cat
# RUN source venv/bin/activate
RUN pip install -r requirment.txt

EXPOSE 8000
RUN python3 /app/server/manage.py migrate
CMD ["python3", "/app/server/manage.py", "runserver", "0.0.0.0:8000"]