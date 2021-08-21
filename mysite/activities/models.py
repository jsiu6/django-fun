from django.db import models
import datetime
from django.utils import timezone


class Activity(models.Model):
    activity_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('Time of Actvity')
    def __str__(self):
        return self.activity_text
    def is_in_past(self):
        return self.start_date <= timezone.now() - datetime.timedelta(days=1)
