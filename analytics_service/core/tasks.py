import json
from celery import shared_task
from .models import Event
import time
from analytics_service.celery import app


@shared_task
def process_event(event_id):
    try:
        event = Event.objects.get(id=event_id)
        json_data = event.data
        text_data = json.dumps(json_data, indent=4)
        event.processed_text = text_data
        event.save()
    except Event.DoesNotExist:
        print(f"Event with ID {event_id} not found.")
