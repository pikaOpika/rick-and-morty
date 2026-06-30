from characters.models import Character

from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            "id", "api_id", "name", "status",
            "gender", "image"
        ]
        