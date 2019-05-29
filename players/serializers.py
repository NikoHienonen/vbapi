from rest_framework import serializers
from players.models import Player

class PlayerSerializer(serializers.ModelSerializer):
  #A serializer that uses our Player-model as a model to either create new or update
  #existing players. The serializer itself is highly automated so we do not have to
  #do much here. The "Meta"-class automatically creates our fields and allows the use of
  #"create()" and "update()" methods.

  class Meta:
    model = Player
    fields = ('id', 'name', 'height', 'position', 'nationality', 'club')

  def create(self, validated_data):
    #Create and return a new Player instance if data is valid

    return Player.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
   # Update and return an existing Player instance if data is valid

    instance.name = validated_data.get('name', instance.name)
    instance.height = validated_data.get('height', instance.height)
    instance.position = validated_data.get('position', instance.position)
    instance.nationality = validated_data.get('nationality', instance.nationality)
    instance.club = validated_data.get('club', instance.club)
    return instance
