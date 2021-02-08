from django.db import models


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """String representation of the model."""
        return str(self.id) + " - " + self.text[:50]
