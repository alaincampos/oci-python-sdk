# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CmosUserGroupInfo(object):
    """
    Identifier and name of the technical support request's user group (`userGroupId` and `userGroupName`).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CmosUserGroupInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_group_id:
            The value to assign to the user_group_id property of this CmosUserGroupInfo.
        :type user_group_id: str

        :param user_group_name:
            The value to assign to the user_group_name property of this CmosUserGroupInfo.
        :type user_group_name: str

        """
        self.swagger_types = {
            'user_group_id': 'str',
            'user_group_name': 'str'
        }

        self.attribute_map = {
            'user_group_id': 'userGroupId',
            'user_group_name': 'userGroupName'
        }

        self._user_group_id = None
        self._user_group_name = None

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this CmosUserGroupInfo.
        Technical support type (`TECH`) only: The identifier of the support request's user group in My Oracle Cloud Support portal.


        :return: The user_group_id of this CmosUserGroupInfo.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this CmosUserGroupInfo.
        Technical support type (`TECH`) only: The identifier of the support request's user group in My Oracle Cloud Support portal.


        :param user_group_id: The user_group_id of this CmosUserGroupInfo.
        :type: str
        """
        self._user_group_id = user_group_id

    @property
    def user_group_name(self):
        """
        Gets the user_group_name of this CmosUserGroupInfo.
        Technical support type (`TECH`) only: Name of the support request's user group in My Oracle Cloud Support portal.


        :return: The user_group_name of this CmosUserGroupInfo.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """
        Sets the user_group_name of this CmosUserGroupInfo.
        Technical support type (`TECH`) only: Name of the support request's user group in My Oracle Cloud Support portal.


        :param user_group_name: The user_group_name of this CmosUserGroupInfo.
        :type: str
        """
        self._user_group_name = user_group_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other