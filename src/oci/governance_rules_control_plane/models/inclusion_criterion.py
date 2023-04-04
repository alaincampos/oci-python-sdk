# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InclusionCriterion(object):
    """
    Represents the criterion for the inclusion of the child tenancies under a governance rule. This can be either TENANCY or TAG.
    """

    #: A constant which can be used with the type property of a InclusionCriterion.
    #: This constant has a value of "TENANCY"
    TYPE_TENANCY = "TENANCY"

    #: A constant which can be used with the type property of a InclusionCriterion.
    #: This constant has a value of "ALL"
    TYPE_ALL = "ALL"

    #: A constant which can be used with the lifecycle_state property of a InclusionCriterion.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a InclusionCriterion.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new InclusionCriterion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InclusionCriterion.
        :type id: str

        :param governance_rule_id:
            The value to assign to the governance_rule_id property of this InclusionCriterion.
        :type governance_rule_id: str

        :param type:
            The value to assign to the type property of this InclusionCriterion.
            Allowed values for this property are: "TENANCY", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param association:
            The value to assign to the association property of this InclusionCriterion.
        :type association: oci.governance_rules_control_plane.models.Association

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InclusionCriterion.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this InclusionCriterion.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this InclusionCriterion.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'governance_rule_id': 'str',
            'type': 'str',
            'association': 'Association',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'governance_rule_id': 'governanceRuleId',
            'type': 'type',
            'association': 'association',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._governance_rule_id = None
        self._type = None
        self._association = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InclusionCriterion.
        The Oracle ID (`OCID`__) of the inclusion criterion.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this InclusionCriterion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InclusionCriterion.
        The Oracle ID (`OCID`__) of the inclusion criterion.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this InclusionCriterion.
        :type: str
        """
        self._id = id

    @property
    def governance_rule_id(self):
        """
        **[Required]** Gets the governance_rule_id of this InclusionCriterion.
        The Oracle ID (`OCID`__) of the governance rule. Every inclusion criterion is associated with a governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The governance_rule_id of this InclusionCriterion.
        :rtype: str
        """
        return self._governance_rule_id

    @governance_rule_id.setter
    def governance_rule_id(self, governance_rule_id):
        """
        Sets the governance_rule_id of this InclusionCriterion.
        The Oracle ID (`OCID`__) of the governance rule. Every inclusion criterion is associated with a governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param governance_rule_id: The governance_rule_id of this InclusionCriterion.
        :type: str
        """
        self._governance_rule_id = governance_rule_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this InclusionCriterion.
        Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.

        Allowed values for this property are: "TENANCY", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this InclusionCriterion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InclusionCriterion.
        Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.


        :param type: The type of this InclusionCriterion.
        :type: str
        """
        allowed_values = ["TENANCY", "ALL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def association(self):
        """
        Gets the association of this InclusionCriterion.

        :return: The association of this InclusionCriterion.
        :rtype: oci.governance_rules_control_plane.models.Association
        """
        return self._association

    @association.setter
    def association(self, association):
        """
        Sets the association of this InclusionCriterion.

        :param association: The association of this InclusionCriterion.
        :type: oci.governance_rules_control_plane.models.Association
        """
        self._association = association

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InclusionCriterion.
        The current state of the inclusion criterion.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InclusionCriterion.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InclusionCriterion.
        The current state of the inclusion criterion.


        :param lifecycle_state: The lifecycle_state of this InclusionCriterion.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InclusionCriterion.
        Date and time the inclusion criterion was created. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this InclusionCriterion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InclusionCriterion.
        Date and time the inclusion criterion was created. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this InclusionCriterion.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this InclusionCriterion.
        Date and time the inclusion criterion was updated. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_updated of this InclusionCriterion.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this InclusionCriterion.
        Date and time the inclusion criterion was updated. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_updated: The time_updated of this InclusionCriterion.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other