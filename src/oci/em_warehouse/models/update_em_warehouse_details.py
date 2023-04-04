# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateEmWarehouseDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateEmWarehouseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateEmWarehouseDetails.
        :type compartment_id: str

        :param em_bridge_id:
            The value to assign to the em_bridge_id property of this UpdateEmWarehouseDetails.
        :type em_bridge_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateEmWarehouseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateEmWarehouseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'em_bridge_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'em_bridge_id': 'emBridgeId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._em_bridge_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateEmWarehouseDetails.
        Compartment Identifier


        :return: The compartment_id of this UpdateEmWarehouseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateEmWarehouseDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this UpdateEmWarehouseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def em_bridge_id(self):
        """
        Gets the em_bridge_id of this UpdateEmWarehouseDetails.
        EMBridge Identifier


        :return: The em_bridge_id of this UpdateEmWarehouseDetails.
        :rtype: str
        """
        return self._em_bridge_id

    @em_bridge_id.setter
    def em_bridge_id(self, em_bridge_id):
        """
        Sets the em_bridge_id of this UpdateEmWarehouseDetails.
        EMBridge Identifier


        :param em_bridge_id: The em_bridge_id of this UpdateEmWarehouseDetails.
        :type: str
        """
        self._em_bridge_id = em_bridge_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateEmWarehouseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateEmWarehouseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateEmWarehouseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateEmWarehouseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateEmWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateEmWarehouseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateEmWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateEmWarehouseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other