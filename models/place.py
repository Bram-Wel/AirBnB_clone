#!/usr/bin/python3
"""The module contains a Place class."""


from models.base_model import BaseModel


class Place(BaseModel):
    """Place class.

    Args:
        @BaseModel: Supeclass
    Attributes:
        city_id (str): City ID ::City.id
        user_id (str): User ID ::User.id
        name (str): Amenity name
        description (str): Information on the Place
        number_rooms (int): No. of rooms
        number_bathrooms (int): No. of bathrooms
        max_guest (int): Maximum no. of guests
        price_by_night (int): Costs at night
        latitude (float): Latitute
        longitude (float): Longitude
        amenity_ids (list): List of Amenity IDs::Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
