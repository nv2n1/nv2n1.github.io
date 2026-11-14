---
title: "nvidia-smi(1)"
name: "nvidia-smi"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvidia-smi/"
description: "nvidia-smi – NVIDIA System Management Interface program"
---

<h2 class="name">NAME</h2>
<p> nvidia-smi &#8211; NVIDIA System Management Interface program </p>
<h2>SYNOPSIS</h2>
<p> nvidia-smi [OPTION1 [ARG1]] [OPTION2 [ARG2]] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> nvidia-smi (also NVSMI) provides monitoring and management capabilities for each of NVIDIA&#8217;s Tesla, Quadro, GRID and GeForce devices from Fermi and higher architecture families. GeForce Titan series devices are supported for most functions with very limited information provided for the remainder of the Geforce brand. NVSMI is a cross platform tool that supports all standard NVIDIA driver-supported Linux distros, as well as 64bit versions of Windows starting with Windows Server 2008 R2. Metrics can be consumed directly by users via stdout, or provided by file via CSV and XML formats for scripting purposes. </p>
<p> Note that much of the functionality of NVSMI is provided by the underlying NVML C-based library. See the NVIDIA developer website link below for more information about NVML. NVML-based python bindings are also available. </p>
<p> The output of NVSMI is not guaranteed to be backwards compatible. However, both NVML and the Python bindings are backwards compatible, and should be the first choice when writing any tools that must be maintained across NVIDIA driver releases. </p>
<p> <code>NVML SDK:</code> <i><a rel="nofollow" href="http://developer.nvidia.com/nvidia-management-library-nvml/">http://developer.nvidia.com/nvidia-management-library-nvml/</a></i> </p>
<p> <code>Python bindings:</code> <i><a rel="nofollow" href="http://pypi.python.org/pypi/nvidia-ml-py/">http://pypi.python.org/pypi/nvidia-ml-py/</a></i> </p>
<h2>OPTIONS</h2>
<h3>GENERAL OPTIONS</h3>
<h3>-h, &#8211;help</h3>
<p> Print usage information and exit. </p>
<h3>SUMMARY OPTIONS</h3>
<h3>-L, &#8211;list-gpus</h3>
<p> List each of the NVIDIA GPUs in the system, along with their UUIDs.</p>
<h3>-B, &#8211;list-excluded-gpus</h3>
<p> List each of the excluded NVIDIA GPUs in the system, along with their UUIDs. </p>
<h3>QUERY OPTIONS</h3>
<h3>-q, &#8211;query</h3>
<p> Display GPU or Unit info. Displayed info includes all data listed in the (<i>GPU ATTRIBUTES</i>) or (<i>UNIT ATTRIBUTES</i>) sections of this document. Some devices and/or environments don&#8217;t support all possible information. Any unsupported data is indicated by a &quot;N/A&quot; in the output. By default information for all available GPUs or Units is displayed. Use the <code>-i</code> option to restrict the output to a single GPU or Unit. </p>
<h3>[plus optional]</h3>
<h3>-u, &#8211;unit</h3>
<p> Display Unit data instead of GPU data. Unit data is only available for NVIDIA S-class Tesla enclosures. </p>
<h3>-i, &#8211;id=ID</h3>
<p> Display data for a single specified GPU or Unit. The specified id may be the GPU/Unit&#8217;s 0-based index in the natural enumeration returned by the driver, the GPU&#8217;s board serial number, the GPU&#8217;s UUID, or the GPU&#8217;s PCI bus ID (as domain:bus:device.function in hex). It is recommended that users desiring consistency use either UUID or PCI bus ID, since device enumeration ordering is not guaranteed to be consistent between reboots and board serial number might be shared between multiple GPUs on the same board. </p>
<h3>-f FILE, &#8211;filename=FILE</h3>
<p> Redirect query output to the specified file in place of the default stdout. The specified file will be overwritten. </p>
<h3>-x, &#8211;xml-format</h3>
<p> Produce XML output in place of the default human-readable format. Both GPU and Unit query outputs conform to corresponding DTDs. These are available via the <code>&#8211;dtd</code> flag. </p>
<h3>&#8211;dtd</h3>
<p> Use with <code>-x</code>. Embed the DTD in the XML output. </p>
<h3>&#8211;debug=FILE</h3>
<p> Produces an encrypted debug log for use in submission of bugs back to NVIDIA. </p>
<h3>-d TYPE, &#8211;display=TYPE</h3>
<p> Display only selected information: MEMORY, UTILIZATION, ECC, TEMPERATURE, POWER, CLOCK, COMPUTE, PIDS, PERFORMANCE, SUPPORTED_CLOCKS, PAGE_RETIREMENT, ACCOUNTING, ENCODER_STATS, ROW_REMAPPER, VOLTAGE. Flags can be combined with comma e.g. &quot;MEMORY,ECC&quot;. Sampling data with max, min and avg is also returned for POWER, UTILIZATION and CLOCK display types. Doesn&#8217;t work with -u/&#8211;unit or -x/&#8211;xml-format flags. </p>
<h3>-l SEC, &#8211;loop=SEC</h3>
<p> Continuously report query data at the specified interval, rather than the default of just once. The application will sleep in-between queries. Note that on Linux ECC error or XID error events will print out during the sleep period if the <i>-x</i> flag was not specified. Pressing Ctrl+C at any time will abort the loop, which will otherwise run indefinitely. If no argument is specified for the <code>-l</code> form a default interval of 5 seconds is used. </p>
<h3>SELECTIVE QUERY OPTIONS</h3>
<p> Allows the caller to pass an explicit list of properties to query. </p>
<h3>[one of]</h3>
<h3>&#8211;query-gpu=</h3>
<p> Information about GPU. Pass comma separated list of properties you want to query. e.g. &#8211;query-gpu=pci.bus_id,persistence_mode. Call &#8211;help-query-gpu for more info. </p>
<h3>&#8211;query-supported-clocks=</h3>
<p> List of supported clocks. Call &#8211;help-query-supported-clocks for more info. </p>
<h3>&#8211;query-compute-apps=</h3>
<p> List of currently active compute processes. Call &#8211;help-query-compute-apps for more info.</p>
<h3>&#8211;query-accounted-apps=</h3>
<p> List of accounted compute processes. Call &#8211;help-query-accounted-apps for more info. This query is not supported on vGPU host. </p>
<h3>&#8211;query-retired-pages=</h3>
<p> List of GPU device memory pages that have been retired. Call &#8211;help-query-retired-pages for more info. </p>
<h3>&#8211;query-remapped-rows=</h3>
<p> Information about remapped rows. Call &#8211;help-query-remapped-rows for more info. </p>
<h3>[mandatory]</h3>
<h3>&#8211;format=</h3>
<p> Comma separated list of format options:</p>
<dl>
<dt>&bull;</p>
<dd> csv &#8211; comma separated values (MANDATORY)</p>
<dt>&bull;</p>
<dd> noheader &#8211; skip first line with column headers</p>
<dt>&bull;</p>
<dd> nounits &#8211; don&#8217;t print units for numerical values </p>
</dl>
<h3>[plus any of]</h3>
<h3>-i, &#8211;id=ID</h3>
<p> Display data for a single specified GPU. The specified id may be the GPU&#8217;s 0-based index in the natural enumeration returned by the driver, the GPU&#8217;s board serial number, the GPU&#8217;s UUID, or the GPU&#8217;s PCI bus ID (as domain:bus:device.function in hex). It is recommended that users desiring consistency use either UUID or PCI bus ID, since device enumeration ordering is not guaranteed to be consistent between reboots and board serial number might be shared between multiple GPUs on the same board. </p>
<h3>-f FILE, &#8211;filename=FILE</h3>
<p> Redirect query output to the specified file in place of the default stdout. The specified file will be overwritten. </p>
<h3>-l SEC, &#8211;loop=SEC</h3>
<p> Continuously report query data at the specified interval, rather than the default of just once. The application will sleep in-between queries. Note that on Linux ECC error or XID error events will print out during the sleep period if the <i>-x</i> flag was not specified. Pressing Ctrl+C at any time will abort the loop, which will otherwise run indefinitely. If no argument is specified for the <code>-l</code> form a default interval of 5 seconds is used. </p>
<h3>-lms ms, &#8211;loop-ms=ms</h3>
<p> Same as -l,&#8211;loop but in milliseconds. </p>
<h3>DEVICE MODIFICATION OPTIONS</h3>
<h3>[any one of]</h3>
<h3>-pm, &#8211;persistence-mode=MODE</h3>
<p> Set the persistence mode for the target GPUs. See the (<i>GPU ATTRIBUTES</i>) section for a description of persistence mode. Requires root. Will impact all GPUs unless a single GPU is specified using the <i>-i</i> argument. The effect of this operation is immediate. However, it does not persist across reboots. After each reboot persistence mode will default to &quot;Disabled&quot;. Available on Linux only. </p>
<h3>-e, &#8211;ecc-config=CONFIG</h3>
<p> Set the ECC mode for the target GPUs. See the (<i>GPU ATTRIBUTES</i>) section for a description of ECC mode. Requires root. Will impact all GPUs unless a single GPU is specified using the <i>-i</i> argument. This setting takes effect after the next reboot and is persistent. </p>
<h3>-p, &#8211;reset-ecc-errors=TYPE</h3>
<p> Reset the ECC error counters for the target GPUs. See the (<i>GPU ATTRIBUTES</i>) section for a description of ECC error counter types. Available arguments are 0|VOLATILE or 1|AGGREGATE. Requires root. Will impact all GPUs unless a single GPU is specified using the <i>-i</i> argument. The effect of this operation is immediate. </p>
<h3>-c, &#8211;compute-mode=MODE</h3>
<p> Set the compute mode for the target GPUs. See the (<i>GPU ATTRIBUTES</i>) section for a description of compute mode. Requires root. Will impact all GPUs unless a single GPU is specified using the <i>-i</i> argument. The effect of this operation is immediate. However, it does not persist across reboots. After each reboot compute mode will reset to &quot;DEFAULT&quot;. </p>
<h3>-dm TYPE, &#8211;driver-model=TYPE</h3>
<h3>-fdm TYPE, &#8211;force-driver-model=TYPE</h3>
<p> Enable or disable TCC driver model. For Windows only. Requires administrator privileges. <i>-dm</i> will fail if a display is attached, but <i>-fdm</i> will force the driver model to change. Will impact all GPUs unless a single GPU is specified using the <i>-i</i> argument. A reboot is required for the change to take place. See <code>Driver Model</code> for more information on Windows driver models. </p>
<h3> &#8211;gom=MODE</h3>
<p> Set GPU Operation Mode: 0/ALL_ON, 1/COMPUTE, 2/LOW_DP Supported on GK110 M-class and X-class Tesla products from the Kepler family. Not supported on Quadro and Tesla C-class products. LOW_DP and ALL_ON are the only modes supported on GeForce Titan devices. Requires administrator privileges. See <i>GPU Operation Mode</i> for more information about GOM. GOM changes take effect after reboot. The reboot requirement might be removed in the future. Compute only GOMs don&#8217;t support WDDM (Windows Display Driver Model) </p>
<h3>-r, &#8211;gpu-reset</h3>
<p> Trigger a reset of one or more GPUs. Can be used to clear GPU HW and SW state in situations that would otherwise require a machine reboot. Typically useful if a double bit ECC error has occurred. Optional <i>-i</i> switch can be used to target one or more specific devices. Without this option, all GPUs are reset. Requires root. There can&#8217;t be any applications using these devices (e.g. CUDA application, graphics application like X server, monitoring application like other instance of nvidia-smi). There also can&#8217;t be any compute applications running on any other GPU in the system. </p>
<p> Starting with the NVIDIA Ampere architecture, GPUs with NVLink connections can be individually reset. On NVSwitch systems, Fabric Manager is required to facilitate reset. </p>
<p> If Fabric Manager is not running, or if any of the GPUs being reset are based on an architecture preceding the NVIDIA Ampere architecture, any GPUs with NVLink connections to a GPU being reset must also be reset in the same command. This can be done either by omitting the <i>-i</i> switch, or using the <i>-i</i> switch to specify the GPUs to be reset. If the <i>-i</i> option does not specify a complete set of NVLink GPUs to reset, this command will issue an error identifying the additional GPUs that must be included in the reset command. </p>
<p> GPU reset is not guaranteed to work in all cases. It is not recommended for production environments at this time. In some situations there may be HW components on the board that fail to revert back to an initial state following the reset request. This is more likely to be seen on Fermi-generation products vs. Kepler, and more likely to be seen if the reset is being performed on a hung GPU. </p>
<p> Following a reset, it is recommended that the health of each reset GPU be verified before further use. If any GPU is not healthy a complete reset should be instigated by power cycling the node. </p>
<p> GPU reset operation will not be supported on MIG enabled vGPU guests. </p>
<p> Visit <i><a rel="nofollow" href="http://developer.nvidia.com/gpu-deployment-kit">http://developer.nvidia.com/gpu-deployment-kit</a></i> to download the GDK. </p>
<h3>-lgc, &#8211;lock-gpu-clocks=MIN_GPU_CLOCK,MAX_GPU_CLOCK</h3>
<p> Specifies &lt;minGpuClock,maxGpuClock&gt; clocks as a pair (e.g. 1500,1500) that defines closest desired locked GPU clock speed in MHz. Input can also use be a singular desired clock value (e.g. &lt;GpuClockValue&gt;). Supported on Volta+. Requires root </p>
<h3>-rgc, &#8211;reset-gpu-clocks</h3>
<p> Resets the GPU clocks to the default value. Supported on Volta+. Requires root. </p>
<h3>-ac, &#8211;applications-clocks=MEM_CLOCK,GRAPHICS_CLOCK</h3>
<p> Specifies maximum &lt;memory,graphics&gt; clocks as a pair (e.g. 2000,800) that defines GPU&#8217;s speed while running applications on a GPU. Supported on Maxwell-based GeForce and from the Kepler+ family in Tesla/Quadro/Titan devices. Requires root. </p>
<h3>-rac, &#8211;reset-applications-clocks</h3>
<p> Resets the applications clocks to the default value. Supported on Maxwell-based GeForce and from the Kepler+ family in Tesla/Quadro/Titan devices. Requires root. </p>
<h3>-pl, &#8211;power-limit=POWER_LIMIT</h3>
<p> Specifies maximum power limit in watts. Accepts integer and floating point numbers. Only on supported devices from Kepler family. Requires administrator privileges. Value needs to be between Min and Max Power Limit as reported by nvidia-smi. </p>
<h3>-cc, &#8211;cuda-clocks=MODE</h3>
<p> Overrides or restores default CUDA clocks Available arguments are 0|RESTORE_DEFAULT or 1|OVERRIDE. </p>
<h3>-am, &#8211;accounting-mode=MODE</h3>
<p> Enables or disables GPU Accounting. With GPU Accounting one can keep track of usage of resources throughout lifespan of a single process. Only on supported devices from Kepler family. Requires administrator privileges. Available arguments are 0|DISABLED or 1|ENABLED. </p>
<h3>-caa, &#8211;clear-accounted-apps</h3>
<p> Clears all processes accounted so far. Only on supported devices from Kepler family. Requires administrator privileges. </p>
<h3> &#8211;auto-boost-default=MODE</h3>
<p> Set the default auto boost policy to 0/DISABLED or 1/ENABLED, enforcing the change only after the last boost client has exited. Only on certain Tesla devices from the Kepler+ family and Maxwell-based GeForce devices. Requires root. </p>
<h3> &#8211;auto-boost-default-force=MODE</h3>
<p> Set the default auto boost policy to 0/DISABLED or 1/ENABLED, enforcing the change immediately. Only on certain Tesla devices from the Kepler+ family and Maxwell-based GeForce devices. Requires root. </p>
<h3> &#8211;auto-boost-permission=MODE</h3>
<p> Allow non-admin/root control over auto boost mode. Available arguments are 0|UNRESTRICTED, 1|RESTRICTED. Only on certain Tesla devices from the Kepler+ family and Maxwell-based GeForce devices. Requires root. </p>
<h3>-mig, &#8211;multi-instance-gpu=MODE</h3>
<p> Enables or disables Multi Instance GPU mode. Only supported on devices based on the NVIDIA Ampere architecture. Requires root. Available arguments are 0|DISABLED or 1|ENABLED. </p>
<h3>[plus optional]</h3>
<h3>-i, &#8211;id=ID</h3>
<p> Modify a single specified GPU. The specified id may be the GPU/Unit&#8217;s 0-based index in the natural enumeration returned by the driver, the GPU&#8217;s board serial number, the GPU&#8217;s UUID, or the GPU&#8217;s PCI bus ID (as domain:bus:device.function in hex). It is recommended that users desiring consistency use either UUID or PCI bus ID, since device enumeration ordering is not guaranteed to be consistent between reboots and board serial number might be shared between multiple GPUs on the same board. </p>
<h3>UNIT MODIFICATION OPTIONS</h3>
<h3>-t, &#8211;toggle-led=STATE</h3>
<p> Set the LED indicator state on the front and back of the unit to the specified color. See the (<i>UNIT ATTRIBUTES</i>) section for a description of the LED states. Allowed colors are 0|GREEN and 1|AMBER. Requires root. </p>
<h3>[plus optional]</h3>
<h3>-i, &#8211;id=ID</h3>
<p> Modify a single specified Unit. The specified id is the Unit&#8217;s 0-based index in the natural enumeration returned by the driver. </p>
<h3>SHOW DTD OPTIONS</h3>
<h3>&#8211;dtd</h3>
<p> Display Device or Unit DTD. </p>
<h3>[plus optional]</h3>
<h3>-f FILE, &#8211;filename=FILE</h3>
<p> Redirect query output to the specified file in place of the default stdout. The specified file will be overwritten. </p>
<h3>-u, &#8211;unit</h3>
<p> Display Unit DTD instead of device DTD. </p>
<h3>stats</h3>
<p> Display statistics information about the GPU. Use &quot;nvidia-smi stats -h&quot; for more information. Linux only. </p>
<h3>topo</h3>
<p> Display topology information about the system. Use &quot;nvidia-smi topo -h&quot; for more information. Linux only. Shows all GPUs NVML is able to detect but CPU and NUMA node affinity information will only be shown for GPUs with Kepler or newer architectures. Note: GPU enumeration is the same as NVML. </p>
<h3>drain</h3>
<p> Display and modify the GPU drain states. Use &quot;nvidia-smi drain -h&quot; for more information. Linux only. </p>
<h3>nvlink</h3>
<p> Display nvlink information. Use &quot;nvidia-smi nvlink -h&quot; for more information. </p>
<h3>clocks</h3>
<p> Query and control clocking behavior. Currently, this only pertains to synchronized boost. Use &quot;nvidia-smi clocks &#8211;help&quot; for more information. </p>
<h3>vgpu</h3>
<p> Display information on GRID virtual GPUs. Use &quot;nvidia-smi vgpu -h&quot; for more information. </p>
<h3>mig</h3>
<p> Provides controls for MIG management. </p>
<h3>boost-slider</h3>
<p> Provides controls for boost sliders management. </p>
<h3>power-hint</h3>
<p> Provides queries for power hint. </p>
<h2>RETURN VALUE</h2>
<p> Return code reflects whether the operation succeeded or failed and what was the reason of failure.</p>
<dl>
<dt>&bull;</p>
<dd> Return code 0 &#8211; Success</p>
<dt>&bull;</p>
<dd> Return code 2 &#8211; A supplied argument or flag is invalid</p>
<dt>&bull;</p>
<dd> Return code 3 &#8211; The requested operation is not available on target device</p>
<dt>&bull;</p>
<dd> Return code 4 &#8211; The current user does not have permission to access this device or perform this operation</p>
<dt>&bull;</p>
<dd> Return code 6 &#8211; A query to find an object was unsuccessful</p>
<dt>&bull;</p>
<dd> Return code 8 &#8211; A device&#8217;s external power cables are not properly attached</p>
<dt>&bull;</p>
<dd> Return code 9 &#8211; NVIDIA driver is not loaded</p>
<dt>&bull;</p>
<dd> Return code 10 &#8211; NVIDIA Kernel detected an interrupt issue with a GPU</p>
<dt>&bull;</p>
<dd> Return code 12 &#8211; NVML Shared Library couldn&#8217;t be found or loaded</p>
<dt>&bull;</p>
<dd> Return code 13 &#8211; Local version of NVML doesn&#8217;t implement this function</p>
<dt>&bull;</p>
<dd> Return code 14 &#8211; infoROM is corrupted</p>
<dt>&bull;</p>
<dd> Return code 15 &#8211; The GPU has fallen off the bus or has otherwise become inaccessible</p>
<dt>&bull;</p>
<dd> Return code 255 &#8211; Other error or internal driver error occurred </p>
</dl>
<h2>GPU ATTRIBUTES</h2>
<p> The following list describes all possible data returned by the <code>-q</code> device query option. Unless otherwise noted all numerical results are base 10 and unitless. </p>
<h3>Timestamp</h3>
<p> The current system timestamp at the time nvidia-smi was invoked. Format is &quot;Day-of-week Month Day HH:MM:SS Year&quot;. </p>
<h3>Driver Version</h3>
<p> The version of the installed NVIDIA display driver. This is an alphanumeric string. </p>
<h3>Attached GPUs</h3>
<p> The number of NVIDIA GPUs in the system. </p>
<h3>Product Name</h3>
<p> The official product name of the GPU. This is an alphanumeric string. For all products. </p>
<h3>Display Mode</h3>
<p> A flag that indicates whether a physical display (e.g. monitor) is currently connected to any of the GPU&#8217;s connectors. &quot;Enabled&quot; indicates an attached display. &quot;Disabled&quot; indicates otherwise. </p>
<h3>Display Active</h3>
<p> A flag that indicates whether a display is initialized on the GPU&#8217;s (e.g. memory is allocated on the device for display). Display can be active even when no monitor is physically attached. &quot;Enabled&quot; indicates an active display. &quot;Disabled&quot; indicates otherwise. </p>
<h3>Persistence Mode</h3>
<p> A flag that indicates whether persistence mode is enabled for the GPU. Value is either &quot;Enabled&quot; or &quot;Disabled&quot;. When persistence mode is enabled the NVIDIA driver remains loaded even when no active clients, such as X11 or nvidia-smi, exist. This minimizes the driver load latency associated with running dependent apps, such as CUDA programs. For all CUDA-capable products. Linux only. </p>
<h3>Accounting Mode</h3>
<p> A flag that indicates whether accounting mode is enabled for the GPU Value is either When accounting is enabled statistics are calculated for each compute process running on the GPU. Statistics can be queried during the lifetime or after termination of the process. The execution time of process is reported as 0 while the process is in running state and updated to actual execution time after the process has terminated. See &#8211;help-query-accounted-apps for more info. </p>
<h3>Accounting Mode Buffer Size</h3>
<p> Returns the size of the circular buffer that holds list of processes that can be queried for accounting stats. This is the maximum number of processes that accounting information will be stored for before information about oldest processes will get overwritten by information about new processes. </p>
<h3>Driver Model</h3>
<p> On Windows, the TCC and WDDM driver models are supported. The driver model can be changed with the (<i>-dm</i>) or (<i>-fdm</i>) flags. The TCC driver model is optimized for compute applications. I.E. kernel launch times will be quicker with TCC. The WDDM driver model is designed for graphics applications and is not recommended for compute applications. Linux does not support multiple driver models, and will always have the value of &quot;N/A&quot;. </p>
<dl>
<dt><code>Current</code></p>
<dd> The driver model currently in use. Always &quot;N/A&quot; on Linux. </p>
<dt><code>Pending</code></p>
<dd> The driver model that will be used on the next reboot. Always &quot;N/A&quot; on Linux. </p>
</dl>
<h3>Serial Number</h3>
<p> This number matches the serial number physically printed on each board. It is a globally unique immutable alphanumeric value. </p>
<h3>GPU UUID</h3>
<p> This value is the globally unique immutable alphanumeric identifier of the GPU. It does not correspond to any physical label on the board. </p>
<h3>Minor Number</h3>
<p> The minor number for the device is such that the Nvidia device node file for each GPU will have the form /dev/nvidia[minor number]. Available only on Linux platform. </p>
<h3>VBIOS Version</h3>
<p> The BIOS of the GPU board. </p>
<h3>MultiGPU Board</h3>
<p> Whether or not this GPU is part of a multiGPU board. </p>
<h3>Board ID</h3>
<p> The unique board ID assigned by the driver. If two or more GPUs have the same board ID and the above &quot;MultiGPU&quot; field is true then the GPUs are on the same board. </p>
<h3>Inforom Version</h3>
<p> Version numbers for each object in the GPU board&#8217;s inforom storage. The inforom is a small, persistent store of configuration and state data for the GPU. All inforom version fields are numerical. It can be useful to know these version numbers because some GPU features are only available with inforoms of a certain version or higher. </p>
<p> If any of the fields below return Unknown Error additional Inforom verification check is performed and appropriate warning message is displayed. </p>
<dl>
<dt><code>Image Version</code></p>
<dd> Global version of the infoROM image. Image version just like VBIOS version uniquely describes the exact version of the infoROM flashed on the board in contrast to infoROM object version which is only an indicator of supported features. </p>
<dt><code>OEM Object</code></p>
<dd> Version for the OEM configuration data. </p>
<dt><code>ECC Object</code></p>
<dd> Version for the ECC recording data. </p>
<dt><code>Power Object</code></p>
<dd> Version for the power management data. </p>
</dl>
<h3>GPU Operation Mode</h3>
<p> GOM allows to reduce power usage and optimize GPU throughput by disabling GPU features. </p>
<p> Each GOM is designed to meet specific user needs. </p>
<p> In &quot;All On&quot; mode everything is enabled and running at full speed. </p>
<p> The &quot;Compute&quot; mode is designed for running only compute tasks. Graphics operations are not allowed. </p>
<p> The &quot;Low Double Precision&quot; mode is designed for running graphics applications that don&#8217;t require high bandwidth double precision. </p>
<p> GOM can be changed with the (<i>&#8211;gom</i>) flag. </p>
<p> Supported on GK110 M-class and X-class Tesla products from the Kepler family. Not supported on Quadro and Tesla C-class products. Low Double Precision and All On modes are the only modes available for supported GeForce Titan products. </p>
<dl>
<dt><code>Current</code></p>
<dd> The GOM currently in use. </p>
<dt><code>Pending</code></p>
<dd> The GOM that will be used on the next reboot. </p>
</dl>
<h3>PCI</h3>
<p> Basic PCI info for the device. Some of this information may change whenever cards are added/removed/moved in a system. For all products. </p>
<dl>
<dt><code>Bus</code></p>
<dd> PCI bus number, in hex </p>
<dt><code>Device</code></p>
<dd> PCI device number, in hex </p>
<dt><code>Domain</code></p>
<dd> PCI domain number, in hex </p>
<dt><code>Device Id</code></p>
<dd> PCI vendor device id, in hex </p>
<dt><code>Sub System Id</code></p>
<dd> PCI Sub System id, in hex </p>
<dt><code>Bus Id</code></p>
<dd> PCI bus id as &quot;domain:bus:device.function&quot;, in hex</dl>
<h3>GPU Link information</h3>
<p> The PCIe link generation and bus width </p>
<dl>
<dt><code>Current</code></p>
<dd> The current link generation and width. These may be reduced when the GPU is not in use. </p>
<dt><code>Maximum</code></p>
<dd> The maximum link generation and width possible with this GPU and system configuration. For example, if the GPU supports a higher PCIe generation than the system supports then this reports the system PCIe generation. </p>
</dl>
<h3>Bridge Chip</h3>
<p> Information related to Bridge Chip on the device. The bridge chip firmware is only present on certain boards and may display &quot;N/A&quot; for some newer multiGPUs boards. </p>
<dl>
<dt><code>Type</code></p>
<dd> The type of bridge chip. Reported as N/A if doesn&#8217;t exist. </p>
<dt><code>Firmware Version</code></p>
<dd> The firmware version of the bridge chip. Reported as N/A if doesn&#8217;t exist. </p>
</dl>
<h3>Replays Since Reset</h3>
<p> The number of PCIe replays since reset.</p>
<h3>Replay Number Rollovers</h3>
<p> The number of PCIe replay number rollovers since reset. A replay number rollover occurs after 4 consecutive replays and results in retraining the link.</p>
<h3>Tx Throughput</h3>
<p> The GPU-centric transmission throughput across the PCIe bus in MB/s over the past 20ms. Only supported on Maxwell architectures and newer.</p>
<h3>Rx Throughput</h3>
<p> The GPU-centric receive throughput across the PCIe bus in MB/s over the past 20ms. Only supported on Maxwell architectures and newer. </p>
<h3>Fan Speed</h3>
<p> The fan speed value is the percent of the product&#8217;s maximum noise tolerance fan speed that the device&#8217;s fan is currently intended to run at. This value may exceed 100% in certain cases. Note: The reported speed is the intended fan speed. If the fan is physically blocked and unable to spin, this output will not match the actual fan speed. Many parts do not report fan speeds because they rely on cooling via fans in the surrounding enclosure. For all discrete products with dedicated fans. </p>
<h3>Performance State</h3>
<p> The current performance state for the GPU. States range from P0 (maximum performance) to P12 (minimum performance). </p>
<h3>Clocks Throttle Reasons</h3>
<p> Retrieves information about factors that are reducing the frequency of clocks. </p>
<p> If all throttle reasons are returned as &quot;Not Active&quot; it means that clocks are running as high as possible. </p>
<dl>
<dt><code>Idle</code></p>
<dd> Nothing is running on the GPU and the clocks are dropping to Idle state. This limiter may be removed in a later release. </p>
<dt><code>Application Clocks Setting</code></p>
<dd> GPU clocks are limited by applications clocks setting. E.g. can be changed using nvidia-smi &#8211;applications-clocks= </p>
<dt><code>SW Power Cap</code></p>
<dd> SW Power Scaling algorithm is reducing the clocks below requested clocks because the GPU is consuming too much power. E.g. SW power cap limit can be changed with nvidia-smi &#8211;power-limit= </p>
<dt><code>HW Slowdown</code></p>
<dd> HW Slowdown (reducing the core clocks by a factor of 2 or more) is engaged. HW Thermal Slowdown and HW Power Brake will be displayed on Pascal+. </p>
<p> This is an indicator of:<br />
 * Temperature being too high (HW Thermal Slowdown)<br />
 * External Power Brake Assertion is triggered (e.g. by the system power supply) (HW Power Brake Slowdown)<br />
 * Power draw is too high and Fast Trigger protection is reducing the clocks </p>
<dt><code>SW Thermal Slowdown</code></p>
<dd> SW Thermal capping algorithm is reducing clocks below requested clocks because GPU temperature is higher than Max Operating Temp </p>
</dl>
<h3>FB Memory Usage</h3>
<p> On-board frame buffer memory information. Reported total memory is affected by ECC state. If ECC is enabled the total available memory is decreased by several percent, due to the requisite parity bits. The driver may also reserve a small amount of memory for internal use, even without active work on the GPU. For all products. </p>
<dl>
<dt><code>Total</code></p>
<dd> Total size of FB memory. </p>
<dt><code>Used</code></p>
<dd> Used size of FB memory. </p>
<dt><code>Free</code></p>
<dd> Available size of FB memory. </p>
</dl>
<h3>BAR1 Memory Usage</h3>
<p> BAR1 is used to map the FB (device memory) so that it can be directly accessed by the CPU or by 3rd party devices (peer-to-peer on the PCIe bus). </p>
<dl>
<dt><code>Total</code></p>
<dd> Total size of BAR1 memory. </p>
<dt><code>Used</code></p>
<dd> Used size of BAR1 memory. </p>
<dt><code>Free</code></p>
<dd> Available size of BAR1 memory. </p>
</dl>
<h3>Compute Mode</h3>
<p> The compute mode flag indicates whether individual or multiple compute applications may run on the GPU. </p>
<p> &quot;Default&quot; means multiple contexts are allowed per device. </p>
<p> &quot;Exclusive Process&quot; means only one context is allowed per device, usable from multiple threads at a time. </p>
<p> &quot;Prohibited&quot; means no contexts are allowed per device (no compute apps). </p>
<p> &quot;EXCLUSIVE_PROCESS&quot; was added in CUDA 4.0. Prior CUDA releases supported only one exclusive mode, which is equivalent to &quot;EXCLUSIVE_THREAD&quot; in CUDA 4.0 and beyond. </p>
<p> For all CUDA-capable products. </p>
<h3>Utilization</h3>
<p> Utilization rates report how busy each GPU is over time, and can be used to determine how much an application is using the GPUs in the system. </p>
<p> Note: During driver initialization when ECC is enabled one can see high GPU and Memory Utilization readings. This is caused by ECC Memory Scrubbing mechanism that is performed during driver initialization. </p>
<dl>
<dt><code>GPU</code></p>
<dd> Percent of time over the past sample period during which one or more kernels was executing on the GPU. The sample period may be between 1 second and 1/6 second depending on the product. </p>
<dt><code>Memory</code></p>
<dd> Percent of time over the past sample period during which global (device) memory was being read or written. The sample period may be between 1 second and 1/6 second depending on the product. </p>
<dt><code>Encoder</code></p>
<dd> Percent of time over the past sample period during which the GPU&#8217;s video encoder was being used. The sampling rate is variable and can be obtained directly via the nvmlDeviceGetEncoderUtilization() API </p>
<dt><code>Decoder</code></p>
<dd> Percent of time over the past sample period during which the GPU&#8217;s video decoder was being used. The sampling rate is variable and can be obtained directly via the nvmlDeviceGetDecoderUtilization() API </p>
</dl>
<h3>Ecc Mode</h3>
<p> A flag that indicates whether ECC support is enabled. May be either &quot;Enabled&quot; or &quot;Disabled&quot;. Changes to ECC mode require a reboot. Requires Inforom ECC object version 1.0 or higher. </p>
<dl>
<dt><code>Current</code></p>
<dd> The ECC mode that the GPU is currently operating under. </p>
<dt><code>Pending</code></p>
<dd> The ECC mode that the GPU will operate under after the next reboot. </p>
</dl>
<h3>ECC Errors</h3>
<p> NVIDIA GPUs can provide error counts for various types of ECC errors. Some ECC errors are either single or double bit, where single bit errors are corrected and double bit errors are uncorrectable. Texture memory errors may be correctable via resend or uncorrectable if the resend fails. These errors are available across two timescales (volatile and aggregate). Single bit ECC errors are automatically corrected by the HW and do not result in data corruption. Double bit errors are detected but not corrected. Please see the ECC documents on the web for information on compute application behavior when double bit errors occur. Volatile error counters track the number of errors detected since the last driver load. Aggregate error counts persist indefinitely and thus act as a lifetime counter. </p>
<p> A note about volatile counts: On Windows this is once per boot. On Linux this can be more frequent. On Linux the driver unloads when no active clients exist. Hence, if persistence mode is enabled or there is always a driver client active (e.g. X11), then Linux also sees per-boot behavior. If not, volatile counts are reset each time a compute app is run. </p>
<p> Tesla and Quadro products from the Fermi and Kepler family can display total ECC error counts, as well as a breakdown of errors based on location on the chip. The locations are described below. Location-based data for aggregate error counts requires Inforom ECC object version 2.0. All other ECC counts require ECC object version 1.0. </p>
<dl>
<dt><code>Device Memory</code></p>
<dd> Errors detected in global device memory. </p>
<dt><code>Register File</code></p>
<dd> Errors detected in register file memory. </p>
<dt><code>L1 Cache</code></p>
<dd> Errors detected in the L1 cache. </p>
<dt><code>L2 Cache</code></p>
<dd> Errors detected in the L2 cache. </p>
<dt><code>Texture Memory</code></p>
<dd> Parity errors detected in texture memory. </p>
<dt><code>Total</code></p>
<dd> Total errors detected across entire chip. Sum of <code>Device Memory</code>, <code>Register File</code>, <code>L1 Cache</code>, <code>L2 Cache</code> and <code>Texture Memory</code>. </p>
</dl>
<h3>Page Retirement</h3>
<p> NVIDIA GPUs can retire pages of GPU device memory when they become unreliable. This can happen when multiple single bit ECC errors occur for the same page, or on a double bit ECC error. When a page is retired, the NVIDIA driver will hide it such that no driver, or application memory allocations can access it. </p>
<p> <code>Double Bit ECC</code> The number of GPU device memory pages that have been retired due to a double bit ECC error. </p>
<p> <code>Single Bit ECC</code> The number of GPU device memory pages that have been retired due to multiple single bit ECC errors. </p>
<p> <code>Pending</code> Checks if any GPU device memory pages are pending blacklist on the next reboot. Pages that are retired but not yet blacklisted can still be allocated, and may cause further reliability issues. </p>
<h3>Row Remapper</h3>
<p> NVIDIA GPUs can remap rows of GPU device memory when they become unreliable. This can happen when a single uncorrectable ECC error or multiple correctable ECC errors occur on the same row. When a row is remapped, the NVIDIA driver will remap the faulty row to a reserved row. All future accesses to the row will access the reserved row instead of the faulty row. </p>
<p> <code>Correctable Error</code> The number of rows that have been remapped due to correctable ECC errors. </p>
<p> <code>Uncorrectable Error</code> The number of rows that have been remapped due to uncorrectable ECC errors. </p>
<p> <code>Pending</code> Indicates whether or not a row is pending remapping. The GPU must be reset for the remapping to go into effect. </p>
<p> <code>Remapping Failure Occurred</code> Indicates whether or not a row remapping has failed in the past. </p>
<p> <code>Bank Remap Availability Histogram</code> Each memory bank has a fixed number of reserved rows that can be used for row remapping. The histogram will classify the remap availability of each bank into Maximum, High, Partial, Low and None. Maximum availability means that all reserved rows are available for remapping while None means that no reserved rows are available. </p>
<h3>Temperature</h3>
<p> Readings from temperature sensors on the board. All readings are in degrees C. Not all products support all reading types. In particular, products in module form factors that rely on case fans or passive cooling do not usually provide temperature readings. See below for restrictions. </p>
<dl>
<dt><code>GPU</code></p>
<dd> Core GPU temperature. For all discrete and S-class products. </p>
<dt><code>Shutdown Temp</code></p>
<dd> The temperature at which a GPU will shutdown.</p>
<dt><code>Slowdown Temp</code></p>
<dd> The temperature at which a GPU will begin slowing itself down through HW, in order to cool.</p>
<dt><code>Max Operating Temp</code></p>
<dd> The temperature at which a GPU will begin slowing itself down through SW, in order to cool. </p>
</dl>
<h3>Power Readings</h3>
<p> Power readings help to shed light on the current power usage of the GPU, and the factors that affect that usage. When power management is enabled the GPU limits power draw under load to fit within a predefined power envelope by manipulating the current performance state. See below for limits of availability. Please note that power readings are not applicable for Pascal and higher GPUs with BA sensor boards. </p>
<dl>
<dt><code>Power State</code></p>
<dd> Power State is deprecated and has been renamed to Performance State in 2.285. To maintain XML compatibility, in XML format Performance State is listed in both places. </p>
<dt><code>Power Management</code></p>
<dd> A flag that indicates whether power management is enabled. Either &quot;Supported&quot; or &quot;N/A&quot;. Requires Inforom PWR object version 3.0 or higher or Kepler device. </p>
<dt><code>Power Draw</code></p>
<dd> The last measured power draw for the entire board, in watts. Only available if power management is supported. Please note that for boards without INA sensors, this refers to the power draw for the GPU and not for the entire board. </p>
<dt><code>Power Limit</code></p>
<dd> The software power limit, in watts. Set by software such as nvidia-smi. Only available if power management is supported. Requires Inforom PWR object version 3.0 or higher or Kepler device. On Kepler devices Power Limit can be adjusted using -pl,&#8211;power-limit= switches. </p>
<dt><code>Enforced Power Limit</code></p>
<dd> The power management algorithm&#8217;s power ceiling, in watts. Total board power draw is manipulated by the power management algorithm such that it stays under this value. This limit is the minimum of various limits such as the software limit listed above. Only available if power management is supported. Requires a Kepler device. Please note that for boards without INA sensors, it is the GPU power draw that is being manipulated. </p>
<dt><code>Default Power Limit</code></p>
<dd> The default power management algorithm&#8217;s power ceiling, in watts. Power Limit will be set back to Default Power Limit after driver unload. Only on supported devices from Kepler family. </p>
<dt><code>Min Power Limit</code></p>
<dd> The minimum value in watts that power limit can be set to. Only on supported devices from Kepler family. </p>
<dt><code>Max Power Limit</code></p>
<dd> The maximum value in watts that power limit can be set to. Only on supported devices from Kepler family. </p>
</dl>
<h3>Clocks</h3>
<p> Current frequency at which parts of the GPU are running. All readings are in MHz. </p>
<dl>
<dt><code>Graphics</code></p>
<dd> Current frequency of graphics (shader) clock. </p>
<dt><code>SM</code></p>
<dd> Current frequency of SM (Streaming Multiprocessor) clock. </p>
<dt><code>Memory</code></p>
<dd> Current frequency of memory clock. </p>
<dt><code>Video</code></p>
<dd> Current frequency of video (encoder + decoder) clocks. </p>
</dl>
<h3>Applications Clocks</h3>
<p> User specified frequency at which applications will be running at. Can be changed with [-ac | &#8211;applications-clocks] switches. </p>
<dl>
<dt><code>Graphics</code></p>
<dd> User specified frequency of graphics (shader) clock. </p>
<dt><code>Memory</code></p>
<dd> User specified frequency of memory clock. </p>
</dl>
<h3>Default Applications Clocks</h3>
<p> Default frequency at which applications will be running at. Application clocks can be changed with [-ac | &#8211;applications-clocks] switches. Application clocks can be set to default using [-rac | &#8211;reset-applications-clocks] switches. </p>
<dl>
<dt><code>Graphics</code></p>
<dd> Default frequency of applications graphics (shader) clock. </p>
<dt><code>Memory</code></p>
<dd> Default frequency of applications memory clock. </p>
</dl>
<h3>Max Clocks</h3>
<p> Maximum frequency at which parts of the GPU are design to run. All readings are in MHz. </p>
<p> On GPUs from Fermi family current P0 clocks (reported in Clocks section) can differ from max clocks by few MHz. </p>
<dl>
<dt><code>Graphics</code></p>
<dd> Maximum frequency of graphics (shader) clock. </p>
<dt><code>SM</code></p>
<dd> Maximum frequency of SM (Streaming Multiprocessor) clock. </p>
<dt><code>Memory</code></p>
<dd> Maximum frequency of memory clock. </p>
<dt><code>Video</code></p>
<dd> Maximum frequency of video (encoder + decoder) clock. </p>
</dl>
<h3>Clock Policy</h3>
<p> User-specified settings for automated clocking changes such as auto boost. </p>
<dl>
<dt><code>Auto Boost</code></p>
<dd> Indicates whether auto boost mode is currently enabled for this GPU (On) or disabled for this GPU (Off). Shows (N/A) if boost is not supported. Auto boost allows dynamic GPU clocking based on power, thermal and utilization. When auto boost is disabled the GPU will attempt to maintain clocks at precisely the Current Application Clocks settings (whenever a CUDA context is active). With auto boost enabled the GPU will still attempt to maintain this floor, but will opportunistically boost to higher clocks when power, thermal and utilization headroom allow. This setting persists for the life of the CUDA context for which it was requested. Apps can request a particular mode either via an NVML call (see NVML SDK) or by setting the CUDA environment variable CUDA_AUTO_BOOST. </p>
<dt><code>Auto Boost Default</code></p>
<dd> Indicates the default setting for auto boost mode, either enabled (On) or disabled (Off). Shows (N/A) if boost is not supported. Apps will run in the default mode if they have not explicitly requested a particular mode. Note: Auto Boost settings can only be modified if &quot;Persistence Mode&quot; is enabled, which is NOT by default. </p>
</dl>
<h3>Supported clocks</h3>
<p> List of possible memory and graphics clocks combinations that the GPU can operate on (not taking into account HW brake reduced clocks). These are the only clock combinations that can be passed to &#8211;applications-clocks flag. Supported Clocks are listed only when -q -d SUPPORTED_CLOCKS switches are provided or in XML format. </p>
<h3>Voltage</h3>
<p> Current voltage reported by the GPU. All units are in mV. </p>
<dl>
<dt><code>Graphics</code></p>
<dd> Current voltage of the graphics unit. </p>
</dl>
<h3>Processes</h3>
<p> List of processes having Compute or Graphics Context on the device. Compute processes are reported on all the fully supported products. Reporting for Graphics processes is limited to the supported products starting with Kepler architecture. </p>
<dl>
<dt>Each Entry is of format &quot;&lt;GPU Index&gt; &lt;PID&gt; &lt;Type&gt; &lt;Process Name&gt; &lt;GPU Memory Usage&gt;&quot;</p>
<dd>
<dt><code>GPU Index</code></p>
<dd> Represents NVML Index of the device. </p>
<dt><code>PID</code></p>
<dd> Represents Process ID corresponding to the active Compute or Graphics context. </p>
<dt><code>Type</code></p>
<dd> Displayed as &quot;C&quot; for Compute Process, &quot;G&quot; for Graphics Process, and &quot;C+G&quot; for the process having both Compute and Graphics contexts. </p>
<dt><code>Process Name</code></p>
<dd> Represents process name for the Compute or Graphics process. </p>
<dt><code>GPU Memory Usage</code></p>
<dd> Amount of memory used on the device by the context. Not available on Windows when running in WDDM mode because Windows KMD manages all the memory not NVIDIA driver. </p>
</dl>
<h3>Stats (EXPERIMENTAL)</h3>
<p> List GPU statistics such as power samples, utilization samples, xid events, clock change events and violation counters.</p>
<dl>
<dt>Supported on Tesla, GRID and Quadro based products under Linux.</p>
<dd>
<dt>Limited to Kepler or newer GPUs.</p>
<dd>
<dt>Displays statistics in CSV format as follows:</p>
<dd>
<dt>&lt;GPU device index&gt;, &lt;metric name&gt;, &lt;CPU Timestamp in us&gt;, &lt;value for metric&gt;</p>
<dd>
<dt>The metrics to display with their units are as follows:</p>
<dd>
<dt>Power samples in Watts.</p>
<dd>
<dt>GPU Temperature samples in degrees Celsius.</p>
<dd>
<dt>GPU, Memory, Encoder and Decoder utilization samples in Percentage.</p>
<dd>
<dt>Xid error events reported with Xid error code. The error code is 999 for unknown xid error.</p>
<dd>
<dt>Processor and Memory clock changes in MHz.</p>
<dd>
<dt>Violation due to Power capping with violation time in ns. (Tesla Only)</p>
<dd>
<dt>Violation due to Thermal capping with violation boolean flag (1/0). (Tesla Only)</p>
<dd>
<dt>Notes:</p>
<dd>
<dt>Any statistic preceded by &quot;#&quot; is a comment.</p>
<dd>
<dt>Non supported device is displayed as &quot;#&lt;device Index&gt;, Device not supported&quot;.</p>
<dd>
<dt>Non supported metric is displayed as &quot;&lt;device index&gt;, &lt;metric name&gt;, N/A, N/A&quot;.</p>
<dd>
<dt>Violation due to Thermal/Power supported only for Tesla based products. Thermal Violations are limited to Tesla K20 and higher.</p>
<dd>
</dl>
<h3>Device Monitoring</h3>
<p> The &quot;nvidia-smi dmon&quot; command-line is used to monitor one or more GPUs (up to 4 devices) plugged into the system. This tool allows the user to see one line of monitoring data per monitoring cycle. The output is in concise format and easy to interpret in interactive mode. The output data per line is limited by the terminal size. It is supported on Tesla, GRID, Quadro and limited GeForce products for Kepler or newer GPUs under bare metal 64 bits Linux. By default, the monitoring data includes Power Usage, Temperature, SM clocks, Memory clocks and Utilization values for SM, Memory, Encoder and Decoder. It can also be configured to report other metrics such as frame buffer memory usage, bar1 memory usage, power/thermal violations and aggregate single/double bit ecc errors. If any of the metric is not supported on the device or any other error in fetching the metric is reported as &quot;-&quot; in the output data. The user can also configure monitoring frequency and the number of monitoring iterations for each run. There is also an option to include date and time at each line. All the supported options are exclusive and can be used together in any order. </p>
<p> <code>Usage:</code></p>
<dl>
<dt><code>1) Default with no arguments</code></p>
<dd>
<dt><i>nvidia-smi dmon</i></p>
<dd>
<dt>Monitors default metrics for up to 4 supported devices under natural enumeration (starting with GPU index 0) at a frequency of 1 sec. Runs until terminated with ^C.</p>
<dd>
<dt><code>2) Select one or more devices</code></p>
<dd>
<dt><i>nvidia-smi dmon -i &lt;device1,device2, .. , deviceN&gt;</i></p>
<dd>
<dt>Reports default metrics for the devices selected by comma separated device list. The tool picks up to 4 supported devices from the list under natural enumeration (starting with GPU index 0).</p>
<dd>
<dt><code>3) Select metrics to be displayed</code></p>
<dd>
<dt><i>nvidia-smi dmon -s &lt;metric_group&gt;</i></p>
<dd>
<dt>&lt;metric_group&gt; can be one or more from the following:</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p &#8211; Power Usage&nbsp;(in Watts)&nbsp;and Gpu/Memory Temperature&nbsp;(in C)&nbsp;if supported</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u &#8211; Utilization&nbsp;(SM, Memory, Encoder and Decoder Utilization in&nbsp;%)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c &#8211; Proc and Mem Clocks&nbsp;(in MHz)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v &#8211; Power Violations&nbsp;(in&nbsp;%)&nbsp;and Thermal Violations&nbsp;(as a boolean flag)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;m &#8211; Frame Buffer and Bar1 memory usage&nbsp;(in MB)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e &#8211; ECC&nbsp;(Number of aggregated single bit, double bit ecc errors)&nbsp;and PCIe Replay errors</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t &#8211; PCIe Rx and Tx Throughput in MB/s&nbsp;(Maxwell and above)</p>
<dd>
<dt><code>4) Configure monitoring iterations</code></p>
<dd>
<dt><i>nvidia-smi dmon -c &lt;number of samples&gt;</i></p>
<dd>
<dt>Displays data for specified number of samples and exit.</p>
<dd>
<dt><code>5) Configure monitoring frequency</code></p>
<dd>
<dt><i>nvidia-smi dmon -d &lt;time in secs&gt;</i></p>
<dd>
<dt>Collects and displays data at every specified monitoring interval until terminated with ^C.</p>
<dd>
<dt><code>6) Display date</code></p>
<dd>
<dt><i>nvidia-smi dmon -o D</i></p>
<dd>
<dt>Prepends monitoring data with date in YYYYMMDD format.</p>
<dd>
<dt><code>7) Display time</code></p>
<dd>
<dt><i>nvidia-smi dmon -o T</i></p>
<dd>
<dt>Prepends monitoring data with time in HH:MM:SS format.</p>
<dd>
<dt><code>8) Help Information</code></p>
<dd>
<dt><i>nvidia-smi dmon -h</i></p>
<dd>
<dt>Displays help information for using the command line.</p>
<dd>
</dl>
<h3>Daemon (EXPERIMENTAL)</h3>
<p> The &quot;nvidia-smi daemon&quot; starts a background process to monitor one or more GPUs plugged in to the system. It monitors the requested GPUs every monitoring cycle and logs the file in compressed format at the user provided path or the default location at /var/log/nvstats/. The log file is created with system&#8217;s date appended to it and of the format nvstats-YYYYMMDD. The flush operation to the log file is done every alternate monitoring cycle. Daemon also logs it&#8217;s own PID at /var/run/nvsmi.pid. By default, the monitoring data to persist includes Power Usage, Temperature, SM clocks, Memory clocks and Utilization values for SM, Memory, Encoder and Decoder. The daemon tools can also be configured to record other metrics such as frame buffer memory usage, bar1 memory usage, power/thermal violations and aggregate single/double bit ecc errors.The default monitoring cycle is set to 10 secs and can be configured via command-line. It is supported on Tesla, GRID, Quadro and GeForce products for Kepler or newer GPUs under bare metal 64 bits Linux. The daemon requires root privileges to run, and only supports running a single instance on the system. All of the supported options are exclusive and can be used together in any order. </p>
<p> <code>Usage:</code></p>
<dl>
<dt><code>1) Default with no arguments</code></p>
<dd>
<dt><i>nvidia-smi daemon</i></p>
<dd>
<dt>Runs in the background to monitor default metrics for up to 4 supported devices under natural enumeration (starting with GPU index 0) at a frequency of 10 sec. The date stamped log file is created at /var/log/nvstats/.</p>
<dd>
<dt><code>2) Select one or more devices</code></p>
<dd>
<dt><i>nvidia-smi daemon -i &lt;device1,device2, .. , deviceN&gt;</i></p>
<dd>
<dt>Runs in the background to monitor default metrics for the devices selected by comma separated device list. The tool picks up to 4 supported devices from the list under natural enumeration (starting with GPU index 0).</p>
<dd>
<dt><code>3) Select metrics to be monitored</code></p>
<dd>
<dt><i>nvidia-smi daemon -s &lt;metric_group&gt;</i></p>
<dd>
<dt>&lt;metric_group&gt; can be one or more from the following:</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p &#8211; Power Usage&nbsp;(in Watts)&nbsp;and Gpu/Memory Temperature&nbsp;(in C)&nbsp;if supported</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u &#8211; Utilization&nbsp;(SM, Memory, Encoder and Decoder Utilization in&nbsp;%)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c &#8211; Proc and Mem Clocks&nbsp;(in MHz)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v &#8211; Power Violations&nbsp;(in&nbsp;%)&nbsp;and Thermal Violations&nbsp;(as a boolean flag)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;m &#8211; Frame Buffer and Bar1 memory usage&nbsp;(in MB)</p>
<dd>
<dt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>e &#8211; ECC (Number of aggregated single bit, double bit ecc errors) and PCIe Replay errors</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t &#8211; PCIe Rx and Tx Throughput in MB/s&nbsp;(Maxwell and above)</p>
<dd>
<dt><code>4) Configure monitoring frequency</code></p>
<dd>
<dt><i>nvidia-smi daemon -d &lt;time in secs&gt;</i></p>
<dd>
<dt>Collects data at every specified monitoring interval until terminated.</p>
<dd>
<dt><code>5) Configure log directory</code></p>
<dd>
<dt><i>nvidia-smi daemon -p &lt;path of directory&gt;</i></p>
<dd>
<dt>The log files are created at the specified directory.</p>
<dd>
<dt><code>6) Configure log file name</code></p>
<dd>
<dt><i>nvidia-smi daemon -j &lt;string to append log file name&gt;</i></p>
<dd>
<dt>The command-line is used to append the log file name with the user provided string.</p>
<dd>
<dt><code>7) Terminate the daemon</code></p>
<dd>
<dt><i>nvidia-smi daemon -t</i></p>
<dd>
<dt>This command-line uses the stored PID (at /var/run/nvsmi.pid) to terminate the daemon. It makes the best effort to stop the daemon and offers no guarantees for it&#8217;s termination. In case the daemon is not terminated, then the user can manually terminate by sending kill signal to the daemon. Performing a GPU reset operation (via nvidia-smi) requires all GPU processes to be exited, including the daemon. Users who have the daemon open will see an error to the effect that the GPU is busy.</p>
<dd>
<dt><code>8) Help Information</code></p>
<dd>
<dt><i>nvidia-smi daemon -h</i></p>
<dd>
<dt>Displays help information for using the command line.</p>
<dd>
</dl>
<h3>Replay Mode (EXPERIMENTAL)</h3>
<p> The &quot;nvidia-smi replay&quot; command-line is used to extract/replay all or parts of log file generated by the daemon. By default, the tool tries to pull the metrics such as Power Usage, Temperature, SM clocks, Memory clocks and Utilization values for SM, Memory, Encoder and Decoder. The replay tool can also fetch other metrics such as frame buffer memory usage, bar1 memory usage, power/thermal violations and aggregate single/double bit ecc errors. There is an option to select a set of metrics to replay, If any of the requested metric is not maintained or logged as not-supported then it&#8217;s shown as &quot;-&quot; in the output. The format of data produced by this mode is such that the user is running the device monitoring utility interactively. The command line requires mandatory option &quot;-f&quot; to specify complete path of the log filename, all the other supported options are exclusive and can be used together in any order. </p>
<p> <code>Usage:</code></p>
<dl>
<dt><code>1) Specify log file to be replayed</code></p>
<dd>
<dt><i>nvidia-smi replay -f &lt;log file name&gt;</i></p>
<dd>
<dt>Fetches monitoring data from the compressed log file and allows the user to see one line of monitoring data (default metrics with time-stamp) for each monitoring iteration stored in the log file. A new line of monitoring data is replayed every other second irrespective of the actual monitoring frequency maintained at the time of collection. It is displayed till the end of file or until terminated by ^C.</p>
<dd>
<dt><code>2) Filter metrics to be replayed</code></p>
<dd>
<dt><i>nvidia-smi replay -f &lt;path to log file&gt; -s &lt;metric_group&gt;</i></p>
<dd>
<dt>&lt;metric_group&gt; can be one or more from the following:</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p &#8211; Power Usage&nbsp;(in Watts)&nbsp;and Gpu/Memory Temperature&nbsp;(in C)&nbsp;if supported</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u &#8211; Utilization&nbsp;(SM, Memory, Encoder and Decoder Utilization in&nbsp;%)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c &#8211; Proc and Mem Clocks&nbsp;(in MHz)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v &#8211; Power Violations&nbsp;(in&nbsp;%)&nbsp;and Thermal Violations&nbsp;(as a boolean flag)</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;m &#8211; Frame Buffer and Bar1 memory usage&nbsp;(in MB)</p>
<dd>
<dt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>e &#8211; ECC (Number of aggregated single bit, double bit ecc errors) and PCIe Replay errors</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t &#8211; PCIe Rx and Tx Throughput in MB/s&nbsp;(Maxwell and above)</p>
<dd>
<dt><code>3) Limit replay to one or more devices</code></p>
<dd>
<dt><i>nvidia-smi replay -f &lt;log file&gt; -i &lt;device1,device2, .. , deviceN&gt;</i></p>
<dd>
<dt>Limits reporting of the metrics to the set of devices selected by comma separated device list. The tool skips any of the devices not maintained in the log file.</p>
<dd>
<dt><code>4) Restrict the time frame between which data is reported</code></p>
<dd>
<dt><i>nvidia-smi replay -f &lt;log file&gt; -b &lt;start time in HH:MM:SS format&gt; -e &lt;end time in HH:MM:SS format&gt;</i></p>
<dd>
<dt>This option allows the data to be limited between the specified time range. Specifying time as 0 with -b or -e option implies start or end file respectively.</p>
<dd>
<dt><code>5) Redirect replay information to a log file</code></p>
<dd>
<dt><i>nvidia-smi replay -f &lt;log file&gt; -r &lt;output file name&gt;</i></p>
<dd>
<dt>This option takes log file as an input and extracts the information related to default metrics in the specified output file.</p>
<dd>
<dt><code>6) Help Information</code></p>
<dd>
<dt><i>nvidia-smi replay -h</i></p>
<dd>
<dt>Displays help information for using the command line.</p>
<dd>
</dl>
<h3>Process Monitoring</h3>
<p> The &quot;nvidia-smi pmon&quot; command-line is used to monitor compute and graphics processes running on one or more GPUs (up to 4 devices) plugged into the system. This tool allows the user to see the statistics for all the running processes on each device at every monitoring cycle. The output is in concise format and easy to interpret in interactive mode. The output data per line is limited by the terminal size. It is supported on Tesla, GRID, Quadro and limited GeForce products for Kepler or newer GPUs under bare metal 64 bits Linux. By default, the monitoring data for each process includes the pid, command name and average utilization values for SM, Memory, Encoder and Decoder since the last monitoring cycle. It can also be configured to report frame buffer memory usage for each process. If there is no process running for the device, then all the metrics are reported as &quot;-&quot; for the device. If any of the metric is not supported on the device or any other error in fetching the metric is also reported as &quot;-&quot; in the output data. The user can also configure monitoring frequency and the number of monitoring iterations for each run. There is also an option to include date and time at each line. All the supported options are exclusive and can be used together in any order. </p>
<p> <code>Usage:</code></p>
<dl>
<dt><code>1) Default with no arguments</code></p>
<dd>
<dt><i>nvidia-smi pmon</i></p>
<dd>
<dt>Monitors all the processes running on each device for up to 4 supported devices under natural enumeration (starting with GPU index 0) at a frequency of 1 sec. Runs until terminated with ^C.</p>
<dd>
<dt><code>2) Select one or more devices</code></p>
<dd>
<dt><i>nvidia-smi pmon -i &lt;device1,device2, .. , deviceN&gt;</i></p>
<dd>
<dt>Reports statistics for all the processes running on the devices selected by comma separated device list. The tool picks up to 4 supported devices from the list under natural enumeration (starting with GPU index 0).</p>
<dd>
<dt><code>3) Select metrics to be displayed</code></p>
<dd>
<dt><i>nvidia-smi pmon -s &lt;metric_group&gt;</i></p>
<dd>
<dt>&lt;metric_group&gt; can be one or more from the following:</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u &#8211; Utilization&nbsp;(SM, Memory, Encoder and Decoder Utilization for the process in&nbsp;%). Reports average utilization since last monitoring cycle.</p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;m &#8211; Frame Buffer usage&nbsp;(in MB). Reports instantaneous value for memory usage.</p>
<dd>
<dt><code>4) Configure monitoring iterations</code></p>
<dd>
<dt><i>nvidia-smi pmon -c &lt;number of samples&gt;</i></p>
<dd>
<dt>Displays data for specified number of samples and exit.</p>
<dd>
<dt><code>5) Configure monitoring frequency</code></p>
<dd>
<dt><i>nvidia-smi pmon -d &lt;time in secs&gt;</i></p>
<dd>
<dt>Collects and displays data at every specified monitoring interval until terminated with ^C. The monitoring frequency must be between 1 to 10 secs.</p>
<dd>
<dt><code>6) Display date</code></p>
<dd>
<dt><i>nvidia-smi pmon -o D</i></p>
<dd>
<dt>Prepends monitoring data with date in YYYYMMDD format.</p>
<dd>
<dt><code>7) Display time</code></p>
<dd>
<dt><i>nvidia-smi pmon -o T</i></p>
<dd>
<dt>Prepends monitoring data with time in HH:MM:SS format.</p>
<dd>
<dt><code>8) Help Information</code></p>
<dd>
<dt><i>nvidia-smi pmon -h</i></p>
<dd>
<dt>Displays help information for using the command line.</p>
<dd>
</dl>
<h3>Topology (EXPERIMENTAL)</h3>
<p> List topology information about the system&#8217;s GPUs, how they connect to each other as well as qualified NICs capable of RDMA </p>
<dl>
<dt>Displays a matrix of available GPUs with the following legend:</p>
<dd>
<dt>
<dd> Legend: </p>
<p>&nbsp;<wbr>&nbsp;X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;Self<br />
&nbsp;<wbr>&nbsp;SYS&nbsp;<wbr>&nbsp;=&nbsp;Connection traversing PCIe as well as the SMP interconnect between NUMA nodes&nbsp;(e.g., QPI/UPI)<br />
&nbsp;<wbr>&nbsp;NODE&nbsp;=&nbsp;Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node<br />
&nbsp;<wbr>&nbsp;PHB&nbsp;<wbr>&nbsp;=&nbsp;Connection traversing PCIe as well as a PCIe Host Bridge&nbsp;(typically the CPU)<br />
&nbsp;<wbr>&nbsp;PXB&nbsp;<wbr>&nbsp;=&nbsp;Connection traversing multiple PCIe switches&nbsp;(without traversing the PCIe Host Bridge)<br />
&nbsp;<wbr>&nbsp;PIX&nbsp;<wbr>&nbsp;=&nbsp;Connection traversing a single PCIe switch<br />
&nbsp;<wbr>&nbsp;NV#&nbsp;<wbr>&nbsp;=&nbsp;Connection traversing a bonded set of&nbsp;#&nbsp;NVLinks </p>
</dl>
<h3>vGPU Management</h3>
<p> The &quot;nvidia-smi vgpu&quot; command reports on GRID vGPUs executing on supported GPUs and hypervisors (refer to driver release notes for supported platforms). Summary reporting provides basic information about vGPUs currently executing on the system. Additional options provide detailed reporting of vGPU properties, per-vGPU reporting of SM, Memory, Encoder, and Decoder utilization, and per-GPU reporting of supported and creatable vGPUs. Periodic reports can be automatically generated by specifying a configurable loop frequency to any command. </p>
<p> <code>Usage:</code> </p>
<dl>
<dt><code>1) Help Information</code></p>
<dd>
<dt><i>nvidia-smi vgpu -h</i></p>
<dd>
<dt>Displays help information for using the command line.</p>
<dd>
<dt><code>2) Default with no arguments</code></p>
<dd>
<dt><i>nvidia-smi vgpu</i></p>
<dd>
<dt>Reports summary of all the vGPUs currently active on each device.</p>
<dd>
<dt><code>3) Display detailed info on currently active vGPUs</code></p>
<dd>
<dt><i>nvidia-smi vgpu -q</i></p>
<dd>
<dt>Collects and displays information on currently active vGPUs on each device, including driver version, utilization, and other information.</p>
<dd>
<dt><code>4) Select one or more devices</code></p>
<dd>
<dt><i>nvidia-smi vgpu -i &lt;device1,device2, .. , deviceN&gt;</i></p>
<dd>
<dt>Reports summary for all the vGPUs currently active on the devices selected by comma-separated device list.</p>
<dd>
<dt><code>5) Display supported vGPUs</code></p>
<dd>
<dt><i>nvidia-smi vgpu -s</i></p>
<dd>
<dt>Displays vGPU types supported on each device. Use the -v / &#8211;verbose option to show detailed info on each vGPU type.</p>
<dd>
<dt><code>6) Display creatable vGPUs</code></p>
<dd>
<dt><i>nvidia-smi vgpu -c</i></p>
<dd>
<dt>Displays vGPU types creatable on each device. This varies dynamically, depending on the vGPUs already active on the device. Use the -v / &#8211;verbose option to show detailed info on each vGPU type.</p>
<dd>
<dt><code>7) Report utilization for currently active vGPUs.</code></p>
<dd>
<dt><i>nvidia-smi vgpu -u</i></p>
<dd>
<dt>Reports average utilization (SM, Memory, Encoder and Decoder) for each active vGPU since last monitoring cycle. The default cycle time is 1 second, and the command runs until terminated with ^C. If a device has no active vGPUs, its metrics are reported as &quot;-&quot;.</p>
<dd>
<dt><code>8) Configure loop frequency</code></p>
<dd>
<dt><i>nvidia-smi vgpu [-s -c -q -u] -l &lt;time in secs&gt;</i></p>
<dd>
<dt>Collects and displays data at a specified loop interval until terminated with ^C. The loop frequency must be between 1 and 10 secs. When no time is specified, the loop frequency defaults to 5 secs.</p>
<dd>
<dt><code>9) Display GPU engine usage</code></p>
<dd>
<dt><i>nvidia-smi vgpu -p</i></p>
<dd>
<dt>Display GPU engine usage of currently active processes running in the vGPU VMs.</p>
<dd>
<dt><code>10) Display migration capabitlities.</code></p>
<dd>
<dt><i>nvidia-smi vgpu -m</i></p>
<dd>
<dt>Display pGPU&#8217;s migration/suspend/resume capability.</p>
<dd>
<dt><code>11) Display Nvidia Encoder session info.</code></p>
<dd>
<dt><i>nvidia-smi vgpu -es</i></p>
<dd>
<dt>Display the information about encoder sessions for currently running vGPUs.</p>
<dd>
<dt><code>12) Display accounting statistics.</code></p>
<dd>
<dt><i>nvidia-smi vgpu &#8211;query-accounted-apps=[input parameters]</i></p>
<dd>
<dt>Display accounting stats for compute/graphics processes.</p>
<dd>
<dt>To find list of properties which can be queried, run &#8211; &#8216;nvidia-smi &#8211;help-query-accounted-apps&#8217;.</p>
<dd>
<dt><code>13) Display Nvidia Frame Buffer Capture session info.</code></p>
<dd>
<dt><i>nvidia-smi vgpu -fs</i></p>
<dd>
<dt>Display the information about FBC sessions for currently running vGPUs.</p>
<dd>
<dt><i>Note : Horizontal resolution, vertical resolution, average FPS and average latency data for a FBC session may be zero if there are no new frames captured since the session started.</i></p>
<dd>
</dl>
<h3>MIG Management</h3>
<p> The privileged &quot;nvidia-smi mig&quot; command-line is used to manage MIG-enabled GPUs. It provides options to create, list and destroy GPU instances and compute instances. </p>
<p> <code>Usage:</code> </p>
<dl>
<dt><code>1) Display help menu</code></p>
<dd>
<dt><i>nvidia-smi mig -h</i></p>
<dd>
<dt>Displays help menu for using the command-line.</p>
<dd>
<dt><code>2) Select one or more GPUs</code></p>
<dd>
<dt><i>nvidia-smi mig -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Selects one or more GPUs using the given comma-separated GPU indexes, PCI bus IDs or UUIDs. If not used, the given command-line option applies to all of the supported GPUs.</p>
<dd>
<dt><code>3) Select one or more GPU instances</code></p>
<dd>
<dt><i>nvidia-smi mig -gi &lt;GPU instance IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;gpu-instance-id &lt;GPU instance IDs&gt;</i></p>
<dd>
<dt>Selects one or more GPU instances using the given comma-separated GPU instance IDs. If not used, the given command-line option applies to all of the GPU instances.</p>
<dd>
<dt><code>4) Select one or more compute instances</code></p>
<dd>
<dt><i>nvidia-smi mig -ci &lt;compute instance IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;compute-instance-id &lt;compute instance IDs&gt;</i></p>
<dd>
<dt>Selects one or more compute instances using the given comma-separated compute instance IDs. If not used, the given command-line option applies to all of the compute instances.</p>
<dd>
<dt><code>5) List GPU instance profiles</code></p>
<dd>
<dt><i>nvidia-smi mig -lgip -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;list-gpu-instance-profiles &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Lists GPU instance profiles, their availability and IDs. Profiles describe the supported types of GPU instances, including all of the GPU resources they exclusively control.</p>
<dd>
<dt><code>6) List GPU instance possible placements</code></p>
<dd>
<dt><i>nvidia-smi mig -lgipp -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;list-gpu-instance-possible-placements &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Lists GPU instance possible placements. Possible placements describe the locations of the supported types of GPU instances within the GPU.</p>
<dd>
<dt><code>7) Create GPU instance</code></p>
<dd>
<dt><i>nvidia-smi mig -cgi &lt;GPU instance specifiers&gt; -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;create-gpu-instance &lt;GPU instance specifiers&gt; &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Creates GPU instances for the given GPU instance specifiers. A GPU instance specifier comprises a GPU instance profile name or ID and an optional placement specifier consisting of a colon and a placement start index. The command fails if the GPU resources required to allocate the requested GPU instances are not available, or if the placement index is not valid for the given profile.</p>
<dd>
<dt><code>8) Create a GPU instance along with the default compute instance</code></p>
<dd>
<dt><i>nvidia-smi mig -cgi &lt;GPU instance profile IDs or names&gt; -i &lt;GPU IDs&gt; -C</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;create-gpu-instance &lt;GPU instance profile IDs or names&gt; &#8211;id &lt;GPU IDs&gt; &#8211;default-compute-instance</i></p>
<dd>
<dt><code>9) List GPU instances</code></p>
<dd>
<dt><i>nvidia-smi mig -lgi -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;list-gpu-instances &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Lists GPU instances and their IDs.</p>
<dd>
<dt><code>10) Destroy GPU instance</code></p>
<dd>
<dt><i>nvidia-smi mig -dgi -gi &lt;GPU instance IDs&gt; -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;destroy-gpu-instances &#8211;gpu-instance-id &lt;GPU instance IDs&gt; &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Destroys GPU instances. The command fails if the requested GPU instance is in use by an application.</p>
<dd>
<dt><code>11) List compute instance profiles</code></p>
<dd>
<dt><i>nvidia-smi mig -lcip -gi &lt;GPU instance IDs&gt; -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;list-compute-instance-profiles &#8211;gpu-instance-id &lt;GPU instance IDs&gt; &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Lists compute instance profiles, their availability and IDs. Profiles describe the supported types of compute instances, including all of the GPU resources they share or exclusively control.</p>
<dd>
<dt><code>12) Create compute instance</code></p>
<dd>
<dt><i>nvidia-smi mig -cci &lt;compute instance profile IDs or names&gt; -gi &lt;GPU instance IDs&gt; -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;create-compute-instance &lt;compute instance profile IDs or names&gt; &#8211;gpu-instance-id &lt;GPU instance IDs&gt; &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Creates compute instances for the given compute instance profile IDs or names. The command fails if the GPU resources required to allocate the requested compute instances are not available.</p>
<dd>
<dt><code>13) List compute instances</code></p>
<dd>
<dt><i>nvidia-smi mig -lci -gi &lt;GPU instance IDs&gt; -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;list-compute-instances &#8211;gpu-instance-id &lt;GPU instance IDs&gt; &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Lists compute instances and their IDs.</p>
<dd>
<dt><code>14) Destroy compute instance</code></p>
<dd>
<dt><i>nvidia-smi mig -dci -ci &lt;compute instance IDs&gt; -gi &lt;GPU instance IDs&gt; -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi mig &#8211;destroy-compute-instance &#8211;compute-instance-id &lt;compute instance IDs&gt; &#8211;gpu-instance-id &lt;GPU instance IDs&gt; &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Destroys compute instances. The command fails if the requested compute instance is in use by an application.</p>
<dd>
</dl>
<h3>Boost Slider</h3>
<p> The privileged &quot;nvidia-smi boost-slider&quot; command-line is used to manage boost slider on GPUs. It provides options to list and control boost sliders. </p>
<p> <code>Usage:</code> </p>
<dl>
<dt><code>1) Display help menu</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -h</i></p>
<dd>
<dt>Displays help menu for using the command-line.</p>
<dd>
<dt><code>2) List one or more GPUs</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi boost-slider &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Selects one or more GPUs using the given comma-separated GPU indexes, PCI bus IDs or UUIDs. If not used, the given command-line option applies to all of the supported GPUs.</p>
<dd>
<dt><code>3) List boost sliders</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -l</i></p>
<dd>
<dt><i>nvidia-smi boost-slider &#8211;list</i></p>
<dd>
<dt>List all boost sliders for the selected devices.</p>
<dd>
<dt><code>4) Set video boost slider</code></p>
<dd>
<dt><i>nvidia-smi boost-slider &#8211;vboost &lt;value&gt;</i></p>
<dd>
<dt>Set the video boost slider for the selected devices.</p>
<dd>
</dl>
<h3>Power Hint</h3>
<p> The privileged &quot;nvidia-smi power-hint&quot; command-line is used to query power hint on GPUs. </p>
<p> <code>Usage:</code> </p>
<dl>
<dt><code>1) Display help menu</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -h</i></p>
<dd>
<dt>Displays help menu for using the command-line.</p>
<dd>
<dt><code>2) List one or more GPUs</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -i &lt;GPU IDs&gt;</i></p>
<dd>
<dt><i>nvidia-smi boost-slider &#8211;id &lt;GPU IDs&gt;</i></p>
<dd>
<dt>Selects one or more GPUs using the given comma-separated GPU indexes, PCI bus IDs or UUIDs. If not used, the given command-line option applies to all of the supported GPUs.</p>
<dd>
<dt><code>3) List power hint info</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -l</i></p>
<dd>
<dt><i>nvidia-smi boost-slider &#8211;list-info</i></p>
<dd>
<dt>List all boost sliders for the selected devices.</p>
<dd>
<dt><code>4) Query power hint</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -gc &lt;value&gt; -t &lt;value&gt; -p &lt;profile ID&gt;</i></p>
<dd>
<dt><i>nvidia-smi boost-slider &#8211;graphics-clock &lt;value&gt; &#8211;temperature &lt;value&gt; &#8211;profile &lt;profile ID&gt;</i></p>
<dd>
<dt>Query power hint with graphics clock, temperature and profile id.</p>
<dd>
<dt><code>5) Query power hint</code></p>
<dd>
<dt><i>nvidia-smi boost-slider -gc &lt;value&gt; -mc &lt;value&gt; -t &lt;value&gt; -p &lt;profile ID&gt;</i></p>
<dd>
<dt><i>nvidia-smi boost-slider &#8211;graphics-clock &lt;value&gt; &#8211;memory-clock &lt;value&gt; &#8211;temperature &lt;value&gt; &#8211;profile &lt;profile ID&gt;</i></p>
<dd>
<dt>Query power hint with graphics clock, memory clock, temperature and profile id.</p>
<dd>
</dl>
<h2>UNIT ATTRIBUTES</h2>
<p> The following list describes all possible data returned by the <code>-q -u</code> unit query option. Unless otherwise noted all numerical results are base 10 and unitless. </p>
<h3>Timestamp</h3>
<p> The current system timestamp at the time nvidia-smi was invoked. Format is &quot;Day-of-week Month Day HH:MM:SS Year&quot;. </p>
<h3>Driver Version</h3>
<p> The version of the installed NVIDIA display driver. Format is &quot;Major-Number.Minor-Number&quot;. </p>
<h3>HIC Info</h3>
<p> Information about any Host Interface Cards (HIC) that are installed in the system. </p>
<dl>
<dt><code>Firmware Version</code></p>
<dd> The version of the firmware running on the HIC. </p>
</dl>
<h3>Attached Units</h3>
<p> The number of attached Units in the system. </p>
<h3>Product Name</h3>
<p> The official product name of the unit. This is an alphanumeric value. For all S-class products. </p>
<h3>Product Id</h3>
<p> The product identifier for the unit. This is an alphanumeric value of the form &quot;part1-part2-part3&quot;. For all S-class products. </p>
<h3>Product Serial</h3>
<p> The immutable globally unique identifier for the unit. This is an alphanumeric value. For all S-class products. </p>
<h3>Firmware Version</h3>
<p> The version of the firmware running on the unit. Format is &quot;Major-Number.Minor-Number&quot;. For all S-class products. </p>
<h3>LED State</h3>
<p> The LED indicator is used to flag systems with potential problems. An LED color of AMBER indicates an issue. For all S-class products. </p>
<dl>
<dt><code>Color</code></p>
<dd> The color of the LED indicator. Either &quot;GREEN&quot; or &quot;AMBER&quot;. </p>
<dt><code>Cause</code></p>
<dd> The reason for the current LED color. The cause may be listed as any combination of &quot;Unknown&quot;, &quot;Set to AMBER by host system&quot;, &quot;Thermal sensor failure&quot;, &quot;Fan failure&quot; and &quot;Temperature exceeds critical limit&quot;. </p>
</dl>
<h3>Temperature</h3>
<p> Temperature readings for important components of the Unit. All readings are in degrees C. Not all readings may be available. For all S-class products. </p>
<dl>
<dt><code>Intake</code></p>
<dd> Air temperature at the unit intake. </p>
<dt><code>Exhaust</code></p>
<dd> Air temperature at the unit exhaust point. </p>
<dt><code>Board</code></p>
<dd> Air temperature across the unit board. </p>
</dl>
<h3>PSU</h3>
<p> Readings for the unit power supply. For all S-class products. </p>
<dl>
<dt><code>State</code></p>
<dd> Operating state of the PSU. The power supply state can be any of the following: &quot;Normal&quot;, &quot;Abnormal&quot;, &quot;High voltage&quot;, &quot;Fan failure&quot;, &quot;Heatsink temperature&quot;, &quot;Current limit&quot;, &quot;Voltage below UV alarm threshold&quot;, &quot;Low-voltage&quot;, &quot;I2C remote off command&quot;, &quot;MOD_DISABLE input&quot; or &quot;Short pin transition&quot;. </p>
<dt><code>Voltage</code></p>
<dd> PSU voltage setting, in volts. </p>
<dt><code>Current</code></p>
<dd> PSU current draw, in amps. </p>
</dl>
<h3>Fan Info</h3>
<p> Fan readings for the unit. A reading is provided for each fan, of which there can be many. For all S-class products. </p>
<dl>
<dt><code>State</code></p>
<dd> The state of the fan, either &quot;NORMAL&quot; or &quot;FAILED&quot;. </p>
<dt><code>Speed</code></p>
<dd> For a healthy fan, the fan&#8217;s speed in RPM. </p>
</dl>
<h3>Attached GPUs</h3>
<p> A list of PCI bus ids that correspond to each of the GPUs attached to the unit. The bus ids have the form &quot;domain:bus:device.function&quot;, in hex. For all S-class products. </p>
<h2>NOTES</h2>
<p> On Linux, NVIDIA device files may be modified by nvidia-smi if run as root. Please see the relevant section of the driver README file. </p>
<p> The <code>-a</code> and <code>-g</code> arguments are now deprecated in favor of <code>-q</code> and <code>-i</code>, respectively. However, the old arguments still work for this release. </p>
<h2>EXAMPLES</h2>
<h3>nvidia-smi -q</h3>
<p> Query attributes for all GPUs once, and display in plain text to stdout.</p>
<h3>nvidia-smi &#8211;format=csv,noheader &#8211;query-gpu=uuid,persistence_mode</h3>
<p> Query UUID and persistence mode of all GPUs in the system.</p>
<h3>nvidia-smi -q -d ECC,POWER -i 0 -l 10 -f out.log</h3>
<p> Query ECC errors and power consumption for GPU 0 at a frequency of 10 seconds, indefinitely, and record to the file out.log.</p>
<h3>nvidia-smi -c 1 -i GPU-b2f5f1b745e3d23d-65a3a26d-097db358-7303e0b6-149642ff3d219f8587cde3a8</h3>
<p> Set the compute mode to &quot;PROHIBITED&quot; for GPU with UUID &quot;GPU-b2f5f1b745e3d23d-65a3a26d-097db358-7303e0b6-149642ff3d219f8587cde3a8&quot;.</p>
<h3>nvidia-smi -q -u -x &#8211;dtd</h3>
<p> Query attributes for all Units once, and display in XML format with embedded DTD to stdout.</p>
<h3>nvidia-smi &#8211;dtd -u -f nvsmi_unit.dtd</h3>
<p> Write the Unit DTD to nvsmi_unit.dtd.</p>
<h3>nvidia-smi -q -d SUPPORTED_CLOCKS</h3>
<p> Display supported clocks of all GPUs.</p>
<h3>nvidia-smi -i 0 &#8211;applications-clocks 2500,745</h3>
<p> Set applications clocks to 2500 MHz memory, and 745 MHz graphics.</p>
<h3>nvidia-smi mig -cgi 19</h3>
<p> Create a MIG GPU instance on profile ID 19.</p>
<h3>nvidia-smi mig -cgi 19:2</h3>
<p> Create a MIG GPU instance on profile ID 19 at placement start index 2.</p>
<h3>nvidia-smi boost-slider -l</h3>
<p> List all boost sliders for all GPUs.</p>
<h3>nvidia-smi boost-slider &#8211;vboost 1</h3>
<p> Set vboost to value 1 for all GPUs.</p>
<h3>nvidia-smi power-hint -l</h3>
<p> List clock range, temperature range and supported profiles of power hint.</p>
<h3>nvidia-smi boost-slider -gc 1350 -t 60 -p 0</h3>
<p> Query power hint with graphics clock at 1350MHz, temperature at 60C and profile ID at 0.</p>
<h3>nvidia-smi boost-slider -gc 1350 -mc 1215 -t n5 -p 1</h3>
<p> Query power hint with graphics clock at 1350MHz, memory clock at 1215MHz, temperature at -5C and profile ID at 1. </p>
<h2>CHANGE LOG</h2>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Known Issues&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;On Linux GPU Reset can&#8217;t be triggered when there is pending GOM change. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;On Linux GPU Reset may not successfully change pending ECC mode. A full reboot may be required to enable the mode change. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;On Linux platforms that configure NVIDIA GPUs as NUMA nodes, enabling persistence mode or resetting GPUs may print&nbsp;&quot;Warning: persistence mode is disabled on device&quot;&nbsp;if nvidia-persistenced is not running, or if nvidia-persistenced cannot access files in the NVIDIA driver&#8217;s procfs directory for the device&nbsp;(/proc/driver/nvidia/gpus/&lt;PCI Config Address&gt;/). During GPU reset and driver reload, this directory will be deleted and recreated, and outstanding references to the deleted directory, such as mounts or shells, can prevent processes from accessing files in the new directory. </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v465 Update and v470&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support to query power hint </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v460 Update and v465&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Removed support for -acp,&#8211;application-clock-permissions option </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v450 Update and v460&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Add option to specify placement when creating a MIG GPU instance. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support to query and control boost slider </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v445 Update and v450&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added &#8211;lock-memory-clock and &#8211;reset-memory-clock command to lock to closest min/max Memory clock provided and ability to reset Memory clock </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Allow fan speeds greater than 100%&nbsp;to be reported </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added topo support to display NUMA node affinity for GPU devices </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support to create MIG instances using profile names </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support to create the default compute instance while creating a GPU instance </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support to query and disable MIG mode on Windows </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Removed support of GPU reset(-r)&nbsp;command on MIG enabled vGPU guests </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v418 Update and v445&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for Multi Instance GPU&nbsp;(MIG) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support to individually reset NVLink-capable GPUs based on the NVIDIA Ampere architecture </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v361 Update and v418&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Support for Volta and Turing architectures, bug fixes, performance improvements, and new features </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v352 Update and v361&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added nvlink support to expose the publicly available NVLINK NVML APIs </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added clocks sub-command with synchronized boost support </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Updated nvidia-smi stats to report GPU temperature metric </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Updated nvidia-smi dmon to support PCIe throughput </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Updated nvidia-smi daemon/replay to support PCIe throughput </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Updated nvidia-smi dmon, daemon and replay to support PCIe Replay Errors </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added GPU part numbers in nvidia-smi -q </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Removed support for exclusive thread compute mode </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added Video&nbsp;(encoder/decode)&nbsp;clocks to the Clocks and Max Clocks display of nvidia-smi -q </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added memory temperature output to nvidia-smi dmon </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added &#8211;lock-gpu-clock and &#8211;reset-gpu-clock command to lock to closest min/max GPU clock provided and reset clock </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added &#8211;cuda-clocks to override or restore default CUDA clocks </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v346 Update and v352&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added topo support to display affinities per GPU </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added topo support to display neighboring GPUs for a given level </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added topo support to show pathway between two given GPUs </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added&nbsp;&quot;nvidia-smi pmon&quot;&nbsp;command-line for process monitoring in scrolling format </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added&nbsp;&quot;&#8211;debug&quot;&nbsp;option to produce an encrypted debug log for use in submission of bugs back to NVIDIA </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Fixed reporting of Used/Free memory under Windows WDDM mode </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;The accounting stats is updated to include both running and terminated processes. The execution time of running process is reported as 0 and updated to actual value when the process is terminated. </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v340 Update and v346&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of PCIe replay counters </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for reporting Graphics processes via nvidia-smi </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of PCIe utilization </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added dmon command-line for device monitoring in scrolling format </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added daemon command-line to run in background and monitor devices as a daemon process. Generates dated log files at&nbsp;/var/log/nvstats/ </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added replay command-line to replay/extract the stat files generated by the daemon tool </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v331 Update and v340&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of temperature threshold information. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of brand information&nbsp;(e.g. Tesla, Quadro, etc.) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for K40d and K80. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of max, min and avg for samples&nbsp;(power, utilization, clock changes). Example commandline: nvidia-smi -q -d power,utilization, clock </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added nvidia-smi stats interface to collect statistics such as power, utilization, clock changes, xid events and perf capping counters with a notion of time attached to each sample. Example commandline: nvidia-smi stats </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for collectively reporting metrics on more than one GPU. Used with comma separated with&nbsp;&quot;-i&quot;&nbsp;option. Example: nvidia-smi -i 0,1,2 </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for displaying the GPU encoder and decoder utilizations </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added nvidia-smi topo interface to display the GPUDirect communication matrix&nbsp;(EXPERIMENTAL) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for displayed the GPU board ID and whether or not it is a multiGPU board </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Removed user-defined throttle reason from XML output </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v5.319 Update and v331&nbsp;=== </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of minor number. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting BAR1 memory size. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of bridge chip firmware. </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v4.319 Production and v4.319 Update&nbsp;=== </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added new &#8211;applications-clocks-permission switch to change permission requirements for setting and resetting applications clocks. </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v4.304 and v4.319 Production&nbsp;=== </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of Display Active state and updated documentation to clarify how it differs from Display Mode and Display Active state </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;For consistency on multi-GPU boards nvidia-smi -L always displays UUID instead of serial number </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added machine readable selective reporting. See SELECTIVE QUERY OPTIONS section of nvidia-smi -h </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added queries for page retirement information.&nbsp;<wbr>&nbsp;See &#8211;help-query-retired-pages and -d PAGE_RETIREMENT </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Renamed Clock Throttle Reason User Defined Clocks to Applications Clocks Setting </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;On error, return codes have distinct non zero values for each error class. See RETURN VALUE section </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;nvidia-smi -i can now query information from healthy GPU when there is a problem with other GPU in the system </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;All messages that point to a problem with a GPU print pci bus id of a GPU at fault </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;New flag &#8211;loop-ms for querying information at higher rates than once a second&nbsp;(can have negative impact on system performance) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added queries for accounting procsses.&nbsp;<wbr>&nbsp;See &#8211;help-query-accounted-apps and -d ACCOUNTING </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added the enforced power limit to the query output </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v4.304 RC and v4.304 Production&nbsp;=== </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of GPU Operation Mode&nbsp;(GOM) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added new &#8211;gom switch to set GPU Operation Mode </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v3.295 and v4.304 RC&nbsp;=== </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Reformatted non-verbose output due to user feedback.&nbsp;<wbr>&nbsp;Removed pending information from table. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Print out helpful message if initialization fails due to kernel module not receiving interrupts </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Better error handling when NVML shared library is not present in the system </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added new &#8211;applications-clocks switch </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added new filter to &#8211;display switch. Run with -d SUPPORTED_CLOCKS to list possible clocks on a GPU </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;When reporting free memory, calculate it from the rounded total and used memory so that values add up </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of power management limit constraints and default limit </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added new &#8211;power-limit switch </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of texture memory ECC errors </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of Clock Throttle Reasons </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v2.285 and v3.295&nbsp;=== </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Clearer error reporting for running commands&nbsp;(like changing compute mode) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;When running commands on multiple GPUs at once N/A errors are treated as warnings. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;nvidia-smi -i now also supports UUID </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;UUID format changed to match UUID standard and will report a different value. </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;===&nbsp;Changes between nvidia-smi v2.0 and v2.285&nbsp;=== </p>
<p>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Report VBIOS version. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added -d/&#8211;display flag to filter parts of data </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of PCI Sub System ID </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Updated docs to indicate we support M2075 and C2075 </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Report HIC HWBC firmware version with -u switch </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Report max(P0)&nbsp;clocks next to current clocks </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added &#8211;dtd flag to print the device or unit DTD </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added message when NVIDIA driver is not running </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added reporting of PCIe link generation&nbsp;(max and current), and link width&nbsp;(max and current). </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Getting pending driver model works on non-admin </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for running nvidia-smi on Windows Guest accounts </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Running nvidia-smi without -q command will output non verbose version of -q instead of help </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Fixed parsing of -l/&#8211;loop=&nbsp;argument&nbsp;(default value, 0, to big value) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Changed format of pciBusId&nbsp;(to XXXX:XX:XX.X &#8211; this change was visible in 280) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Parsing of busId for -i command is less restrictive. You can pass 0:2:0.0 or 0000:02:00 and other variations </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Changed versioning scheme to also include&nbsp;&quot;driver version&quot; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;XML format always conforms to DTD, even when error conditions occur </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added support for single and double bit ECC events and XID errors&nbsp;(enabled by default with -l flag disabled for -x flag) </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added device reset -r &#8211;gpu-reset flags </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Added listing of compute running processes&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Renamed power state to performance state. Deprecated support exists in XML output only. </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;Updated DTD version number to 2.0 to match the updated XML output </p>
<h2>SEE ALSO</h2>
<p> On Linux, the driver README is installed as /usr/share/doc/NVIDIA_GLX-1.0/README.txt </p>
<h2>AUTHOR</h2>
<p> NVIDIA Corporation</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2011-2023 NVIDIA Corporation. </p>
<h2>Index</h2>
