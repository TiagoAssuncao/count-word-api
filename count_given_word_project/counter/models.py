from django.db import models
import urllib.request

class Counter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100)
    web_page = models.TextField()
    count = models.PositiveIntegerField(null=True,blank=True)

    class Meta:
        ordering = ('created',)

    def get_web_page(self):
        response = urllib.request.urlopen(self.web_page)
        content_page = response.read()
        return str(content_page)

    def count_words(self, content_page):
        word_list = content_page.split()
        word_frequence = 0

        for word in word_list:
            if self.word in word:
                word_frequence += 1

        self.count = word_frequence
        self.save()

