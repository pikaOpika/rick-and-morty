from django.conf import settings
from django.db.utils import IntegrityError


from characters.models import Character
import requests


def scrape_characters() -> list[Character]:
    url = settings.RICK_AND_MORTY_API_CHARACTER_URL
    characters = []
    while url is not None:
        character_response = requests.get(url).json()
        for character in character_response["results"]:
            characters.append(
                Character(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"],
                )
            )
        url = character_response["info"]["next"]
    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print(f"Character with api_id {character.api_id} already exists")


def sync_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
