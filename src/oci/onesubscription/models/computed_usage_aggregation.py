# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputedUsageAggregation(object):
    """
    Computed Usage Aggregation object
    """

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "PROMOTION"
    TYPE_PROMOTION = "PROMOTION"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "DO_NOT_BILL"
    TYPE_DO_NOT_BILL = "DO_NOT_BILL"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "USAGE"
    TYPE_USAGE = "USAGE"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "COMMIT"
    TYPE_COMMIT = "COMMIT"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "OVERAGE"
    TYPE_OVERAGE = "OVERAGE"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "PAY_AS_YOU_GO"
    TYPE_PAY_AS_YOU_GO = "PAY_AS_YOU_GO"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "MONTHLY_MINIMUM"
    TYPE_MONTHLY_MINIMUM = "MONTHLY_MINIMUM"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "DELAYED_USAGE_INVOICE_TIMING"
    TYPE_DELAYED_USAGE_INVOICE_TIMING = "DELAYED_USAGE_INVOICE_TIMING"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "DELAYED_USAGE_COMMITMENT_EXP"
    TYPE_DELAYED_USAGE_COMMITMENT_EXP = "DELAYED_USAGE_COMMITMENT_EXP"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "ON_ACCOUNT_CREDIT"
    TYPE_ON_ACCOUNT_CREDIT = "ON_ACCOUNT_CREDIT"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "SERVICE_CREDIT"
    TYPE_SERVICE_CREDIT = "SERVICE_CREDIT"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "COMMITMENT_EXPIRATION"
    TYPE_COMMITMENT_EXPIRATION = "COMMITMENT_EXPIRATION"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "FUNDED_ALLOCATION"
    TYPE_FUNDED_ALLOCATION = "FUNDED_ALLOCATION"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "DONOT_BILL_USAGE_POST_TERMINATION"
    TYPE_DONOT_BILL_USAGE_POST_TERMINATION = "DONOT_BILL_USAGE_POST_TERMINATION"

    #: A constant which can be used with the type property of a ComputedUsageAggregation.
    #: This constant has a value of "DELAYED_USAGE_POST_TERMINATION"
    TYPE_DELAYED_USAGE_POST_TERMINATION = "DELAYED_USAGE_POST_TERMINATION"

    def __init__(self, **kwargs):
        """
        Initializes a new ComputedUsageAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param quantity:
            The value to assign to the quantity property of this ComputedUsageAggregation.
        :type quantity: str

        :param product:
            The value to assign to the product property of this ComputedUsageAggregation.
        :type product: oci.onesubscription.models.ComputedUsageProduct

        :param data_center:
            The value to assign to the data_center property of this ComputedUsageAggregation.
        :type data_center: str

        :param time_metered_on:
            The value to assign to the time_metered_on property of this ComputedUsageAggregation.
        :type time_metered_on: datetime

        :param net_unit_price:
            The value to assign to the net_unit_price property of this ComputedUsageAggregation.
        :type net_unit_price: str

        :param cost_unrounded:
            The value to assign to the cost_unrounded property of this ComputedUsageAggregation.
        :type cost_unrounded: str

        :param cost:
            The value to assign to the cost property of this ComputedUsageAggregation.
        :type cost: str

        :param type:
            The value to assign to the type property of this ComputedUsageAggregation.
            Allowed values for this property are: "PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", "COMMITMENT_EXPIRATION", "FUNDED_ALLOCATION", "DONOT_BILL_USAGE_POST_TERMINATION", "DELAYED_USAGE_POST_TERMINATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'quantity': 'str',
            'product': 'ComputedUsageProduct',
            'data_center': 'str',
            'time_metered_on': 'datetime',
            'net_unit_price': 'str',
            'cost_unrounded': 'str',
            'cost': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'quantity': 'quantity',
            'product': 'product',
            'data_center': 'dataCenter',
            'time_metered_on': 'timeMeteredOn',
            'net_unit_price': 'netUnitPrice',
            'cost_unrounded': 'costUnrounded',
            'cost': 'cost',
            'type': 'type'
        }

        self._quantity = None
        self._product = None
        self._data_center = None
        self._time_metered_on = None
        self._net_unit_price = None
        self._cost_unrounded = None
        self._cost = None
        self._type = None

    @property
    def quantity(self):
        """
        Gets the quantity of this ComputedUsageAggregation.
        Total Quantity that was used for computation


        :return: The quantity of this ComputedUsageAggregation.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ComputedUsageAggregation.
        Total Quantity that was used for computation


        :param quantity: The quantity of this ComputedUsageAggregation.
        :type: str
        """
        self._quantity = quantity

    @property
    def product(self):
        """
        Gets the product of this ComputedUsageAggregation.

        :return: The product of this ComputedUsageAggregation.
        :rtype: oci.onesubscription.models.ComputedUsageProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this ComputedUsageAggregation.

        :param product: The product of this ComputedUsageAggregation.
        :type: oci.onesubscription.models.ComputedUsageProduct
        """
        self._product = product

    @property
    def data_center(self):
        """
        Gets the data_center of this ComputedUsageAggregation.
        Data Center Attribute as sent by MQS to SPM.


        :return: The data_center of this ComputedUsageAggregation.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """
        Sets the data_center of this ComputedUsageAggregation.
        Data Center Attribute as sent by MQS to SPM.


        :param data_center: The data_center of this ComputedUsageAggregation.
        :type: str
        """
        self._data_center = data_center

    @property
    def time_metered_on(self):
        """
        Gets the time_metered_on of this ComputedUsageAggregation.
        Metered Service date , expressed in RFC 3339 timestamp format.


        :return: The time_metered_on of this ComputedUsageAggregation.
        :rtype: datetime
        """
        return self._time_metered_on

    @time_metered_on.setter
    def time_metered_on(self, time_metered_on):
        """
        Sets the time_metered_on of this ComputedUsageAggregation.
        Metered Service date , expressed in RFC 3339 timestamp format.


        :param time_metered_on: The time_metered_on of this ComputedUsageAggregation.
        :type: datetime
        """
        self._time_metered_on = time_metered_on

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this ComputedUsageAggregation.
        Net Unit Price for the product in consideration.


        :return: The net_unit_price of this ComputedUsageAggregation.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this ComputedUsageAggregation.
        Net Unit Price for the product in consideration.


        :param net_unit_price: The net_unit_price of this ComputedUsageAggregation.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def cost_unrounded(self):
        """
        Gets the cost_unrounded of this ComputedUsageAggregation.
        Sum of Computed Line Amount unrounded


        :return: The cost_unrounded of this ComputedUsageAggregation.
        :rtype: str
        """
        return self._cost_unrounded

    @cost_unrounded.setter
    def cost_unrounded(self, cost_unrounded):
        """
        Sets the cost_unrounded of this ComputedUsageAggregation.
        Sum of Computed Line Amount unrounded


        :param cost_unrounded: The cost_unrounded of this ComputedUsageAggregation.
        :type: str
        """
        self._cost_unrounded = cost_unrounded

    @property
    def cost(self):
        """
        Gets the cost of this ComputedUsageAggregation.
        Sum of Computed Line Amount rounded


        :return: The cost of this ComputedUsageAggregation.
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this ComputedUsageAggregation.
        Sum of Computed Line Amount rounded


        :param cost: The cost of this ComputedUsageAggregation.
        :type: str
        """
        self._cost = cost

    @property
    def type(self):
        """
        Gets the type of this ComputedUsageAggregation.
        Usage compute type in SPM.

        Allowed values for this property are: "PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", "COMMITMENT_EXPIRATION", "FUNDED_ALLOCATION", "DONOT_BILL_USAGE_POST_TERMINATION", "DELAYED_USAGE_POST_TERMINATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ComputedUsageAggregation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ComputedUsageAggregation.
        Usage compute type in SPM.


        :param type: The type of this ComputedUsageAggregation.
        :type: str
        """
        allowed_values = ["PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", "COMMITMENT_EXPIRATION", "FUNDED_ALLOCATION", "DONOT_BILL_USAGE_POST_TERMINATION", "DELAYED_USAGE_POST_TERMINATION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other