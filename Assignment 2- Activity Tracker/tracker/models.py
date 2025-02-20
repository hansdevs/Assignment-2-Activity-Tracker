from django.db import models
from datetime import timedelta

class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def time_spent(self):
        """
        Sums all the durations for this activity's time logs.
        """
        delta = timedelta()
        for timelog in self.timelog_set.all():
            if timelog.end_time and timelog.start_time:
                delta += (timelog.end_time - timelog.start_time)
        return str(delta)

class TimeLog(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"TimeLog for {self.activity.name} from {self.start_time} to {self.end_time}"
