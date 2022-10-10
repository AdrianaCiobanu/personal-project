from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.name} {self.description}'
