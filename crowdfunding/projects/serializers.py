from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        ###To create "is_deleted" for soft deletion method###
        #instance.is_deleted = validated_data.get('is_deleted', instance.pledge)
        instance.save()
        return instance
    def to_representation(self, instance):
        #This customises the representation of a Pledge object depending on who is viewing it
        #This will allow us to hide the User info for anonymous donations
        data = super().to_representation(instance)
        request = self.context.get('request') #This obtains the info for WHO is requesting the Pledge Detail
        if instance.anonymous and request and request.user != instance.supporter and not request.user.is_superuser: 
            #We are now determining if the requester is the pledge owner or superuser if so they can view
            data.pop('supporter') #Hides the supporter field


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        ###To create "is_deleted" for soft deletion method###
        #instance.isdeleted = validated_data.get('is_deleted', instance.pledge)
        instance.save()
        return instance