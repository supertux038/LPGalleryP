import os

from celery import Celery
from celery.schedules import crontab

from LPGallery import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LPGallery.settings')

app = Celery('security', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send_mail_every_day': {
        'task': 'security.tasks.send_users_amount',
        'schedule': crontab(hour=9)
    }
}

app.autodiscover_tasks()