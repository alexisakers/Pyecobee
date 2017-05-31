"""
This module is home to the Alert class
"""
from pyecobee.ecobee_object import EcobeeObject


class Alert(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Alert.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_text', '_acknowledge_ref', '_date', '_time', '_severity', '_alert_number', '_alert_type',
                 '_is_operator_alert', '_reminder', '_show_idt', '_show_web', '_send_email', '_acknowledgement',
                 '_remind_me_later', '_thermostat_identifier', '_notification_type']

    attribute_name_map = {'text': 'text', 'acknowledge_ref': 'acknowledgeRef', 'acknowledgeRef': 'acknowledge_ref',
                          'date': 'date', 'time': 'time', 'severity': 'severity', 'alert_number': 'alertNumber',
                          'alertNumber': 'alert_number', 'alert_type': 'alertType', 'alertType': 'alert_type',
                          'is_operator_alert': 'isOperatorAlert', 'isOperatorAlert': 'is_operator_alert',
                          'reminder': 'reminder', 'show_idt': 'showIdt', 'showIdt': 'show_idt', 'show_web': 'showWeb',
                          'showWeb': 'show_web', 'send_email': 'sendEmail', 'sendEmail': 'send_email',
                          'acknowledgement': 'acknowledgement', 'remind_me_later': 'remindMeLater',
                          'remindMeLater': 'remind_me_later', 'thermostat_identifier': 'thermostatIdentifier',
                          'thermostatIdentifier': 'thermostat_identifier', 'notification_type': 'notificationType',
                          'notificationType': 'notification_type'}

    attribute_type_map = {'text': 'six.text_type', 'acknowledge_ref': 'six.text_type', 'date': 'six.text_type',
                          'time': 'six.text_type', 'severity': 'six.text_type', 'alert_number': 'int',
                          'alert_type': 'six.text_type', 'is_operator_alert': 'bool', 'reminder': 'six.text_type',
                          'show_idt': 'bool', 'show_web': 'bool', 'send_email': 'bool',
                          'acknowledgement': 'six.text_type', 'remind_me_later': 'bool',
                          'thermostat_identifier': 'six.text_type', 'notification_type': 'six.text_type'}

    def __init__(self, text, acknowledge_ref=None, date=None, time=None, severity=None, alert_number=None,
                 alert_type=None, is_operator_alert=None, reminder=None, show_idt=None, show_web=None, send_email=None,
                 acknowledgement=None, remind_me_later=None, thermostat_identifier=None, notification_type=None):
        """
        Construct an Alert instance
        """
        self._text = text
        self._acknowledge_ref = acknowledge_ref
        self._date = date
        self._time = time
        self._severity = severity
        self._alert_number = alert_number
        self._alert_type = alert_type
        self._is_operator_alert = is_operator_alert
        self._reminder = reminder
        self._show_idt = show_idt
        self._show_web = show_web
        self._send_email = send_email
        self._acknowledgement = acknowledgement
        self._remind_me_later = remind_me_later
        self._thermostat_identifier = thermostat_identifier
        self._notification_type = notification_type

    @property
    def text(self):
        """
        Gets the text attribute of this Alert instance.

        :return: The value of the text attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._text

    @property
    def acknowledge_ref(self):
        """
        Gets the acknowledge_ref attribute of this Alert instance.

        :return: The value of the acknowledge_ref attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._acknowledge_ref

    @property
    def date(self):
        """
        Gets the date attribute of this Alert instance.

        :return: The value of the date attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._date

    @property
    def time(self):
        """
        Gets the time attribute of this Alert instance.

        :return: The value of the time attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._time

    @property
    def severity(self):
        """
        Gets the severity attribute of this Alert instance.

        :return: The value of the severity attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._severity

    @property
    def alert_number(self):
        """
        Gets the alert_number attribute of this Alert instance.

        :return: The value of the alert_number attribute of this Alert instance.
        :rtype: int
        """

        return self._alert_number

    @property
    def alert_type(self):
        """
        Gets the alert_type attribute of this Alert instance.

        :return: The value of the alert_type attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._alert_type

    @property
    def is_operator_alert(self):
        """
        Gets the is_operator_alert attribute of this Alert instance.

        :return: The value of the is_operator_alert attribute of this Alert instance.
        :rtype: bool
        """

        return self._is_operator_alert

    @property
    def reminder(self):
        """
        Gets the reminder attribute of this Alert instance.

        :return: The value of the reminder attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._reminder

    @property
    def show_idt(self):
        """
        Gets the show_idt attribute of this Alert instance.

        :return: The value of the show_idt attribute of this Alert instance.
        :rtype: bool
        """

        return self._show_idt

    @property
    def show_web(self):
        """
        Gets the show_web attribute of this Alert instance.

        :return: The value of the show_web attribute of this Alert instance.
        :rtype: bool
        """

        return self._show_web

    @property
    def send_email(self):
        """
        Gets the send_email attribute of this Alert instance.

        :return: The value of the send_email attribute of this Alert instance.
        :rtype: bool
        """

        return self._send_email

    @property
    def acknowledgement(self):
        """
        Gets the acknowledgement attribute of this Alert instance.

        :return: The value of the acknowledgement attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._acknowledgement

    @property
    def remind_me_later(self):
        """
        Gets the remind_me_later attribute of this Alert instance.

        :return: The value of the remind_me_later attribute of this Alert instance.
        :rtype: bool
        """

        return self._remind_me_later

    @property
    def thermostat_identifier(self):
        """
        Gets the thermostat_identifier attribute of this Alert instance.

        :return: The value of the thermostat_identifier attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._thermostat_identifier

    @property
    def notification_type(self):
        """
        Gets the notification_type attribute of this Alert instance.

        :return: The value of the notification_type attribute of this Alert instance.
        :rtype: six.text_type
        """

        return self._notification_type
