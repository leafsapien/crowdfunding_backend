from django.shortcuts import render

from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from projects.models import Project, Pledge
from .serializers import CustomUserSerializer
from .permissions import IsOwnerOrSuperUser, IsSuperUser

class CustomUserList(APIView):
    #Defines/overrides permissions as to ensure anybody can create a new user
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [
        permissions.IsAuthenticated, IsSuperUser
    ]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        self.permission_classes = [AllowAny] #Overrides above permissions and allows anybody to create a new user to prevent permission blocking
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CustomUserDetail(APIView):
    #Only User themselves and SuperUser has permission to view User Detail
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrSuperUser
    ]
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"404: That User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        self.check_permissions(request, user) #Checks if the User has permission to edit through PUT method
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance=user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk):
        self.check_permissions(request)
        user = self.get_object(pk)
        if request.user.is_superuser:
            user.delete()
            return Response({"200: User deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"403: Forbidden.  You are not authorised to delete this User"}, status=status.HTTP_403_FORBIDDEN)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })

# Custom GET permissions for the "My Details" page on front end
# This will pull all projects/pledges owned by the user
class MeDetail(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        # Fetches projects and pledges related to the matching user/owner/support ID
        projects = Project.objects.filter(owner=user)
        pledges=Pledge.objects.filter(supporter=user)
        project_data = [
            {
                "id": project.id,
                "title": project.title,
                "description": project.description,
                "goal": project.goal,
                "is_open": project.is_open,
                "date_created": project.date_created,
            }
            for project in projects
        ]

        pledge_data = [
            {
                "id": pledge.id,
                "amount": pledge.amount,
                "anonymous": pledge.anonymous,
                "comment": pledge.comment,
                "project": {"id": pledge.project.id, "title": pledge.project.title},
            }
            for pledge in pledges
        ]

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "projects": project_data,
            "pledges": pledge_data,
        })