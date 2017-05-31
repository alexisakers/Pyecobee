"""
This module is home to the Action class
"""
from pyecobee.ecobee_object import EcobeeObject


class Action(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Action.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_type', '_send_alert', '_send_update', '_activation_delay', '_deactivation_delay',
                 '_min_action_duration', '_heat_adjust_temp', '_cool_adjust_temp', '_activate_relay',
                 '_activate_relay_open']

    attribute_name_map = {'type': 'type', 'send_alert': 'sendAlert', 'sendAlert': 'send_alert',
                          'send_update': 'sendUpdate', 'sendUpdate': 'send_update',
                          'activation_delay': 'activationDelay', 'activationDelay': 'activation_delay',
                          'deactivation_delay': 'deactivationDelay', 'deactivationDelay': 'deactivation_delay',
                          'min_action_duration': 'minActionDuration', 'minActionDuration': 'min_action_duration',
                          'heat_adjust_temp': 'heatAdjustTemp', 'heatAdjustTemp': 'heat_adjust_temp',
                          'cool_adjust_temp': 'coolAdjustTemp', 'coolAdjustTemp': 'cool_adjust_temp',
                          'activate_relay': 'activateRelay', 'activateRelay': 'activate_relay',
                          'activate_relay_open': 'activateRelayOpen', 'activateRelayOpen': 'activate_relay_open'}

    attribute_type_map = {'type': 'six.text_type', 'send_alert': 'bool', 'send_update': 'bool',
                          'activation_delay': 'int', 'deactivation_delay': 'int', 'min_action_duration': 'int',
                          'heat_adjust_temp': 'int', 'cool_adjust_temp': 'int', 'activate_relay': 'six.text_type',
                          'activate_relay_open': 'bool'}

    def __init__(self, type=None, send_alert=None, send_update=None, activation_delay=None, deactivation_delay=None,
                 min_action_duration=None, heat_adjust_temp=None, cool_adjust_temp=None, activate_relay=None,
                 activate_relay_open=None):
        """
        Construct an Action instance
        """
        self._type = type
        self._send_alert = send_alert
        self._send_update = send_update
        self._activation_delay = activation_delay
        self._deactivation_delay = deactivation_delay
        self._min_action_duration = min_action_duration
        self._heat_adjust_temp = heat_adjust_temp
        self._cool_adjust_temp = cool_adjust_temp
        self._activate_relay = activate_relay
        self._activate_relay_open = activate_relay_open

    @property
    def type(self):
        """
        Gets the type attribute of this Action instance.

        :return: The value of the type attribute of this Action instance.
        :rtype: six.text_type
        """

        return self._type

    @property
    def send_alert(self):
        """
        Gets the send_alert attribute of this Action instance.

        :return: The value of the send_alert attribute of this Action instance.
        :rtype: bool
        """

        return self._send_alert

    @property
    def send_update(self):
        """
        Gets the send_update attribute of this Action instance.

        :return: The value of the send_update attribute of this Action instance.
        :rtype: bool
        """

        return self._send_update

    @property
    def activation_delay(self):
        """
        Gets the activation_delay attribute of this Action instance.

        :return: The value of the activation_delay attribute of this Action instance.
        :rtype: int
        """

        return self._activation_delay

    @property
    def deactivation_delay(self):
        """
        Gets the deactivation_delay attribute of this Action instance.

        :return: The value of the deactivation_delay attribute of this Action instance.
        :rtype: int
        """

        return self._deactivation_delay

    @property
    def min_action_duration(self):
        """
        Gets the min_action_duration attribute of this Action instance.

        :return: The value of the min_action_duration attribute of this Action instance.
        :rtype: int
        """

        return self._min_action_duration

    @property
    def heat_adjust_temp(self):
        """
        Gets the heat_adjust_temp attribute of this Action instance.

        :return: The value of the heat_adjust_temp attribute of this Action instance.
        :rtype: int
        """

        return self._heat_adjust_temp

    @property
    def cool_adjust_temp(self):
        """
        Gets the cool_adjust_temp attribute of this Action instance.

        :return: The value of the cool_adjust_temp attribute of this Action instance.
        :rtype: int
        """

        return self._cool_adjust_temp

    @property
    def activate_relay(self):
        """
        Gets the activate_relay attribute of this Action instance.

        :return: The value of the activate_relay attribute of this Action instance.
        :rtype: six.text_type
        """

        return self._activate_relay

    @property
    def activate_relay_open(self):
        """
        Gets the activate_relay_open attribute of this Action instance.

        :return: The value of the activate_relay_open attribute of this Action instance.
        :rtype: bool
        """

        return self._activate_relay_open
