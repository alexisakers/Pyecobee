"""
This module is home to the Capabilities class
"""
from pyecobee.ecobee_object import EcobeeObject
from pyecobee.objects.fan_capabilities import FanCapabilities

class Capabilities(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Capabilities.shtml

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

    __slots__ = ['_fan_capabilities']

    attribute_name_map = {
        'fanCapabilities': 'fan_capabilities',
        'fan_capabilities': 'fanCapabilities',
    }

    attribute_type_map = {
        'fan_capabilities': 'FanCapabilities',
    }

    def __init__(self, fan_capabilities=None):
        """
        Construct a Capabilities instance
        """
        self._fan_capabilities = fan_capabilities

    @property
    def fan_capabilities(self):
        return self._fan_capabilities
