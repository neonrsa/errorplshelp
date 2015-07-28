from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})