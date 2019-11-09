from django.db import models

# Create your models here.
class Personality(models.Model):
    user_personality = models.CharField(max_length=50)

    def __str__(self):
        return self.user_personality

class TripCategories(models.Model):
    categories_text = models.CharField(max_length=100)

    def __str__(self):
        return self.categories_text    