# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwsEc2Properties(object):
    """
    AWS virtual machine related properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwsEc2Properties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param architecture:
            The value to assign to the architecture property of this AwsEc2Properties.
        :type architecture: str

        :param boot_mode:
            The value to assign to the boot_mode property of this AwsEc2Properties.
        :type boot_mode: str

        :param capacity_reservation_key:
            The value to assign to the capacity_reservation_key property of this AwsEc2Properties.
        :type capacity_reservation_key: str

        :param are_elastic_inference_accelerators_present:
            The value to assign to the are_elastic_inference_accelerators_present property of this AwsEc2Properties.
        :type are_elastic_inference_accelerators_present: bool

        :param is_enclave_options:
            The value to assign to the is_enclave_options property of this AwsEc2Properties.
        :type is_enclave_options: bool

        :param is_hibernation_options:
            The value to assign to the is_hibernation_options property of this AwsEc2Properties.
        :type is_hibernation_options: bool

        :param image_key:
            The value to assign to the image_key property of this AwsEc2Properties.
        :type image_key: str

        :param instance_key:
            The value to assign to the instance_key property of this AwsEc2Properties.
        :type instance_key: str

        :param instance_lifecycle:
            The value to assign to the instance_lifecycle property of this AwsEc2Properties.
        :type instance_lifecycle: str

        :param instance_type:
            The value to assign to the instance_type property of this AwsEc2Properties.
        :type instance_type: str

        :param ip_address:
            The value to assign to the ip_address property of this AwsEc2Properties.
        :type ip_address: str

        :param ipv6_address:
            The value to assign to the ipv6_address property of this AwsEc2Properties.
        :type ipv6_address: str

        :param kernel_key:
            The value to assign to the kernel_key property of this AwsEc2Properties.
        :type kernel_key: str

        :param time_launch:
            The value to assign to the time_launch property of this AwsEc2Properties.
        :type time_launch: datetime

        :param licenses:
            The value to assign to the licenses property of this AwsEc2Properties.
        :type licenses: list[str]

        :param maintenance_options:
            The value to assign to the maintenance_options property of this AwsEc2Properties.
        :type maintenance_options: str

        :param monitoring:
            The value to assign to the monitoring property of this AwsEc2Properties.
        :type monitoring: str

        :param network_interfaces:
            The value to assign to the network_interfaces property of this AwsEc2Properties.
        :type network_interfaces: list[oci.cloud_bridge.models.InstanceNetworkInterface]

        :param placement:
            The value to assign to the placement property of this AwsEc2Properties.
        :type placement: oci.cloud_bridge.models.Placement

        :param private_dns_name:
            The value to assign to the private_dns_name property of this AwsEc2Properties.
        :type private_dns_name: str

        :param private_ip_address:
            The value to assign to the private_ip_address property of this AwsEc2Properties.
        :type private_ip_address: str

        :param root_device_name:
            The value to assign to the root_device_name property of this AwsEc2Properties.
        :type root_device_name: str

        :param root_device_type:
            The value to assign to the root_device_type property of this AwsEc2Properties.
        :type root_device_type: str

        :param security_groups:
            The value to assign to the security_groups property of this AwsEc2Properties.
        :type security_groups: list[oci.cloud_bridge.models.GroupIdentifier]

        :param is_source_dest_check:
            The value to assign to the is_source_dest_check property of this AwsEc2Properties.
        :type is_source_dest_check: bool

        :param is_spot_instance:
            The value to assign to the is_spot_instance property of this AwsEc2Properties.
        :type is_spot_instance: bool

        :param sriov_net_support:
            The value to assign to the sriov_net_support property of this AwsEc2Properties.
        :type sriov_net_support: str

        :param state:
            The value to assign to the state property of this AwsEc2Properties.
        :type state: oci.cloud_bridge.models.InstanceState

        :param subnet_key:
            The value to assign to the subnet_key property of this AwsEc2Properties.
        :type subnet_key: str

        :param tags:
            The value to assign to the tags property of this AwsEc2Properties.
        :type tags: list[oci.cloud_bridge.models.Tag]

        :param tpm_support:
            The value to assign to the tpm_support property of this AwsEc2Properties.
        :type tpm_support: str

        :param virtualization_type:
            The value to assign to the virtualization_type property of this AwsEc2Properties.
        :type virtualization_type: str

        :param vpc_key:
            The value to assign to the vpc_key property of this AwsEc2Properties.
        :type vpc_key: str

        """
        self.swagger_types = {
            'architecture': 'str',
            'boot_mode': 'str',
            'capacity_reservation_key': 'str',
            'are_elastic_inference_accelerators_present': 'bool',
            'is_enclave_options': 'bool',
            'is_hibernation_options': 'bool',
            'image_key': 'str',
            'instance_key': 'str',
            'instance_lifecycle': 'str',
            'instance_type': 'str',
            'ip_address': 'str',
            'ipv6_address': 'str',
            'kernel_key': 'str',
            'time_launch': 'datetime',
            'licenses': 'list[str]',
            'maintenance_options': 'str',
            'monitoring': 'str',
            'network_interfaces': 'list[InstanceNetworkInterface]',
            'placement': 'Placement',
            'private_dns_name': 'str',
            'private_ip_address': 'str',
            'root_device_name': 'str',
            'root_device_type': 'str',
            'security_groups': 'list[GroupIdentifier]',
            'is_source_dest_check': 'bool',
            'is_spot_instance': 'bool',
            'sriov_net_support': 'str',
            'state': 'InstanceState',
            'subnet_key': 'str',
            'tags': 'list[Tag]',
            'tpm_support': 'str',
            'virtualization_type': 'str',
            'vpc_key': 'str'
        }

        self.attribute_map = {
            'architecture': 'architecture',
            'boot_mode': 'bootMode',
            'capacity_reservation_key': 'capacityReservationKey',
            'are_elastic_inference_accelerators_present': 'areElasticInferenceAcceleratorsPresent',
            'is_enclave_options': 'isEnclaveOptions',
            'is_hibernation_options': 'isHibernationOptions',
            'image_key': 'imageKey',
            'instance_key': 'instanceKey',
            'instance_lifecycle': 'instanceLifecycle',
            'instance_type': 'instanceType',
            'ip_address': 'ipAddress',
            'ipv6_address': 'ipv6Address',
            'kernel_key': 'kernelKey',
            'time_launch': 'timeLaunch',
            'licenses': 'licenses',
            'maintenance_options': 'maintenanceOptions',
            'monitoring': 'monitoring',
            'network_interfaces': 'networkInterfaces',
            'placement': 'placement',
            'private_dns_name': 'privateDnsName',
            'private_ip_address': 'privateIpAddress',
            'root_device_name': 'rootDeviceName',
            'root_device_type': 'rootDeviceType',
            'security_groups': 'securityGroups',
            'is_source_dest_check': 'isSourceDestCheck',
            'is_spot_instance': 'isSpotInstance',
            'sriov_net_support': 'sriovNetSupport',
            'state': 'state',
            'subnet_key': 'subnetKey',
            'tags': 'tags',
            'tpm_support': 'tpmSupport',
            'virtualization_type': 'virtualizationType',
            'vpc_key': 'vpcKey'
        }

        self._architecture = None
        self._boot_mode = None
        self._capacity_reservation_key = None
        self._are_elastic_inference_accelerators_present = None
        self._is_enclave_options = None
        self._is_hibernation_options = None
        self._image_key = None
        self._instance_key = None
        self._instance_lifecycle = None
        self._instance_type = None
        self._ip_address = None
        self._ipv6_address = None
        self._kernel_key = None
        self._time_launch = None
        self._licenses = None
        self._maintenance_options = None
        self._monitoring = None
        self._network_interfaces = None
        self._placement = None
        self._private_dns_name = None
        self._private_ip_address = None
        self._root_device_name = None
        self._root_device_type = None
        self._security_groups = None
        self._is_source_dest_check = None
        self._is_spot_instance = None
        self._sriov_net_support = None
        self._state = None
        self._subnet_key = None
        self._tags = None
        self._tpm_support = None
        self._virtualization_type = None
        self._vpc_key = None

    @property
    def architecture(self):
        """
        **[Required]** Gets the architecture of this AwsEc2Properties.
        The architecture of the image.


        :return: The architecture of this AwsEc2Properties.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this AwsEc2Properties.
        The architecture of the image.


        :param architecture: The architecture of this AwsEc2Properties.
        :type: str
        """
        self._architecture = architecture

    @property
    def boot_mode(self):
        """
        Gets the boot_mode of this AwsEc2Properties.
        The boot mode of the instance.


        :return: The boot_mode of this AwsEc2Properties.
        :rtype: str
        """
        return self._boot_mode

    @boot_mode.setter
    def boot_mode(self, boot_mode):
        """
        Sets the boot_mode of this AwsEc2Properties.
        The boot mode of the instance.


        :param boot_mode: The boot_mode of this AwsEc2Properties.
        :type: str
        """
        self._boot_mode = boot_mode

    @property
    def capacity_reservation_key(self):
        """
        Gets the capacity_reservation_key of this AwsEc2Properties.
        The ID of the Capacity Reservation.


        :return: The capacity_reservation_key of this AwsEc2Properties.
        :rtype: str
        """
        return self._capacity_reservation_key

    @capacity_reservation_key.setter
    def capacity_reservation_key(self, capacity_reservation_key):
        """
        Sets the capacity_reservation_key of this AwsEc2Properties.
        The ID of the Capacity Reservation.


        :param capacity_reservation_key: The capacity_reservation_key of this AwsEc2Properties.
        :type: str
        """
        self._capacity_reservation_key = capacity_reservation_key

    @property
    def are_elastic_inference_accelerators_present(self):
        """
        Gets the are_elastic_inference_accelerators_present of this AwsEc2Properties.
        Indicates if the elastic inference accelerators attached to an instance


        :return: The are_elastic_inference_accelerators_present of this AwsEc2Properties.
        :rtype: bool
        """
        return self._are_elastic_inference_accelerators_present

    @are_elastic_inference_accelerators_present.setter
    def are_elastic_inference_accelerators_present(self, are_elastic_inference_accelerators_present):
        """
        Sets the are_elastic_inference_accelerators_present of this AwsEc2Properties.
        Indicates if the elastic inference accelerators attached to an instance


        :param are_elastic_inference_accelerators_present: The are_elastic_inference_accelerators_present of this AwsEc2Properties.
        :type: bool
        """
        self._are_elastic_inference_accelerators_present = are_elastic_inference_accelerators_present

    @property
    def is_enclave_options(self):
        """
        Gets the is_enclave_options of this AwsEc2Properties.
        Indicates whether the instance is enabled for AWS Nitro Enclaves.


        :return: The is_enclave_options of this AwsEc2Properties.
        :rtype: bool
        """
        return self._is_enclave_options

    @is_enclave_options.setter
    def is_enclave_options(self, is_enclave_options):
        """
        Sets the is_enclave_options of this AwsEc2Properties.
        Indicates whether the instance is enabled for AWS Nitro Enclaves.


        :param is_enclave_options: The is_enclave_options of this AwsEc2Properties.
        :type: bool
        """
        self._is_enclave_options = is_enclave_options

    @property
    def is_hibernation_options(self):
        """
        Gets the is_hibernation_options of this AwsEc2Properties.
        Indicates whether the instance is enabled for hibernation.


        :return: The is_hibernation_options of this AwsEc2Properties.
        :rtype: bool
        """
        return self._is_hibernation_options

    @is_hibernation_options.setter
    def is_hibernation_options(self, is_hibernation_options):
        """
        Sets the is_hibernation_options of this AwsEc2Properties.
        Indicates whether the instance is enabled for hibernation.


        :param is_hibernation_options: The is_hibernation_options of this AwsEc2Properties.
        :type: bool
        """
        self._is_hibernation_options = is_hibernation_options

    @property
    def image_key(self):
        """
        Gets the image_key of this AwsEc2Properties.
        The ID of the AMI used to launch the instance.


        :return: The image_key of this AwsEc2Properties.
        :rtype: str
        """
        return self._image_key

    @image_key.setter
    def image_key(self, image_key):
        """
        Sets the image_key of this AwsEc2Properties.
        The ID of the AMI used to launch the instance.


        :param image_key: The image_key of this AwsEc2Properties.
        :type: str
        """
        self._image_key = image_key

    @property
    def instance_key(self):
        """
        **[Required]** Gets the instance_key of this AwsEc2Properties.
        The ID of the instance.


        :return: The instance_key of this AwsEc2Properties.
        :rtype: str
        """
        return self._instance_key

    @instance_key.setter
    def instance_key(self, instance_key):
        """
        Sets the instance_key of this AwsEc2Properties.
        The ID of the instance.


        :param instance_key: The instance_key of this AwsEc2Properties.
        :type: str
        """
        self._instance_key = instance_key

    @property
    def instance_lifecycle(self):
        """
        Gets the instance_lifecycle of this AwsEc2Properties.
        Indicates whether this is a Spot Instance or a Scheduled Instance.


        :return: The instance_lifecycle of this AwsEc2Properties.
        :rtype: str
        """
        return self._instance_lifecycle

    @instance_lifecycle.setter
    def instance_lifecycle(self, instance_lifecycle):
        """
        Sets the instance_lifecycle of this AwsEc2Properties.
        Indicates whether this is a Spot Instance or a Scheduled Instance.


        :param instance_lifecycle: The instance_lifecycle of this AwsEc2Properties.
        :type: str
        """
        self._instance_lifecycle = instance_lifecycle

    @property
    def instance_type(self):
        """
        **[Required]** Gets the instance_type of this AwsEc2Properties.
        The instance type.


        :return: The instance_type of this AwsEc2Properties.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """
        Sets the instance_type of this AwsEc2Properties.
        The instance type.


        :param instance_type: The instance_type of this AwsEc2Properties.
        :type: str
        """
        self._instance_type = instance_type

    @property
    def ip_address(self):
        """
        Gets the ip_address of this AwsEc2Properties.
        The public IPv4 address, or the Carrier IP address assigned to the instance.


        :return: The ip_address of this AwsEc2Properties.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this AwsEc2Properties.
        The public IPv4 address, or the Carrier IP address assigned to the instance.


        :param ip_address: The ip_address of this AwsEc2Properties.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        """
        Gets the ipv6_address of this AwsEc2Properties.
        The IPv6 address assigned to the instance.


        :return: The ipv6_address of this AwsEc2Properties.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """
        Sets the ipv6_address of this AwsEc2Properties.
        The IPv6 address assigned to the instance.


        :param ipv6_address: The ipv6_address of this AwsEc2Properties.
        :type: str
        """
        self._ipv6_address = ipv6_address

    @property
    def kernel_key(self):
        """
        Gets the kernel_key of this AwsEc2Properties.
        The kernel associated with this instance, if applicable.


        :return: The kernel_key of this AwsEc2Properties.
        :rtype: str
        """
        return self._kernel_key

    @kernel_key.setter
    def kernel_key(self, kernel_key):
        """
        Sets the kernel_key of this AwsEc2Properties.
        The kernel associated with this instance, if applicable.


        :param kernel_key: The kernel_key of this AwsEc2Properties.
        :type: str
        """
        self._kernel_key = kernel_key

    @property
    def time_launch(self):
        """
        Gets the time_launch of this AwsEc2Properties.
        The time the instance was launched.


        :return: The time_launch of this AwsEc2Properties.
        :rtype: datetime
        """
        return self._time_launch

    @time_launch.setter
    def time_launch(self, time_launch):
        """
        Sets the time_launch of this AwsEc2Properties.
        The time the instance was launched.


        :param time_launch: The time_launch of this AwsEc2Properties.
        :type: datetime
        """
        self._time_launch = time_launch

    @property
    def licenses(self):
        """
        Gets the licenses of this AwsEc2Properties.
        The license configurations for the instance.


        :return: The licenses of this AwsEc2Properties.
        :rtype: list[str]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """
        Sets the licenses of this AwsEc2Properties.
        The license configurations for the instance.


        :param licenses: The licenses of this AwsEc2Properties.
        :type: list[str]
        """
        self._licenses = licenses

    @property
    def maintenance_options(self):
        """
        Gets the maintenance_options of this AwsEc2Properties.
        Provides information on the recovery and maintenance options of your instance.


        :return: The maintenance_options of this AwsEc2Properties.
        :rtype: str
        """
        return self._maintenance_options

    @maintenance_options.setter
    def maintenance_options(self, maintenance_options):
        """
        Sets the maintenance_options of this AwsEc2Properties.
        Provides information on the recovery and maintenance options of your instance.


        :param maintenance_options: The maintenance_options of this AwsEc2Properties.
        :type: str
        """
        self._maintenance_options = maintenance_options

    @property
    def monitoring(self):
        """
        Gets the monitoring of this AwsEc2Properties.
        The monitoring for the instance.


        :return: The monitoring of this AwsEc2Properties.
        :rtype: str
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """
        Sets the monitoring of this AwsEc2Properties.
        The monitoring for the instance.


        :param monitoring: The monitoring of this AwsEc2Properties.
        :type: str
        """
        self._monitoring = monitoring

    @property
    def network_interfaces(self):
        """
        Gets the network_interfaces of this AwsEc2Properties.
        The network interfaces for the instance.


        :return: The network_interfaces of this AwsEc2Properties.
        :rtype: list[oci.cloud_bridge.models.InstanceNetworkInterface]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """
        Sets the network_interfaces of this AwsEc2Properties.
        The network interfaces for the instance.


        :param network_interfaces: The network_interfaces of this AwsEc2Properties.
        :type: list[oci.cloud_bridge.models.InstanceNetworkInterface]
        """
        self._network_interfaces = network_interfaces

    @property
    def placement(self):
        """
        Gets the placement of this AwsEc2Properties.

        :return: The placement of this AwsEc2Properties.
        :rtype: oci.cloud_bridge.models.Placement
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        """
        Sets the placement of this AwsEc2Properties.

        :param placement: The placement of this AwsEc2Properties.
        :type: oci.cloud_bridge.models.Placement
        """
        self._placement = placement

    @property
    def private_dns_name(self):
        """
        Gets the private_dns_name of this AwsEc2Properties.
        (IPv4 only) The private DNS hostname name assigned to the instance.


        :return: The private_dns_name of this AwsEc2Properties.
        :rtype: str
        """
        return self._private_dns_name

    @private_dns_name.setter
    def private_dns_name(self, private_dns_name):
        """
        Sets the private_dns_name of this AwsEc2Properties.
        (IPv4 only) The private DNS hostname name assigned to the instance.


        :param private_dns_name: The private_dns_name of this AwsEc2Properties.
        :type: str
        """
        self._private_dns_name = private_dns_name

    @property
    def private_ip_address(self):
        """
        Gets the private_ip_address of this AwsEc2Properties.
        The private IPv4 address assigned to the instance.


        :return: The private_ip_address of this AwsEc2Properties.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """
        Sets the private_ip_address of this AwsEc2Properties.
        The private IPv4 address assigned to the instance.


        :param private_ip_address: The private_ip_address of this AwsEc2Properties.
        :type: str
        """
        self._private_ip_address = private_ip_address

    @property
    def root_device_name(self):
        """
        **[Required]** Gets the root_device_name of this AwsEc2Properties.
        The device name of the root device volume.


        :return: The root_device_name of this AwsEc2Properties.
        :rtype: str
        """
        return self._root_device_name

    @root_device_name.setter
    def root_device_name(self, root_device_name):
        """
        Sets the root_device_name of this AwsEc2Properties.
        The device name of the root device volume.


        :param root_device_name: The root_device_name of this AwsEc2Properties.
        :type: str
        """
        self._root_device_name = root_device_name

    @property
    def root_device_type(self):
        """
        Gets the root_device_type of this AwsEc2Properties.
        The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.


        :return: The root_device_type of this AwsEc2Properties.
        :rtype: str
        """
        return self._root_device_type

    @root_device_type.setter
    def root_device_type(self, root_device_type):
        """
        Sets the root_device_type of this AwsEc2Properties.
        The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.


        :param root_device_type: The root_device_type of this AwsEc2Properties.
        :type: str
        """
        self._root_device_type = root_device_type

    @property
    def security_groups(self):
        """
        Gets the security_groups of this AwsEc2Properties.
        The security groups for the instance.


        :return: The security_groups of this AwsEc2Properties.
        :rtype: list[oci.cloud_bridge.models.GroupIdentifier]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """
        Sets the security_groups of this AwsEc2Properties.
        The security groups for the instance.


        :param security_groups: The security_groups of this AwsEc2Properties.
        :type: list[oci.cloud_bridge.models.GroupIdentifier]
        """
        self._security_groups = security_groups

    @property
    def is_source_dest_check(self):
        """
        Gets the is_source_dest_check of this AwsEc2Properties.
        Indicates whether source/destination checking is enabled.


        :return: The is_source_dest_check of this AwsEc2Properties.
        :rtype: bool
        """
        return self._is_source_dest_check

    @is_source_dest_check.setter
    def is_source_dest_check(self, is_source_dest_check):
        """
        Sets the is_source_dest_check of this AwsEc2Properties.
        Indicates whether source/destination checking is enabled.


        :param is_source_dest_check: The is_source_dest_check of this AwsEc2Properties.
        :type: bool
        """
        self._is_source_dest_check = is_source_dest_check

    @property
    def is_spot_instance(self):
        """
        Gets the is_spot_instance of this AwsEc2Properties.
        If the request is a Spot Instance request, this value will be true.


        :return: The is_spot_instance of this AwsEc2Properties.
        :rtype: bool
        """
        return self._is_spot_instance

    @is_spot_instance.setter
    def is_spot_instance(self, is_spot_instance):
        """
        Sets the is_spot_instance of this AwsEc2Properties.
        If the request is a Spot Instance request, this value will be true.


        :param is_spot_instance: The is_spot_instance of this AwsEc2Properties.
        :type: bool
        """
        self._is_spot_instance = is_spot_instance

    @property
    def sriov_net_support(self):
        """
        Gets the sriov_net_support of this AwsEc2Properties.
        Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.


        :return: The sriov_net_support of this AwsEc2Properties.
        :rtype: str
        """
        return self._sriov_net_support

    @sriov_net_support.setter
    def sriov_net_support(self, sriov_net_support):
        """
        Sets the sriov_net_support of this AwsEc2Properties.
        Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.


        :param sriov_net_support: The sriov_net_support of this AwsEc2Properties.
        :type: str
        """
        self._sriov_net_support = sriov_net_support

    @property
    def state(self):
        """
        **[Required]** Gets the state of this AwsEc2Properties.

        :return: The state of this AwsEc2Properties.
        :rtype: oci.cloud_bridge.models.InstanceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AwsEc2Properties.

        :param state: The state of this AwsEc2Properties.
        :type: oci.cloud_bridge.models.InstanceState
        """
        self._state = state

    @property
    def subnet_key(self):
        """
        Gets the subnet_key of this AwsEc2Properties.
        EC2-VPC The ID of the subnet in which the instance is running.


        :return: The subnet_key of this AwsEc2Properties.
        :rtype: str
        """
        return self._subnet_key

    @subnet_key.setter
    def subnet_key(self, subnet_key):
        """
        Sets the subnet_key of this AwsEc2Properties.
        EC2-VPC The ID of the subnet in which the instance is running.


        :param subnet_key: The subnet_key of this AwsEc2Properties.
        :type: str
        """
        self._subnet_key = subnet_key

    @property
    def tags(self):
        """
        Gets the tags of this AwsEc2Properties.
        Any tags assigned to the instance.


        :return: The tags of this AwsEc2Properties.
        :rtype: list[oci.cloud_bridge.models.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AwsEc2Properties.
        Any tags assigned to the instance.


        :param tags: The tags of this AwsEc2Properties.
        :type: list[oci.cloud_bridge.models.Tag]
        """
        self._tags = tags

    @property
    def tpm_support(self):
        """
        Gets the tpm_support of this AwsEc2Properties.
        If the instance is configured for NitroTPM support, the value is v2.0.


        :return: The tpm_support of this AwsEc2Properties.
        :rtype: str
        """
        return self._tpm_support

    @tpm_support.setter
    def tpm_support(self, tpm_support):
        """
        Sets the tpm_support of this AwsEc2Properties.
        If the instance is configured for NitroTPM support, the value is v2.0.


        :param tpm_support: The tpm_support of this AwsEc2Properties.
        :type: str
        """
        self._tpm_support = tpm_support

    @property
    def virtualization_type(self):
        """
        Gets the virtualization_type of this AwsEc2Properties.
        The virtualization type of the instance.


        :return: The virtualization_type of this AwsEc2Properties.
        :rtype: str
        """
        return self._virtualization_type

    @virtualization_type.setter
    def virtualization_type(self, virtualization_type):
        """
        Sets the virtualization_type of this AwsEc2Properties.
        The virtualization type of the instance.


        :param virtualization_type: The virtualization_type of this AwsEc2Properties.
        :type: str
        """
        self._virtualization_type = virtualization_type

    @property
    def vpc_key(self):
        """
        Gets the vpc_key of this AwsEc2Properties.
        EC2-VPC The ID of the VPC in which the instance is running.


        :return: The vpc_key of this AwsEc2Properties.
        :rtype: str
        """
        return self._vpc_key

    @vpc_key.setter
    def vpc_key(self, vpc_key):
        """
        Sets the vpc_key of this AwsEc2Properties.
        EC2-VPC The ID of the VPC in which the instance is running.


        :param vpc_key: The vpc_key of this AwsEc2Properties.
        :type: str
        """
        self._vpc_key = vpc_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other