# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dbm_resource import DbmResource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataInfrastructureSummary(DbmResource):
    """
    The Exadata infrastructure.
    """

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureSummary.
    #: This constant has a value of "FULL"
    RACK_SIZE_FULL = "FULL"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureSummary.
    #: This constant has a value of "HALF"
    RACK_SIZE_HALF = "HALF"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureSummary.
    #: This constant has a value of "QUARTER"
    RACK_SIZE_QUARTER = "QUARTER"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureSummary.
    #: This constant has a value of "EIGHTH"
    RACK_SIZE_EIGHTH = "EIGHTH"

    #: A constant which can be used with the license_model property of a ExternalExadataInfrastructureSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a ExternalExadataInfrastructureSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataInfrastructureSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalExadataInfrastructureSummary.resource_type` attribute
        of this class is ``INFRASTRUCTURE_SUMMARY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataInfrastructureSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalExadataInfrastructureSummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalExadataInfrastructureSummary.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalExadataInfrastructureSummary.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalExadataInfrastructureSummary.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalExadataInfrastructureSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ExternalExadataInfrastructureSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalExadataInfrastructureSummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalExadataInfrastructureSummary.
        :type lifecycle_details: str

        :param additional_details:
            The value to assign to the additional_details property of this ExternalExadataInfrastructureSummary.
        :type additional_details: dict(str, str)

        :param resource_type:
            The value to assign to the resource_type property of this ExternalExadataInfrastructureSummary.
            Allowed values for this property are: "INFRASTRUCTURE_SUMMARY", "INFRASTRUCTURE", "STORAGE_SERVER_SUMMARY", "STORAGE_SERVER", "STORAGE_GRID_SUMMARY", "STORAGE_GRID", "STORAGE_CONNECTOR_SUMMARY", "STORAGE_CONNECTOR", "DATABASE_SYSTEM_SUMMARY", "DATABASE_SUMMARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param rack_size:
            The value to assign to the rack_size property of this ExternalExadataInfrastructureSummary.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rack_size: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalExadataInfrastructureSummary.
        :type compartment_id: str

        :param license_model:
            The value to assign to the license_model property of this ExternalExadataInfrastructureSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param grid_home_path:
            The value to assign to the grid_home_path property of this ExternalExadataInfrastructureSummary.
        :type grid_home_path: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'additional_details': 'dict(str, str)',
            'resource_type': 'str',
            'rack_size': 'str',
            'compartment_id': 'str',
            'license_model': 'str',
            'grid_home_path': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'additional_details': 'additionalDetails',
            'resource_type': 'resourceType',
            'rack_size': 'rackSize',
            'compartment_id': 'compartmentId',
            'license_model': 'licenseModel',
            'grid_home_path': 'gridHomePath'
        }

        self._id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._additional_details = None
        self._resource_type = None
        self._rack_size = None
        self._compartment_id = None
        self._license_model = None
        self._grid_home_path = None
        self._resource_type = 'INFRASTRUCTURE_SUMMARY'

    @property
    def rack_size(self):
        """
        Gets the rack_size of this ExternalExadataInfrastructureSummary.
        The rack size of the Exadata infrastructure.

        Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rack_size of this ExternalExadataInfrastructureSummary.
        :rtype: str
        """
        return self._rack_size

    @rack_size.setter
    def rack_size(self, rack_size):
        """
        Sets the rack_size of this ExternalExadataInfrastructureSummary.
        The rack size of the Exadata infrastructure.


        :param rack_size: The rack_size of this ExternalExadataInfrastructureSummary.
        :type: str
        """
        allowed_values = ["FULL", "HALF", "QUARTER", "EIGHTH"]
        if not value_allowed_none_or_none_sentinel(rack_size, allowed_values):
            rack_size = 'UNKNOWN_ENUM_VALUE'
        self._rack_size = rack_size

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalExadataInfrastructureSummary.
        The `OCID`__ of compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalExadataInfrastructureSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalExadataInfrastructureSummary.
        The `OCID`__ of compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalExadataInfrastructureSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def license_model(self):
        """
        Gets the license_model of this ExternalExadataInfrastructureSummary.
        The Oracle license model that applies to the database management resources.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this ExternalExadataInfrastructureSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this ExternalExadataInfrastructureSummary.
        The Oracle license model that applies to the database management resources.


        :param license_model: The license_model of this ExternalExadataInfrastructureSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def grid_home_path(self):
        """
        Gets the grid_home_path of this ExternalExadataInfrastructureSummary.
        The Oracle grid home path.


        :return: The grid_home_path of this ExternalExadataInfrastructureSummary.
        :rtype: str
        """
        return self._grid_home_path

    @grid_home_path.setter
    def grid_home_path(self, grid_home_path):
        """
        Sets the grid_home_path of this ExternalExadataInfrastructureSummary.
        The Oracle grid home path.


        :param grid_home_path: The grid_home_path of this ExternalExadataInfrastructureSummary.
        :type: str
        """
        self._grid_home_path = grid_home_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other