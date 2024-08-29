FROM python:3.10.12

WORKDIR /app

# COPY /home/john/Documents/nfl_hof_app /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

CMD ["python3", "app.py"]