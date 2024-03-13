from rest_framework import serializers
from .models import Movie
from .models import MovieRating

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(MovieRating.choices, default=MovieRating.G_CATEGORY)
    synopsis = serializers.CharField(allow_null=True, default="")
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance: Movie, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance