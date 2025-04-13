import os
from celery import Celery

# Налаштування Django для Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analytics_service.settings")

app = Celery("analytics_service")

# Використовуємо налаштування з Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматичне виявлення задач
app.autodiscover_tasks()
