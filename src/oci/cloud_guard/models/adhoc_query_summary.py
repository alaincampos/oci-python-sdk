# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdhocQuerySummary(object):
    """
    Summary information for a adhoc query.
    """

    #: A constant which can be used with the status property of a AdhocQuerySummary.
    #: This constant has a value of "CREATING"
    STATUS_CREATING = "CREATING"

    #: A constant which can be used with the status property of a AdhocQuerySummary.
    #: This constant has a value of "CREATED"
    STATUS_CREATED = "CREATED"

    #: A constant which can be used with the status property of a AdhocQuerySummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a AdhocQuerySummary.
    #: This constant has a value of "PARTIALLY_COMPLETED"
    STATUS_PARTIALLY_COMPLETED = "PARTIALLY_COMPLETED"

    #: A constant which can be used with the status property of a AdhocQuerySummary.
    #: This constant has a value of "EXPIRED"
    STATUS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the status property of a AdhocQuerySummary.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a AdhocQuerySummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AdhocQuerySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AdhocQuerySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AdhocQuerySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AdhocQuerySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AdhocQuerySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AdhocQuerySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AdhocQuerySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AdhocQuerySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AdhocQuerySummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AdhocQuerySummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this AdhocQuerySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AdhocQuerySummary.
        :type time_updated: datetime

        :param status:
            The value to assign to the status property of this AdhocQuerySummary.
            Allowed values for this property are: "CREATING", "CREATED", "IN_PROGRESS", "PARTIALLY_COMPLETED", "EXPIRED", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param adhoc_query_regional_details:
            The value to assign to the adhoc_query_regional_details property of this AdhocQuerySummary.
        :type adhoc_query_regional_details: list[oci.cloud_guard.models.AdhocQueryRegionalDetails]

        :param adhoc_query_details:
            The value to assign to the adhoc_query_details property of this AdhocQuerySummary.
        :type adhoc_query_details: oci.cloud_guard.models.AdhocQueryDetails

        :param error_message:
            The value to assign to the error_message property of this AdhocQuerySummary.
        :type error_message: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AdhocQuerySummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AdhocQuerySummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AdhocQuerySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AdhocQuerySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AdhocQuerySummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'status': 'str',
            'adhoc_query_regional_details': 'list[AdhocQueryRegionalDetails]',
            'adhoc_query_details': 'AdhocQueryDetails',
            'error_message': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'status': 'status',
            'adhoc_query_regional_details': 'adhocQueryRegionalDetails',
            'adhoc_query_details': 'adhocQueryDetails',
            'error_message': 'errorMessage',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._status = None
        self._adhoc_query_regional_details = None
        self._adhoc_query_details = None
        self._error_message = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AdhocQuerySummary.
        OCID for adhoc query


        :return: The id of this AdhocQuerySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AdhocQuerySummary.
        OCID for adhoc query


        :param id: The id of this AdhocQuerySummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AdhocQuerySummary.
        Compartment OCID of the adhoc query


        :return: The compartment_id of this AdhocQuerySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AdhocQuerySummary.
        Compartment OCID of the adhoc query


        :param compartment_id: The compartment_id of this AdhocQuerySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this AdhocQuerySummary.
        The date and time the adhoc query was created. Format defined by RFC3339.


        :return: The time_created of this AdhocQuerySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AdhocQuerySummary.
        The date and time the adhoc query was created. Format defined by RFC3339.


        :param time_created: The time_created of this AdhocQuerySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AdhocQuerySummary.
        The date and time the adhoc query was updated. Format defined by RFC3339.


        :return: The time_updated of this AdhocQuerySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AdhocQuerySummary.
        The date and time the adhoc query was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this AdhocQuerySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AdhocQuerySummary.
        Status of the adhoc query

        Allowed values for this property are: "CREATING", "CREATED", "IN_PROGRESS", "PARTIALLY_COMPLETED", "EXPIRED", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AdhocQuerySummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AdhocQuerySummary.
        Status of the adhoc query


        :param status: The status of this AdhocQuerySummary.
        :type: str
        """
        allowed_values = ["CREATING", "CREATED", "IN_PROGRESS", "PARTIALLY_COMPLETED", "EXPIRED", "COMPLETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def adhoc_query_regional_details(self):
        """
        Gets the adhoc_query_regional_details of this AdhocQuerySummary.
        List of instance level status values for each region


        :return: The adhoc_query_regional_details of this AdhocQuerySummary.
        :rtype: list[oci.cloud_guard.models.AdhocQueryRegionalDetails]
        """
        return self._adhoc_query_regional_details

    @adhoc_query_regional_details.setter
    def adhoc_query_regional_details(self, adhoc_query_regional_details):
        """
        Sets the adhoc_query_regional_details of this AdhocQuerySummary.
        List of instance level status values for each region


        :param adhoc_query_regional_details: The adhoc_query_regional_details of this AdhocQuerySummary.
        :type: list[oci.cloud_guard.models.AdhocQueryRegionalDetails]
        """
        self._adhoc_query_regional_details = adhoc_query_regional_details

    @property
    def adhoc_query_details(self):
        """
        **[Required]** Gets the adhoc_query_details of this AdhocQuerySummary.

        :return: The adhoc_query_details of this AdhocQuerySummary.
        :rtype: oci.cloud_guard.models.AdhocQueryDetails
        """
        return self._adhoc_query_details

    @adhoc_query_details.setter
    def adhoc_query_details(self, adhoc_query_details):
        """
        Sets the adhoc_query_details of this AdhocQuerySummary.

        :param adhoc_query_details: The adhoc_query_details of this AdhocQuerySummary.
        :type: oci.cloud_guard.models.AdhocQueryDetails
        """
        self._adhoc_query_details = adhoc_query_details

    @property
    def error_message(self):
        """
        Gets the error_message of this AdhocQuerySummary.
        Error message to show on UI in case of failure


        :return: The error_message of this AdhocQuerySummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this AdhocQuerySummary.
        Error message to show on UI in case of failure


        :param error_message: The error_message of this AdhocQuerySummary.
        :type: str
        """
        self._error_message = error_message

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AdhocQuerySummary.
        The current lifecycle state of the resource

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AdhocQuerySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AdhocQuerySummary.
        The current lifecycle state of the resource


        :param lifecycle_state: The lifecycle_state of this AdhocQuerySummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AdhocQuerySummary.
        A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.


        :return: The lifecycle_details of this AdhocQuerySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AdhocQuerySummary.
        A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.


        :param lifecycle_details: The lifecycle_details of this AdhocQuerySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AdhocQuerySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this AdhocQuerySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AdhocQuerySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this AdhocQuerySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AdhocQuerySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AdhocQuerySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AdhocQuerySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AdhocQuerySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AdhocQuerySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this AdhocQuerySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AdhocQuerySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this AdhocQuerySummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other