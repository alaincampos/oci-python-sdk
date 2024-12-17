# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParameterFileVersionSummary(object):
    """
    A parameter file detatails
    """

    #: A constant which can be used with the kind property of a ParameterFileVersionSummary.
    #: This constant has a value of "EXTRACT"
    KIND_EXTRACT = "EXTRACT"

    #: A constant which can be used with the kind property of a ParameterFileVersionSummary.
    #: This constant has a value of "REPLICAT"
    KIND_REPLICAT = "REPLICAT"

    def __init__(self, **kwargs):
        """
        Initializes a new ParameterFileVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ParameterFileVersionSummary.
        :type name: str

        :param kind:
            The value to assign to the kind property of this ParameterFileVersionSummary.
            Allowed values for this property are: "EXTRACT", "REPLICAT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param description:
            The value to assign to the description property of this ParameterFileVersionSummary.
        :type description: str

        :param is_current:
            The value to assign to the is_current property of this ParameterFileVersionSummary.
        :type is_current: bool

        :param is_factory:
            The value to assign to the is_factory property of this ParameterFileVersionSummary.
        :type is_factory: bool

        :param time_created:
            The value to assign to the time_created property of this ParameterFileVersionSummary.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ParameterFileVersionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ParameterFileVersionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ParameterFileVersionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'kind': 'str',
            'description': 'str',
            'is_current': 'bool',
            'is_factory': 'bool',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'kind': 'kind',
            'description': 'description',
            'is_current': 'isCurrent',
            'is_factory': 'isFactory',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._name = None
        self._kind = None
        self._description = None
        self._is_current = None
        self._is_factory = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ParameterFileVersionSummary.
        A unique name associated with the current migration/job and extract/replicat name


        :return: The name of this ParameterFileVersionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ParameterFileVersionSummary.
        A unique name associated with the current migration/job and extract/replicat name


        :param name: The name of this ParameterFileVersionSummary.
        :type: str
        """
        self._name = name

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this ParameterFileVersionSummary.
        Indicator of Parameter File 'kind' (for an EXTRACT or a REPLICAT)

        Allowed values for this property are: "EXTRACT", "REPLICAT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The kind of this ParameterFileVersionSummary.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this ParameterFileVersionSummary.
        Indicator of Parameter File 'kind' (for an EXTRACT or a REPLICAT)


        :param kind: The kind of this ParameterFileVersionSummary.
        :type: str
        """
        allowed_values = ["EXTRACT", "REPLICAT"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            kind = 'UNKNOWN_ENUM_VALUE'
        self._kind = kind

    @property
    def description(self):
        """
        Gets the description of this ParameterFileVersionSummary.
        A description to discribe the current parameter file version


        :return: The description of this ParameterFileVersionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ParameterFileVersionSummary.
        A description to discribe the current parameter file version


        :param description: The description of this ParameterFileVersionSummary.
        :type: str
        """
        self._description = description

    @property
    def is_current(self):
        """
        **[Required]** Gets the is_current of this ParameterFileVersionSummary.
        Return boolean true/false for the currently in-use parameter file (factory or a versioned file)


        :return: The is_current of this ParameterFileVersionSummary.
        :rtype: bool
        """
        return self._is_current

    @is_current.setter
    def is_current(self, is_current):
        """
        Sets the is_current of this ParameterFileVersionSummary.
        Return boolean true/false for the currently in-use parameter file (factory or a versioned file)


        :param is_current: The is_current of this ParameterFileVersionSummary.
        :type: bool
        """
        self._is_current = is_current

    @property
    def is_factory(self):
        """
        **[Required]** Gets the is_factory of this ParameterFileVersionSummary.
        Return true/false for whether the parameter file is oracle provided (Factory)


        :return: The is_factory of this ParameterFileVersionSummary.
        :rtype: bool
        """
        return self._is_factory

    @is_factory.setter
    def is_factory(self, is_factory):
        """
        Sets the is_factory of this ParameterFileVersionSummary.
        Return true/false for whether the parameter file is oracle provided (Factory)


        :param is_factory: The is_factory of this ParameterFileVersionSummary.
        :type: bool
        """
        self._is_factory = is_factory

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ParameterFileVersionSummary.
        The time when this parameter file was applied on the process


        :return: The time_created of this ParameterFileVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ParameterFileVersionSummary.
        The time when this parameter file was applied on the process


        :param time_created: The time_created of this ParameterFileVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ParameterFileVersionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see Resource Tags. Example: {\"Department\": \"Finance\"}


        :return: The freeform_tags of this ParameterFileVersionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ParameterFileVersionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see Resource Tags. Example: {\"Department\": \"Finance\"}


        :param freeform_tags: The freeform_tags of this ParameterFileVersionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ParameterFileVersionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ParameterFileVersionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ParameterFileVersionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ParameterFileVersionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ParameterFileVersionSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ParameterFileVersionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ParameterFileVersionSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ParameterFileVersionSummary.
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