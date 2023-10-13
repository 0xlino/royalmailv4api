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

class RoyalMailLabelFormatShipmentInformation(object):
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
        'action': 'CreateShipmentAction',
        'label_format': 'RoyalMailLabelFormat',
        'content_type': 'ContentType',
        'service_code': 'str',
        'description_of_goods': 'str',
        'business_transaction_type': 'BusinessTransactionType',
        'shipment_date': 'date',
        'declared_value': 'float',
        'declared_weight': 'float',
        'currency_code': 'str',
        'weight_unit_of_measure': 'WeightUnitOfMeasure',
        'dimensions_unit_of_measure': 'DimensionsUnitOfMeasure'
    }

    attribute_map = {
        'action': 'Action',
        'label_format': 'LabelFormat',
        'content_type': 'ContentType',
        'service_code': 'ServiceCode',
        'description_of_goods': 'DescriptionOfGoods',
        'business_transaction_type': 'BusinessTransactionType',
        'shipment_date': 'ShipmentDate',
        'declared_value': 'DeclaredValue',
        'declared_weight': 'DeclaredWeight',
        'currency_code': 'CurrencyCode',
        'weight_unit_of_measure': 'WeightUnitOfMeasure',
        'dimensions_unit_of_measure': 'DimensionsUnitOfMeasure'
    }

    def __init__(self, action=None, label_format=None, content_type=None, service_code=None, description_of_goods=None, business_transaction_type=None, shipment_date=None, declared_value=None, declared_weight=None, currency_code=None, weight_unit_of_measure=None, dimensions_unit_of_measure=None):  # noqa: E501
        """RoyalMailLabelFormatShipmentInformation - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._label_format = None
        self._content_type = None
        self._service_code = None
        self._description_of_goods = None
        self._business_transaction_type = None
        self._shipment_date = None
        self._declared_value = None
        self._declared_weight = None
        self._currency_code = None
        self._weight_unit_of_measure = None
        self._dimensions_unit_of_measure = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if label_format is not None:
            self.label_format = label_format
        self.content_type = content_type
        self.service_code = service_code
        self.description_of_goods = description_of_goods
        if business_transaction_type is not None:
            self.business_transaction_type = business_transaction_type
        if shipment_date is not None:
            self.shipment_date = shipment_date
        if declared_value is not None:
            self.declared_value = declared_value
        if declared_weight is not None:
            self.declared_weight = declared_weight
        if currency_code is not None:
            self.currency_code = currency_code
        if weight_unit_of_measure is not None:
            self.weight_unit_of_measure = weight_unit_of_measure
        if dimensions_unit_of_measure is not None:
            self.dimensions_unit_of_measure = dimensions_unit_of_measure

    @property
    def action(self):
        """Gets the action of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501


        :return: The action of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: CreateShipmentAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RoyalMailLabelFormatShipmentInformation.


        :param action: The action of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: CreateShipmentAction
        """

        self._action = action

    @property
    def label_format(self):
        """Gets the label_format of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501


        :return: The label_format of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: RoyalMailLabelFormat
        """
        return self._label_format

    @label_format.setter
    def label_format(self, label_format):
        """Sets the label_format of this RoyalMailLabelFormatShipmentInformation.


        :param label_format: The label_format of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: RoyalMailLabelFormat
        """

        self._label_format = label_format

    @property
    def content_type(self):
        """Gets the content_type of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501


        :return: The content_type of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: ContentType
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this RoyalMailLabelFormatShipmentInformation.


        :param content_type: The content_type of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: ContentType
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def service_code(self):
        """Gets the service_code of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501

        The code of the shipping service used to deliver the shipment.  # noqa: E501

        :return: The service_code of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this RoyalMailLabelFormatShipmentInformation.

        The code of the shipping service used to deliver the shipment.  # noqa: E501

        :param service_code: The service_code of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: str
        """
        if service_code is None:
            raise ValueError("Invalid value for `service_code`, must not be `None`")  # noqa: E501

        self._service_code = service_code

    @property
    def description_of_goods(self):
        """Gets the description_of_goods of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501

        A general description of the type of goods being sent.  # noqa: E501

        :return: The description_of_goods of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: str
        """
        return self._description_of_goods

    @description_of_goods.setter
    def description_of_goods(self, description_of_goods):
        """Sets the description_of_goods of this RoyalMailLabelFormatShipmentInformation.

        A general description of the type of goods being sent.  # noqa: E501

        :param description_of_goods: The description_of_goods of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: str
        """
        if description_of_goods is None:
            raise ValueError("Invalid value for `description_of_goods`, must not be `None`")  # noqa: E501

        self._description_of_goods = description_of_goods

    @property
    def business_transaction_type(self):
        """Gets the business_transaction_type of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501


        :return: The business_transaction_type of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: BusinessTransactionType
        """
        return self._business_transaction_type

    @business_transaction_type.setter
    def business_transaction_type(self, business_transaction_type):
        """Sets the business_transaction_type of this RoyalMailLabelFormatShipmentInformation.


        :param business_transaction_type: The business_transaction_type of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: BusinessTransactionType
        """

        self._business_transaction_type = business_transaction_type

    @property
    def shipment_date(self):
        """Gets the shipment_date of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501

        The date the shipment packages will be shipped. <br />Shipment Date cannot be in the past and cannot be more than 28 days in the future. <br />Defaults to the current date if not populated. <br />Accepted Format: YYYY-MM-DD  # noqa: E501

        :return: The shipment_date of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: date
        """
        return self._shipment_date

    @shipment_date.setter
    def shipment_date(self, shipment_date):
        """Sets the shipment_date of this RoyalMailLabelFormatShipmentInformation.

        The date the shipment packages will be shipped. <br />Shipment Date cannot be in the past and cannot be more than 28 days in the future. <br />Defaults to the current date if not populated. <br />Accepted Format: YYYY-MM-DD  # noqa: E501

        :param shipment_date: The shipment_date of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: date
        """

        self._shipment_date = shipment_date

    @property
    def declared_value(self):
        """Gets the declared_value of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501

        The declared value of the total shipment in the currency specified. <br />If provided, the value must be equal to or greater than the sum of all item values. <br />If not provided it defaults to the sum of all item values. <br />Ignored for Non-Consignment Services where multiple packages are declared - use the Declared Value at package level instead.  # noqa: E501

        :return: The declared_value of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: float
        """
        return self._declared_value

    @declared_value.setter
    def declared_value(self, declared_value):
        """Sets the declared_value of this RoyalMailLabelFormatShipmentInformation.

        The declared value of the total shipment in the currency specified. <br />If provided, the value must be equal to or greater than the sum of all item values. <br />If not provided it defaults to the sum of all item values. <br />Ignored for Non-Consignment Services where multiple packages are declared - use the Declared Value at package level instead.  # noqa: E501

        :param declared_value: The declared_value of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: float
        """

        self._declared_value = declared_value

    @property
    def declared_weight(self):
        """Gets the declared_weight of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501

        The declared weight of the total shipment in the unit of measure specified by WeightUnitOfMeasure (defaults to KG). <br />The minimum weight allowed is 1 gram. <br />The maximum weight is dependent on the carrier / service / destination. <br />The weight must be equal to or greater than the sum of all package weights and/or item weights. <br />Required for Consignment Services. <br />Ignored for Non-Consignment Services - use the Declared Weight at package level instead.  # noqa: E501

        :return: The declared_weight of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: float
        """
        return self._declared_weight

    @declared_weight.setter
    def declared_weight(self, declared_weight):
        """Sets the declared_weight of this RoyalMailLabelFormatShipmentInformation.

        The declared weight of the total shipment in the unit of measure specified by WeightUnitOfMeasure (defaults to KG). <br />The minimum weight allowed is 1 gram. <br />The maximum weight is dependent on the carrier / service / destination. <br />The weight must be equal to or greater than the sum of all package weights and/or item weights. <br />Required for Consignment Services. <br />Ignored for Non-Consignment Services - use the Declared Weight at package level instead.  # noqa: E501

        :param declared_weight: The declared_weight of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: float
        """

        self._declared_weight = declared_weight

    @property
    def currency_code(self):
        """Gets the currency_code of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501

        The currency code used for any monetary value related to the shipment. <br />3 letter ISO Currency Code. <br />*Required if any monetary values other than zero are provided.*  # noqa: E501

        :return: The currency_code of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this RoyalMailLabelFormatShipmentInformation.

        The currency code used for any monetary value related to the shipment. <br />3 letter ISO Currency Code. <br />*Required if any monetary values other than zero are provided.*  # noqa: E501

        :param currency_code: The currency_code of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def weight_unit_of_measure(self):
        """Gets the weight_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501


        :return: The weight_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: WeightUnitOfMeasure
        """
        return self._weight_unit_of_measure

    @weight_unit_of_measure.setter
    def weight_unit_of_measure(self, weight_unit_of_measure):
        """Sets the weight_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.


        :param weight_unit_of_measure: The weight_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: WeightUnitOfMeasure
        """

        self._weight_unit_of_measure = weight_unit_of_measure

    @property
    def dimensions_unit_of_measure(self):
        """Gets the dimensions_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501


        :return: The dimensions_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :rtype: DimensionsUnitOfMeasure
        """
        return self._dimensions_unit_of_measure

    @dimensions_unit_of_measure.setter
    def dimensions_unit_of_measure(self, dimensions_unit_of_measure):
        """Sets the dimensions_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.


        :param dimensions_unit_of_measure: The dimensions_unit_of_measure of this RoyalMailLabelFormatShipmentInformation.  # noqa: E501
        :type: DimensionsUnitOfMeasure
        """

        self._dimensions_unit_of_measure = dimensions_unit_of_measure

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
        if issubclass(RoyalMailLabelFormatShipmentInformation, dict):
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
        if not isinstance(other, RoyalMailLabelFormatShipmentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
