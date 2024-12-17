# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelProperty(object):
    """
    Global metadata element details.
    """

    #: A constant which can be used with the lifecycle_state property of a ModelProperty.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ModelProperty.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ModelProperty.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the selection property of a ModelProperty.
    #: This constant has a value of "SINGLE_CHOICE"
    SELECTION_SINGLE_CHOICE = "SINGLE_CHOICE"

    #: A constant which can be used with the selection property of a ModelProperty.
    #: This constant has a value of "MULTI_CHOICE"
    SELECTION_MULTI_CHOICE = "MULTI_CHOICE"

    #: A constant which can be used with the selection property of a ModelProperty.
    #: This constant has a value of "DEFAULT_TEXT"
    SELECTION_DEFAULT_TEXT = "DEFAULT_TEXT"

    #: A constant which can be used with the value_type property of a ModelProperty.
    #: This constant has a value of "STRING"
    VALUE_TYPE_STRING = "STRING"

    #: A constant which can be used with the value_type property of a ModelProperty.
    #: This constant has a value of "NUMERIC"
    VALUE_TYPE_NUMERIC = "NUMERIC"

    #: A constant which can be used with the scope property of a ModelProperty.
    #: This constant has a value of "TAXONOMY"
    SCOPE_TAXONOMY = "TAXONOMY"

    #: A constant which can be used with the scope property of a ModelProperty.
    #: This constant has a value of "PLATFORM_CONFIG"
    SCOPE_PLATFORM_CONFIG = "PLATFORM_CONFIG"

    #: A constant which can be used with the type property of a ModelProperty.
    #: This constant has a value of "USER_DEFINED"
    TYPE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the type property of a ModelProperty.
    #: This constant has a value of "ORACLE_DEFINED"
    TYPE_ORACLE_DEFINED = "ORACLE_DEFINED"

    #: A constant which can be used with the type property of a ModelProperty.
    #: This constant has a value of "SYSTEM_DEFINED"
    TYPE_SYSTEM_DEFINED = "SYSTEM_DEFINED"

    def __init__(self, **kwargs):
        """
        Initializes a new ModelProperty object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ModelProperty.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ModelProperty.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ModelProperty.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this ModelProperty.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ModelProperty.
        :type time_updated: datetime

        :param resource_region:
            The value to assign to the resource_region property of this ModelProperty.
        :type resource_region: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ModelProperty.
            Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ModelProperty.
        :type lifecycle_details: str

        :param selection:
            The value to assign to the selection property of this ModelProperty.
            Allowed values for this property are: "SINGLE_CHOICE", "MULTI_CHOICE", "DEFAULT_TEXT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type selection: str

        :param value_type:
            The value to assign to the value_type property of this ModelProperty.
            Allowed values for this property are: "STRING", "NUMERIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_type: str

        :param values:
            The value to assign to the values property of this ModelProperty.
        :type values: list[str]

        :param scope:
            The value to assign to the scope property of this ModelProperty.
            Allowed values for this property are: "TAXONOMY", "PLATFORM_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param type:
            The value to assign to the type property of this ModelProperty.
            Allowed values for this property are: "USER_DEFINED", "ORACLE_DEFINED", "SYSTEM_DEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ModelProperty.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ModelProperty.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ModelProperty.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'resource_region': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'selection': 'str',
            'value_type': 'str',
            'values': 'list[str]',
            'scope': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'resource_region': 'resourceRegion',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'selection': 'selection',
            'value_type': 'valueType',
            'values': 'values',
            'scope': 'scope',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._resource_region = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._selection = None
        self._value_type = None
        self._values = None
        self._scope = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ModelProperty.
        The OCID of the resource.


        :return: The id of this ModelProperty.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModelProperty.
        The OCID of the resource.


        :param id: The id of this ModelProperty.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ModelProperty.
        Tenancy OCID


        :return: The compartment_id of this ModelProperty.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ModelProperty.
        Tenancy OCID


        :param compartment_id: The compartment_id of this ModelProperty.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ModelProperty.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this ModelProperty.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ModelProperty.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this ModelProperty.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ModelProperty.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this ModelProperty.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ModelProperty.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this ModelProperty.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ModelProperty.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this ModelProperty.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ModelProperty.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this ModelProperty.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def resource_region(self):
        """
        **[Required]** Gets the resource_region of this ModelProperty.
        Associated region


        :return: The resource_region of this ModelProperty.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this ModelProperty.
        Associated region


        :param resource_region: The resource_region of this ModelProperty.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ModelProperty.
        The current state of the Property.

        Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ModelProperty.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ModelProperty.
        The current state of the Property.


        :param lifecycle_state: The lifecycle_state of this ModelProperty.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ModelProperty.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ModelProperty.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ModelProperty.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ModelProperty.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def selection(self):
        """
        Gets the selection of this ModelProperty.
        Text selection of the property.

        Allowed values for this property are: "SINGLE_CHOICE", "MULTI_CHOICE", "DEFAULT_TEXT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The selection of this ModelProperty.
        :rtype: str
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """
        Sets the selection of this ModelProperty.
        Text selection of the property.


        :param selection: The selection of this ModelProperty.
        :type: str
        """
        allowed_values = ["SINGLE_CHOICE", "MULTI_CHOICE", "DEFAULT_TEXT"]
        if not value_allowed_none_or_none_sentinel(selection, allowed_values):
            selection = 'UNKNOWN_ENUM_VALUE'
        self._selection = selection

    @property
    def value_type(self):
        """
        Gets the value_type of this ModelProperty.
        Format of the value.

        Allowed values for this property are: "STRING", "NUMERIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The value_type of this ModelProperty.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this ModelProperty.
        Format of the value.


        :param value_type: The value_type of this ModelProperty.
        :type: str
        """
        allowed_values = ["STRING", "NUMERIC"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            value_type = 'UNKNOWN_ENUM_VALUE'
        self._value_type = value_type

    @property
    def values(self):
        """
        Gets the values of this ModelProperty.
        Values of the property (must be a single value if selection = 'SINGLE_CHOICE').


        :return: The values of this ModelProperty.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this ModelProperty.
        Values of the property (must be a single value if selection = 'SINGLE_CHOICE').


        :param values: The values of this ModelProperty.
        :type: list[str]
        """
        self._values = values

    @property
    def scope(self):
        """
        Gets the scope of this ModelProperty.
        The scope of the property.

        Allowed values for this property are: "TAXONOMY", "PLATFORM_CONFIG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope of this ModelProperty.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this ModelProperty.
        The scope of the property.


        :param scope: The scope of this ModelProperty.
        :type: str
        """
        allowed_values = ["TAXONOMY", "PLATFORM_CONFIG"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            scope = 'UNKNOWN_ENUM_VALUE'
        self._scope = scope

    @property
    def type(self):
        """
        Gets the type of this ModelProperty.
        The type of the property.

        Allowed values for this property are: "USER_DEFINED", "ORACLE_DEFINED", "SYSTEM_DEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ModelProperty.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ModelProperty.
        The type of the property.


        :param type: The type of this ModelProperty.
        :type: str
        """
        allowed_values = ["USER_DEFINED", "ORACLE_DEFINED", "SYSTEM_DEFINED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ModelProperty.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ModelProperty.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ModelProperty.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ModelProperty.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ModelProperty.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ModelProperty.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ModelProperty.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ModelProperty.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ModelProperty.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ModelProperty.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ModelProperty.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ModelProperty.
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