from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, serializers
from django.http import Http404
from django.apps import apps
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
from users.serializers import CustomUserSerializer

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            return Response({"404": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
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
        project = self.get_object(pk)
        #Only Super Users can delete
        if request.user.is_superuser:
            project.delete()
            return Response({"200: Project deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"403: Forbidden.  You are not authorised to delete this Project"}, status=status.HTTP_403_FORBIDDEN)

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.SerializerMethodField() #Uses a method to customise the supporter field

    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

    def get_supporter(self, instance):
        #Custom method that will handle supporter info determined whether "anonymous"
        request = self.context.get('request')
        if instance.anonymous and request.user != instance.supporter and not request.user.is_superuser:
            return "Anonymous"
            #If supporter anonymous=True, and requester is not the supporter owner and/or superuser, the pledge supporter info will be anonymous
        return { #Otherwise, will return normal supporter details
            "username": instance.supporter.username,
            "first_name": instance.supporter.first_name,
            "last_name": instance.supporter.last_name    
        }

class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True, context={'request':request})
        if request.user.is_superuser:
            return Response(serializer.data)
        else:
            return Response({"403: Forbidden.  You are not authorised to view the entire Pledge List."}, status=status.HTTP_403_FORBIDDEN)
        #Returns list of all Pledges only to the Super User
        
    def post(self, request):
        #Checks if user is authenticated first so as to return correct 402 error
        if not request.user or not request.user.is_authenticated:
            return Response({"401 Forbidden: Authentication credentials are required to perform this action"})
        serializer = PledgeSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):
    def get_permissions(self):
        #Only allow either owners of the pledge or superusers to edit/delete it
        if self.request.method in ['GET', 'PUT', 'DELETE']:
            return [IsSupporterOrReadOnly()]
        return super().get_permissions()
        
    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404({"404: This Pledge does not exist"}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge, context={'request': request}) #This context is required for the method that determines anonymous permissions in the serializers is applicable
        return Response(serializer.data)
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(instance=pledge,data=request.data,partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk):
        pledge = self.get_object(pk)
        #Only Super Users can delete
        if request.user.is_superuser:
            pledge.delete()
            return Response({"200: Pledge deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"403: Forbidden.  You are not authorised to delete this Pledge"}, status=status.HTTP_403_FORBIDDEN)

