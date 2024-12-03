from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_year = models.IntegerField()
    plot_summary = models.TextField()
    cast = models.TextField()
    trailer_url = models.URLField()

    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # For simplicity; replace with actual User model later
    score = models.IntegerField()  # Rating out of 5

    def __str__(self):
        return f"{self.movie.title} - {self.score}"