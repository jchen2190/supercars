from django.db import models
from django.urls import reverse

class Post(models.Model):
    make = models.CharField(max_length = 100, blank=False, default="")
    model = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000, blank=True, default="")
    max_speed = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.make} {self.model}"
    
    def get_absolute_url(self):
        return reverse("posts-detail", kwargs={"pk":self.id})