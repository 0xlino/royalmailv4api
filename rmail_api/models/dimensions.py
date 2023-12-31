# coding: utf-8

"""
    PRO SHIPPING API

    # Introduction Here you will find requirements for integrating with PRO SHIPPING API.  The documentation specifically covers how the API can be used by business customers to conduct shipping activity with available carriers and provides the technical information to build this integration. The API allows customers to create and manage shipments, produce labels, customs documentation, and collection manifests, retrieve reference data such as carriers and countries, and maintain their own data such as shipping account details.  Pro Shipping API is a fully RESTful service implemented using JSON messaging. You, as the customer are responsible for sending JSON messages and for maintaining the capability of receiving JSON messages in the format described in this specification. Request and response examples for each API service are included in this specification.  # Authentication  The PRO SHIPPING API uses OAuth2 authentication.  To request the authorization token you need to create API credentials (Client ID and Secret) on the system first. If you have not done it already, log into your account and go to API Credentials or follow the link [add a link here with the path to the API Credentials menu]. Use the credentials to retrieve the authorization token.  Note: Make sure you copy the Secret and keep it secure as you won't be able to view it again on the system.  <!-- ReDoc-Inject: <SecurityDefinitions /> -->   # noqa: E501

    OpenAPI spec version: v4.0-RM
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Dimensions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'length': 'float',
        'width': 'float',
        'height': 'float'
    }

    attribute_map = {
        'length': 'Length',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, length=None, width=None, height=None):  # noqa: E501
        """Dimensions - a model defined in Swagger"""  # noqa: E501
        self._length = None
        self._width = None
        self._height = None
        self.discriminator = None
        self.length = length
        self.width = width
        self.height = height

    @property
    def length(self):
        """Gets the length of this Dimensions.  # noqa: E501

        The length of the shipment package in the unit of measure specified in the DimensionsUnitOfMeasure field (DimensionsUnitOfMeasure defaults to CM if not provided). <br />The maximum length accepted is dependent on the service and package type.  # noqa: E501

        :return: The length of this Dimensions.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Dimensions.

        The length of the shipment package in the unit of measure specified in the DimensionsUnitOfMeasure field (DimensionsUnitOfMeasure defaults to CM if not provided). <br />The maximum length accepted is dependent on the service and package type.  # noqa: E501

        :param length: The length of this Dimensions.  # noqa: E501
        :type: float
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def width(self):
        """Gets the width of this Dimensions.  # noqa: E501

        The width of the shipment package in the unit of measure specified in the DimensionsUnitOfMeasure field (DimensionsUnitOfMeasure defaults to CM if not provided). <br />The maximum width accepted is dependent on the service and package type.  # noqa: E501

        :return: The width of this Dimensions.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Dimensions.

        The width of the shipment package in the unit of measure specified in the DimensionsUnitOfMeasure field (DimensionsUnitOfMeasure defaults to CM if not provided). <br />The maximum width accepted is dependent on the service and package type.  # noqa: E501

        :param width: The width of this Dimensions.  # noqa: E501
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this Dimensions.  # noqa: E501

        The height of the shipment package in the unit of measure specified in the DimensionsUnitOfMeasure field (DimensionsUnitOfMeasure defaults to CM if not provided). <br />The maximum height accepted is dependent on the service and package type.  # noqa: E501

        :return: The height of this Dimensions.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Dimensions.

        The height of the shipment package in the unit of measure specified in the DimensionsUnitOfMeasure field (DimensionsUnitOfMeasure defaults to CM if not provided). <br />The maximum height accepted is dependent on the service and package type.  # noqa: E501

        :param height: The height of this Dimensions.  # noqa: E501
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Dimensions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Dimensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
