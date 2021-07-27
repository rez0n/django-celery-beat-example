# django-celery-beat-example

## Create venv and install requirements
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Run Celery worker and beat
> Each in different terminal window
```
celery -A app worker -l INFO
celery -A app beat -l INFO
```
