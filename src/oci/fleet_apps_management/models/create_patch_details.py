# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePatchDetails(object):
    """
    The information about new Patch.
    """

    #: A constant which can be used with the severity property of a CreatePatchDetails.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a CreatePatchDetails.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a CreatePatchDetails.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a CreatePatchDetails.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePatchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreatePatchDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreatePatchDetails.
        :type description: str

        :param patch_type:
            The value to assign to the patch_type property of this CreatePatchDetails.
        :type patch_type: oci.fleet_apps_management.models.PatchType

        :param severity:
            The value to assign to the severity property of this CreatePatchDetails.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW"
        :type severity: str

        :param time_released:
            The value to assign to the time_released property of this CreatePatchDetails.
        :type time_released: datetime

        :param artifact_details:
            The value to assign to the artifact_details property of this CreatePatchDetails.
        :type artifact_details: oci.fleet_apps_management.models.ArtifactDetails

        :param product:
            The value to assign to the product property of this CreatePatchDetails.
        :type product: oci.fleet_apps_management.models.PatchProduct

        :param dependent_patches:
            The value to assign to the dependent_patches property of this CreatePatchDetails.
        :type dependent_patches: list[oci.fleet_apps_management.models.DependentPatchDetails]

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePatchDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePatchDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePatchDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'patch_type': 'PatchType',
            'severity': 'str',
            'time_released': 'datetime',
            'artifact_details': 'ArtifactDetails',
            'product': 'PatchProduct',
            'dependent_patches': 'list[DependentPatchDetails]',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'patch_type': 'patchType',
            'severity': 'severity',
            'time_released': 'timeReleased',
            'artifact_details': 'artifactDetails',
            'product': 'product',
            'dependent_patches': 'dependentPatches',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._description = None
        self._patch_type = None
        self._severity = None
        self._time_released = None
        self._artifact_details = None
        self._product = None
        self._dependent_patches = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreatePatchDetails.
        A user-friendly name. Should be unique within the tenancy, and cannot be changed after creation.
        Avoid entering confidential information.


        :return: The name of this CreatePatchDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePatchDetails.
        A user-friendly name. Should be unique within the tenancy, and cannot be changed after creation.
        Avoid entering confidential information.


        :param name: The name of this CreatePatchDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreatePatchDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this CreatePatchDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePatchDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this CreatePatchDetails.
        :type: str
        """
        self._description = description

    @property
    def patch_type(self):
        """
        **[Required]** Gets the patch_type of this CreatePatchDetails.

        :return: The patch_type of this CreatePatchDetails.
        :rtype: oci.fleet_apps_management.models.PatchType
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """
        Sets the patch_type of this CreatePatchDetails.

        :param patch_type: The patch_type of this CreatePatchDetails.
        :type: oci.fleet_apps_management.models.PatchType
        """
        self._patch_type = patch_type

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this CreatePatchDetails.
        Patch Severity.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW"


        :return: The severity of this CreatePatchDetails.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this CreatePatchDetails.
        Patch Severity.


        :param severity: The severity of this CreatePatchDetails.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            raise ValueError(
                f"Invalid value for `severity`, must be None or one of {allowed_values}"
            )
        self._severity = severity

    @property
    def time_released(self):
        """
        **[Required]** Gets the time_released of this CreatePatchDetails.
        Date when the patch was released.


        :return: The time_released of this CreatePatchDetails.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this CreatePatchDetails.
        Date when the patch was released.


        :param time_released: The time_released of this CreatePatchDetails.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def artifact_details(self):
        """
        **[Required]** Gets the artifact_details of this CreatePatchDetails.

        :return: The artifact_details of this CreatePatchDetails.
        :rtype: oci.fleet_apps_management.models.ArtifactDetails
        """
        return self._artifact_details

    @artifact_details.setter
    def artifact_details(self, artifact_details):
        """
        Sets the artifact_details of this CreatePatchDetails.

        :param artifact_details: The artifact_details of this CreatePatchDetails.
        :type: oci.fleet_apps_management.models.ArtifactDetails
        """
        self._artifact_details = artifact_details

    @property
    def product(self):
        """
        **[Required]** Gets the product of this CreatePatchDetails.

        :return: The product of this CreatePatchDetails.
        :rtype: oci.fleet_apps_management.models.PatchProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this CreatePatchDetails.

        :param product: The product of this CreatePatchDetails.
        :type: oci.fleet_apps_management.models.PatchProduct
        """
        self._product = product

    @property
    def dependent_patches(self):
        """
        Gets the dependent_patches of this CreatePatchDetails.
        Dependent Patches for this patch.


        :return: The dependent_patches of this CreatePatchDetails.
        :rtype: list[oci.fleet_apps_management.models.DependentPatchDetails]
        """
        return self._dependent_patches

    @dependent_patches.setter
    def dependent_patches(self, dependent_patches):
        """
        Sets the dependent_patches of this CreatePatchDetails.
        Dependent Patches for this patch.


        :param dependent_patches: The dependent_patches of this CreatePatchDetails.
        :type: list[oci.fleet_apps_management.models.DependentPatchDetails]
        """
        self._dependent_patches = dependent_patches

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePatchDetails.
        OCID of the compartment to which the resource belongs to.


        :return: The compartment_id of this CreatePatchDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePatchDetails.
        OCID of the compartment to which the resource belongs to.


        :param compartment_id: The compartment_id of this CreatePatchDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePatchDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreatePatchDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePatchDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreatePatchDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePatchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreatePatchDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePatchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreatePatchDetails.
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