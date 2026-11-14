---
title: "driverctl(8)"
name: "driverctl"
section: "8"
letter: "d"
url: "/docs/linux/man/8-driverctl/"
description: "driverctl – Device driver control utility."
---

<p>driverctl &#8211; Device driver control utility.</p>
<h2>Synopsis</h2>
<p><code>driverctl</code> [OPTIONS] COMMAND [DEVICE [DRIVER]] </p>
<h2>Description</h2>
<p><code>driverctl</code> may be used to manipulate and inspect the system device driver choices. Devices are normally assigned to their sole designated kernel driver by default. However in some situations it may be desireable to override that default, for example to try an older driver to work around a regression in a driver or to try an experimental alternative driver. Another common use-case is pass-through drivers and driver stubs to allow userspace to drive the device, such as in case of virtualization. <code>driverctl</code> integrates with <code>udev</code> to support overriding driver selection for both cold- and hotplugged devices from the moment of discovery, but can also change already assigned drivers, assuming they are not in use by the system. The driver overrides created by <code>driverctl</code> are persistent across system reboots by default. </p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;bus &lt;BUS&gt;</code></p>
<dl>
<dd>Operate on devices on a given bus, such as <code>pci</code> or <code>usb</code>. Available options depend on system hardware. By default <code>pci</code> bus is used.</dl>
<p> <code>&#8211;debug|&#8211;verbose|-v</code></p>
<dl>
<dd>Verbose mode, output more detailed information during operation.</dl>
<p> <code>-h|&#8211;help</code></p>
<dl>
<dd>Output usage information.</dl>
<p> <code>&#8211;noprobe</code></p>
<dl>
<dd>Do not (re)probe the device after changing the driver. Applies to the <code>*-override</code> commands.</dl>
<p> <code>&#8211;nosave</code></p>
<dl>
<dd>Do not set/unset permanently. Applies to <code>set-override</code> and <code>unset-override</code> commands.</dl>
<h2>Commands</h2>
<p>The following commands are understood: </p>
<p> <code>set-override</code> &lt;DEVICE&gt; &lt;DRIVER&gt;</p>
<dl>
<dd>Set a driver override for a device. By default the current driver is unbound from the device, the new driver is loaded into kernel, bound and the override is saved permanently. </p>
<p> As a special case, specifying &quot;none&quot; as the driver will prevent any driver to be bound to the device until the override is removed.</dl>
<p> <code>unset-override</code> &lt;DEVICE&gt;</p>
<dl>
<dd>Unset a driver override for a device. By default the current driver is unbound from the device, the default driver of the device is bound and the override is permanently removed.</dl>
<p> <code>load-override</code> &lt;DEVICE&gt;</p>
<dl>
<dd>Load a previously set driver override for device from disk. There&#8217;s usually no need to invoke this manually, the command exists mostly for udev interaction.</dl>
<p> <code>list-devices</code></p>
<dl>
<dd>List currently plugged, overridable system devices on a bus (<code>pci</code> by default) along with their current drivers. Any overridden drivers are marked with <code>[*]</code>. With <code>-v</code> options, additional device description from udev database is shown to help identify devices.</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>Examples</h2>
<pre>Find devices currently driven by <code>ixgbe</code> driver:
# driverctl -v list-devices | grep ixgbe
0000:01:00.0 ixgbe (Ethernet 10G 4P X520/I350 rNDC)
0000:01:00.1 ixgbe (Ethernet 10G 4P X520/I350 rNDC)
Change them to use the <code>vfio-pci</code> driver:
# driverctl set-override 0000:01:00.0 vfio-pci
# driverctl set-override 0000:01:00.1 vfio-pci
Find devices with driver overrides:
[root [at] wsfd-netdev32 ~]# driverctl -v list-devices|grep \*
0000:01:00.0 vfio-pci [*] (Ethernet 10G 4P X520/I350 rNDC)
0000:01:00.1 vfio-pci [*] (Ethernet 10G 4P X520/I350 rNDC)
Remove the override from slot 0000:01:00.1:
# driverctl unset-override 0000:01:00.1</pre>
<h2>Files</h2>
<p><i>/etc/driverctl.d/*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) <code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8) <code><a href="/docs/linux/man/8-lsusb/">lsusb</a></code>(8) </p>
