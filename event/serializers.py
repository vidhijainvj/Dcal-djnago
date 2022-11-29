from rest_framework import serializers
from .models import event

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=event
        fields = ('id','title','date','start_time','end_time','imp')