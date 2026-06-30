from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from drf_spectacular.utils import extend_schema, OpenApiParameter

from random import choice
  
from characters.models import Character
from characters.serializers import CharacterSerializer


@extend_schema(
        responses={status.HTTP_200_OK: CharacterSerializer},
    )
@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    """Get a random character from Rick & Morty world"""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serialzier = CharacterSerializer(random_character)
    return Response(serialzier.data, status=status.HTTP_200_OK)


class ListCharacters(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = Character.objects.filter(name__icontains=name)
        return queryset
    
    @extend_schema(
            parameters=[
                OpenApiParameter(
                    name="name", description="filter by name of character",
                    required=False, type=str
                )   
            ]
    )
    def get(self, request, *args, **kwargs):
        """List characters with filter by name"""
        return super().get(request, *args, **kwargs)