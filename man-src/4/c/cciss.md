---
title: "cciss(4)"
name: "cciss"
section: "4"
letter: "c"
url: "/docs/linux/man/4-cciss/"
description: "cciss – HP Smart Array block driver"
---

<p>cciss &#8211; HP Smart Array block driver</p>
<h2>Synopsis</h2>
<pre>modprobe cciss [ cciss_allow_hpsa=1 ]</pre>
<h2>Description</h2>
<p><code>Note</code>: This obsolete driver was removed from the kernel in version 4.14, as it is superseded by the <code><a href="/docs/linux/man/4-hpsa/">hpsa</a></code>(4) driver in newer kernels. </p>
<p> <code>cciss</code> is a block driver for older HP Smart Array RAID controllers.</p>
<h3>Options</h3>
<p><i>cciss_allow_hpsa=1</i>: This option prevents the <code>cciss</code> driver from attempting to drive any controllers that the <code><a href="/docs/linux/man/4-hpsa/">hpsa</a></code>(4) driver is capable of controlling, which is to say, the <code>cciss</code> driver is restricted by this option to the following controllers: </p>
<pre> Smart Array 5300
 Smart Array 5i
 Smart Array 532
 Smart Array 5312
 Smart Array 641
 Smart Array 642
 Smart Array 6400
 Smart Array 6400 EM
 Smart Array 6i
 Smart Array P600
 Smart Array P400i
 Smart Array E200i
 Smart Array E200
 Smart Array E200i
 Smart Array E200i
 Smart Array E200i
 Smart Array E500</pre>
<h3>Supported hardware</h3>
<p>The <code>cciss</code> driver supports the following Smart Array boards: </p>
<pre> Smart Array 5300
 Smart Array 5i
 Smart Array 532
 Smart Array 5312
 Smart Array 641
 Smart Array 642
 Smart Array 6400
 Smart Array 6400 U320 Expansion Module
 Smart Array 6i
 Smart Array P600
 Smart Array P800
 Smart Array E400
 Smart Array P400i
 Smart Array E200
 Smart Array E200i
 Smart Array E500
 Smart Array P700m
 Smart Array P212
 Smart Array P410
 Smart Array P410i
 Smart Array P411
 Smart Array P812
 Smart Array P712m
 Smart Array P711m</pre>
<h3>Configuration details</h3>
<p>To configure HP Smart Array controllers, use the HP Array Configuration Utility (either <code><a href="/docs/linux/man/8-hpacuxe/">hpacuxe</a></code>(8) or <code><a href="/docs/linux/man/8-hpacucli/">hpacucli</a></code>(8)) or the Offline ROM-based Configuration Utility (ORCA) run from the Smart Array&#8217;s option ROM at boot time.</p>
<h2>Files</h2>
<h3>Device nodes</h3>
<p>The device naming scheme is as follows: </p>
<p> Major numbers: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;104&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;105&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;106&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;105&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;108&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;109&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss5<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;110&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss6<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;111&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cciss7 </p>
<p> Minor numbers: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;b7 b6 b5 b4 b3 b2 b1 b0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&#8212;-+&#8212;-| |&#8212;-+&#8212;-|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+&#8212;&#8212;&#8211; Partition ID&nbsp;(0=wholedev, 1-15 partition)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; Logical Volume number </p>
<p> The device naming scheme is: </p>
<table>
<tr VALIGN=top>
<td><i>/dev/cciss/c0d0</i></td>
<td>Controller 0, disk 0, whole device
</td>
</tr>
<tr VALIGN=top>
<td><i>/dev/cciss/c0d0p1</i></td>
<td>Controller 0, disk 0, partition 1
</td>
</tr>
<tr VALIGN=top>
<td><i>/dev/cciss/c0d0p2</i></td>
<td>Controller 0, disk 0, partition 2
</td>
</tr>
<tr VALIGN=top>
<td><i>/dev/cciss/c0d0p3</i></td>
<td>Controller 0, disk 0, partition 3
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>/dev/cciss/c1d1</i></td>
<td>Controller 1, disk 1, whole device
</td>
</tr>
<tr VALIGN=top>
<td><i>/dev/cciss/c1d1p1</i></td>
<td>Controller 1, disk 1, partition 1
</td>
</tr>
<tr VALIGN=top>
<td><i>/dev/cciss/c1d1p2</i></td>
<td>Controller 1, disk 1, partition 2
</td>
</tr>
<tr VALIGN=top>
<td><i>/dev/cciss/c1d1p3</i></td>
<td>Controller 1, disk 1, partition 3
</td>
</tr>
</table>
<h3>Files in /proc</h3>
<p>The files <i>/proc/driver/cciss/cciss[0-9]+</i> contain information about the configuration of each controller. For example: </p>
<p> $ <code>cd /proc/driver/cciss</code> $ <code>ls -l</code> total 0 -rw-r&#8211;r&#8211; 1 root root 0 2010-09-10 10:38 cciss0 -rw-r&#8211;r&#8211; 1 root root 0 2010-09-10 10:38 cciss1 -rw-r&#8211;r&#8211; 1 root root 0 2010-09-10 10:38 cciss2 $ <code>cat cciss2</code> cciss2: HP Smart Array P800 Controller Board ID: 0x3223103c Firmware Version: 7.14 IRQ: 16 Logical drives: 1 Current Q depth: 0 Current # commands on controller: 0 Max Q depth since init: 1 Max # commands on controller since init: 2 Max SG entries since init: 32 Sequential access devices: 0 </p>
<p> cciss/c2d0: 36.38GB RAID 0</p>
<h3>Files in /sys</h3>
<dl>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/model</i></p>
<dd>Displays the SCSI INQUIRY page 0 model for logical drive <i>Y</i> of controller <i>X</i>.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/rev</i></p>
<dd>Displays the SCSI INQUIRY page 0 revision for logical drive <i>Y</i> of controller <i>X</i>.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/unique_id</i></p>
<dd>Displays the SCSI INQUIRY page 83 serial number for logical drive <i>Y</i> of controller <i>X</i>.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/vendor</i></p>
<dd>Displays the SCSI INQUIRY page 0 vendor for logical drive <i>Y</i> of controller <i>X</i>.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/block:cciss!cXdY</i></p>
<dd>A symbolic link to <i>/sys/block/cciss!cXdY</i>.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/rescan</i></p>
<dd>When this file is written to, the driver rescans the controller to discover any new, removed, or modified logical drives.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/resettable</i></p>
<dd>A value of 1 displayed in this file indicates that the &quot;reset_devices=1&quot; kernel parameter (used by <code>kdump</code>) is honored by this controller. A value of 0 indicates that the &quot;reset_devices=1&quot; kernel parameter will not be honored. Some models of Smart Array are not able to honor this parameter.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/lunid</i></p>
<dd>Displays the 8-byte LUN ID used to address logical drive <i>Y</i> of controller <i>X</i>.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/raid_level</i></p>
<dd>Displays the RAID level of logical drive <i>Y</i> of controller <i>X</i>.</p>
<dt><i>/sys/bus/pci/devices/&lt;dev&gt;/ccissX/cXdY/usage_count</i></p>
<dd>Displays the usage count (number of opens) of logical drive <i>Y</i> of controller <i>X</i>.</dl>
<h3>SCSI tape drive and medium changer support</h3>
<p>SCSI sequential access devices and medium changer devices are supported and appropriate device nodes are automatically created (e.g., <i>/dev/st0</i>, <i>/dev/st1</i>, etc.; see <code><a href="/docs/linux/man/4-st/">st</a></code>(4) for more details.) You must enable &quot;SCSI tape drive support for Smart Array 5xxx&quot; and &quot;SCSI support&quot; in your kernel configuration to be able to use SCSI tape drives with your Smart Array 5xxx controller. </p>
<p> Additionally, note that the driver will not engage the SCSI core at init time. The driver must be directed to dynamically engage the SCSI core via the <i>/proc</i> filesystem entry, which the &quot;block&quot; side of the driver creates as <i>/proc/driver/cciss/cciss*</i> at run time. This is because at driver init time, the SCSI core may not yet be initialized (because the driver is a block driver) and attempting to register it with the SCSI core in such a case would cause a hang. This is best done via an initialization script (typically in <i>/etc/init.d</i>, but could vary depending on distribution). For example: </p>
<p> for x in /proc/driver/cciss/cciss[0-9]* do<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;echo&nbsp;&quot;engage scsi&quot;&nbsp;&gt;&nbsp;$x done </p>
<p> Once the SCSI core is engaged by the driver, it cannot be disengaged (except by unloading the driver, if it happens to be linked as a module.) </p>
<p> Note also that if no sequential access devices or medium changers are detected, the SCSI core will not be engaged by the action of the above script.</p>
<h3>Hot plug support for SCSI tape drives</h3>
<p>Hot plugging of SCSI tape drives is supported, with some caveats. The <code>cciss</code> driver must be informed that changes to the SCSI bus have been made. This may be done via the <i>/proc</i> filesystem. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;echo&nbsp;&quot;rescan&quot;&nbsp;&gt;&nbsp;/proc/scsi/cciss0/1 </p>
<p> This causes the driver to:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>query the adapter about changes to the physical SCSI buses and/or fiber channel arbitrated loop, and</p>
<dt>2.</p>
<dd>make note of any new or removed sequential access devices or medium changers.</dl>
</dl>
<p> The driver will output messages indicating which devices have been added or removed and the controller, bus, target, and lun used to address each device. The driver then notifies the SCSI midlayer of these changes. </p>
<p> Note that the naming convention of the <i>/proc</i> filesystem entries contains a number in addition to the driver name (e.g., &quot;cciss0&quot; instead of just &quot;cciss&quot;, which you might expect). </p>
<p> Note: <i>Only</i> sequential access devices and medium changers are presented as SCSI devices to the SCSI midlayer by the <code>cciss</code> driver. Specifically, physical SCSI disk drives are <i>not</i> presented to the SCSI midlayer. The only disk devices that are presented to the kernel are logical drives that the array controller constructs from regions on the physical drives. The logical drives are presented to the block layer (not to the SCSI midlayer). It is important for the driver to prevent the kernel from accessing the physical drives directly, since these drives are used by the array controller to construct the logical drives.</p>
<h3>SCSI error handling for tape drives and medium changers</h3>
<p>The Linux SCSI midlayer provides an error-handling protocol that is initiated whenever a SCSI command fails to complete within a certain amount of time (which can vary depending on the command). The <code>cciss</code> driver participates in this protocol to some extent. The normal protocol is a four-step process:</p>
<dl>
<dt>*</p>
<dd>First, the device is told to abort the command.</p>
<dt>*</p>
<dd>If that doesn&#8217;t work, the device is reset.</p>
<dt>*</p>
<dd>If that doesn&#8217;t work, the SCSI bus is reset.</p>
<dt>*</p>
<dd>If that doesn&#8217;t work, the host bus adapter is reset.</dl>
<p> The <code>cciss</code> driver is a block driver as well as a SCSI driver and only the tape drives and medium changers are presented to the SCSI midlayer. Furthermore, unlike more straightforward SCSI drivers, disk I/O continues through the block side during the SCSI error-recovery process. Therefore, the <code>cciss</code> driver implements only the first two of these actions, aborting the command, and resetting the device. Note also that most tape drives will not oblige in aborting commands, and sometimes it appears they will not even obey a reset command, though in most circumstances they will. If the command cannot be aborted and the device cannot be reset, the device will be set offline. </p>
<p> In the event that the error-handling code is triggered and a tape drive is successfully reset or the tardy command is successfully aborted, the tape drive may still not allow I/O to continue until some command is issued that positions the tape to a known position. Typically you must rewind the tape (by issuing <i>mt -f /dev/st0 rewind</i> for example) before I/O can proceed again to a tape drive that was reset.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-hpsa/">hpsa</a></code>(4), <code><a href="/docs/linux/man/8-cciss_vol_status/">cciss_vol_status</a></code>(8), <code><a href="/docs/linux/man/8-hpacucli/">hpacucli</a></code>(8), <code><a href="/docs/linux/man/8-hpacuxe/">hpacuxe</a></code>(8) </p>
<p> and <i>Documentation/blockdev/cciss.txt</i> and <i>Documentation/ABI/testing/sysfs-bus-pci-devices-cciss</i> in the Linux kernel source tree</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
