from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    def __unicode__(self):
        return self.title
        
