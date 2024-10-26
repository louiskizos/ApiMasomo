from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.forms import model_to_dict
from .models import *
from .seralizer import *
from rest_framework import generics
#from  .tests import EtablissementSerializer

# Create your views here.


@api_view(['GET'])
def etablissemntView(request):
    
    query = Etablissements.objects.all().order_by('?')[:3]  # Sélectionner 3 éléments aléatoires
    if query == None:
        data = {'Error' : 'Table is empty'}
        return Response(data)
    if query:
        serializer = EtablissementSerializer(query, many=True)
        
    return Response(serializer.data)



@api_view(['POST'])
def tout_etablissement(request):
        
    query = Etablissements.objects.all()  # Sélectionner tout les éléments
    if query == None:
        data = {'Error' : 'Table is empty'}
        return Response(data)
    if query:
        serializer = EtablissementSerializer(query, many = True)
    return Response(serializer.data)
        


@api_view(['GET'])
def test(request):
    
    query = Test.objects.all().order_by('?').first()  # Sélectionner tout les éléments
    if query == None:
        data = {'Error' : 'Table is empty'}
        return Response(data)
    data = []
    if query:
        data = TestSeralizer(query).data
    return Response(data)

@api_view(['POST'])
def test_post(request):
    
    serializer = TestSeralizer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    else:
         
         return Response({'details':'data invalid'})
     
 ### RECHERCER    
class recherche_get(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSeralizer
    
    
# INSERT

class CreateApiViewTest(generics.ListCreateAPIView):
    queryset = Etablissements.objects.all()
    serializer_class = EtablissementSerializer


class UpdateApiViewTest(generics.UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSeralizer
class DeleteApiView(generics.DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSeralizer
    lookup_field = 'pk'