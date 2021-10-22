from django.db import models

class Algorithm(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    info = models.TextField()

    def __str__(self):  #We do that in order not to show just Algorithm: object Algorithm in shell and to show Algorithm: object title
        return self.title

    def snippet(self):
        return self.info[:100] + '...'#From 0 to 50 chars.
