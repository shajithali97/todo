from django.db import models

class Task(models.Model):
    task_name=models.CharField(max_length=200)
    task_priority=models.IntegerField()
    task_date=models.DateField()

    def __str__(self) -> str:
        return self.task_name
