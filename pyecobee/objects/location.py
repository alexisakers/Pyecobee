"""
This module is home to the Location class
"""
from pyecobee.ecobee_object import EcobeeObject


class Location(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Location.shtml

    Attribute names have been generated by converting ecobee property
    names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value
    of READONLY is "no".

    An __init__ argument without a default value has been generated if
    the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated
    if the value of REQUIRED is "no".
    """
    __slots__ = [
        '_time_zone_offset_minutes',
        '_time_zone',
        '_is_daylight_saving',
        '_street_address',
        '_city',
        '_province_state',
        '_country',
        '_postal_code',
        '_phone_number',
        '_map_coordinates']

    attribute_name_map = {
        'time_zone_offset_minutes': 'timeZoneOffsetMinutes',
        'timeZoneOffsetMinutes': 'time_zone_offset_minutes',
        'time_zone': 'timeZone',
        'timeZone': 'time_zone',
        'is_daylight_saving': 'isDaylightSaving',
        'isDaylightSaving': 'is_daylight_saving',
        'street_address': 'streetAddress',
        'streetAddress': 'street_address',
        'city': 'city',
        'province_state': 'provinceState',
        'provinceState': 'province_state',
        'country': 'country',
        'postal_code': 'postalCode',
        'postalCode': 'postal_code',
        'phone_number': 'phoneNumber',
        'phoneNumber': 'phone_number',
        'map_coordinates': 'mapCoordinates',
        'mapCoordinates': 'map_coordinates'}

    attribute_type_map = {
        'time_zone_offset_minutes': 'int',
        'time_zone': 'six.text_type',
        'is_daylight_saving': 'bool',
        'street_address': 'six.text_type',
        'city': 'six.text_type',
        'province_state': 'six.text_type',
        'country': 'six.text_type',
        'postal_code': 'six.text_type',
        'phone_number': 'six.text_type',
        'map_coordinates': 'six.text_type'}

    def __init__(self, time_zone_offset_minutes=None, time_zone=None, is_daylight_saving=None,
                 street_address=None, city=None, province_state=None, country=None,
                 postal_code=None, phone_number=None, map_coordinates=None):
        """
        Construct a Location instance
        """
        self._time_zone_offset_minutes = time_zone_offset_minutes
        self._time_zone = time_zone
        self._is_daylight_saving = is_daylight_saving
        self._street_address = street_address
        self._city = city
        self._province_state = province_state
        self._country = country
        self._postal_code = postal_code
        self._phone_number = phone_number
        self._map_coordinates = map_coordinates

    @property
    def time_zone_offset_minutes(self):
        """
        Gets the time_zone_offset_minutes attribute of this Location
        instance.

        :return: The value of the time_zone_offset_minutes attribute of
        this Location instance.
        :rtype: int
        """

        return self._time_zone_offset_minutes

    @property
    def time_zone(self):
        """
        Gets the time_zone attribute of this Location instance.

        :return: The value of the time_zone attribute of this Location
        instance.
        :rtype: six.text_type
        """

        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone attribute of this Location instance.

        :param time_zone: The time_zone value to set for the time_zone
        attribute of this Location instance.
        :type: six.text_type
        """

        self._time_zone = time_zone

    @property
    def is_daylight_saving(self):
        """
        Gets the is_daylight_saving attribute of this Location instance.

        :return: The value of the is_daylight_saving attribute of this
        Location instance.
        :rtype: bool
        """

        return self._is_daylight_saving

    @is_daylight_saving.setter
    def is_daylight_saving(self, is_daylight_saving):
        """
        Sets the is_daylight_saving attribute of this Location instance.

        :param is_daylight_saving: The is_daylight_saving value to set
        for the is_daylight_saving attribute of this Location instance.
        :type: bool
        """

        self._is_daylight_saving = is_daylight_saving

    @property
    def street_address(self):
        """
        Gets the street_address attribute of this Location instance.

        :return: The value of the street_address attribute of this
        Location instance.
        :rtype: six.text_type
        """

        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """
        Sets the street_address attribute of this Location instance.

        :param street_address: The street_address value to set for the
        street_address attribute of this Location instance.
        :type: six.text_type
        """

        self._street_address = street_address

    @property
    def city(self):
        """
        Gets the city attribute of this Location instance.

        :return: The value of the city attribute of this Location
        instance.
        :rtype: six.text_type
        """

        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city attribute of this Location instance.

        :param city: The city value to set for the city attribute of
        this Location instance.
        :type: six.text_type
        """

        self._city = city

    @property
    def province_state(self):
        """
        Gets the province_state attribute of this Location instance.

        :return: The value of the province_state attribute of this
        Location instance.
        :rtype: six.text_type
        """

        return self._province_state

    @province_state.setter
    def province_state(self, province_state):
        """
        Sets the province_state attribute of this Location instance.

        :param province_state: The province_state value to set for the
        province_state attribute of this Location instance.
        :type: six.text_type
        """

        self._province_state = province_state

    @property
    def country(self):
        """
        Gets the country attribute of this Location instance.

        :return: The value of the country attribute of this Location
        instance.
        :rtype: six.text_type
        """

        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country attribute of this Location instance.

        :param country: The country value to set for the country
        attribute of this Location instance.
        :type: six.text_type
        """

        self._country = country

    @property
    def postal_code(self):
        """
        Gets the postal_code attribute of this Location instance.

        :return: The value of the postal_code attribute of this Location
        instance.
        :rtype: six.text_type
        """

        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code attribute of this Location instance.

        :param postal_code: The postal_code value to set for the
        postal_code attribute of this Location instance.
        :type: six.text_type
        """

        self._postal_code = postal_code

    @property
    def phone_number(self):
        """
        Gets the phone_number attribute of this Location instance.

        :return: The value of the phone_number attribute of this
        Location instance.
        :rtype: six.text_type
        """

        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number attribute of this Location instance.

        :param phone_number: The phone_number value to set for the
        phone_number attribute of this Location instance.
        :type: six.text_type
        """

        self._phone_number = phone_number

    @property
    def map_coordinates(self):
        """
        Gets the map_coordinates attribute of this Location instance.

        :return: The value of the map_coordinates attribute of this
        Location instance.
        :rtype: six.text_type
        """

        return self._map_coordinates

    @map_coordinates.setter
    def map_coordinates(self, map_coordinates):
        """
        Sets the map_coordinates attribute of this Location instance.

        :param map_coordinates: The map_coordinates value to set for the
        map_coordinates attribute of this Location instance.
        :type: six.text_type
        """

        self._map_coordinates = map_coordinates
