from django.db import models

class User(models.Model):
    slackUsername = models.CharField(max_length=120)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.TextField()

    def _str_(self):
        return self.slackUsername

