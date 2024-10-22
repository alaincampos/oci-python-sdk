# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RetentionSetting(object):
    """
    Retention setting details of the model.
    """

    #: A constant which can be used with the customer_notification_type property of a RetentionSetting.
    #: This constant has a value of "NONE"
    CUSTOMER_NOTIFICATION_TYPE_NONE = "NONE"

    #: A constant which can be used with the customer_notification_type property of a RetentionSetting.
    #: This constant has a value of "ALL"
    CUSTOMER_NOTIFICATION_TYPE_ALL = "ALL"

    #: A constant which can be used with the customer_notification_type property of a RetentionSetting.
    #: This constant has a value of "ON_FAILURE"
    CUSTOMER_NOTIFICATION_TYPE_ON_FAILURE = "ON_FAILURE"

    #: A constant which can be used with the customer_notification_type property of a RetentionSetting.
    #: This constant has a value of "ON_SUCCESS"
    CUSTOMER_NOTIFICATION_TYPE_ON_SUCCESS = "ON_SUCCESS"

    def __init__(self, **kwargs):
        """
        Initializes a new RetentionSetting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param archive_after_days:
            The value to assign to the archive_after_days property of this RetentionSetting.
        :type archive_after_days: int

        :param delete_after_days:
            The value to assign to the delete_after_days property of this RetentionSetting.
        :type delete_after_days: int

        :param customer_notification_type:
            The value to assign to the customer_notification_type property of this RetentionSetting.
            Allowed values for this property are: "NONE", "ALL", "ON_FAILURE", "ON_SUCCESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type customer_notification_type: str

        """
        self.swagger_types = {
            'archive_after_days': 'int',
            'delete_after_days': 'int',
            'customer_notification_type': 'str'
        }

        self.attribute_map = {
            'archive_after_days': 'archiveAfterDays',
            'delete_after_days': 'deleteAfterDays',
            'customer_notification_type': 'customerNotificationType'
        }

        self._archive_after_days = None
        self._delete_after_days = None
        self._customer_notification_type = None

    @property
    def archive_after_days(self):
        """
        **[Required]** Gets the archive_after_days of this RetentionSetting.
        Number of days after which the model will be archived.


        :return: The archive_after_days of this RetentionSetting.
        :rtype: int
        """
        return self._archive_after_days

    @archive_after_days.setter
    def archive_after_days(self, archive_after_days):
        """
        Sets the archive_after_days of this RetentionSetting.
        Number of days after which the model will be archived.


        :param archive_after_days: The archive_after_days of this RetentionSetting.
        :type: int
        """
        self._archive_after_days = archive_after_days

    @property
    def delete_after_days(self):
        """
        Gets the delete_after_days of this RetentionSetting.
        Number of days after which the archived model will be deleted.


        :return: The delete_after_days of this RetentionSetting.
        :rtype: int
        """
        return self._delete_after_days

    @delete_after_days.setter
    def delete_after_days(self, delete_after_days):
        """
        Sets the delete_after_days of this RetentionSetting.
        Number of days after which the archived model will be deleted.


        :param delete_after_days: The delete_after_days of this RetentionSetting.
        :type: int
        """
        self._delete_after_days = delete_after_days

    @property
    def customer_notification_type(self):
        """
        Gets the customer_notification_type of this RetentionSetting.
        Customer notification options on success/failure of archival, deletion events.

        Allowed values for this property are: "NONE", "ALL", "ON_FAILURE", "ON_SUCCESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The customer_notification_type of this RetentionSetting.
        :rtype: str
        """
        return self._customer_notification_type

    @customer_notification_type.setter
    def customer_notification_type(self, customer_notification_type):
        """
        Sets the customer_notification_type of this RetentionSetting.
        Customer notification options on success/failure of archival, deletion events.


        :param customer_notification_type: The customer_notification_type of this RetentionSetting.
        :type: str
        """
        allowed_values = ["NONE", "ALL", "ON_FAILURE", "ON_SUCCESS"]
        if not value_allowed_none_or_none_sentinel(customer_notification_type, allowed_values):
            customer_notification_type = 'UNKNOWN_ENUM_VALUE'
        self._customer_notification_type = customer_notification_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
