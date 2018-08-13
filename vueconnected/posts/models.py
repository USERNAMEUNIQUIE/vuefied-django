from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    objects = models.Manager()



    def __str__(self):
        return self.title

    def article(self):
        return self.body[:100] + '.........'