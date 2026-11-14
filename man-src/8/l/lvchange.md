---
title: "lvchange(8)"
name: "lvchange"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvchange/"
description: "lvchange – Change the attributes of logical volume(s)"
---

<p>lvchange &#8211; Change the attributes of logical volume(s)</p>
<h2>Synopsis</h2>
<p><code>lvchange</code> <i>option_args</i> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<code>-a</code>|<code>&#8211;activate</code>&nbsp;<code>y</code>|<code>n</code>|<code>ay</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;activationmode</code>&nbsp;<code>partial</code>|<code>degraded</code>|<code>complete</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;addtag</code>&nbsp;<i>Tag</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;alloc</code>&nbsp;<code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> </p>
<p>&nbsp;<code>-A</code>|<code>&#8211;autobackup</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachemode</code>&nbsp;<code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachepolicy</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachesettings</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;commandprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;compression</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;config</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-C</code>|<code>&#8211;contiguous</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-d</code>|<code>&#8211;debug</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deduplication</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deltag</code>&nbsp;<i>Tag</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;detachprofile</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;discards</code>&nbsp;<code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;driverloaded</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;errorwhenfull</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-f</code>|<code>&#8211;force</code> </p>
<p>&nbsp;<code>-h</code>|<code>&#8211;help</code> </p>
<p>&nbsp;<code>-K</code>|<code>&#8211;ignoreactivationskip</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;ignorelockingfailure</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;ignoremonitoring</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockopt</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;longhelp</code> </p>
<p>&nbsp;<code>-j</code>|<code>&#8211;major</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]maxrecoveryrate</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;metadataprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;minor</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]minrecoveryrate</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;monitor</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nolocking</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;noudevsync</code> </p>
<p>&nbsp;<code>-P</code>|<code>&#8211;partial</code> </p>
<p>&nbsp;<code>-p</code>|<code>&#8211;permission</code>&nbsp;<code>rw</code>|<code>r</code> </p>
<p>&nbsp;<code>-M</code>|<code>&#8211;persistent</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poll</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-q</code>|<code>&#8211;quiet</code> </p>
<p>&nbsp;<code>-r</code>|<code>&#8211;readahead</code>&nbsp;<code>auto</code>|<code>none</code>|<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;readonly</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;rebuild</code>&nbsp;<i>PV</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;refresh</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;reportformat</code>&nbsp;<code>basic</code>|<code>json</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;resync</code> </p>
<p>&nbsp;<code>-S</code>|<code>&#8211;select</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-k</code>|<code>&#8211;setactivationskip</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]syncaction</code>&nbsp;<code>check</code>|<code>repair</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;sysinit</code> </p>
<p>&nbsp;<code>-t</code>|<code>&#8211;test</code> </p>
<p>&nbsp;<code>-v</code>|<code>&#8211;verbose</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;version</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]writebehind</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]writemostly</code>&nbsp;<i>PV</i>[<code>:t</code>|<code>n</code>|<code>y</code>] </p>
<p>&nbsp;<code>-y</code>|<code>&#8211;yes</code> </p>
<p>&nbsp;<code>-Z</code>|<code>&#8211;zero</code>&nbsp;<code>y</code>|<code>n</code></p>
<h2>Description</h2>
<p>lvchange changes LV attributes in the VG, changes LV activation in the kernel, and includes other utilities for LV maintenance.</p>
<h2>Usage</h2>
<p>Change a general LV attribute.<br />
 For options listed in parentheses, any one is<br />
 required, after which the others are optional. </p>
<p> <code>lvchange</code></p>
<dl>
<dd>( <code>-C</code>|<code>&#8211;contiguous</code> <code>y</code>|<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-p</code>|<code>&#8211;permission</code>&nbsp;<code>rw</code>|<code>r</code>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-r</code>|<code>&#8211;readahead</code>&nbsp;<code>auto</code>|<code>none</code>|<i>Number</i>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-k</code>|<code>&#8211;setactivationskip</code>&nbsp;<code>y</code>|<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-Z</code>|<code>&#8211;zero</code>&nbsp;<code>y</code>|<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<code>-M</code>|<code>&#8211;persistent</code>&nbsp;<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;addtag</code>&nbsp;<i>Tag</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deltag</code>&nbsp;<i>Tag</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;alloc</code>&nbsp;<code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;compression</code>&nbsp;<code>y</code>|<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deduplication</code>&nbsp;<code>y</code>|<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;detachprofile</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;metadataprofile</code>&nbsp;<i>String</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;errorwhenfull</code>&nbsp;<code>y</code>|<code>n</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;discards</code>&nbsp;<code>passdown</code>|<code>nopassdown</code>|<code>ignore</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachemode</code>&nbsp;<code>writethrough</code>|<code>writeback</code>|<code>passthrough</code>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachepolicy</code>&nbsp;<i>String</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachesettings</code>&nbsp;<i>String</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]minrecoveryrate</code>&nbsp;<i>Size</i>[k|UNIT], </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]maxrecoveryrate</code>&nbsp;<i>Size</i>[k|UNIT], </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]writebehind</code>&nbsp;<i>Number</i>, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]writemostly</code>&nbsp;<i>PV</i>[<code>:t</code>|<code>n</code>|<code>y</code>]&nbsp;)</dl>
<dl>
<dd>&nbsp;<i>VG</i>|<i>LV</i>|<i>Tag</i>|<i>Select</i>&nbsp;&#8230;</dl>
<dl>
<dd>[ <code>-a</code>|<code>&#8211;activate</code> <code>y</code>|<code>n</code>|<code>ay</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;monitor</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Resyncronize a mirror or raid LV.<br />
 Use to reset &#8216;R&#8217; attribute on a not initially synchronized LV. </p>
<p> <code>lvchange</code> <code>&#8211;resync</code> <i>VG</i>|<i>LV</i><i>_mirror_raid</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ <code>-a</code>|<code>&#8211;activate</code> <code>y</code>|<code>n</code>|<code>ay</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Resynchronize or check a raid LV. </p>
<p> <code>lvchange</code> <code>&#8211;syncaction</code> <code>check</code>|<code>repair</code> <i>VG</i>|<i>LV</i><i>_raid</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Reconstruct data on specific PVs of a raid LV. </p>
<p> <code>lvchange</code> <code>&#8211;rebuild</code> <i>PV</i> <i>VG</i>|<i>LV</i><i>_raid</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Activate or deactivate an LV. </p>
<p> <code>lvchange</code> <code>-a</code>|<code>&#8211;activate</code> <code>y</code>|<code>n</code>|<code>ay</code> <i>VG</i>|<i>LV</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ <code>-P</code>|<code>&#8211;partial</code> ]<br />
 [ <code>-K</code>|<code>&#8211;ignoreactivationskip</code> ]<br />
 [ <code>&#8211;activationmode</code> <code>partial</code>|<code>degraded</code>|<code>complete</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;monitor</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;ignorelockingfailure</code> ]<br />
 [ <code>&#8211;sysinit</code> ]<br />
 [ <code>&#8211;readonly</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Reactivate an LV using the latest metadata. </p>
<p> <code>lvchange</code> <code>&#8211;refresh</code> <i>VG</i>|<i>LV</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ <code>-P</code>|<code>&#8211;partial</code> ]<br />
 [ <code>&#8211;activationmode</code> <code>partial</code>|<code>degraded</code>|<code>complete</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;monitor</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Start or stop monitoring an LV from dmeventd. </p>
<p> <code>lvchange</code> <code>&#8211;monitor</code> <code>y</code>|<code>n</code> <i>VG</i>|<i>LV</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Start or stop processing an LV conversion. </p>
<p> <code>lvchange</code> <code>&#8211;poll</code> <code>y</code>|<code>n</code> <i>VG</i>|<i>LV</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ <code>&#8211;monitor</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Make the minor device number persistent for an LV. </p>
<p> <code>lvchange</code> <code>-M</code>|<code>&#8211;persistent</code> <code>y</code> <code>&#8211;minor</code> <i>Number</i> <i>LV</i> </p>
<dl>
<dd>[ <code>-j</code>|<code>&#8211;major</code> <i>Number</i> ]<br />
 [ <code>-a</code>|<code>&#8211;activate</code> <code>y</code>|<code>n</code>|<code>ay</code> ]<br />
 [ <code>&#8211;poll</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;monitor</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Common options for command:</p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>&#8211;ignoremonitoring</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]</dl>
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
<dt> <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code></p>
<dd>
<dd>Specifies when writes to a cache LV should be considered complete. <code>writeback</code> considers a write complete as soon as it is stored in the cache pool. <code>writethough</code> considers a write complete only when it has been stored in both the cache pool and on the origin LV. While writethrough may be slower for writes, it is more resilient if something should happen to a device associated with the cache pool LV. With <code>passthrough</code>, all reads are served from the origin LV (all reads miss the cache) and all writes are forwarded to the origin LV; additionally, write hits cause cache block invalidates. See <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information.</p>
<dt> <code>&#8211;cachepolicy</code> <i>String</i></p>
<dd>
<dd>Specifies the cache policy for a cache LV. See <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information.</p>
<dt> <code>&#8211;cachesettings</code> <i>String</i></p>
<dd>
<dd>Specifies tunable values for a cache LV in &quot;Key = Value&quot; form. Repeat this option to specify multiple values. (The default values should usually be adequate.) The special string value <code>default</code> switches settings back to their default kernel values and removes them from the list of settings stored in LVM metadata. See <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information.</p>
<dt> <code>&#8211;commandprofile</code> <i>String</i></p>
<dd>
<dd>The command profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;compression</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Controls whether compression is enabled or disable for VDO volume. See <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7) for more information about VDO usage.</p>
<dt> <code>&#8211;config</code> <i>String</i></p>
<dd>
<dd>Config settings for the command. These override lvm.conf settings. The String arg uses the same format as lvm.conf, or may use section/field syntax. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about config.</p>
<dt> <code>-C</code>|<code>&#8211;contiguous</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Sets or resets the contiguous allocation policy for LVs. Default is no contiguous allocation based on a next free principle. It is only possible to change a non-contiguous allocation policy to contiguous if all of the allocated physical extents in the LV are already contiguous.</p>
<dt> <code>-d</code>|<code>&#8211;debug</code> &#8230;</p>
<dd>
<dd>Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).</p>
<dt> <code>&#8211;deduplication</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Controls whether deduplication is enabled or disable for VDO volume. See <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7) for more information about VDO usage.</p>
<dt> <code>&#8211;deltag</code> <i>Tag</i></p>
<dd>
<dd>Deletes a tag from a PV, VG or LV. This option can be repeated to delete multiple tags at once. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tags.</p>
<dt> <code>&#8211;detachprofile</code></p>
<dd>
<dd>Detaches a metadata profile from a VG or LV. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code></p>
<dd>
<dd>Specifies how the device-mapper thin pool layer in the kernel should handle discards. <code>ignore</code> causes the thin pool to ignore discards. <code>nopassdown</code> causes the thin pool to process discards itself to allow reuse of unneeded extents in the thin pool. <code>passdown</code> causes the thin pool to process discards itself (like nopassdown) and pass the discards to the underlying device. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information.</p>
<dt> <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>If set to no, the command will not attempt to use device-mapper. For testing and debugging.</p>
<dt> <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Specifies thin pool behavior when data space is exhausted. When yes, device-mapper will immediately return an error when a thin pool is full and an I/O request requires space. When no, device-mapper will queue these I/O requests for a period of time to allow the thin pool to be extended. Errors are returned if no space is available after the timeout. (Also see dm-thin-pool kernel module option no_space_timeout.) See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information.</p>
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
<dt> <code>&#8211;longhelp</code></p>
<dd>
<dd>Display long help text.</p>
<dt> <code>-j</code>|<code>&#8211;major</code> <i>Number</i></p>
<dd>
<dd>Sets the major number of an LV block device.</p>
<dt> <code>&#8211;[raid]maxrecoveryrate</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>Sets the maximum recovery rate for a RAID LV. The rate value is an amount of data per second for each device in the array. Setting the rate to 0 means it will be unbounded. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
<dt> <code>&#8211;metadataprofile</code> <i>String</i></p>
<dd>
<dd>The metadata profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;minor</code> <i>Number</i></p>
<dd>
<dd>Sets the minor number of an LV block device.</p>
<dt> <code>&#8211;[raid]minrecoveryrate</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>Sets the minimum recovery rate for a RAID LV. The rate value is an amount of data per second for each device in the array. Setting the rate to 0 means it will be unbounded. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
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
<dt> <code>-p</code>|<code>&#8211;permission</code> <code>rw</code>|<code>r</code></p>
<dd>
<dd>Set access permission to read only <code>r</code> or read and write <code>rw</code>.</p>
<dt> <code>-M</code>|<code>&#8211;persistent</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>When yes, makes the specified minor number persistent.</p>
<dt> <code>&#8211;poll</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>When yes, start the background transformation of an LV. An incomplete transformation, e.g. pvmove or lvconvert interrupted by reboot or crash, can be restarted from the last checkpoint with &#8211;poll y. When no, background transformation of an LV will not occur, and the transformation will not complete. It may not be appropriate to immediately poll an LV after activation, in which case &#8211;poll n can be used to defer polling until a later &#8211;poll y command.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i></p>
<dd>
<dd>Sets read ahead sector count of an LV. <code>auto</code> is the default which allows the kernel to choose a suitable value automatically. <code>none</code> is equivalent to zero.</p>
<dt> <code>&#8211;readonly</code></p>
<dd>
<dd>Run the command in a special read-only mode which will read on-disk metadata without needing to take any locks. This can be used to peek inside metadata used by a virtual machine image while the virtual machine is running. No attempt will be made to communicate with the device-mapper kernel driver, so this option is unable to report whether or not LVs are actually in use.</p>
<dt> <code>&#8211;rebuild</code> <i>PV</i></p>
<dd>
<dd>Selects a PV to rebuild in a raid LV. Multiple PVs can be rebuilt by repeating this option. Use this option in place of &#8211;resync or &#8211;syncaction repair when the PVs with corrupted data are known, and their data should be reconstructed rather than reconstructing default (rotating) data. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
<dt> <code>&#8211;refresh</code></p>
<dd>
<dd>If the LV is active, reload its metadata. This is not necessary in normal operation, but may be useful if something has gone wrong, or if some form of manual LV sharing is being used.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
<dt> <code>&#8211;resync</code></p>
<dd>
<dd>Initiates mirror synchronization. Synchronization generally happens automatically, but this option forces it to run. Also see &#8211;rebuild to synchronize a specific PV. During synchronization, data is read from the primary mirror device and copied to the others. This can take considerable time, during which the LV is without a complete redundant copy of the data. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
<dt> <code>-S</code>|<code>&#8211;select</code> <i>String</i></p>
<dd>
<dd>Select objects for processing and reporting based on specified criteria. The criteria syntax is described by <code>&#8211;select help</code> and <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7). For reporting commands, one row is displayed for each object matching the criteria. See <code>&#8211;options help</code> for selectable object fields. Rows can be displayed with an additional &quot;selected&quot; field (-o selected) showing 1 if the row matches the selection and 0 otherwise. For non-reporting commands which process LVM entities, the selection is used to choose items to process.</p>
<dt> <code>-k</code>|<code>&#8211;setactivationskip</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Persistently sets (yes) or clears (no) the &quot;activation skip&quot; flag on an LV. An LV with this flag set is not activated unless the &#8211;ignoreactivationskip option is used by the activation command. This flag is set by default on new thin snapshot LVs. The flag is not applied to deactivation. The current value of the flag is indicated in the lvs lv_attr bits.</p>
<dt> <code>&#8211;[raid]syncaction</code> <code>check</code>|<code>repair</code></p>
<dd>
<dd>Initiate different types of RAID synchronization. This causes the RAID LV to read all data and parity blocks in the array and check for discrepancies (mismatches between mirrors or incorrect parity values). <code>check</code> will count but not correct discrepancies. <code>repair</code> will correct discrepancies. See lvs for reporting discrepancies found or repaired.</p>
<dt> <code>&#8211;sysinit</code></p>
<dd>
<dd>Indicates that vgchange/lvchange is being invoked from early system initialisation scripts (e.g. rc.sysinit or an initrd), before writable filesystems are available. As such, some functionality needs to be disabled and this option acts as a shortcut which selects an appropriate set of options. Currently, this is equivalent to using &#8211;ignorelockingfailure, &#8211;ignoremonitoring, &#8211;poll n, and setting env var LVM_SUPPRESS_LOCKING_FAILURE_MESSAGES. vgchange/lvchange skip autoactivation, and defer to pvscan autoactivation.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code> &#8230;</p>
<dd>
<dd>Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.</p>
<dt> <code>&#8211;version</code></p>
<dd>
<dd>Display version information.</p>
<dt> <code>&#8211;[raid]writebehind</code> <i>Number</i></p>
<dd>
<dd>The maximum number of outstanding writes that are allowed to devices in a RAID1 LV that is marked write-mostly. Once this value is exceeded, writes become synchronous (i.e. all writes to the constituent devices must complete before the array signals the write has completed). Setting the value to zero clears the preference and allows the system to choose the value arbitrarily.</p>
<dt> <code>&#8211;[raid]writemostly</code> <i>PV</i>[<code>:t</code>|<code>n</code>|<code>y</code>]</p>
<dd>
<dd>Mark a device in a RAID1 LV as write-mostly. All reads to these drives will be avoided unless absolutely necessary. This keeps the number of I/Os to the drive to a minimum. The default behavior is to set the write-mostly attribute for the specified PV. It is also possible to remove the write-mostly flag by adding the suffix <code>:n</code> at the end of the PV name, or to toggle the value with the suffix <code>:t</code>. Repeat this option to change the attribute on multiple PVs.</p>
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</p>
<dt> <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Set zeroing mode for thin pool. Note: already provisioned blocks from pool in non-zero mode are not cleared in unwritten parts when setting &#8211;zero y.</dl>
<h2>Variables</h2>
<dl>
<dt> <i>VG</i></p>
<dd>
<dd>Volume Group name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names.</p>
<dt> <i>LV</i></p>
<dd>
<dd>Logical Volume name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names. An LV positional arg generally includes the VG name and LV name, e.g. VG/LV. LV followed by _&lt;type&gt; indicates that an LV of the given type is required. (raid represents raid&lt;N&gt; type)</p>
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
<h2>Examples</h2>
<p>Change LV permission to read-only: </p>
<p> <code>lvchange -pr vg00/lvol1</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
