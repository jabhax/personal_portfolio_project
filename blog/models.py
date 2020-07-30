from django.db import models


class Blog(models.Model):
    subject = models.CharField(max_length=255)
    timestamp = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.subject
