# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousContainerDatabaseVersionSummary(object):
    """
    The supported Autonomous Database version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousContainerDatabaseVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this AutonomousContainerDatabaseVersionSummary.
        :type version: str

        :param details:
            The value to assign to the details property of this AutonomousContainerDatabaseVersionSummary.
        :type details: str

        :param supported_apps:
            The value to assign to the supported_apps property of this AutonomousContainerDatabaseVersionSummary.
        :type supported_apps: list[oci.database.models.AppVersionSummary]

        """
        self.swagger_types = {
            'version': 'str',
            'details': 'str',
            'supported_apps': 'list[AppVersionSummary]'
        }

        self.attribute_map = {
            'version': 'version',
            'details': 'details',
            'supported_apps': 'supportedApps'
        }

        self._version = None
        self._details = None
        self._supported_apps = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this AutonomousContainerDatabaseVersionSummary.
        A valid Oracle Database version for provisioning an Autonomous Container Database.


        :return: The version of this AutonomousContainerDatabaseVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AutonomousContainerDatabaseVersionSummary.
        A valid Oracle Database version for provisioning an Autonomous Container Database.


        :param version: The version of this AutonomousContainerDatabaseVersionSummary.
        :type: str
        """
        self._version = version

    @property
    def details(self):
        """
        Gets the details of this AutonomousContainerDatabaseVersionSummary.
        A URL that points to a detailed description of the Autonomous Container Database version.


        :return: The details of this AutonomousContainerDatabaseVersionSummary.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this AutonomousContainerDatabaseVersionSummary.
        A URL that points to a detailed description of the Autonomous Container Database version.


        :param details: The details of this AutonomousContainerDatabaseVersionSummary.
        :type: str
        """
        self._details = details

    @property
    def supported_apps(self):
        """
        **[Required]** Gets the supported_apps of this AutonomousContainerDatabaseVersionSummary.
        The list of applications supported for the given version.


        :return: The supported_apps of this AutonomousContainerDatabaseVersionSummary.
        :rtype: list[oci.database.models.AppVersionSummary]
        """
        return self._supported_apps

    @supported_apps.setter
    def supported_apps(self, supported_apps):
        """
        Sets the supported_apps of this AutonomousContainerDatabaseVersionSummary.
        The list of applications supported for the given version.


        :param supported_apps: The supported_apps of this AutonomousContainerDatabaseVersionSummary.
        :type: list[oci.database.models.AppVersionSummary]
        """
        self._supported_apps = supported_apps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other