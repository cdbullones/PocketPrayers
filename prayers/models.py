from django.db import models

class Prayer(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
