from django.db import models

class Counter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100)
    web_page = models.TextField()
    count = models.PositiveIntegerField(null=True,blank=True)

    class Meta:
        ordering = ('created',)
