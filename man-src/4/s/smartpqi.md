---
title: "smartpqi(4)"
name: "smartpqi"
section: "4"
letter: "s"
url: "/docs/linux/man/4-smartpqi/"
description: "smartpqi – Microsemi Smart Family SCSI driver"
---

<p>smartpqi &#8211; Microsemi Smart Family SCSI driver</p>
<h2>Synopsis</h2>
<p>[<code>disable_device_id_wildcards=</code>{<code>0</code>|<code>1</code>}] [<code>disable_heartbeat=</code>{<code>0</code>|<code>1</code>}] [<code>disable_ctrl_shutdown=</code>{<code>0</code>|<code>1</code>}] [<code>lockup_action=</code>{<code>none</code>|<code>reboot</code>|<code>panic</code>}] [<code>expose_ld_first=</code>{<code>0</code>|<code>1</code>}] [<code>hide_vsep=</code>{<code>0</code>|<code>1</code>}]</p>
<h2>Description</h2>
<p><code>smartpqi</code> is a SCSI driver for Microsemi Smart Family controllers.</p>
<h3>Supported ioctl/() operations</h3>
<p>For compatibility with applications written for the <code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4) and <code><a href="/docs/linux/man/4-hpsa/">hpsa</a></code>(4) drivers, many, but not all of the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations supported by the <code>hpsa</code> driver are also supported by the <code>smartpqi</code> driver. The data structures used by these operations are described in the Linux kernel source file <i>include/linux/cciss_ioctl.h</i>.</p>
<dl>
<dt><code>CCISS_DEREGDISK</code>, <code>CCISS_REGNEWDISK</code>, <code>CCISS_REGNEWD</code></p>
<dd>These operations all do exactly the same thing, which is to cause the driver to re-scan for new devices. This does exactly the same thing as writing to the <code>smartpqi</code>-specific host <i>rescan</i> attribute.</p>
<dt><code>CCISS_GETPCIINFO</code></p>
<dd>This operation Returns the PCI domain, bus, device and function and &quot;board ID&quot; (PCI subsystem ID).</p>
<dt><code>CCISS_GETDRIVVER</code></p>
<dd>This operation returns the driver version in four bytes, encoded as:</p>
<dd>(major_version &lt;&lt; 28) | (minor_version &lt;&lt; 24) |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(release&nbsp;&lt;&lt;&nbsp;16)&nbsp;| revision</p>
<dt><code>CCISS_PASSTHRU</code></p>
<dd>Allows BMIC and CISS commands to be passed through to the controller.</dl>
<h3>Boot options</h3>
<dl>
<dt><code>disable_device_id_wildcards=</code>{<code>0</code>|<code>1</code>}</p>
<dd>Disables support for device ID wildcards. The default value is 0.</p>
<dt><code>disable_heartbeat=</code>{<code>0</code>|<code>1</code>}</p>
<dd>Disables support for the controller&#8217;s heartbeat check. This parameter is used for debugging purposes. The default value is 0, leaving the controller&#8217;s heartbeat check active.</p>
<dt><code>disable_ctrl_shutdown=</code>{<code>0</code>|<code>1</code>}</p>
<dd>Disables support for shutting down the controller in the event of a controller lockup. The default value is 0.</p>
<dt><code>lockup_action=</code>{<code>none</code>|<code>reboot</code>|<code>panic</code>}</p>
<dd>Specifies the action the driver takes when a controller lockup is detected. The default action is <code>none</code>. </p>
<table>
<tr VALIGN=top>
<td>parameter</td>
<td>action
</td>
</tr>
<tr VALIGN=top>
<td><code>none</code></td>
</tr>
<tr VALIGN=top>
<td><code>reboot</code></td>
<td>reboot the system
</td>
</tr>
<tr VALIGN=top>
<td><code>panic</code></td>
<td>panic the system
</td>
</tr>
</table>
<dt><code>expose_ld_first=</code>{<code>0</code>|<code>1</code>}</p>
<dd>This option enables support for exposing logical devices to the operating system before physical devices. The default value is 0.</p>
<dt><code>hide_vsep=</code>{<code>0</code>|<code>1</code>}</p>
<dd>This option enables disabling exposure of the virtual SEP to the host. This is usually associated with direct attached drives. The default value is 0.</dl>
<h2>Files</h2>
<h3>Device nodes</h3>
<p>Logical drives are accessed via the SCSI disk driver (<i>sd</i>), tape drives via the SCSI tape driver (<i>st</i>), and the RAID controller via the SCSI generic driver (<i>sg</i>), with device nodes named <i>/dev/sd</i>*, <i>/dev/st</i>*, and <i>/dev/sg</i>*, respectively.</p>
<h3>SmartPQI-specific host attribute files in /sys</h3>
<dl>
<dt><i>/sys/class/scsi_host/host</i>*<i>/rescan</i></p>
<dd>The host <i>rescan</i> attribute is a write-only attribute. Writing to this attribute will cause the driver to scan for new, changed, or removed devices (e.g., hot-plugged tape drives, or newly configured or deleted logical drives) and notify the SCSI mid-layer of any changes detected. Usually this action is triggered automatically by configuration changes, so the user should not normally have to write to this file. Doing so may be useful when hot-plugging devices such as tape drives or entire storage boxes containing pre-configured logical drives.</p>
<dt><i>/sys/class/scsi_host/host</i>*<i>/version</i></p>
<dd>The host <i>version</i> attribute is a read-only attribute. This attribute contains the driver version and the controller firmware version.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_host/host1/version</code> driver: 1.1.2-126 firmware: 1.29-112</p>
<dt><i>/sys/class/scsi_host/host</i>*<i>/lockup_action</i></p>
<dd>The host <i>lockup_action</i> attribute is a read/write attribute. This attribute will cause the driver to perform a specific action in the unlikely event that a controller lockup has been detected. See <code>OPTIONS</code> above for an explanation of the <i>lockup_action</i> values.</p>
<dt><i>/sys/class/scsi_host/host*/driver_version</i></p>
<dd>The <i>driver_version</i> attribute is read-only. This attribute contains the smartpqi driver version.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_host/host1/driver_version</code> 1.1.2-126</p>
<dt><i>/sys/class/scsi_host/host*/firmware_version</i></p>
<dd>The <i>firmware_version</i> attribute is read-only. This attribute contains the controller firmware version.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_host/host1/firmware_version</code> 1.29-112</p>
<dt><i>/sys/class/scsi_host/host*/model</i></p>
<dd>The <i>model</i> attribute is read-only. This attribute contains the product identification string of the controller.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_host/host1/model</code> 1100-16i</p>
<dt><i>/sys/class/scsi_host/host*/serial_number</i></p>
<dd>The <i>serial_number</i> attribute is read-only. This attribute contains the unique identification number of the controller.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_host/host1/serial_number</code> 6A316373777</p>
<dt><i>/sys/class/scsi_host/host*/vendor</i></p>
<dd>The <i>vendor</i> attribute is read-only. This attribute contains the vendor identification string of the controller.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_host/host1/vendor</code> Adaptec</dl>
<h3>SmartPQI-specific disk attribute files in /sys</h3>
<p>In the file specifications below, <i>c</i> stands for the number of the appropriate SCSI controller, <i>b</i> is the bus number, <i>t</i> the target number, and <i>l</i> is the logical unit number (LUN).</p>
<dl>
<dt><i>/sys/class/scsi_disk/</i>c<i>:</i>b<i>:</i>t<i>:</i>l<i>/device/raid_level</i></p>
<dd>The <i>raid_level</i> attribute is read-only. This attribute contains the RAID level of each logical drive.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_disk/4:0:0:0/device/raid_level</code> RAID 0</p>
<dt><i>/sys/class/scsi_disk/c</i>:<i>b</i>:<i>t</i>:<i>l/device/sas_address</i></p>
<dd>The <i>sas_address</i> attribute is read-only. This attribute contains the unique identifier of the disk.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_disk/1:0:3:0/device/sas_address</code> 0x5001173d028543a2</p>
<dt><i>/sys/class/scsi_disk/c</i>:<i>b</i>:<i>t</i>:<i>l/device/ssd_smart_path_enabled</i></p>
<dd>The <i>ssd_smart_path_enabled</i> attribute is read-only. This attribute is for ioaccel-enabled volumes. (Ioaccel is an alternative driver submission path that allows the driver to send I/O requests directly to backend SCSI devices, bypassing the controller firmware. This results in an increase in performance. This method is used for HBA disks and for logical volumes comprised of SSDs.) Contains 1 if ioaccel is enabled for the volume and 0 otherwise.</p>
<dd>For example:</p>
<dd>$ <code>cat /sys/class/scsi_disk/1:0:3:0/device/ssd_smart_path_enabled</code> 0</dl>
<h2>Versions</h2>
<p>The <code>smartpqi</code> driver was added in Linux 4.9.</p>
<h2>Notes</h2>
<h3>Configuration</h3>
<p>To configure a Microsemi Smart Family controller, refer to the User Guide for the controller, which can be found by searching for the specific controller at</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4), <code><a href="/docs/linux/man/4-hpsa/">hpsa</a></code>(4), <code><a href="/docs/linux/man/4-sd/">sd</a></code>(4), <code><a href="/docs/linux/man/4-st/">st</a></code>(4) </p>
<p> <i>Documentation/ABI/testing/sysfs-bus-pci-devices-cciss</i> in the Linux kernel source tree.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
