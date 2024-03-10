import requests
from rest_framework.views import Response, status
from rest_framework.viewsets import ModelViewSet

from ..models import Character
from ..utils import get_random_index
from .serializers import CharacterSerializer


class CharacterViewset(ModelViewSet):
  queryset = Character.objects.all()
  serializer_class = CharacterSerializer
  
  def create(self, request, *args, **kwargs):
    rick_morty_api_url = "https://rickandmortyapi.com/api/"

    if not request.data['name']:
      return Response({"message": "Name are required"}, status=status.HTTP_400_BAD_REQUEST)
    
    response = requests.get(f"{rick_morty_api_url}character/?name={request.data['name']}")

    char = response.json().get("results")[get_random_index(response.json().get("results"))]

    serializer = CharacterSerializer(data={
      "name": char.get("name"), 
      "status": char.get("status"), 
      "species": char.get("species"), 
      "char_type": char.get("type") if char.get("type") else "Not Deffined", 
      "gender": char.get("gender"), 
      "image": char.get("image")
    })

    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    
    return Response(serializer.validated_data, status=status.HTTP_201_CREATED)