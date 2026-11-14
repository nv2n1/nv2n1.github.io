---
title: "hpsa(4)"
name: "hpsa"
section: "4"
letter: "h"
url: "/docs/linux/man/4-hpsa/"
description: "hpsa – HP Smart Array SCSI driver"
---

<p>hpsa &#8211; HP Smart Array SCSI driver</p>
<h2>Synopsis</h2>
<pre>modprobe hpsa [ hpsa_allow_any=1 ]</pre>
<h2>Description</h2>
<p><code>hpsa</code> is a SCSI driver for HP Smart Array RAID controllers.</p>
<h3>Options</h3>
<p><i>hpsa_allow_any=1</i>: This option allows the driver to attempt to operate on any HP Smart Array hardware RAID controller, even if it is not explicitly known to the driver. This allows newer hardware to work with older drivers. Typically this is used to allow installation of operating systems from media that predates the RAID controller, though it may also be used to enable <code>hpsa</code> to drive older controllers that would normally be handled by the <code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4) driver. These older boards have not been tested and are not supported with <code>hpsa</code>, and <code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4) should still be used for these.</p>
<h3>Supported hardware</h3>
<p>The <code>hpsa</code> driver supports the following Smart Array boards: </p>
<pre> Smart Array P700M
 Smart Array P212
 Smart Array P410
 Smart Array P410i
 Smart Array P411
 Smart Array P812
 Smart Array P712m
 Smart Array P711m
 StorageWorks P1210m</pre>
<p>Since Linux 4.14, the following Smart Array boards are also supported: </p>
<pre> Smart Array 5300
 Smart Array 5312
 Smart Array 532
 Smart Array 5i
 Smart Array 6400
 Smart Array 6400 EM
 Smart Array 641
 Smart Array 642
 Smart Array 6i
 Smart Array E200
 Smart Array E200i
 Smart Array E200i
 Smart Array E200i
 Smart Array E200i
 Smart Array E500
 Smart Array P400
 Smart Array P400i
 Smart Array P600
 Smart Array P700m
 Smart Array P800</pre>
<h3>Configuration details</h3>
<p>To configure HP Smart Array controllers, use the HP Array Configuration Utility (either <code><a href="/docs/linux/man/8-hpacuxe/">hpacuxe</a></code>(8) or <code><a href="/docs/linux/man/8-hpacucli/">hpacucli</a></code>(8)) or the Offline ROM-based Configuration Utility (ORCA) run from the Smart Array&#8217;s option ROM at boot time.</p>
<h2>Files</h2>
<h3>Device nodes</h3>
<p>Logical drives are accessed via the SCSI disk driver (<code><a href="/docs/linux/man/4-sd/">sd</a></code>(4)), tape drives via the SCSI tape driver (<code><a href="/docs/linux/man/4-st/">st</a></code>(4)), and the RAID controller via the SCSI generic driver (<code><a href="/docs/linux/man/4-sg/">sg</a></code>(4)), with device nodes named <i>/dev/sd*</i>, <i>/dev/st*</i>, and <i>/dev/sg*</i>, respectively.</p>
<h3>HPSA-specific host attribute files in /sys</h3>
<dl>
<dt><i>/sys/class/scsi_host/host*/rescan</i></p>
<dd>This is a write-only attribute. Writing to this attribute will cause the driver to scan for new, changed, or removed devices (e.g., hot-plugged tape drives, or newly configured or deleted logical drives, etc.) and notify the SCSI midlayer of any changes detected. Normally a rescan is triggered automatically by HP&#8217;s Array Configuration Utility (either the GUI or the command-line variety); thus, for logical drive changes, the user should not normally have to use this attribute. This attribute may be useful when hot plugging devices like tape drives, or entire storage boxes containing preconfigured logical drives.</p>
<dt><i>/sys/class/scsi_host/host*/firmware_revision</i></p>
<dd>This attribute contains the firmware version of the Smart Array.</p>
<dd>For example:</p>
<dd># <code>cd /sys/class/scsi_host/host4</code> # <code>cat firmware_revision</code> 7.14</dl>
<h3>HPSA-specific disk attribute files in /sys</h3>
<dl>
<dt><i>/sys/class/scsi_disk/c:b:t:l/device/unique_id</i></p>
<dd>This attribute contains a 32 hex-digit unique ID for each logical drive.</p>
<dd>For example:</p>
<dd># <code>cd /sys/class/scsi_disk/4:0:0:0/device</code> # <code>cat unique_id</code> 600508B1001044395355323037570F77</p>
<dt><i>/sys/class/scsi_disk/c:b:t:l/device/raid_level</i></p>
<dd>This attribute contains the RAID level of each logical drive.</p>
<dd>For example:</p>
<dd># <code>cd /sys/class/scsi_disk/4:0:0:0/device</code> # <code>cat raid_level</code> RAID 0</p>
<dt><i>/sys/class/scsi_disk/c:b:t:l/device/lunid</i></p>
<dd>This attribute contains the 16 hex-digit (8 byte) LUN ID by which a logical drive or physical device can be addressed. <i>c</i>:<i>b</i>:<i>t</i>:<i>l</i> are the controller, bus, target, and lun of the device.</dl>
<p> For example:</p>
<dl>
<dd># <code>cd /sys/class/scsi_disk/4:0:0:0/device</code> # <code>cat lunid</code> 0x0000004000000000</dl>
<h3>Supported ioctl() operations</h3>
<p>For compatibility with applications written for the <code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4) driver, many, but not all of the ioctls supported by the <code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4) driver are also supported by the <code>hpsa</code> driver. The data structures used by these ioctls are described in the Linux kernel source file <i>include/linux/cciss_ioctl.h</i>.</p>
<dl>
<dt><code>CCISS_DEREGDISK</code>, <code>CCISS_REGNEWDISK</code>, <code>CCISS_REGNEWD</code></p>
<dd>These three ioctls all do exactly the same thing, which is to cause the driver to rescan for new devices. This does exactly the same thing as writing to the hpsa-specific host &quot;rescan&quot; attribute.</p>
<dt><code>CCISS_GETPCIINFO</code></p>
<dd>Returns PCI domain, bus, device and function and &quot;board ID&quot; (PCI subsystem ID).</p>
<dt><code>CCISS_GETDRIVVER</code></p>
<dd>Returns driver version in three bytes encoded as:</p>
<dd>(major_version &lt;&lt; 16) | (minor_version &lt;&lt; 8) |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(subminor_version)</p>
<dt><code>CCISS_PASSTHRU</code>, <code>CCISS_BIG_PASSTHRU</code></p>
<dd>Allows &quot;BMIC&quot; and &quot;CISS&quot; commands to be passed through to the Smart Array. These are used extensively by the HP Array Configuration Utility, SNMP storage agents, and so on. See <i>cciss_vol_status</i> at for some examples.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4), <code><a href="/docs/linux/man/4-sd/">sd</a></code>(4), <code><a href="/docs/linux/man/4-st/">st</a></code>(4), <code><a href="/docs/linux/man/8-cciss_vol_status/">cciss_vol_status</a></code>(8), <code><a href="/docs/linux/man/8-hpacucli/">hpacucli</a></code>(8), <code><a href="/docs/linux/man/8-hpacuxe/">hpacuxe</a></code>(8), </p>
<p> and <i>Documentation/scsi/hpsa.txt</i> and <i>Documentation/ABI/testing/sysfs-bus-pci-devices-cciss</i> in the Linux kernel source tree</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
