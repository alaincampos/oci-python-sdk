# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchedulerJobDimension(object):
    """
    Aggregated summary information for a SchedulerJob.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SchedulerJobDimension object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SchedulerJobDimension.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'lifecycle_details': 'lifecycleDetails'
        }

        self._lifecycle_details = None

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this SchedulerJobDimension.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this SchedulerJobDimension.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SchedulerJobDimension.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this SchedulerJobDimension.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other