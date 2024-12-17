# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwsEbsProperties(object):
    """
    AWS EBS volume related properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwsEbsProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attachments:
            The value to assign to the attachments property of this AwsEbsProperties.
        :type attachments: list[oci.cloud_bridge.models.VolumeAttachment]

        :param availability_zone:
            The value to assign to the availability_zone property of this AwsEbsProperties.
        :type availability_zone: str

        :param is_encrypted:
            The value to assign to the is_encrypted property of this AwsEbsProperties.
        :type is_encrypted: bool

        :param iops:
            The value to assign to the iops property of this AwsEbsProperties.
        :type iops: int

        :param is_multi_attach_enabled:
            The value to assign to the is_multi_attach_enabled property of this AwsEbsProperties.
        :type is_multi_attach_enabled: bool

        :param size_in_gi_bs:
            The value to assign to the size_in_gi_bs property of this AwsEbsProperties.
        :type size_in_gi_bs: int

        :param status:
            The value to assign to the status property of this AwsEbsProperties.
        :type status: str

        :param tags:
            The value to assign to the tags property of this AwsEbsProperties.
        :type tags: list[oci.cloud_bridge.models.Tag]

        :param throughput:
            The value to assign to the throughput property of this AwsEbsProperties.
        :type throughput: int

        :param volume_key:
            The value to assign to the volume_key property of this AwsEbsProperties.
        :type volume_key: str

        :param volume_type:
            The value to assign to the volume_type property of this AwsEbsProperties.
        :type volume_type: str

        """
        self.swagger_types = {
            'attachments': 'list[VolumeAttachment]',
            'availability_zone': 'str',
            'is_encrypted': 'bool',
            'iops': 'int',
            'is_multi_attach_enabled': 'bool',
            'size_in_gi_bs': 'int',
            'status': 'str',
            'tags': 'list[Tag]',
            'throughput': 'int',
            'volume_key': 'str',
            'volume_type': 'str'
        }

        self.attribute_map = {
            'attachments': 'attachments',
            'availability_zone': 'availabilityZone',
            'is_encrypted': 'isEncrypted',
            'iops': 'iops',
            'is_multi_attach_enabled': 'isMultiAttachEnabled',
            'size_in_gi_bs': 'sizeInGiBs',
            'status': 'status',
            'tags': 'tags',
            'throughput': 'throughput',
            'volume_key': 'volumeKey',
            'volume_type': 'volumeType'
        }

        self._attachments = None
        self._availability_zone = None
        self._is_encrypted = None
        self._iops = None
        self._is_multi_attach_enabled = None
        self._size_in_gi_bs = None
        self._status = None
        self._tags = None
        self._throughput = None
        self._volume_key = None
        self._volume_type = None

    @property
    def attachments(self):
        """
        Gets the attachments of this AwsEbsProperties.
        Information about the volume attachments.


        :return: The attachments of this AwsEbsProperties.
        :rtype: list[oci.cloud_bridge.models.VolumeAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this AwsEbsProperties.
        Information about the volume attachments.


        :param attachments: The attachments of this AwsEbsProperties.
        :type: list[oci.cloud_bridge.models.VolumeAttachment]
        """
        self._attachments = attachments

    @property
    def availability_zone(self):
        """
        Gets the availability_zone of this AwsEbsProperties.
        The Availability Zone for the volume.


        :return: The availability_zone of this AwsEbsProperties.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """
        Sets the availability_zone of this AwsEbsProperties.
        The Availability Zone for the volume.


        :param availability_zone: The availability_zone of this AwsEbsProperties.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def is_encrypted(self):
        """
        **[Required]** Gets the is_encrypted of this AwsEbsProperties.
        Indicates whether the volume is encrypted.


        :return: The is_encrypted of this AwsEbsProperties.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """
        Sets the is_encrypted of this AwsEbsProperties.
        Indicates whether the volume is encrypted.


        :param is_encrypted: The is_encrypted of this AwsEbsProperties.
        :type: bool
        """
        self._is_encrypted = is_encrypted

    @property
    def iops(self):
        """
        Gets the iops of this AwsEbsProperties.
        The number of I/O operations per second.


        :return: The iops of this AwsEbsProperties.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """
        Sets the iops of this AwsEbsProperties.
        The number of I/O operations per second.


        :param iops: The iops of this AwsEbsProperties.
        :type: int
        """
        self._iops = iops

    @property
    def is_multi_attach_enabled(self):
        """
        **[Required]** Gets the is_multi_attach_enabled of this AwsEbsProperties.
        Indicates whether Amazon EBS Multi-Attach is enabled.


        :return: The is_multi_attach_enabled of this AwsEbsProperties.
        :rtype: bool
        """
        return self._is_multi_attach_enabled

    @is_multi_attach_enabled.setter
    def is_multi_attach_enabled(self, is_multi_attach_enabled):
        """
        Sets the is_multi_attach_enabled of this AwsEbsProperties.
        Indicates whether Amazon EBS Multi-Attach is enabled.


        :param is_multi_attach_enabled: The is_multi_attach_enabled of this AwsEbsProperties.
        :type: bool
        """
        self._is_multi_attach_enabled = is_multi_attach_enabled

    @property
    def size_in_gi_bs(self):
        """
        **[Required]** Gets the size_in_gi_bs of this AwsEbsProperties.
        The size of the volume, in GiBs.


        :return: The size_in_gi_bs of this AwsEbsProperties.
        :rtype: int
        """
        return self._size_in_gi_bs

    @size_in_gi_bs.setter
    def size_in_gi_bs(self, size_in_gi_bs):
        """
        Sets the size_in_gi_bs of this AwsEbsProperties.
        The size of the volume, in GiBs.


        :param size_in_gi_bs: The size_in_gi_bs of this AwsEbsProperties.
        :type: int
        """
        self._size_in_gi_bs = size_in_gi_bs

    @property
    def status(self):
        """
        Gets the status of this AwsEbsProperties.
        The volume state.


        :return: The status of this AwsEbsProperties.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AwsEbsProperties.
        The volume state.


        :param status: The status of this AwsEbsProperties.
        :type: str
        """
        self._status = status

    @property
    def tags(self):
        """
        Gets the tags of this AwsEbsProperties.
        Any tags assigned to the volume.


        :return: The tags of this AwsEbsProperties.
        :rtype: list[oci.cloud_bridge.models.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AwsEbsProperties.
        Any tags assigned to the volume.


        :param tags: The tags of this AwsEbsProperties.
        :type: list[oci.cloud_bridge.models.Tag]
        """
        self._tags = tags

    @property
    def throughput(self):
        """
        Gets the throughput of this AwsEbsProperties.
        The throughput that the volume supports, in MiB/s.


        :return: The throughput of this AwsEbsProperties.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """
        Sets the throughput of this AwsEbsProperties.
        The throughput that the volume supports, in MiB/s.


        :param throughput: The throughput of this AwsEbsProperties.
        :type: int
        """
        self._throughput = throughput

    @property
    def volume_key(self):
        """
        **[Required]** Gets the volume_key of this AwsEbsProperties.
        The ID of the volume.


        :return: The volume_key of this AwsEbsProperties.
        :rtype: str
        """
        return self._volume_key

    @volume_key.setter
    def volume_key(self, volume_key):
        """
        Sets the volume_key of this AwsEbsProperties.
        The ID of the volume.


        :param volume_key: The volume_key of this AwsEbsProperties.
        :type: str
        """
        self._volume_key = volume_key

    @property
    def volume_type(self):
        """
        **[Required]** Gets the volume_type of this AwsEbsProperties.
        The volume type.


        :return: The volume_type of this AwsEbsProperties.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """
        Sets the volume_type of this AwsEbsProperties.
        The volume type.


        :param volume_type: The volume_type of this AwsEbsProperties.
        :type: str
        """
        self._volume_type = volume_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other