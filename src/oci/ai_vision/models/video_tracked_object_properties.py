# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoTrackedObjectProperties(object):
    """
    Properties of a tracked object in a video.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VideoTrackedObjectProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param axle_count:
            The value to assign to the axle_count property of this VideoTrackedObjectProperties.
        :type axle_count: int

        """
        self.swagger_types = {
            'axle_count': 'int'
        }

        self.attribute_map = {
            'axle_count': 'axleCount'
        }

        self._axle_count = None

    @property
    def axle_count(self):
        """
        Gets the axle_count of this VideoTrackedObjectProperties.
        The axle count value of a tracked vehicle.


        :return: The axle_count of this VideoTrackedObjectProperties.
        :rtype: int
        """
        return self._axle_count

    @axle_count.setter
    def axle_count(self, axle_count):
        """
        Sets the axle_count of this VideoTrackedObjectProperties.
        The axle count value of a tracked vehicle.


        :param axle_count: The axle_count of this VideoTrackedObjectProperties.
        :type: int
        """
        self._axle_count = axle_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other