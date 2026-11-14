---
title: "vgchange(8)"
name: "vgchange"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vgchange/"
description: "vgchange – Change volume group attributes"
---

<p>vgchange &#8211; Change volume group attributes</p>
<h2>Synopsis</h2>
<p><code>vgchange</code> <i>option_args</i> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>position_args</i>&nbsp;] </p>
<p>&nbsp;<code>-a</code>|<code>&#8211;activate</code>&nbsp;<code>y</code>|<code>n</code>|<code>ay</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;activationmode</code>&nbsp;<code>partial</code>|<code>degraded</code>|<code>complete</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;addtag</code>&nbsp;<i>Tag</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;alloc</code>&nbsp;<code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> </p>
<p>&nbsp;<code>-A</code>|<code>&#8211;autobackup</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;commandprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;config</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-d</code>|<code>&#8211;debug</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deltag</code>&nbsp;<i>Tag</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;detachprofile</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;driverloaded</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-f</code>|<code>&#8211;force</code> </p>
<p>&nbsp;<code>-h</code>|<code>&#8211;help</code> </p>
<p>&nbsp;<code>-K</code>|<code>&#8211;ignoreactivationskip</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;ignorelockingfailure</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;ignoremonitoring</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockopt</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockstart</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockstop</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;locktype</code>&nbsp;<code>sanlock</code>|<code>dlm</code>|<code>none</code> </p>
<p>&nbsp;<code>-l</code>|<code>&#8211;logicalvolume</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;longhelp</code> </p>
<p>&nbsp;<code>-p</code>|<code>&#8211;maxphysicalvolumes</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;metadataprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;monitor</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nolocking</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;noudevsync</code> </p>
<p>&nbsp;<code>-P</code>|<code>&#8211;partial</code> </p>
<p>&nbsp;<code>-s</code>|<code>&#8211;physicalextentsize</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poll</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;pvmetadatacopies</code>&nbsp;<code>0</code>|<code>1</code>|<code>2</code> </p>
<p>&nbsp;<code>-q</code>|<code>&#8211;quiet</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;readonly</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;refresh</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;reportformat</code>&nbsp;<code>basic</code>|<code>json</code> </p>
<p>&nbsp;<code>-x</code>|<code>&#8211;resizeable</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-S</code>|<code>&#8211;select</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;sysinit</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;systemid</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-t</code>|<code>&#8211;test</code> </p>
<p>&nbsp;<code>-u</code>|<code>&#8211;uuid</code> </p>
<p>&nbsp;<code>-v</code>|<code>&#8211;verbose</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;version</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[vg]metadatacopies</code>&nbsp;<code>all</code>|<code>unmanaged</code>|<i>Number</i> </p>
<p>&nbsp;<code>-y</code>|<code>&#8211;yes</code></p>
<h2>Description</h2>
<p>vgchange changes VG attributes, changes LV activation in the kernel, and includes other utilities for VG maintenance.</p>
<h2>Usage</h2>
<p>Change a general VG attribute.<br />
 For options listed in parentheses, any one is<br />
 required, after which the others are optional. </p>
<p> <code>vgchange</code></p>
<dl>
<dd>( <code>-l</code>|<code>&#8211;logicalvolume</code> <i>Number</i>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-p</code>|<code>&#8211;maxphysicalvolumes</code>&nbsp;<i>Number</i>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-u</code>|<code>&#8211;uuid</code>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-s</code>|<code>&#8211;physicalextentsize</code>&nbsp;<i>Size</i>[m|UNIT], </p>
<p>&nbsp;<wbr>&nbsp;<code>-x</code>|<code>&#8211;resizeable</code>&nbsp;<code>y</code>|<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;addtag</code>&nbsp;<i>Tag</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deltag</code>&nbsp;<i>Tag</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;alloc</code>&nbsp;<code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;pvmetadatacopies</code>&nbsp;<code>0</code>|<code>1</code>|<code>2</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[vg]metadatacopies</code>&nbsp;<code>all</code>|<code>unmanaged</code>|<i>Number</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;detachprofile</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;metadataprofile</code>&nbsp;<i>String</i>&nbsp;)</dl>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;ignoremonitoring</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i>|<i>Select</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Start or stop monitoring LVs from dmeventd. </p>
<p> <code>vgchange</code> <code>&#8211;monitor</code> <code>y</code>|<code>n</code> </p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>&#8211;sysinit</code> ]<br />
 [ <code>&#8211;ignorelockingfailure</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;ignoremonitoring</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i>|<i>Select</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Start or stop processing LV conversions. </p>
<p> <code>vgchange</code> <code>&#8211;poll</code> <code>y</code>|<code>n</code> </p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>&#8211;ignorelockingfailure</code> ]<br />
 [ <code>&#8211;ignoremonitoring</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i>|<i>Select</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Activate or deactivate LVs. </p>
<p> <code>vgchange</code> <code>-a</code>|<code>&#8211;activate</code> <code>y</code>|<code>n</code>|<code>ay</code> </p>
<dl>
<dd>[ <code>-K</code>|<code>&#8211;ignoreactivationskip</code> ]<br />
 [ <code>-P</code>|<code>&#8211;partial</code> ]<br />
 [ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>&#8211;activationmode</code> <code>partial</code>|<code>degraded</code>|<code>complete</code> ]<br />
 [ <code>&#8211;sysinit</code> ]<br />
 [ <code>&#8211;readonly</code> ]<br />
 [ <code>&#8211;ignorelockingfailure</code> ]<br />
 [ <code>&#8211;monitor</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;ignoremonitoring</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i>|<i>Select</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Reactivate LVs using the latest metadata. </p>
<p> <code>vgchange</code> <code>&#8211;refresh</code> </p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>&#8211;sysinit</code> ]<br />
 [ <code>&#8211;ignorelockingfailure</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;ignoremonitoring</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i>|<i>Select</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Change the system ID of a VG. </p>
<p> <code>vgchange</code> <code>&#8211;systemid</code> <i>String</i> <i>VG</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Start the lockspace of a shared VG in lvmlockd. </p>
<p> <code>vgchange</code> <code>&#8211;lockstart</code> </p>
<dl>
<dd>[ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i>|<i>Select</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Stop the lockspace of a shared VG in lvmlockd. </p>
<p> <code>vgchange</code> <code>&#8211;lockstop</code> </p>
<dl>
<dd>[ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i>|<i>Select</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Change the lock type for a shared VG. </p>
<p> <code>vgchange</code> <code>&#8211;locktype</code> <code>sanlock</code>|<code>dlm</code>|<code>none</code> <i>VG</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Common options for command:</p>
<dl>
<dd></dl>
<p> Common options for lvm:</p>
<dl>
<dd>[ <code>-d</code>|<code>&#8211;debug</code> ]<br />
 [ <code>-h</code>|<code>&#8211;help</code> ]<br />
 [ <code>-q</code>|<code>&#8211;quiet</code> ]<br />
 [ <code>-t</code>|<code>&#8211;test</code> ]<br />
 [ <code>-v</code>|<code>&#8211;verbose</code> ]<br />
 [ <code>-y</code>|<code>&#8211;yes</code> ]<br />
 [ <code>&#8211;commandprofile</code> <i>String</i> ]<br />
 [ <code>&#8211;config</code> <i>String</i> ]<br />
 [ <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;lockopt</code> <i>String</i> ]<br />
 [ <code>&#8211;longhelp</code> ]<br />
 [ <code>&#8211;nolocking</code> ]<br />
 [ <code>&#8211;profile</code> <i>String</i> ]<br />
 [ <code>&#8211;version</code> ]</dl>
<h2>Options</h2>
<dl>
<dt> <code>-a</code>|<code>&#8211;activate</code> <code>y</code>|<code>n</code>|<code>ay</code></p>
<dd>
<dd>Change the active state of LVs. An active LV can be used through a block device, allowing data on the LV to be accessed. <code>y</code> makes LVs active, or available. <code>n</code> makes LVs inactive, or unavailable. The block device for the LV is added or removed from the system using device-mapper in the kernel. A symbolic link /dev/VGName/LVName pointing to the device node is also added/removed. All software and scripts should access the device through the symbolic link and present this as the name of the device. The location and name of the underlying device node may depend on the distribution, configuration (e.g. udev), or release version. <code>ay</code> specifies autoactivation, in which case an LV is activated only if it matches an item in lvm.conf activation/auto_activation_volume_list. If the list is not set, all LVs are considered to match, and if if the list is set but empty, no LVs match. Autoactivation should be used during system boot to make it possible to select which LVs should be automatically activated by the system. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information about activation options <code>ey</code> and <code>sy</code> for shared VGs.</p>
<dt> <code>&#8211;activationmode</code> <code>partial</code>|<code>degraded</code>|<code>complete</code></p>
<dd>
<dd>Determines if LV activation is allowed when PVs are missing, e.g. because of a device failure. <code>complete</code> only allows LVs with no missing PVs to be activated, and is the most restrictive mode. <code>degraded</code> allows RAID LVs with missing PVs to be activated. (This does not include the &quot;mirror&quot; type, see &quot;raid1&quot; instead.) <code>partial</code> allows any LV with missing PVs to be activated, and should only be used for recovery or repair. For default, see lvm.conf/activation_mode. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
<dt> <code>&#8211;addtag</code> <i>Tag</i></p>
<dd>
<dd>Adds a tag to a PV, VG or LV. This option can be repeated to add multiple tags at once. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tags.</p>
<dt> <code>&#8211;alloc</code> <code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code></p>
<dd>
<dd>Determines the allocation policy when a command needs to allocate Physical Extents (PEs) from the VG. Each VG and LV has an allocation policy which can be changed with vgchange/lvchange, or overriden on the command line. <code>normal</code> applies common sense rules such as not placing parallel stripes on the same PV. <code>inherit</code> applies the VG policy to an LV. <code>contiguous</code> requires new PEs be placed adjacent to existing PEs. <code>cling</code> places new PEs on the same PV as existing PEs in the same stripe of the LV. If there are sufficient PEs for an allocation, but normal does not use them, <code>anywhere</code> will use them even if it reduces performance, e.g. by placing two stripes on the same PV. Optional positional PV args on the command line can also be used to limit which PVs the command will use for allocation. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for more information about allocation.</p>
<dt> <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Specifies if metadata should be backed up automatically after a change. Enabling this is strongly advised! See <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) for more information.</p>
<dt> <code>&#8211;commandprofile</code> <i>String</i></p>
<dd>
<dd>The command profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;config</code> <i>String</i></p>
<dd>
<dd>Config settings for the command. These override lvm.conf settings. The String arg uses the same format as lvm.conf, or may use section/field syntax. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about config.</p>
<dt> <code>-d</code>|<code>&#8211;debug</code> &#8230;</p>
<dd>
<dd>Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).</p>
<dt> <code>&#8211;deltag</code> <i>Tag</i></p>
<dd>
<dd>Deletes a tag from a PV, VG or LV. This option can be repeated to delete multiple tags at once. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tags.</p>
<dt> <code>&#8211;detachprofile</code></p>
<dd>
<dd>Detaches a metadata profile from a VG or LV. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>If set to no, the command will not attempt to use device-mapper. For testing and debugging.</p>
<dt> <code>-f</code>|<code>&#8211;force</code> &#8230;</p>
<dd>
<dd>Override various checks, confirmations and protections. Use with extreme caution.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display help text.</p>
<dt> <code>-K</code>|<code>&#8211;ignoreactivationskip</code></p>
<dd>
<dd>Ignore the &quot;activation skip&quot; LV flag during activation to allow LVs with the flag set to be activated.</p>
<dt> <code>&#8211;ignorelockingfailure</code></p>
<dd>
<dd>Allows a command to continue with read-only metadata operations after locking failures.</p>
<dt> <code>&#8211;ignoremonitoring</code></p>
<dd>
<dd>Do not interact with dmeventd unless &#8211;monitor is specified. Do not use this if dmeventd is already monitoring a device.</p>
<dt> <code>&#8211;lockopt</code> <i>String</i></p>
<dd>
<dd>Used to pass options for special cases to lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;lockstart</code></p>
<dd>
<dd>Start the lockspace of a shared VG in lvmlockd. lvmlockd locks becomes available for the VG, allowing LVM to use the VG. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;lockstop</code></p>
<dd>
<dd>Stop the lockspace of a shared VG in lvmlockd. lvmlockd locks become unavailable for the VG, preventing LVM from using the VG. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;locktype</code> <code>sanlock</code>|<code>dlm</code>|<code>none</code></p>
<dd>
<dd>Change the VG lock type to or from a shared lock type used with lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>-l</code>|<code>&#8211;logicalvolume</code> <i>Number</i></p>
<dd>
<dd>Sets the maximum number of LVs allowed in a VG.</p>
<dt> <code>&#8211;longhelp</code></p>
<dd>
<dd>Display long help text.</p>
<dt> <code>-p</code>|<code>&#8211;maxphysicalvolumes</code> <i>Number</i></p>
<dd>
<dd>Sets the maximum number of PVs that can belong to the VG. The value 0 removes any limitation. For large numbers of PVs, also see options &#8211;pvmetadatacopies, and &#8211;vgmetadatacopies for improving performance.</p>
<dt> <code>&#8211;metadataprofile</code> <i>String</i></p>
<dd>
<dd>The metadata profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;monitor</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Start (yes) or stop (no) monitoring an LV with dmeventd. dmeventd monitors kernel events for an LV, and performs automated maintenance for the LV in reponse to specific events. See <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) for more information.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;noudevsync</code></p>
<dd>
<dd>Disables udev synchronisation. The process will not wait for notification from udev. It will continue irrespective of any possible udev processing in the background. Only use this if udev is not running or has rules that ignore the devices LVM creates.</p>
<dt> <code>-P</code>|<code>&#8211;partial</code></p>
<dd>
<dd>Commands will do their best to activate LVs with missing PV extents. Missing extents may be replaced with error or zero segments according to the lvm.conf missing_stripe_filler setting. Metadata may not be changed with this option.</p>
<dt> <code>-s</code>|<code>&#8211;physicalextentsize</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>Sets the physical extent size of PVs in the VG. The value must be either a power of 2 of at least 1 sector (where the sector size is the largest sector size of the PVs currently used in the VG), or at least 128KiB. Once this value has been set, it is difficult to change without recreating the VG, unless no extents need moving. Before increasing the physical extent size, you might need to use lvresize, pvresize and/or pvmove so that everything fits. For example, every contiguous range of extents used in a LV must start and end on an extent boundary.</p>
<dt> <code>&#8211;poll</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>When yes, start the background transformation of an LV. An incomplete transformation, e.g. pvmove or lvconvert interrupted by reboot or crash, can be restarted from the last checkpoint with &#8211;poll y. When no, background transformation of an LV will not occur, and the transformation will not complete. It may not be appropriate to immediately poll an LV after activation, in which case &#8211;poll n can be used to defer polling until a later &#8211;poll y command.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>&#8211;pvmetadatacopies</code> <code>0</code>|<code>1</code>|<code>2</code></p>
<dd>
<dd>The number of metadata areas to set aside on a PV for storing VG metadata. When 2, one copy of the VG metadata is stored at the front of the PV and a second copy is stored at the end. When 1, one copy of the VG metadata is stored at the front of the PV. When 0, no copies of the VG metadata are stored on the given PV. This may be useful in VGs containing many PVs (this places limitations on the ability to use vgsplit later.)</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;readonly</code></p>
<dd>
<dd>Run the command in a special read-only mode which will read on-disk metadata without needing to take any locks. This can be used to peek inside metadata used by a virtual machine image while the virtual machine is running. No attempt will be made to communicate with the device-mapper kernel driver, so this option is unable to report whether or not LVs are actually in use.</p>
<dt> <code>&#8211;refresh</code></p>
<dd>
<dd>If the LV is active, reload its metadata. This is not necessary in normal operation, but may be useful if something has gone wrong, or if some form of manual LV sharing is being used.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
<dt> <code>-x</code>|<code>&#8211;resizeable</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Enables or disables the addition or removal of PVs to/from a VG (by vgextend/vgreduce).</p>
<dt> <code>-S</code>|<code>&#8211;select</code> <i>String</i></p>
<dd>
<dd>Select objects for processing and reporting based on specified criteria. The criteria syntax is described by <code>&#8211;select help</code> and <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7). For reporting commands, one row is displayed for each object matching the criteria. See <code>&#8211;options help</code> for selectable object fields. Rows can be displayed with an additional &quot;selected&quot; field (-o selected) showing 1 if the row matches the selection and 0 otherwise. For non-reporting commands which process LVM entities, the selection is used to choose items to process.</p>
<dt> <code>&#8211;sysinit</code></p>
<dd>
<dd>Indicates that vgchange/lvchange is being invoked from early system initialisation scripts (e.g. rc.sysinit or an initrd), before writable filesystems are available. As such, some functionality needs to be disabled and this option acts as a shortcut which selects an appropriate set of options. Currently, this is equivalent to using &#8211;ignorelockingfailure, &#8211;ignoremonitoring, &#8211;poll n, and setting env var LVM_SUPPRESS_LOCKING_FAILURE_MESSAGES. vgchange/lvchange skip autoactivation, and defer to pvscan autoactivation.</p>
<dt> <code>&#8211;systemid</code> <i>String</i></p>
<dd>
<dd>Changes the system ID of the VG. Using this option requires caution because the VG may become foreign to the host running the command, leaving the host unable to access it. See <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) for more information.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>-u</code>|<code>&#8211;uuid</code></p>
<dd>
<dd>Generate new random UUID for specified VGs.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code> &#8230;</p>
<dd>
<dd>Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.</p>
<dt> <code>&#8211;version</code></p>
<dd>
<dd>Display version information.</p>
<dt> <code>&#8211;[vg]metadatacopies</code> <code>all</code>|<code>unmanaged</code>|<i>Number</i></p>
<dd>
<dd>Number of copies of the VG metadata that are kept. VG metadata is kept in VG metadata areas on PVs in the VG, i.e. reserved space at the start and/or end of the PVs. Keeping a copy of the VG metadata on every PV can reduce performance in VGs containing a large number of PVs. When this number is set to a non-zero value, LVM will automatically choose PVs on which to store metadata, using the metadataignore flags on PVs to achieve the specified number. The number can also be replaced with special string values: <code>unmanaged</code> causes LVM to not automatically manage the PV metadataignore flags. <code>all</code> causes LVM to first clear the metadataignore flags on all PVs, and then to become unmanaged.</p>
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</dl>
<h2>Variables</h2>
<dl>
<dt> <i>VG</i></p>
<dd>
<dd>Volume Group name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names.</p>
<dt> <i>Tag</i></p>
<dd>
<dd>Tag name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tag names and using tags in place of a VG, LV or PV.</p>
<dt> <i>Select</i></p>
<dd>
<dd>Select indicates that a required positional parameter can be omitted if the <code>&#8211;select</code> option is used. No arg appears in this position.</p>
<dt> <i>String</i></p>
<dd>
<dd>See the option description for information about the string content.</p>
<dt> <i>Size</i>[UNIT]</p>
<dd>
<dd>Size is an input number that accepts an optional unit. Input units are always treated as base two values, regardless of capitalization, e.g. &#8216;k&#8217; and &#8216;K&#8217; both refer to 1024. The default input unit is specified by letter, followed by |UNIT. UNIT represents other possible input units: <code>bBsSkKmMgGtTpPeE</code>. b|B is bytes, s|S is sectors of 512 bytes, k|K is kilobytes, m|M is megabytes, g|G is gigabytes, t|T is terabytes, p|P is petabytes, e|E is exabytes. (This should not be confused with the output control &#8211;units, where capital letters mean multiple of 1000.)</dl>
<h2>Environment Variables</h2>
<p>See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about environment variables used by lvm. For example, LVM_VG_NAME can generally be substituted for a required VG parameter.</p>
<h2>Notes</h2>
<p>If vgchange recognizes COW snapshot LVs that were dropped because they ran out of space, it displays a message informing the administrator that the snapshots should be removed.</p>
<h2>Examples</h2>
<p>Activate all LVs in all VGs on all existing devices.<br />
 <code>vgchange -a y</code> </p>
<p> Change the maximum number of LVs for an inactive VG.<br />
 <code>vgchange -l 128 vg00</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
