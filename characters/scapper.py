from django.conf import settings

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
        character.save()


def sync_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
