import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")

# читаем конфиг из settings.py, начинающиеся с CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

# автопоиск задач
app.autodiscover_tasks()
