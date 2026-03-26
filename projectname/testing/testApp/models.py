from django.db import models

# creates database for chords
class Chord(models.Model):
    name = models.CharField(max_length = 50)
    notes = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='chord_images', blank=True, null=True)

    def __str__(self):
        return self.name # This part is for formatting

