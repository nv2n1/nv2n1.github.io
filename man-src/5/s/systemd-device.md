---
title: "systemd-device(5)"
name: "systemd-device"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-device/"
description: "systemd.device – Device unit configuration"
---

<p>systemd.device &#8211; Device unit configuration</p>
<h2>Synopsis</h2>
<p><i>device</i>.device</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.device&quot; encodes information about a device unit as exposed in the sysfs/<code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) device tree. This may be used to define dependencies between devices and other units. </p>
<p> This unit type has no specific options. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. A separate [Device] section does not exist, since no device-specific options may be configured. </p>
<p> systemd will dynamically create device units for all kernel devices that are marked with the &quot;systemd&quot; udev tag (by default all block and network devices, and a few others). Note that <i>if </i><i>systemd-udev.service</i><i> is not running, no device units will be available (for example in a typical container)</i>. </p>
<p> Device units are named after the /sys/ and /dev/ paths they control. Example: the device /dev/sda5 is exposed in systemd as dev-sda5.device. For details about the escaping logic used to convert a file system path to a unit name see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). </p>
<p> To tag a udev device, use &quot;TAG+=&quot;systemd&quot;&quot; in the udev rules file, see <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) for details. </p>
<p> Device units will be reloaded by systemd whenever the corresponding device generates a &quot;changed&quot; event. Other units can use <i>ReloadPropagatedFrom=</i> to react to that event.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>Many unit types automatically acquire dependencies on device units of devices they require. For example, .socket unit acquire dependencies on the device units of the network interface specified in <i>BindToDevice=</i>. Similar, swap and mount units acquire dependencies on the units encapsulating their backing block devices.</p>
<h3>Default Dependencies</h3>
<p>There are no default dependencies for device units.</p>
<h2>The Udev Database</h2>
<p>Unit settings of device units may either be configured via unit files, or directly from the udev database. The following udev device properties are understood by the service manager: </p>
<p> <i>SYSTEMD_WANTS=</i>, <i>SYSTEMD_USER_WANTS=</i></p>
<dl>
<dd>Adds dependencies of type <i>Wants=</i> from the device unit to the specified units. <i>SYSTEMD_WANTS=</i> is read by the system service manager, <i>SYSTEMD_USER_WANTS=</i> by user service manager instances. These properties may be used to activate arbitrary units when a specific device becomes available. </p>
<p> Note that this and the other udev device properties are not taken into account unless the device is tagged with the &quot;systemd&quot; tag in the udev database, because otherwise the device is not exposed as a systemd unit (see above). </p>
<p> Note that systemd will only act on <i>Wants=</i> dependencies when a device first becomes active. It will not act on them if they are added to devices that are already active. Use <i>SYSTEMD_READY=</i> (see below) to configure when a udev device shall be considered active, and thus when to trigger the dependencies. </p>
<p> The specified property value should be a space-separated list of valid unit names. If a unit template name is specified (that is, a unit name containing an &quot;@&quot; character indicating a unit name to use for multiple instantiation, but with an empty instance name following the &quot;@&quot;), it will be automatically instantiated by the device&#8217;s &quot;sysfs&quot; path (that is: the path is escaped and inserted as instance name into the template unit name). This is useful in order to instantiate a specific template unit once for each device that appears and matches specific properties.</dl>
<p> <i>SYSTEMD_ALIAS=</i></p>
<dl>
<dd>Adds an additional alias name to the device unit. This must be an absolute path that is automatically transformed into a unit name. (See above.)</dl>
<p> <i>SYSTEMD_READY=</i></p>
<dl>
<dd>If set to 0, systemd will consider this device unplugged even if it shows up in the udev tree. If this property is unset or set to 1, the device will be considered plugged if it is visible in the udev tree. </p>
<p> This option is useful for devices that initially show up in an uninitialized state in the tree, and for which a &quot;changed&quot; event is generated the moment they are fully set up. Note that <i>SYSTEMD_WANTS=</i> (see above) is not acted on as long as <i>SYSTEMD_READY=0</i> is set for a device.</dl>
<p> <i>ID_MODEL_FROM_DATABASE=</i>, <i>ID_MODEL=</i></p>
<dl>
<dd>If set, this property is used as description string for the device unit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
