# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BasePermissionsSummary(object):
    """
    Permissions object sent as part of the response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BasePermissionsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_permissions:
            The value to assign to the user_permissions property of this BasePermissionsSummary.
        :type user_permissions: list[str]

        """
        self.swagger_types = {
            'user_permissions': 'list[str]'
        }

        self.attribute_map = {
            'user_permissions': 'userPermissions'
        }

        self._user_permissions = None

    @property
    def user_permissions(self):
        """
        Gets the user_permissions of this BasePermissionsSummary.
        An array of permissions.


        :return: The user_permissions of this BasePermissionsSummary.
        :rtype: list[str]
        """
        return self._user_permissions

    @user_permissions.setter
    def user_permissions(self, user_permissions):
        """
        Sets the user_permissions of this BasePermissionsSummary.
        An array of permissions.


        :param user_permissions: The user_permissions of this BasePermissionsSummary.
        :type: list[str]
        """
        self._user_permissions = user_permissions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
