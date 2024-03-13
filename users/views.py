from rest_framework.views import APIView, status, Request, Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .permissions import IsUserOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def get(self, req: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)
    
    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    def get(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)