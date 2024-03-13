from rest_framework.views import APIView, status, Request, Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView, PageNumberPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)
    

class MovieDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        found_movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(found_movie)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def delete(self, request: Request, movie_id: int) -> Response:
        found_movie = get_object_or_404(Movie, id=movie_id)
        found_movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)