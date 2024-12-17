# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOccCustomerGroupDetails(object):
    """
    Details about the create request for the customer group.
    """

    #: A constant which can be used with the status property of a CreateOccCustomerGroupDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a CreateOccCustomerGroupDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOccCustomerGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOccCustomerGroupDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateOccCustomerGroupDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateOccCustomerGroupDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOccCustomerGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOccCustomerGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CreateOccCustomerGroupDetails.
        :type lifecycle_details: str

        :param status:
            The value to assign to the status property of this CreateOccCustomerGroupDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type status: str

        :param customers_list:
            The value to assign to the customers_list property of this CreateOccCustomerGroupDetails.
        :type customers_list: list[oci.capacity_management.models.CreateOccCustomerDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_details': 'str',
            'status': 'str',
            'customers_list': 'list[CreateOccCustomerDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_details': 'lifecycleDetails',
            'status': 'status',
            'customers_list': 'customersList'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_details = None
        self._status = None
        self._customers_list = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOccCustomerGroupDetails.
        Since all resources are at tenancy level hence this will be the ocid of the tenancy where operation is to be performed.


        :return: The compartment_id of this CreateOccCustomerGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOccCustomerGroupDetails.
        Since all resources are at tenancy level hence this will be the ocid of the tenancy where operation is to be performed.


        :param compartment_id: The compartment_id of this CreateOccCustomerGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateOccCustomerGroupDetails.
        The name of the customer group.


        :return: The display_name of this CreateOccCustomerGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateOccCustomerGroupDetails.
        The name of the customer group.


        :param display_name: The display_name of this CreateOccCustomerGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateOccCustomerGroupDetails.
        A description about the customer group.


        :return: The description of this CreateOccCustomerGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateOccCustomerGroupDetails.
        A description about the customer group.


        :param description: The description of this CreateOccCustomerGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOccCustomerGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOccCustomerGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOccCustomerGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOccCustomerGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOccCustomerGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOccCustomerGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOccCustomerGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOccCustomerGroupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CreateOccCustomerGroupDetails.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :return: The lifecycle_details of this CreateOccCustomerGroupDetails.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CreateOccCustomerGroupDetails.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :param lifecycle_details: The lifecycle_details of this CreateOccCustomerGroupDetails.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def status(self):
        """
        Gets the status of this CreateOccCustomerGroupDetails.
        To determine whether the customer group is enabled/disabled.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The status of this CreateOccCustomerGroupDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreateOccCustomerGroupDetails.
        To determine whether the customer group is enabled/disabled.


        :param status: The status of this CreateOccCustomerGroupDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                f"Invalid value for `status`, must be None or one of {allowed_values}"
            )
        self._status = status

    @property
    def customers_list(self):
        """
        Gets the customers_list of this CreateOccCustomerGroupDetails.
        A list containing all the customers that belong to this customer group.


        :return: The customers_list of this CreateOccCustomerGroupDetails.
        :rtype: list[oci.capacity_management.models.CreateOccCustomerDetails]
        """
        return self._customers_list

    @customers_list.setter
    def customers_list(self, customers_list):
        """
        Sets the customers_list of this CreateOccCustomerGroupDetails.
        A list containing all the customers that belong to this customer group.


        :param customers_list: The customers_list of this CreateOccCustomerGroupDetails.
        :type: list[oci.capacity_management.models.CreateOccCustomerDetails]
        """
        self._customers_list = customers_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other