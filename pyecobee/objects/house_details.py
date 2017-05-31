"""
This module is home to the HouseDetails class
"""
from pyecobee.ecobee_object import EcobeeObject


class HouseDetails(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/HouseDetails.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_style', '_size', '_number_of_floors', '_number_of_rooms', '_number_of_occupants', '_age',
                 '_window_efficiency']

    attribute_name_map = {'style': 'style', 'size': 'size', 'number_of_floors': 'numberOfFloors',
                          'numberOfFloors': 'number_of_floors', 'number_of_rooms': 'numberOfRooms',
                          'numberOfRooms': 'number_of_rooms', 'number_of_occupants': 'numberOfOccupants',
                          'numberOfOccupants': 'number_of_occupants', 'age': 'age',
                          'window_efficiency': 'windowEfficiency', 'windowEfficiency': 'window_efficiency'}

    attribute_type_map = {'style': 'six.text_type', 'size': 'int', 'number_of_floors': 'int', 'number_of_rooms': 'int',
                          'number_of_occupants': 'int', 'age': 'int', 'window_efficiency': 'int'}

    def __init__(self, style=None, size=None, number_of_floors=None, number_of_rooms=None, number_of_occupants=None,
                 age=None, window_efficiency=None):
        """
        Construct a HouseDetails instance
        """
        self._style = style
        self._size = size
        self._number_of_floors = number_of_floors
        self._number_of_rooms = number_of_rooms
        self._number_of_occupants = number_of_occupants
        self._age = age
        self._window_efficiency = window_efficiency

    @property
    def style(self):
        """
        Gets the style attribute of this HouseDetails instance.

        :return: The value of the style attribute of this HouseDetails instance.
        :rtype: six.text_type

        Sets the style attribute of this HouseDetails instance.

        :param style: The style value to set for the style attribute of this HouseDetails instance.
        :type: six.text_type
        """

        return self._style

    @style.setter
    def style(self, style):
        self._style = style

    @property
    def size(self):
        """
        Gets the size attribute of this HouseDetails instance.

        :return: The value of the size attribute of this HouseDetails instance.
        :rtype: int

        Sets the size attribute of this HouseDetails instance.

        :param size: The size value to set for the size attribute of this HouseDetails instance.
        :type: int
        """

        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def number_of_floors(self):
        """
        Gets the number_of_floors attribute of this HouseDetails instance.

        :return: The value of the number_of_floors attribute of this HouseDetails instance.
        :rtype: int

        Sets the number_of_floors attribute of this HouseDetails instance.

        :param number_of_floors: The number_of_floors value to set for the number_of_floors attribute of this HouseDetails instance.
        :type: int
        """

        return self._number_of_floors

    @number_of_floors.setter
    def number_of_floors(self, number_of_floors):
        self._number_of_floors = number_of_floors

    @property
    def number_of_rooms(self):
        """
        Gets the number_of_rooms attribute of this HouseDetails instance.

        :return: The value of the number_of_rooms attribute of this HouseDetails instance.
        :rtype: int

        Sets the number_of_rooms attribute of this HouseDetails instance.

        :param number_of_rooms: The number_of_rooms value to set for the number_of_rooms attribute of this HouseDetails instance.
        :type: int
        """

        return self._number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, number_of_rooms):
        self._number_of_rooms = number_of_rooms

    @property
    def number_of_occupants(self):
        """
        Gets the number_of_occupants attribute of this HouseDetails instance.

        :return: The value of the number_of_occupants attribute of this HouseDetails instance.
        :rtype: int

        Sets the number_of_occupants attribute of this HouseDetails instance.

        :param number_of_occupants: The number_of_occupants value to set for the number_of_occupants attribute of this HouseDetails instance.
        :type: int
        """

        return self._number_of_occupants

    @number_of_occupants.setter
    def number_of_occupants(self, number_of_occupants):
        self._number_of_occupants = number_of_occupants

    @property
    def age(self):
        """
        Gets the age attribute of this HouseDetails instance.

        :return: The value of the age attribute of this HouseDetails instance.
        :rtype: int

        Sets the age attribute of this HouseDetails instance.

        :param age: The age value to set for the age attribute of this HouseDetails instance.
        :type: int
        """

        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def window_efficiency(self):
        """
        Gets the window_efficiency attribute of this HouseDetails instance.

        :return: The value of the window_efficiency attribute of this HouseDetails instance.
        :rtype: int

        Sets the window_efficiency attribute of this HouseDetails instance.

        :param window_efficiency: The window_efficiency value to set for the window_efficiency attribute of this HouseDetails instance.
        :type: int
        """

        return self._window_efficiency

    @window_efficiency.setter
    def window_efficiency(self, window_efficiency):
        self._window_efficiency = window_efficiency
