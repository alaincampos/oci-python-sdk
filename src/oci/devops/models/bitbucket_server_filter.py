# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .filter import Filter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BitbucketServerFilter(Filter):
    """
    The filter for Bitbucket Server events.
    """

    #: A constant which can be used with the events property of a BitbucketServerFilter.
    #: This constant has a value of "PUSH"
    EVENTS_PUSH = "PUSH"

    #: A constant which can be used with the events property of a BitbucketServerFilter.
    #: This constant has a value of "PULL_REQUEST_OPENED"
    EVENTS_PULL_REQUEST_OPENED = "PULL_REQUEST_OPENED"

    #: A constant which can be used with the events property of a BitbucketServerFilter.
    #: This constant has a value of "PULL_REQUEST_MODIFIED"
    EVENTS_PULL_REQUEST_MODIFIED = "PULL_REQUEST_MODIFIED"

    #: A constant which can be used with the events property of a BitbucketServerFilter.
    #: This constant has a value of "PULL_REQUEST_MERGED"
    EVENTS_PULL_REQUEST_MERGED = "PULL_REQUEST_MERGED"

    def __init__(self, **kwargs):
        """
        Initializes a new BitbucketServerFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.BitbucketServerFilter.trigger_source` attribute
        of this class is ``BITBUCKET_SERVER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trigger_source:
            The value to assign to the trigger_source property of this BitbucketServerFilter.
        :type trigger_source: str

        :param events:
            The value to assign to the events property of this BitbucketServerFilter.
            Allowed values for items in this list are: "PUSH", "PULL_REQUEST_OPENED", "PULL_REQUEST_MODIFIED", "PULL_REQUEST_MERGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type events: list[str]

        :param include:
            The value to assign to the include property of this BitbucketServerFilter.
        :type include: oci.devops.models.BitbucketServerFilterAttributes

        """
        self.swagger_types = {
            'trigger_source': 'str',
            'events': 'list[str]',
            'include': 'BitbucketServerFilterAttributes'
        }

        self.attribute_map = {
            'trigger_source': 'triggerSource',
            'events': 'events',
            'include': 'include'
        }

        self._trigger_source = None
        self._events = None
        self._include = None
        self._trigger_source = 'BITBUCKET_SERVER'

    @property
    def events(self):
        """
        Gets the events of this BitbucketServerFilter.
        The events, for example, PUSH, PULL_REQUEST_MERGE.

        Allowed values for items in this list are: "PUSH", "PULL_REQUEST_OPENED", "PULL_REQUEST_MODIFIED", "PULL_REQUEST_MERGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The events of this BitbucketServerFilter.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this BitbucketServerFilter.
        The events, for example, PUSH, PULL_REQUEST_MERGE.


        :param events: The events of this BitbucketServerFilter.
        :type: list[str]
        """
        allowed_values = ["PUSH", "PULL_REQUEST_OPENED", "PULL_REQUEST_MODIFIED", "PULL_REQUEST_MERGED"]
        if events:
            events[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in events]
        self._events = events

    @property
    def include(self):
        """
        Gets the include of this BitbucketServerFilter.

        :return: The include of this BitbucketServerFilter.
        :rtype: oci.devops.models.BitbucketServerFilterAttributes
        """
        return self._include

    @include.setter
    def include(self, include):
        """
        Sets the include of this BitbucketServerFilter.

        :param include: The include of this BitbucketServerFilter.
        :type: oci.devops.models.BitbucketServerFilterAttributes
        """
        self._include = include

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other