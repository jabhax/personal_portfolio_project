from django.db import models


class Project(models.Model):
    FRONTEND = 'Frontend'
    BACKEND = 'Backend'
    FULLSTACK = 'Fullstack'
    OTHER = 'Other'
    CATEGORY_CHOICES = ( 
        (FRONTEND, 'FE'),
        (BACKEND,'BE'),
        (FULLSTACK, 'FS'),
        (OTHER, 'OT'),
    )   

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, default=OTHER)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
