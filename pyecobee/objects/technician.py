"""
This module is home to the Technician class
"""
from pyecobee.ecobee_object import EcobeeObject


class Technician(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Technician.shtml

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
        '_contractor_ref',
        '_name',
        '_phone',
        '_street_address',
        '_city',
        '_province_state',
        '_country',
        '_postal_code',
        '_email',
        '_web']

    attribute_name_map = {
        'contractor_ref': 'contractorRef',
        'contractorRef': 'contractor_ref',
        'name': 'name',
        'phone': 'phone',
        'street_address': 'streetAddress',
        'streetAddress': 'street_address',
        'city': 'city',
        'province_state': 'provinceState',
        'provinceState': 'province_state',
        'country': 'country',
        'postal_code': 'postalCode',
        'postalCode': 'postal_code',
        'email': 'email',
        'web': 'web'}

    attribute_type_map = {
        'contractor_ref': 'six.text_type',
        'name': 'six.text_type',
        'phone': 'six.text_type',
        'street_address': 'six.text_type',
        'city': 'six.text_type',
        'province_state': 'six.text_type',
        'country': 'six.text_type',
        'postal_code': 'six.text_type',
        'email': 'six.text_type',
        'web': 'six.text_type'}

    def __init__(self, contractor_ref=None, name=None, phone=None, street_address=None, city=None,
                 province_state=None, country=None, postal_code=None, email=None, web=None):
        """
        Construct a Technician instance
        """
        self._contractor_ref = contractor_ref
        self._name = name
        self._phone = phone
        self._street_address = street_address
        self._city = city
        self._province_state = province_state
        self._country = country
        self._postal_code = postal_code
        self._email = email
        self._web = web

    @property
    def contractor_ref(self):
        """
        Gets the contractor_ref attribute of this Technician instance.

        :return: The value of the contractor_ref attribute of this
        Technician instance.
        :rtype: six.text_type
        """

        return self._contractor_ref

    @property
    def name(self):
        """
        Gets the name attribute of this Technician instance.

        :return: The value of the name attribute of this Technician
        instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def phone(self):
        """
        Gets the phone attribute of this Technician instance.

        :return: The value of the phone attribute of this Technician
        instance.
        :rtype: six.text_type
        """

        return self._phone

    @property
    def street_address(self):
        """
        Gets the street_address attribute of this Technician instance.

        :return: The value of the street_address attribute of this
        Technician instance.
        :rtype: six.text_type
        """

        return self._street_address

    @property
    def city(self):
        """
        Gets the city attribute of this Technician instance.

        :return: The value of the city attribute of this Technician
        instance.
        :rtype: six.text_type
        """

        return self._city

    @property
    def province_state(self):
        """
        Gets the province_state attribute of this Technician instance.

        :return: The value of the province_state attribute of this
        Technician instance.
        :rtype: six.text_type
        """

        return self._province_state

    @property
    def country(self):
        """
        Gets the country attribute of this Technician instance.

        :return: The value of the country attribute of this Technician
        instance.
        :rtype: six.text_type
        """

        return self._country

    @property
    def postal_code(self):
        """
        Gets the postal_code attribute of this Technician instance.

        :return: The value of the postal_code attribute of this
        Technician instance.
        :rtype: six.text_type
        """

        return self._postal_code

    @property
    def email(self):
        """
        Gets the email attribute of this Technician instance.

        :return: The value of the email attribute of this Technician
        instance.
        :rtype: six.text_type
        """

        return self._email

    @property
    def web(self):
        """
        Gets the web attribute of this Technician instance.

        :return: The value of the web attribute of this Technician
        instance.
        :rtype: six.text_type
        """

        return self._web
