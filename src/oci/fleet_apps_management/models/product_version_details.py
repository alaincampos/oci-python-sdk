# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProductVersionDetails(object):
    """
    A specific product version or a specific version and succeeding.
    Example: 12.1 or 12.1 and above for Oracle WebLogic Application server.
    The policy applies to the next version only, and not to other versions such as, 12.1.x.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProductVersionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this ProductVersionDetails.
        :type version: str

        :param is_applicable_for_all_higher_versions:
            The value to assign to the is_applicable_for_all_higher_versions property of this ProductVersionDetails.
        :type is_applicable_for_all_higher_versions: bool

        """
        self.swagger_types = {
            'version': 'str',
            'is_applicable_for_all_higher_versions': 'bool'
        }

        self.attribute_map = {
            'version': 'version',
            'is_applicable_for_all_higher_versions': 'isApplicableForAllHigherVersions'
        }

        self._version = None
        self._is_applicable_for_all_higher_versions = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ProductVersionDetails.
        Product version the rule is applicable.


        :return: The version of this ProductVersionDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProductVersionDetails.
        Product version the rule is applicable.


        :param version: The version of this ProductVersionDetails.
        :type: str
        """
        self._version = version

    @property
    def is_applicable_for_all_higher_versions(self):
        """
        Gets the is_applicable_for_all_higher_versions of this ProductVersionDetails.
        Is rule applicable to all higher versions also


        :return: The is_applicable_for_all_higher_versions of this ProductVersionDetails.
        :rtype: bool
        """
        return self._is_applicable_for_all_higher_versions

    @is_applicable_for_all_higher_versions.setter
    def is_applicable_for_all_higher_versions(self, is_applicable_for_all_higher_versions):
        """
        Sets the is_applicable_for_all_higher_versions of this ProductVersionDetails.
        Is rule applicable to all higher versions also


        :param is_applicable_for_all_higher_versions: The is_applicable_for_all_higher_versions of this ProductVersionDetails.
        :type: bool
        """
        self._is_applicable_for_all_higher_versions = is_applicable_for_all_higher_versions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other