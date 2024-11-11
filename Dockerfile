FROM python:3.9

COPY calendar_cli.py /app/calendar_cli.py

WORKDIR /app

ENTRYPOINT ["python", "calendar_cli.py"]