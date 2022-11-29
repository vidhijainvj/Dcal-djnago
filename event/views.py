from django.shortcuts import render
from rest_framework import viewsets
from .serializers import eventSerializer
from .models import event

# Create your views here.

class eventView(viewsets.ModelViewSet):
    model = event
    serializer_class = eventSerializer
    queryset = event.objects.all()




    # def delete_event(request):
    #     print(request.query_params('datee'))
    
    # date_delete = event.objects.get(date = datee)
    # date_delete.delete()
    
     
    # filter_fields = ('date')
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['date']


    # def deletelist(request):
        
    #     id=request.query_params.get('id')
    #     if id is not None:
    #        queryset = event.objects.delete(id=id)
    #     return queryset