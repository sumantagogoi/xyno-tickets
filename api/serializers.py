from rest_framework import serializers
from ticketing.models import *




class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    client = ClientSerializer() 
    class Meta:
        model = Event
        fields = ['id', 'client', 'name', 'event_creative', 'start_date', 'end_date', 'status']

    def to_representation(self, instance): 
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            representation['event_creative_url'] = request.build_absolute_uri(instance.event_creative.url)
        return representation




