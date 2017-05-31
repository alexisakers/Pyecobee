"""
This module is home to the Climate class
"""
from pyecobee.ecobee_object import EcobeeObject


class Climate(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Climate.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_name', '_climate_ref', '_is_occupied', '_is_optimized', '_cool_fan', '_heat_fan', '_vent',
                 '_ventilator_min_on_time', '_owner', '_type', '_colour', '_cool_temp', '_heat_temp', '_sensors']

    attribute_name_map = {'name': 'name', 'climate_ref': 'climateRef', 'climateRef': 'climate_ref',
                          'is_occupied': 'isOccupied', 'isOccupied': 'is_occupied', 'is_optimized': 'isOptimized',
                          'isOptimized': 'is_optimized', 'cool_fan': 'coolFan', 'coolFan': 'cool_fan',
                          'heat_fan': 'heatFan', 'heatFan': 'heat_fan', 'vent': 'vent',
                          'ventilator_min_on_time': 'ventilatorMinOnTime',
                          'ventilatorMinOnTime': 'ventilator_min_on_time', 'owner': 'owner', 'type': 'type',
                          'colour': 'colour', 'cool_temp': 'coolTemp', 'coolTemp': 'cool_temp', 'heat_temp': 'heatTemp',
                          'heatTemp': 'heat_temp', 'sensors': 'sensors'}

    attribute_type_map = {'name': 'six.text_type', 'climate_ref': 'six.text_type', 'is_occupied': 'bool',
                          'is_optimized': 'bool', 'cool_fan': 'six.text_type', 'heat_fan': 'six.text_type',
                          'vent': 'six.text_type', 'ventilator_min_on_time': 'int', 'owner': 'six.text_type',
                          'type': 'six.text_type', 'colour': 'int', 'cool_temp': 'int', 'heat_temp': 'int',
                          'sensors': 'List[RemoteSensor]'}

    def __init__(self, name, climate_ref=None, is_occupied=None, is_optimized=None, cool_fan=None, heat_fan=None,
                 vent=None, ventilator_min_on_time=None, owner=None, type=None, colour=None, cool_temp=None,
                 heat_temp=None, sensors=None):
        """
        Construct a Climate instance
        """
        self._name = name
        self._climate_ref = climate_ref
        self._is_occupied = is_occupied
        self._is_optimized = is_optimized
        self._cool_fan = cool_fan
        self._heat_fan = heat_fan
        self._vent = vent
        self._ventilator_min_on_time = ventilator_min_on_time
        self._owner = owner
        self._type = type
        self._colour = colour
        self._cool_temp = cool_temp
        self._heat_temp = heat_temp
        self._sensors = sensors

    @property
    def name(self):
        """
        Gets the name attribute of this Climate instance.

        :return: The value of the name attribute of this Climate instance.
        :rtype: six.text_type

        Sets the name attribute of this Climate instance.

        :param name: The name value to set for the name attribute of this Climate instance.
        :type: six.text_type
        """

        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def climate_ref(self):
        """
        Gets the climate_ref attribute of this Climate instance.

        :return: The value of the climate_ref attribute of this Climate instance.
        :rtype: six.text_type
        """

        return self._climate_ref

    @property
    def is_occupied(self):
        """
        Gets the is_occupied attribute of this Climate instance.

        :return: The value of the is_occupied attribute of this Climate instance.
        :rtype: bool

        Sets the is_occupied attribute of this Climate instance.

        :param is_occupied: The is_occupied value to set for the is_occupied attribute of this Climate instance.
        :type: bool
        """

        return self._is_occupied

    @is_occupied.setter
    def is_occupied(self, is_occupied):
        self._is_occupied = is_occupied

    @property
    def is_optimized(self):
        """
        Gets the is_optimized attribute of this Climate instance.

        :return: The value of the is_optimized attribute of this Climate instance.
        :rtype: bool

        Sets the is_optimized attribute of this Climate instance.

        :param is_optimized: The is_optimized value to set for the is_optimized attribute of this Climate instance.
        :type: bool
        """

        return self._is_optimized

    @is_optimized.setter
    def is_optimized(self, is_optimized):
        self._is_optimized = is_optimized

    @property
    def cool_fan(self):
        """
        Gets the cool_fan attribute of this Climate instance.

        :return: The value of the cool_fan attribute of this Climate instance.
        :rtype: six.text_type

        Sets the cool_fan attribute of this Climate instance.

        :param cool_fan: The cool_fan value to set for the cool_fan attribute of this Climate instance.
        :type: six.text_type
        """

        return self._cool_fan

    @cool_fan.setter
    def cool_fan(self, cool_fan):
        self._cool_fan = cool_fan

    @property
    def heat_fan(self):
        """
        Gets the heat_fan attribute of this Climate instance.

        :return: The value of the heat_fan attribute of this Climate instance.
        :rtype: six.text_type

        Sets the heat_fan attribute of this Climate instance.

        :param heat_fan: The heat_fan value to set for the heat_fan attribute of this Climate instance.
        :type: six.text_type
        """

        return self._heat_fan

    @heat_fan.setter
    def heat_fan(self, heat_fan):
        self._heat_fan = heat_fan

    @property
    def vent(self):
        """
        Gets the vent attribute of this Climate instance.

        :return: The value of the vent attribute of this Climate instance.
        :rtype: six.text_type

        Sets the vent attribute of this Climate instance.

        :param vent: The vent value to set for the vent attribute of this Climate instance.
        :type: six.text_type
        """

        return self._vent

    @vent.setter
    def vent(self, vent):
        self._vent = vent

    @property
    def ventilator_min_on_time(self):
        """
        Gets the ventilator_min_on_time attribute of this Climate instance.

        :return: The value of the ventilator_min_on_time attribute of this Climate instance.
        :rtype: int

        Sets the ventilator_min_on_time attribute of this Climate instance.

        :param ventilator_min_on_time: The ventilator_min_on_time value to set for the ventilator_min_on_time attribute of this Climate instance.
        :type: int
        """

        return self._ventilator_min_on_time

    @ventilator_min_on_time.setter
    def ventilator_min_on_time(self, ventilator_min_on_time):
        self._ventilator_min_on_time = ventilator_min_on_time

    @property
    def owner(self):
        """
        Gets the owner attribute of this Climate instance.

        :return: The value of the owner attribute of this Climate instance.
        :rtype: six.text_type

        Sets the owner attribute of this Climate instance.

        :param owner: The owner value to set for the owner attribute of this Climate instance.
        :type: six.text_type
        """

        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def type(self):
        """
        Gets the type attribute of this Climate instance.

        :return: The value of the type attribute of this Climate instance.
        :rtype: six.text_type

        Sets the type attribute of this Climate instance.

        :param type: The type value to set for the type attribute of this Climate instance.
        :type: six.text_type
        """

        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def colour(self):
        """
        Gets the colour attribute of this Climate instance.

        :return: The value of the colour attribute of this Climate instance.
        :rtype: int

        Sets the colour attribute of this Climate instance.

        :param colour: The colour value to set for the colour attribute of this Climate instance.
        :type: int
        """

        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour

    @property
    def cool_temp(self):
        """
        Gets the cool_temp attribute of this Climate instance.

        :return: The value of the cool_temp attribute of this Climate instance.
        :rtype: int

        Sets the cool_temp attribute of this Climate instance.

        :param cool_temp: The cool_temp value to set for the cool_temp attribute of this Climate instance.
        :type: int
        """

        return self._cool_temp

    @cool_temp.setter
    def cool_temp(self, cool_temp):
        self._cool_temp = cool_temp

    @property
    def heat_temp(self):
        """
        Gets the heat_temp attribute of this Climate instance.

        :return: The value of the heat_temp attribute of this Climate instance.
        :rtype: int

        Sets the heat_temp attribute of this Climate instance.

        :param heat_temp: The heat_temp value to set for the heat_temp attribute of this Climate instance.
        :type: int
        """

        return self._heat_temp

    @heat_temp.setter
    def heat_temp(self, heat_temp):
        self._heat_temp = heat_temp

    @property
    def sensors(self):
        """
        Gets the sensors attribute of this Climate instance.

        :return: The value of the sensors attribute of this Climate instance.
        :rtype: List[RemoteSensor]

        Sets the sensors attribute of this Climate instance.

        :param sensors: The sensors value to set for the sensors attribute of this Climate instance.
        :type: List[RemoteSensor]
        """

        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        self._sensors = sensors
