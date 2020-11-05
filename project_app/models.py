from project_app.validators import ingredients_validator, time_validator
from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField, URLField

class Recipe(models.Model):
    """Model definition for Recipe."""

    title = CharField(max_length=30)
    image_url = URLField()
    description = TextField()
    ingredients = CharField(max_length=250,verbose_name="Ingredients (Please separate the ingredients with ','", validators=(ingredients_validator,))
    time = models.IntegerField(
        "Time (Minutes)",
        validators=(time_validator, )
    )

    class Meta:
        """Meta definition for Recipe."""

        verbose_name = 'Recipe' 
        verbose_name_plural = 'Recipes'

    def __str__(self):
        """Unicode representation of Recipe."""
        return f"{self.title}"



