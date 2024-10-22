# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActionGroupDetails(object):
    """
    Action Group details.
    """

    #: A constant which can be used with the type property of a ActionGroupDetails.
    #: This constant has a value of "PRODUCT"
    TYPE_PRODUCT = "PRODUCT"

    #: A constant which can be used with the type property of a ActionGroupDetails.
    #: This constant has a value of "ENVIRONMENT"
    TYPE_ENVIRONMENT = "ENVIRONMENT"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "WAITING"
    STATUS_WAITING = "WAITING"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "SKIPPED"
    STATUS_SKIPPED = "SKIPPED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "IGNORED"
    STATUS_IGNORED = "IGNORED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "NOT_APPLICABLE"
    STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "ABORTED"
    STATUS_ABORTED = "ABORTED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "TIMED_OUT"
    STATUS_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "PAUSED"
    STATUS_PAUSED = "PAUSED"

    def __init__(self, **kwargs):
        """
        Initializes a new ActionGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this ActionGroupDetails.
        :type resource_id: str

        :param name:
            The value to assign to the name property of this ActionGroupDetails.
        :type name: str

        :param type:
            The value to assign to the type property of this ActionGroupDetails.
            Allowed values for this property are: "PRODUCT", "ENVIRONMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param application_type:
            The value to assign to the application_type property of this ActionGroupDetails.
        :type application_type: str

        :param product:
            The value to assign to the product property of this ActionGroupDetails.
        :type product: str

        :param lifecycle_operation:
            The value to assign to the lifecycle_operation property of this ActionGroupDetails.
        :type lifecycle_operation: str

        :param activity_id:
            The value to assign to the activity_id property of this ActionGroupDetails.
        :type activity_id: str

        :param status:
            The value to assign to the status property of this ActionGroupDetails.
            Allowed values for this property are: "ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_started:
            The value to assign to the time_started property of this ActionGroupDetails.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this ActionGroupDetails.
        :type time_ended: datetime

        :param runbook_id:
            The value to assign to the runbook_id property of this ActionGroupDetails.
        :type runbook_id: str

        """
        self.swagger_types = {
            'resource_id': 'str',
            'name': 'str',
            'type': 'str',
            'application_type': 'str',
            'product': 'str',
            'lifecycle_operation': 'str',
            'activity_id': 'str',
            'status': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'runbook_id': 'str'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'name': 'name',
            'type': 'type',
            'application_type': 'applicationType',
            'product': 'product',
            'lifecycle_operation': 'lifecycleOperation',
            'activity_id': 'activityId',
            'status': 'status',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'runbook_id': 'runbookId'
        }

        self._resource_id = None
        self._name = None
        self._type = None
        self._application_type = None
        self._product = None
        self._lifecycle_operation = None
        self._activity_id = None
        self._status = None
        self._time_started = None
        self._time_ended = None
        self._runbook_id = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this ActionGroupDetails.
        The ID of the ActionGroup resource.
        Ex:fleetId.


        :return: The resource_id of this ActionGroupDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ActionGroupDetails.
        The ID of the ActionGroup resource.
        Ex:fleetId.


        :param resource_id: The resource_id of this ActionGroupDetails.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        """
        Gets the name of this ActionGroupDetails.
        Name of the ActionGroup.


        :return: The name of this ActionGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ActionGroupDetails.
        Name of the ActionGroup.


        :param name: The name of this ActionGroupDetails.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ActionGroupDetails.
        Type of the ActionGroup

        Allowed values for this property are: "PRODUCT", "ENVIRONMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ActionGroupDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ActionGroupDetails.
        Type of the ActionGroup


        :param type: The type of this ActionGroupDetails.
        :type: str
        """
        allowed_values = ["PRODUCT", "ENVIRONMENT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def application_type(self):
        """
        Gets the application_type of this ActionGroupDetails.
        Application Type associated.
        Only applicable if actionGroup type is ENVIRONMENT.


        :return: The application_type of this ActionGroupDetails.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this ActionGroupDetails.
        Application Type associated.
        Only applicable if actionGroup type is ENVIRONMENT.


        :param application_type: The application_type of this ActionGroupDetails.
        :type: str
        """
        self._application_type = application_type

    @property
    def product(self):
        """
        Gets the product of this ActionGroupDetails.
        Product associated.
        Only applicable if actionGroup type is PRODUCT.


        :return: The product of this ActionGroupDetails.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this ActionGroupDetails.
        Product associated.
        Only applicable if actionGroup type is PRODUCT.


        :param product: The product of this ActionGroupDetails.
        :type: str
        """
        self._product = product

    @property
    def lifecycle_operation(self):
        """
        Gets the lifecycle_operation of this ActionGroupDetails.
        LifeCycle Operation.


        :return: The lifecycle_operation of this ActionGroupDetails.
        :rtype: str
        """
        return self._lifecycle_operation

    @lifecycle_operation.setter
    def lifecycle_operation(self, lifecycle_operation):
        """
        Sets the lifecycle_operation of this ActionGroupDetails.
        LifeCycle Operation.


        :param lifecycle_operation: The lifecycle_operation of this ActionGroupDetails.
        :type: str
        """
        self._lifecycle_operation = lifecycle_operation

    @property
    def activity_id(self):
        """
        Gets the activity_id of this ActionGroupDetails.
        Unique producer Id at Action Group Level


        :return: The activity_id of this ActionGroupDetails.
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """
        Sets the activity_id of this ActionGroupDetails.
        Unique producer Id at Action Group Level


        :param activity_id: The activity_id of this ActionGroupDetails.
        :type: str
        """
        self._activity_id = activity_id

    @property
    def status(self):
        """
        Gets the status of this ActionGroupDetails.
        Status of the Job at Action Group Level.

        Allowed values for this property are: "ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ActionGroupDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ActionGroupDetails.
        Status of the Job at Action Group Level.


        :param status: The status of this ActionGroupDetails.
        :type: str
        """
        allowed_values = ["ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_started(self):
        """
        Gets the time_started of this ActionGroupDetails.
        The time the Scheduler Job started. An RFC3339 formatted datetime string.


        :return: The time_started of this ActionGroupDetails.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this ActionGroupDetails.
        The time the Scheduler Job started. An RFC3339 formatted datetime string.


        :param time_started: The time_started of this ActionGroupDetails.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this ActionGroupDetails.
        The time the Scheduler Job ended. An RFC3339 formatted datetime string.


        :return: The time_ended of this ActionGroupDetails.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this ActionGroupDetails.
        The time the Scheduler Job ended. An RFC3339 formatted datetime string.


        :param time_ended: The time_ended of this ActionGroupDetails.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def runbook_id(self):
        """
        **[Required]** Gets the runbook_id of this ActionGroupDetails.
        OCID of the runbook.


        :return: The runbook_id of this ActionGroupDetails.
        :rtype: str
        """
        return self._runbook_id

    @runbook_id.setter
    def runbook_id(self, runbook_id):
        """
        Sets the runbook_id of this ActionGroupDetails.
        OCID of the runbook.


        :param runbook_id: The runbook_id of this ActionGroupDetails.
        :type: str
        """
        self._runbook_id = runbook_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
