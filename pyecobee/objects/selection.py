"""
This module is home to the Selection class
"""
from pyecobee.ecobee_object import EcobeeObject


class Selection(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Selection.shtml

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
        '_selection_type',
        '_selection_match',
        '_include_runtime',
        '_include_extended_runtime',
        '_include_electricity',
        '_include_settings',
        '_include_location',
        '_include_program',
        '_include_events',
        '_include_device',
        '_include_technician',
        '_include_utility',
        '_include_management',
        '_include_alerts',
        '_include_reminders',
        '_include_weather',
        '_include_house_details',
        '_include_oem_cfg',
        '_include_equipment_status',
        '_include_notification_settings',
        '_include_privacy',
        '_include_version',
        '_include_security_settings',
        '_include_sensors',
        '_include_audio',
        '_include_energy']

    attribute_name_map = {
        'selection_type': 'selectionType', 'selectionType': 'selection_type',
        'selection_match': 'selectionMatch', 'selectionMatch': 'selection_match',
        'include_runtime': 'includeRuntime', 'includeRuntime': 'include_runtime',
        'include_extended_runtime': 'includeExtendedRuntime',
        'includeExtendedRuntime': 'include_extended_runtime',
        'include_electricity': 'includeElectricity', 'includeElectricity': 'include_electricity',
        'include_settings': 'includeSettings', 'includeSettings': 'include_settings',
        'include_location': 'includeLocation', 'includeLocation': 'include_location',
        'include_program': 'includeProgram', 'includeProgram': 'include_program',
        'include_events': 'includeEvents', 'includeEvents': 'include_events',
        'include_device': 'includeDevice', 'includeDevice': 'include_device',
        'include_technician': 'includeTechnician', 'includeTechnician': 'include_technician',
        'include_utility': 'includeUtility', 'includeUtility': 'include_utility',
        'include_management': 'includeManagement', 'includeManagement': 'include_management',
        'include_alerts': 'includeAlerts', 'includeAlerts': 'include_alerts',
        'include_reminders': 'includeReminders', 'includeReminders': 'include_reminders',
        'include_weather': 'includeWeather', 'includeWeather': 'include_weather',
        'include_house_details': 'includeHouseDetails',
        'includeHouseDetails': 'include_house_details', 'include_oem_cfg': 'includeOemCfg',
        'includeOemCfg': 'include_oem_cfg', 'include_equipment_status': 'includeEquipmentStatus',
        'includeEquipmentStatus': 'include_equipment_status',
        'include_notification_settings': 'includeNotificationSettings',
        'includeNotificationSettings': 'include_notification_settings',
        'include_privacy': 'includePrivacy', 'includePrivacy': 'include_privacy',
        'include_version': 'includeVersion', 'includeVersion': 'include_version',
        'include_security_settings': 'includeSecuritySettings',
        'includeSecuritySettings': 'include_security_settings',
        'include_sensors': 'includeSensors', 'includeSensors': 'include_sensors',
        'include_audio': 'includeAudio', 'includeAudio': 'include_audio',
        'include_energy': 'includeEnergy', 'includeEnergy': 'include_energy'}

    attribute_type_map = {
        'selection_type': 'six.text_type',
        'selection_match': 'six.text_type',
        'include_runtime': 'boolean',
        'include_extended_runtime': 'boolean',
        'include_electricity': 'boolean',
        'include_settings': 'boolean',
        'include_location': 'boolean',
        'include_program': 'boolean',
        'include_events': 'boolean',
        'include_device': 'boolean',
        'include_technician': 'boolean',
        'include_utility': 'boolean',
        'include_management': 'boolean',
        'include_alerts': 'boolean',
        'include_reminders': 'boolean',
        'include_weather': 'boolean',
        'include_house_details': 'boolean',
        'include_oem_cfg': 'boolean',
        'include_equipment_status': 'boolean',
        'include_notification_settings': 'boolean',
        'include_privacy': 'boolean',
        'include_version': 'boolean',
        'include_security_settings': 'boolean',
        'include_sensors': 'boolean',
        'include_audio': 'boolean',
        'include_energy': 'boolean'}

    def __init__(self, selection_type, selection_match, include_runtime=None,
                 include_extended_runtime=None, include_electricity=None, include_settings=None,
                 include_location=None, include_program=None, include_events=None,
                 include_device=None, include_technician=None, include_utility=None,
                 include_management=None, include_alerts=None, include_reminders=None,
                 include_weather=None, include_house_details=None, include_oem_cfg=None,
                 include_equipment_status=None, include_notification_settings=None,
                 include_privacy=None, include_version=None, include_security_settings=None,
                 include_sensors=None, include_audio=None, include_energy=None):
        """
        Construct a Selection instance
        """
        self._selection_type = selection_type
        self._selection_match = selection_match
        self._include_runtime = include_runtime
        self._include_extended_runtime = include_extended_runtime
        self._include_electricity = include_electricity
        self._include_settings = include_settings
        self._include_location = include_location
        self._include_program = include_program
        self._include_events = include_events
        self._include_device = include_device
        self._include_technician = include_technician
        self._include_utility = include_utility
        self._include_management = include_management
        self._include_alerts = include_alerts
        self._include_reminders = include_reminders
        self._include_weather = include_weather
        self._include_house_details = include_house_details
        self._include_oem_cfg = include_oem_cfg
        self._include_equipment_status = include_equipment_status
        self._include_notification_settings = include_notification_settings
        self._include_privacy = include_privacy
        self._include_version = include_version
        self._include_security_settings = include_security_settings
        self._include_sensors = include_sensors
        self._include_audio = include_audio
        self._include_energy = include_energy

    @property
    def selection_type(self):
        """
        Gets the selection_type attribute of this Selection instance.

        :return: The value of the selection_type attribute of this
        Selection instance.
        :rtype: six.text_type
        """

        return self._selection_type

    @selection_type.setter
    def selection_type(self, selection_type):
        """
        Sets the selection_type attribute of this Selection instance.

        :param selection_type: The selection_type value to set for the
        selection_type attribute of this Selection instance.
        :type: six.text_type
        """

        self._selection_type = selection_type

    @property
    def selection_match(self):
        """
        Gets the selection_match attribute of this Selection instance.

        :return: The value of the selection_match attribute of this
        Selection instance.
        :rtype: six.text_type
        """

        return self._selection_match

    @selection_match.setter
    def selection_match(self, selection_match):
        """
        Sets the selection_match attribute of this Selection instance.

        :param selection_match: The selection_match value to set for the
        selection_match attribute of this Selection instance.
        :type: six.text_type
        """

        self._selection_match = selection_match

    @property
    def include_runtime(self):
        """
        Gets the include_runtime attribute of this Selection instance.

        :return: The value of the include_runtime attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_runtime

    @include_runtime.setter
    def include_runtime(self, include_runtime):
        """
        Sets the include_runtime attribute of this Selection instance.

        :param include_runtime: The include_runtime value to set for the
        include_runtime attribute of this Selection instance.
        :type: boolean
        """

        self._include_runtime = include_runtime

    @property
    def include_extended_runtime(self):
        """
        Gets the include_extended_runtime attribute of this Selection
        instance.

        :return: The value of the include_extended_runtime attribute of
        this Selection instance.
        :rtype: boolean
        """

        return self._include_extended_runtime

    @include_extended_runtime.setter
    def include_extended_runtime(self, include_extended_runtime):
        """
        Sets the include_extended_runtime attribute of this Selection
        instance.

        :param include_extended_runtime: The include_extended_runtime
        value to set for the include_extended_runtime attribute of this
        Selection instance.
        :type: boolean
        """

        self._include_extended_runtime = include_extended_runtime

    @property
    def include_electricity(self):
        """
        Gets the include_electricity attribute of this Selection
        instance.

        :return: The value of the include_electricity attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_electricity

    @include_electricity.setter
    def include_electricity(self, include_electricity):
        """
        Sets the include_electricity attribute of this Selection
        instance.

        :param include_electricity: The include_electricity value to set
        for the include_electricity attribute of this Selection
        instance.
        :type: boolean
        """

        self._include_electricity = include_electricity

    @property
    def include_settings(self):
        """
        Gets the include_settings attribute of this Selection instance.

        :return: The value of the include_settings attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_settings

    @include_settings.setter
    def include_settings(self, include_settings):
        """
        Sets the include_settings attribute of this Selection instance.

        :param include_settings: The include_settings value to set for
        the include_settings attribute of this Selection instance.
        :type: boolean
        """

        self._include_settings = include_settings

    @property
    def include_location(self):
        """
        Gets the include_location attribute of this Selection instance.

        :return: The value of the include_location attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_location

    @include_location.setter
    def include_location(self, include_location):
        """
        Sets the include_location attribute of this Selection instance.

        :param include_location: The include_location value to set for
        the include_location attribute of this Selection instance.
        :type: boolean
        """

        self._include_location = include_location

    @property
    def include_program(self):
        """
        Gets the include_program attribute of this Selection instance.

        :return: The value of the include_program attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_program

    @include_program.setter
    def include_program(self, include_program):
        """
        Sets the include_program attribute of this Selection instance.

        :param include_program: The include_program value to set for the
        include_program attribute of this Selection instance.
        :type: boolean
        """

        self._include_program = include_program

    @property
    def include_events(self):
        """
        Gets the include_events attribute of this Selection instance.

        :return: The value of the include_events attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_events

    @include_events.setter
    def include_events(self, include_events):
        """
        Sets the include_events attribute of this Selection instance.

        :param include_events: The include_events value to set for the
        include_events attribute of this Selection instance.
        :type: boolean
        """

        self._include_events = include_events

    @property
    def include_device(self):
        """
        Gets the include_device attribute of this Selection instance.

        :return: The value of the include_device attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_device

    @include_device.setter
    def include_device(self, include_device):
        """
        Sets the include_device attribute of this Selection instance.

        :param include_device: The include_device value to set for the
        include_device attribute of this Selection instance.
        :type: boolean
        """

        self._include_device = include_device

    @property
    def include_technician(self):
        """
        Gets the include_technician attribute of this Selection
        instance.

        :return: The value of the include_technician attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_technician

    @include_technician.setter
    def include_technician(self, include_technician):
        """
        Sets the include_technician attribute of this Selection
        instance.

        :param include_technician: The include_technician value to set
        for the include_technician attribute of this Selection instance.
        :type: boolean
        """

        self._include_technician = include_technician

    @property
    def include_utility(self):
        """
        Gets the include_utility attribute of this Selection instance.

        :return: The value of the include_utility attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_utility

    @include_utility.setter
    def include_utility(self, include_utility):
        """
        Sets the include_utility attribute of this Selection instance.

        :param include_utility: The include_utility value to set for the
        include_utility attribute of this Selection instance.
        :type: boolean
        """

        self._include_utility = include_utility

    @property
    def include_management(self):
        """
        Gets the include_management attribute of this Selection
        instance.

        :return: The value of the include_management attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_management

    @include_management.setter
    def include_management(self, include_management):
        """
        Sets the include_management attribute of this Selection
        instance.

        :param include_management: The include_management value to set
        for the include_management attribute of this Selection instance.
        :type: boolean
        """

        self._include_management = include_management

    @property
    def include_alerts(self):
        """
        Gets the include_alerts attribute of this Selection instance.

        :return: The value of the include_alerts attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_alerts

    @include_alerts.setter
    def include_alerts(self, include_alerts):
        """
        Sets the include_alerts attribute of this Selection instance.

        :param include_alerts: The include_alerts value to set for the
        include_alerts attribute of this Selection instance.
        :type: boolean
        """

        self._include_alerts = include_alerts

    @property
    def include_reminders(self):
        """
        Gets the include_reminders attribute of this Selection instance.

        :return: The value of the include_reminders attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_reminders

    @include_reminders.setter
    def include_reminders(self, include_reminders):
        """
        Sets the include_reminders attribute of this Selection instance.

        :param include_reminders: The include_reminders value to set for
        the include_reminders attribute of this Selection instance.
        :type: boolean
        """

        self._include_reminders = include_reminders

    @property
    def include_weather(self):
        """
        Gets the include_weather attribute of this Selection instance.

        :return: The value of the include_weather attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_weather

    @include_weather.setter
    def include_weather(self, include_weather):
        """
        Sets the include_weather attribute of this Selection instance.

        :param include_weather: The include_weather value to set for the
        include_weather attribute of this Selection instance.
        :type: boolean
        """

        self._include_weather = include_weather

    @property
    def include_house_details(self):
        """
        Gets the include_house_details attribute of this Selection
        instance.

        :return: The value of the include_house_details attribute of
        this Selection instance.
        :rtype: boolean
        """

        return self._include_house_details

    @include_house_details.setter
    def include_house_details(self, include_house_details):
        """
        Sets the include_house_details attribute of this Selection
        instance.

        :param include_house_details: The include_house_details value to
        set for the include_house_details attribute of this Selection
        instance.
        :type: boolean
        """

        self._include_house_details = include_house_details

    @property
    def include_oem_cfg(self):
        """
        Gets the include_oem_cfg attribute of this Selection instance.

        :return: The value of the include_oem_cfg attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_oem_cfg

    @include_oem_cfg.setter
    def include_oem_cfg(self, include_oem_cfg):
        """
        Sets the include_oem_cfg attribute of this Selection instance.

        :param include_oem_cfg: The include_oem_cfg value to set for the
        include_oem_cfg attribute of this Selection instance.
        :type: boolean
        """

        self._include_oem_cfg = include_oem_cfg

    @property
    def include_equipment_status(self):
        """
        Gets the include_equipment_status attribute of this Selection
        instance.

        :return: The value of the include_equipment_status attribute of
        this Selection instance.
        :rtype: boolean
        """

        return self._include_equipment_status

    @include_equipment_status.setter
    def include_equipment_status(self, include_equipment_status):
        """
        Sets the include_equipment_status attribute of this Selection
        instance.

        :param include_equipment_status: The include_equipment_status
        value to set for the include_equipment_status attribute of this
        Selection instance.
        :type: boolean
        """

        self._include_equipment_status = include_equipment_status

    @property
    def include_notification_settings(self):
        """
        Gets the include_notification_settings attribute of this
        Selection instance.

        :return: The value of the include_notification_settings
        attribute of this Selection instance.
        :rtype: boolean
        """

        return self._include_notification_settings

    @include_notification_settings.setter
    def include_notification_settings(self, include_notification_settings):
        """
        Sets the include_notification_settings attribute of this
        Selection instance.

        :param include_notification_settings: The
        include_notification_settings value to set for the
        include_notification_settings attribute of this Selection
        instance.
        :type: boolean
        """

        self._include_notification_settings = include_notification_settings

    @property
    def include_privacy(self):
        """
        Gets the include_privacy attribute of this Selection instance.

        :return: The value of the include_privacy attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_privacy

    @include_privacy.setter
    def include_privacy(self, include_privacy):
        """
        Sets the include_privacy attribute of this Selection instance.

        :param include_privacy: The include_privacy value to set for the
        include_privacy attribute of this Selection instance.
        :type: boolean
        """

        self._include_privacy = include_privacy

    @property
    def include_version(self):
        """
        Gets the include_version attribute of this Selection instance.

        :return: The value of the include_version attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_version

    @include_version.setter
    def include_version(self, include_version):
        """
        Sets the include_version attribute of this Selection instance.

        :param include_version: The include_version value to set for the
        include_version attribute of this Selection instance.
        :type: boolean
        """

        self._include_version = include_version

    @property
    def include_security_settings(self):
        """
        Gets the include_security_settings attribute of this Selection
        instance.

        :return: The value of the include_security_settings attribute of
        this Selection instance.
        :rtype: boolean
        """

        return self._include_security_settings

    @include_security_settings.setter
    def include_security_settings(self, include_security_settings):
        """
        Sets the include_security_settings attribute of this Selection
        instance.

        :param include_security_settings: The include_security_settings
        value to set for the include_security_settings attribute of this
        Selection instance.
        :type: boolean
        """

        self._include_security_settings = include_security_settings

    @property
    def include_sensors(self):
        """
        Gets the include_sensors attribute of this Selection instance.

        :return: The value of the include_sensors attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_sensors

    @include_sensors.setter
    def include_sensors(self, include_sensors):
        """
        Sets the include_sensors attribute of this Selection instance.

        :param include_sensors: The include_sensors value to set for the
        include_sensors attribute of this Selection instance.
        :type: boolean
        """

        self._include_sensors = include_sensors

    @property
    def include_audio(self):
        """
        Gets the include_audio attribute of this Selection instance.

        :return: The value of the include_audio attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_audio

    @include_audio.setter
    def include_audio(self, include_audio):
        """
        Sets the include_audio attribute of this Selection instance.

        :param include_audio: The include_audio value to set for the
        include_audio attribute of this Selection instance.
        :type: boolean
        """

        self._include_audio = include_audio

    @property
    def include_energy(self):
        """
        Gets the include_energy attribute of this Selection instance.

        :return: The value of the include_energy attribute of this
        Selection instance.
        :rtype: boolean
        """

        return self._include_energy

    @include_energy.setter
    def include_energy(self, include_energy):
        """
        Sets the include_energy attribute of this Selection instance.

        :param include_energy: The include_energy value to set for the
        include_energy attribute of this Selection instance.
        :type: boolean
        """

        self._include_energy = include_energy
