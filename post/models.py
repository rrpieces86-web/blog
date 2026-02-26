from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"
    Name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, help_text="write a description about the status")

    def __str__(self):
        return f"{self.Name}"
class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
    

