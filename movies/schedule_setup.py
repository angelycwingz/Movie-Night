from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask


def schedule_setup():
    min_schedule, created = IntervalSchedule.objects.get_or_create(period=IntervalSchedule.MINUTES,every=1)
    
    pt = PeriodicTask.objects.create(name="Movie notification",interval=min_schedule,task="movies.tasks.notify_of_starting_soon")