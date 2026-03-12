from django.db import models

# creates database for chords
class Chord(models.Model):
    name = models.CharField(max_length = 50)
    notes = models.CharField(max_length = 100)


    def __str__(self):
        return self.name # This part is for formatting

