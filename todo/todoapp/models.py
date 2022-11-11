from django.db import models

class Mytodo(models.Model):
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.task
