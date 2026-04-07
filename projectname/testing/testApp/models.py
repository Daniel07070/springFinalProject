from django.db import models

# creates database for chords
class Chord(models.Model):
    name = models.CharField(max_length = 50)
    notes = models.CharField(max_length = 100)

    def __str__(self):
        return self.name # This part is for formatting
class ChordImage(models.Model):
    chord = models.ForeignKey(Chord, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='chord_images/')

    def __str__(self):
        return f"Image for {self.chord.name}"
