FROM python:3.11.6
WORKDIR /app
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x docker-entrypoint.sh
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["/app/docker-entrypoint.sh"]
