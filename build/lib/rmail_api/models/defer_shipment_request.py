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

class DeferShipmentRequest(object):
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
        'shipment_id': 'str',
        'shipment_date': 'date'
    }

    attribute_map = {
        'shipment_id': 'ShipmentId',
        'shipment_date': 'ShipmentDate'
    }

    def __init__(self, shipment_id=None, shipment_date=None):  # noqa: E501
        """DeferShipmentRequest - a model defined in Swagger"""  # noqa: E501
        self._shipment_id = None
        self._shipment_date = None
        self.discriminator = None
        self.shipment_id = shipment_id
        self.shipment_date = shipment_date

    @property
    def shipment_id(self):
        """Gets the shipment_id of this DeferShipmentRequest.  # noqa: E501

        Shipment Id <br />The shipment to apply the change to. <br />             <br />The Shipment Id may be an id or a tracking/barcode number.  # noqa: E501

        :return: The shipment_id of this DeferShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this DeferShipmentRequest.

        Shipment Id <br />The shipment to apply the change to. <br />             <br />The Shipment Id may be an id or a tracking/barcode number.  # noqa: E501

        :param shipment_id: The shipment_id of this DeferShipmentRequest.  # noqa: E501
        :type: str
        """
        if shipment_id is None:
            raise ValueError("Invalid value for `shipment_id`, must not be `None`")  # noqa: E501

        self._shipment_id = shipment_id

    @property
    def shipment_date(self):
        """Gets the shipment_date of this DeferShipmentRequest.  # noqa: E501

        Shipment Date <br />The new date that the packages are being shipped. <br />The date must not be in the past and cannot be more than 28 days in the future. <br />             <br />Accepted Format: YYYY-MM-DD  # noqa: E501

        :return: The shipment_date of this DeferShipmentRequest.  # noqa: E501
        :rtype: date
        """
        return self._shipment_date

    @shipment_date.setter
    def shipment_date(self, shipment_date):
        """Sets the shipment_date of this DeferShipmentRequest.

        Shipment Date <br />The new date that the packages are being shipped. <br />The date must not be in the past and cannot be more than 28 days in the future. <br />             <br />Accepted Format: YYYY-MM-DD  # noqa: E501

        :param shipment_date: The shipment_date of this DeferShipmentRequest.  # noqa: E501
        :type: date
        """
        if shipment_date is None:
            raise ValueError("Invalid value for `shipment_date`, must not be `None`")  # noqa: E501

        self._shipment_date = shipment_date

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
        if issubclass(DeferShipmentRequest, dict):
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
        if not isinstance(other, DeferShipmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
