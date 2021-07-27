from celery import shared_task
from app.celery import app as celery_app
from celery.schedules import crontab
from datetime import timedelta



@shared_task
def test_task():
    print('HELLO WORLD')


celery_app.conf.beat_schedule = {
    'test_task': {
        'task': 'app.tasks.test_task',
        'schedule': timedelta(seconds=30),
        'options': {
                'expires': 300,
        },
    },
}