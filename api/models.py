from django.db import models

# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=100)
    Complete = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.Title

