# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableLatestPolicyDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableLatestPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param can_latest_fams_policies_be_enabled:
            The value to assign to the can_latest_fams_policies_be_enabled property of this EnableLatestPolicyDetails.
        :type can_latest_fams_policies_be_enabled: bool

        """
        self.swagger_types = {
            'can_latest_fams_policies_be_enabled': 'bool'
        }

        self.attribute_map = {
            'can_latest_fams_policies_be_enabled': 'canLatestFamsPoliciesBeEnabled'
        }

        self._can_latest_fams_policies_be_enabled = None

    @property
    def can_latest_fams_policies_be_enabled(self):
        """
        Gets the can_latest_fams_policies_be_enabled of this EnableLatestPolicyDetails.
        A value determining if latest Fleet Application Management policies should be enabled


        :return: The can_latest_fams_policies_be_enabled of this EnableLatestPolicyDetails.
        :rtype: bool
        """
        return self._can_latest_fams_policies_be_enabled

    @can_latest_fams_policies_be_enabled.setter
    def can_latest_fams_policies_be_enabled(self, can_latest_fams_policies_be_enabled):
        """
        Sets the can_latest_fams_policies_be_enabled of this EnableLatestPolicyDetails.
        A value determining if latest Fleet Application Management policies should be enabled


        :param can_latest_fams_policies_be_enabled: The can_latest_fams_policies_be_enabled of this EnableLatestPolicyDetails.
        :type: bool
        """
        self._can_latest_fams_policies_be_enabled = can_latest_fams_policies_be_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other