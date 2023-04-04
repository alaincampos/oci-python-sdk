# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportModelArtifactDetails(object):
    """
    Details required for exporting the model artifact from source to service bucket
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportModelArtifactDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param artifact_export_details:
            The value to assign to the artifact_export_details property of this ExportModelArtifactDetails.
        :type artifact_export_details: oci.data_science.models.ArtifactExportDetails

        """
        self.swagger_types = {
            'artifact_export_details': 'ArtifactExportDetails'
        }

        self.attribute_map = {
            'artifact_export_details': 'artifactExportDetails'
        }

        self._artifact_export_details = None

    @property
    def artifact_export_details(self):
        """
        **[Required]** Gets the artifact_export_details of this ExportModelArtifactDetails.

        :return: The artifact_export_details of this ExportModelArtifactDetails.
        :rtype: oci.data_science.models.ArtifactExportDetails
        """
        return self._artifact_export_details

    @artifact_export_details.setter
    def artifact_export_details(self, artifact_export_details):
        """
        Sets the artifact_export_details of this ExportModelArtifactDetails.

        :param artifact_export_details: The artifact_export_details of this ExportModelArtifactDetails.
        :type: oci.data_science.models.ArtifactExportDetails
        """
        self._artifact_export_details = artifact_export_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other