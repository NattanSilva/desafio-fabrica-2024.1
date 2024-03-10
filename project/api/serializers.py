from rest_framework.serializers import ModelSerializer

from ..models import Character


class CharacterSerializer(ModelSerializer):
  class Meta:
    model = Character
    fields = '__all__'

  def create(self, validated_data):
    return Character.objects.update_or_create(**validated_data)