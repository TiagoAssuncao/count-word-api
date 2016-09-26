from django.db import models

class Counter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100, blank=True)
    web_page = models.TextField()
    count = models.PositiveIntegerField()

    class Meta:
        ordering = ('created',)
