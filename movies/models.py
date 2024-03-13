from django.db import models

class MovieRating(models.TextChoices):
    G_CATEGORY = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R_CATEGORY = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default="", blank=True, null=True)
    rating = models.CharField(max_length=20, choices=MovieRating.choices, default=MovieRating.G_CATEGORY)
    synopsis = models.TextField(default="", blank=True, null=True)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies")
    movies_orders = models.ManyToManyField("users.User", related_name="movies_orders", through="movies_orders.MovieOrder")