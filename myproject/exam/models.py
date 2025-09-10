from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveSmallIntegerField()  # 1 to 5
    comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
