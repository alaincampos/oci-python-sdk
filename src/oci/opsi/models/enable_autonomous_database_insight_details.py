# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .enable_database_insight_details import EnableDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableAutonomousDatabaseInsightDetails(EnableDatabaseInsightDetails):
    """
    The information about database to be analyzed. When isAdvancedFeaturesEnabled is set to false, parameters connectionDetails, credentialDetails and opsiPrivateEndpoint are optional. Otherwise, connectionDetails and crendetialDetails are required to enable full OPSI service features. If the Autonomouse Database is configured with private, restricted or dedicated access, opsiPrivateEndpoint parameter is required.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableAutonomousDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EnableAutonomousDatabaseInsightDetails.entity_source` attribute
        of this class is ``AUTONOMOUS_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EnableAutonomousDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", "MDS_MYSQL_DATABASE_SYSTEM", "MACS_MANAGED_CLOUD_DATABASE"
        :type entity_source: str

        :param database_resource_type:
            The value to assign to the database_resource_type property of this EnableAutonomousDatabaseInsightDetails.
        :type database_resource_type: str

        :param is_advanced_features_enabled:
            The value to assign to the is_advanced_features_enabled property of this EnableAutonomousDatabaseInsightDetails.
        :type is_advanced_features_enabled: bool

        :param connection_details:
            The value to assign to the connection_details property of this EnableAutonomousDatabaseInsightDetails.
        :type connection_details: oci.opsi.models.ConnectionDetails

        :param credential_details:
            The value to assign to the credential_details property of this EnableAutonomousDatabaseInsightDetails.
        :type credential_details: oci.opsi.models.CredentialDetails

        :param opsi_private_endpoint_id:
            The value to assign to the opsi_private_endpoint_id property of this EnableAutonomousDatabaseInsightDetails.
        :type opsi_private_endpoint_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EnableAutonomousDatabaseInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EnableAutonomousDatabaseInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EnableAutonomousDatabaseInsightDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_source': 'str',
            'database_resource_type': 'str',
            'is_advanced_features_enabled': 'bool',
            'connection_details': 'ConnectionDetails',
            'credential_details': 'CredentialDetails',
            'opsi_private_endpoint_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'database_resource_type': 'databaseResourceType',
            'is_advanced_features_enabled': 'isAdvancedFeaturesEnabled',
            'connection_details': 'connectionDetails',
            'credential_details': 'credentialDetails',
            'opsi_private_endpoint_id': 'opsiPrivateEndpointId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._entity_source = None
        self._database_resource_type = None
        self._is_advanced_features_enabled = None
        self._connection_details = None
        self._credential_details = None
        self._opsi_private_endpoint_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._entity_source = 'AUTONOMOUS_DATABASE'

    @property
    def database_resource_type(self):
        """
        Gets the database_resource_type of this EnableAutonomousDatabaseInsightDetails.
        OCI database resource type


        :return: The database_resource_type of this EnableAutonomousDatabaseInsightDetails.
        :rtype: str
        """
        return self._database_resource_type

    @database_resource_type.setter
    def database_resource_type(self, database_resource_type):
        """
        Sets the database_resource_type of this EnableAutonomousDatabaseInsightDetails.
        OCI database resource type


        :param database_resource_type: The database_resource_type of this EnableAutonomousDatabaseInsightDetails.
        :type: str
        """
        self._database_resource_type = database_resource_type

    @property
    def is_advanced_features_enabled(self):
        """
        **[Required]** Gets the is_advanced_features_enabled of this EnableAutonomousDatabaseInsightDetails.
        Flag is to identify if advanced features for autonomous database is enabled or not


        :return: The is_advanced_features_enabled of this EnableAutonomousDatabaseInsightDetails.
        :rtype: bool
        """
        return self._is_advanced_features_enabled

    @is_advanced_features_enabled.setter
    def is_advanced_features_enabled(self, is_advanced_features_enabled):
        """
        Sets the is_advanced_features_enabled of this EnableAutonomousDatabaseInsightDetails.
        Flag is to identify if advanced features for autonomous database is enabled or not


        :param is_advanced_features_enabled: The is_advanced_features_enabled of this EnableAutonomousDatabaseInsightDetails.
        :type: bool
        """
        self._is_advanced_features_enabled = is_advanced_features_enabled

    @property
    def connection_details(self):
        """
        Gets the connection_details of this EnableAutonomousDatabaseInsightDetails.

        :return: The connection_details of this EnableAutonomousDatabaseInsightDetails.
        :rtype: oci.opsi.models.ConnectionDetails
        """
        return self._connection_details

    @connection_details.setter
    def connection_details(self, connection_details):
        """
        Sets the connection_details of this EnableAutonomousDatabaseInsightDetails.

        :param connection_details: The connection_details of this EnableAutonomousDatabaseInsightDetails.
        :type: oci.opsi.models.ConnectionDetails
        """
        self._connection_details = connection_details

    @property
    def credential_details(self):
        """
        Gets the credential_details of this EnableAutonomousDatabaseInsightDetails.

        :return: The credential_details of this EnableAutonomousDatabaseInsightDetails.
        :rtype: oci.opsi.models.CredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this EnableAutonomousDatabaseInsightDetails.

        :param credential_details: The credential_details of this EnableAutonomousDatabaseInsightDetails.
        :type: oci.opsi.models.CredentialDetails
        """
        self._credential_details = credential_details

    @property
    def opsi_private_endpoint_id(self):
        """
        Gets the opsi_private_endpoint_id of this EnableAutonomousDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The opsi_private_endpoint_id of this EnableAutonomousDatabaseInsightDetails.
        :rtype: str
        """
        return self._opsi_private_endpoint_id

    @opsi_private_endpoint_id.setter
    def opsi_private_endpoint_id(self, opsi_private_endpoint_id):
        """
        Sets the opsi_private_endpoint_id of this EnableAutonomousDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param opsi_private_endpoint_id: The opsi_private_endpoint_id of this EnableAutonomousDatabaseInsightDetails.
        :type: str
        """
        self._opsi_private_endpoint_id = opsi_private_endpoint_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EnableAutonomousDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EnableAutonomousDatabaseInsightDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EnableAutonomousDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EnableAutonomousDatabaseInsightDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EnableAutonomousDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EnableAutonomousDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EnableAutonomousDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EnableAutonomousDatabaseInsightDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EnableAutonomousDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this EnableAutonomousDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EnableAutonomousDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this EnableAutonomousDatabaseInsightDetails.
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