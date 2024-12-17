# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostGpuConfiguration(HostConfigurationMetricGroup):
    """
    GPU configuration metrics
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostGpuConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostGpuConfiguration.metric_name` attribute
        of this class is ``HOST_GPU_CONFIGURATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostGpuConfiguration.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES", "HOST_FILESYSTEM_CONFIGURATION", "HOST_GPU_CONFIGURATION", "HOST_CONTAINERS"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostGpuConfiguration.
        :type time_collected: datetime

        :param gpu_id:
            The value to assign to the gpu_id property of this HostGpuConfiguration.
        :type gpu_id: int

        :param product_name:
            The value to assign to the product_name property of this HostGpuConfiguration.
        :type product_name: str

        :param vendor:
            The value to assign to the vendor property of this HostGpuConfiguration.
        :type vendor: str

        :param bus_id:
            The value to assign to the bus_id property of this HostGpuConfiguration.
        :type bus_id: str

        :param bus_width:
            The value to assign to the bus_width property of this HostGpuConfiguration.
        :type bus_width: int

        :param gpu_capabilities:
            The value to assign to the gpu_capabilities property of this HostGpuConfiguration.
        :type gpu_capabilities: str

        :param total_power:
            The value to assign to the total_power property of this HostGpuConfiguration.
        :type total_power: float

        :param total_memory:
            The value to assign to the total_memory property of this HostGpuConfiguration.
        :type total_memory: float

        :param total_video_clock_speed:
            The value to assign to the total_video_clock_speed property of this HostGpuConfiguration.
        :type total_video_clock_speed: float

        :param total_sm_clock_speed:
            The value to assign to the total_sm_clock_speed property of this HostGpuConfiguration.
        :type total_sm_clock_speed: float

        :param total_graphics_clock_speed:
            The value to assign to the total_graphics_clock_speed property of this HostGpuConfiguration.
        :type total_graphics_clock_speed: float

        :param total_memory_clock_speed:
            The value to assign to the total_memory_clock_speed property of this HostGpuConfiguration.
        :type total_memory_clock_speed: float

        :param cuda_version:
            The value to assign to the cuda_version property of this HostGpuConfiguration.
        :type cuda_version: str

        :param driver_version:
            The value to assign to the driver_version property of this HostGpuConfiguration.
        :type driver_version: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'gpu_id': 'int',
            'product_name': 'str',
            'vendor': 'str',
            'bus_id': 'str',
            'bus_width': 'int',
            'gpu_capabilities': 'str',
            'total_power': 'float',
            'total_memory': 'float',
            'total_video_clock_speed': 'float',
            'total_sm_clock_speed': 'float',
            'total_graphics_clock_speed': 'float',
            'total_memory_clock_speed': 'float',
            'cuda_version': 'str',
            'driver_version': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'gpu_id': 'gpuId',
            'product_name': 'productName',
            'vendor': 'vendor',
            'bus_id': 'busId',
            'bus_width': 'busWidth',
            'gpu_capabilities': 'gpuCapabilities',
            'total_power': 'totalPower',
            'total_memory': 'totalMemory',
            'total_video_clock_speed': 'totalVideoClockSpeed',
            'total_sm_clock_speed': 'totalSmClockSpeed',
            'total_graphics_clock_speed': 'totalGraphicsClockSpeed',
            'total_memory_clock_speed': 'totalMemoryClockSpeed',
            'cuda_version': 'cudaVersion',
            'driver_version': 'driverVersion'
        }

        self._metric_name = None
        self._time_collected = None
        self._gpu_id = None
        self._product_name = None
        self._vendor = None
        self._bus_id = None
        self._bus_width = None
        self._gpu_capabilities = None
        self._total_power = None
        self._total_memory = None
        self._total_video_clock_speed = None
        self._total_sm_clock_speed = None
        self._total_graphics_clock_speed = None
        self._total_memory_clock_speed = None
        self._cuda_version = None
        self._driver_version = None
        self._metric_name = 'HOST_GPU_CONFIGURATION'

    @property
    def gpu_id(self):
        """
        **[Required]** Gets the gpu_id of this HostGpuConfiguration.
        GPU Identifier


        :return: The gpu_id of this HostGpuConfiguration.
        :rtype: int
        """
        return self._gpu_id

    @gpu_id.setter
    def gpu_id(self, gpu_id):
        """
        Sets the gpu_id of this HostGpuConfiguration.
        GPU Identifier


        :param gpu_id: The gpu_id of this HostGpuConfiguration.
        :type: int
        """
        self._gpu_id = gpu_id

    @property
    def product_name(self):
        """
        **[Required]** Gets the product_name of this HostGpuConfiguration.
        GPU Product Name


        :return: The product_name of this HostGpuConfiguration.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this HostGpuConfiguration.
        GPU Product Name


        :param product_name: The product_name of this HostGpuConfiguration.
        :type: str
        """
        self._product_name = product_name

    @property
    def vendor(self):
        """
        **[Required]** Gets the vendor of this HostGpuConfiguration.
        GPU Vendor


        :return: The vendor of this HostGpuConfiguration.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this HostGpuConfiguration.
        GPU Vendor


        :param vendor: The vendor of this HostGpuConfiguration.
        :type: str
        """
        self._vendor = vendor

    @property
    def bus_id(self):
        """
        **[Required]** Gets the bus_id of this HostGpuConfiguration.
        Bus Identifier


        :return: The bus_id of this HostGpuConfiguration.
        :rtype: str
        """
        return self._bus_id

    @bus_id.setter
    def bus_id(self, bus_id):
        """
        Sets the bus_id of this HostGpuConfiguration.
        Bus Identifier


        :param bus_id: The bus_id of this HostGpuConfiguration.
        :type: str
        """
        self._bus_id = bus_id

    @property
    def bus_width(self):
        """
        **[Required]** Gets the bus_width of this HostGpuConfiguration.
        Bus Width


        :return: The bus_width of this HostGpuConfiguration.
        :rtype: int
        """
        return self._bus_width

    @bus_width.setter
    def bus_width(self, bus_width):
        """
        Sets the bus_width of this HostGpuConfiguration.
        Bus Width


        :param bus_width: The bus_width of this HostGpuConfiguration.
        :type: int
        """
        self._bus_width = bus_width

    @property
    def gpu_capabilities(self):
        """
        Gets the gpu_capabilities of this HostGpuConfiguration.
        GPU Capabilities


        :return: The gpu_capabilities of this HostGpuConfiguration.
        :rtype: str
        """
        return self._gpu_capabilities

    @gpu_capabilities.setter
    def gpu_capabilities(self, gpu_capabilities):
        """
        Sets the gpu_capabilities of this HostGpuConfiguration.
        GPU Capabilities


        :param gpu_capabilities: The gpu_capabilities of this HostGpuConfiguration.
        :type: str
        """
        self._gpu_capabilities = gpu_capabilities

    @property
    def total_power(self):
        """
        **[Required]** Gets the total_power of this HostGpuConfiguration.
        Power Capacity


        :return: The total_power of this HostGpuConfiguration.
        :rtype: float
        """
        return self._total_power

    @total_power.setter
    def total_power(self, total_power):
        """
        Sets the total_power of this HostGpuConfiguration.
        Power Capacity


        :param total_power: The total_power of this HostGpuConfiguration.
        :type: float
        """
        self._total_power = total_power

    @property
    def total_memory(self):
        """
        **[Required]** Gets the total_memory of this HostGpuConfiguration.
        Total Memory Allocated to GPU


        :return: The total_memory of this HostGpuConfiguration.
        :rtype: float
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """
        Sets the total_memory of this HostGpuConfiguration.
        Total Memory Allocated to GPU


        :param total_memory: The total_memory of this HostGpuConfiguration.
        :type: float
        """
        self._total_memory = total_memory

    @property
    def total_video_clock_speed(self):
        """
        **[Required]** Gets the total_video_clock_speed of this HostGpuConfiguration.
        Max Video Clock Speed


        :return: The total_video_clock_speed of this HostGpuConfiguration.
        :rtype: float
        """
        return self._total_video_clock_speed

    @total_video_clock_speed.setter
    def total_video_clock_speed(self, total_video_clock_speed):
        """
        Sets the total_video_clock_speed of this HostGpuConfiguration.
        Max Video Clock Speed


        :param total_video_clock_speed: The total_video_clock_speed of this HostGpuConfiguration.
        :type: float
        """
        self._total_video_clock_speed = total_video_clock_speed

    @property
    def total_sm_clock_speed(self):
        """
        **[Required]** Gets the total_sm_clock_speed of this HostGpuConfiguration.
        Max SM (Streaming Multiprocessor) Clock Speed


        :return: The total_sm_clock_speed of this HostGpuConfiguration.
        :rtype: float
        """
        return self._total_sm_clock_speed

    @total_sm_clock_speed.setter
    def total_sm_clock_speed(self, total_sm_clock_speed):
        """
        Sets the total_sm_clock_speed of this HostGpuConfiguration.
        Max SM (Streaming Multiprocessor) Clock Speed


        :param total_sm_clock_speed: The total_sm_clock_speed of this HostGpuConfiguration.
        :type: float
        """
        self._total_sm_clock_speed = total_sm_clock_speed

    @property
    def total_graphics_clock_speed(self):
        """
        **[Required]** Gets the total_graphics_clock_speed of this HostGpuConfiguration.
        Max Graphics Clock Speed


        :return: The total_graphics_clock_speed of this HostGpuConfiguration.
        :rtype: float
        """
        return self._total_graphics_clock_speed

    @total_graphics_clock_speed.setter
    def total_graphics_clock_speed(self, total_graphics_clock_speed):
        """
        Sets the total_graphics_clock_speed of this HostGpuConfiguration.
        Max Graphics Clock Speed


        :param total_graphics_clock_speed: The total_graphics_clock_speed of this HostGpuConfiguration.
        :type: float
        """
        self._total_graphics_clock_speed = total_graphics_clock_speed

    @property
    def total_memory_clock_speed(self):
        """
        **[Required]** Gets the total_memory_clock_speed of this HostGpuConfiguration.
        Max Memory Clock Speed


        :return: The total_memory_clock_speed of this HostGpuConfiguration.
        :rtype: float
        """
        return self._total_memory_clock_speed

    @total_memory_clock_speed.setter
    def total_memory_clock_speed(self, total_memory_clock_speed):
        """
        Sets the total_memory_clock_speed of this HostGpuConfiguration.
        Max Memory Clock Speed


        :param total_memory_clock_speed: The total_memory_clock_speed of this HostGpuConfiguration.
        :type: float
        """
        self._total_memory_clock_speed = total_memory_clock_speed

    @property
    def cuda_version(self):
        """
        **[Required]** Gets the cuda_version of this HostGpuConfiguration.
        CUDA library version


        :return: The cuda_version of this HostGpuConfiguration.
        :rtype: str
        """
        return self._cuda_version

    @cuda_version.setter
    def cuda_version(self, cuda_version):
        """
        Sets the cuda_version of this HostGpuConfiguration.
        CUDA library version


        :param cuda_version: The cuda_version of this HostGpuConfiguration.
        :type: str
        """
        self._cuda_version = cuda_version

    @property
    def driver_version(self):
        """
        **[Required]** Gets the driver_version of this HostGpuConfiguration.
        GPU Driver version


        :return: The driver_version of this HostGpuConfiguration.
        :rtype: str
        """
        return self._driver_version

    @driver_version.setter
    def driver_version(self, driver_version):
        """
        Sets the driver_version of this HostGpuConfiguration.
        GPU Driver version


        :param driver_version: The driver_version of this HostGpuConfiguration.
        :type: str
        """
        self._driver_version = driver_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other