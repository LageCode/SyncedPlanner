from django.db import models

# Create your models here.


class Event(models.Model):
    label = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def get_label(self):
        return self.label

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
