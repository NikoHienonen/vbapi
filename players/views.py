from django.http import Http404
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from players.models import Player
from players.serializers import PlayerSerializer

class PlayerList(APIView):
  #List all players(get()) or create a new player(post())

  def get(self, request, format=None):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(APIView):
  #Retrieve, update or delete a specific player by their id
  #Notice that only the "get_object"-method needs to check if the player exists
  #since it raises the 404-error directly if the player is not found

  def get_object(self, id):
    #A simple re-usable method that fetches a specific player,
    #Raises a Http404-error if the player doesn't exist
    try:
      return Player.objects.get(id=id)
    except Player.DoesNotExist:
      raise Http404

  def get(self, request, id, format=None):
    #By using the "get_object"-method, gets a specific player and returns it
    player = self.get_object(id)
    serializer = PlayerSerializer(player)
    return Response(serializer.data)

  def put(self, request, id, format=None):
    #Uses the "get_object"-method to retrieve a player and edits it if data is valid
    player = self.get_object(id)
    serializer = PlayerSerializer(player, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id, format=None):
    #Gets a player with the "get_object"-method and deletes it
    player = self.get_object(id)
    player.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
