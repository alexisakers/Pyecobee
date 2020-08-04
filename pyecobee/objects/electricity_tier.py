"""
This module is home to the ElectricityTier class
"""
from pyecobee.ecobee_object import EcobeeObject


class ElectricityTier(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/ElectricityTier.shtml

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
    __slots__ = ['_name', '_consumption', '_cost']

    attribute_name_map = {'name': 'name', 'consumption': 'consumption', 'cost': 'cost'}

    attribute_type_map = {
        'name': 'six.text_type',
        'consumption': 'six.text_type',
        'cost': 'six.text_type'}

    def __init__(self, name=None, consumption=None, cost=None):
        """
        Construct an ElectricityTier instance
        """
        self._name = name
        self._consumption = consumption
        self._cost = cost

    @property
    def name(self):
        """
        Gets the name attribute of this ElectricityTier instance.

        :return: The value of the name attribute of this ElectricityTier
        instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def consumption(self):
        """
        Gets the consumption attribute of this ElectricityTier instance.

        :return: The value of the consumption attribute of this
        ElectricityTier instance.
        :rtype: six.text_type
        """

        return self._consumption

    @property
    def cost(self):
        """
        Gets the cost attribute of this ElectricityTier instance.

        :return: The value of the cost attribute of this ElectricityTier
        instance.
        :rtype: six.text_type
        """

        return self._cost
