"""
This module is home to the Energy class
"""
from pyecobee.ecobee_object import EcobeeObject


class Energy(EcobeeObject):
    """
    This class has been manually generated by reverse engineering

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
    __slots__ = ['_tou', '_energy_feature_state', '_feels_like_mode', '_comfort_preferences']

    attribute_name_map = {
        'tou': 'tou',
        'energy_feature_state': 'energyFeatureState',
        'energyFeatureState': 'energy_feature_state',
        'feels_like_mode': 'feelsLikeMode',
        'feelsLikeMode': 'feels_like_mode',
        'comfort_preferences': 'comfortPreferences',
        'comfortPreferences': 'comfort_preferences'}

    attribute_type_map = {
        'tou': 'TimeOfUse',
        'energy_feature_state': 'six.text_type',
        'feels_like_mode': 'six.text_type',
        'comfort_preferences': 'six.text_type'}

    def __init__(self, tou=None, energy_feature_state=None, feels_like_mode=None,
                 comfort_preferences=None):
        """
        Construct a Energy instance
        """
        self._tou = tou
        self._energy_feature_state = energy_feature_state
        self._feels_like_mode = feels_like_mode
        self._comfort_preferences = comfort_preferences

    @property
    def tou(self):
        """
        Gets the tou attribute of this Energy instance.

        :return: The value of the tou attribute of this Energy
        instance.
        :rtype: TimeOfUse
        """

        return self._tou

    @property
    def energy_feature_state(self):
        """
        Gets the energy_feature_state attribute of this Energy instance.

        :return: The value of the energy_feature_state attribute of this Energy
        instance.
        :rtype: six.text_type
        """

        return self._energy_feature_state

    @property
    def feels_like_mode(self):
        """
        Gets the feels_like_mode attribute of this Energy instance.

        :return: The value of the feels_like_mode attribute of this Energy
        instance.
        :rtype: six.text_type
        """

        return self._feels_like_mode

    @property
    def comfort_preferences(self):
        """
        Gets the comfort_preferences attribute of this Energy instance.

        :return: The value of the comfort_preferences attribute of this Energy
        instance.
        :rtype: six.text_type
        """

        return self._comfort_preferences
