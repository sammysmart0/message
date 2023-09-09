from django.db import models

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.TextField()
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title