---
title: "lvcreate(8)"
name: "lvcreate"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvcreate/"
description: "lvcreate – Create a logical volume"
---

<p>lvcreate &#8211; Create a logical volume</p>
<h2>Synopsis</h2>
<p><code>lvcreate</code> <i>option_args</i> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>position_args</i>&nbsp;] </p>
<p>&nbsp;<code>-a</code>|<code>&#8211;activate</code>&nbsp;<code>y</code>|<code>n</code>|<code>ay</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;addtag</code>&nbsp;<i>Tag</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;alloc</code>&nbsp;<code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> </p>
<p>&nbsp;<code>-A</code>|<code>&#8211;autobackup</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-H</code>|<code>&#8211;cache</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachemetadataformat</code>&nbsp;<code>auto</code>|<code>1</code>|<code>2</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachemode</code>&nbsp;<code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachepolicy</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachepool</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachesettings</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-c</code>|<code>&#8211;chunksize</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;commandprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;compression</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;config</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-C</code>|<code>&#8211;contiguous</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-d</code>|<code>&#8211;debug</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deduplication</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;discards</code>&nbsp;<code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;driverloaded</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;errorwhenfull</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-l</code>|<code>&#8211;extents</code>&nbsp;<i>Number</i>[PERCENT] </p>
<p>&nbsp;<code>-h</code>|<code>&#8211;help</code> </p>
<p>&nbsp;<code>-K</code>|<code>&#8211;ignoreactivationskip</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;ignoremonitoring</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockopt</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;longhelp</code> </p>
<p>&nbsp;<code>-j</code>|<code>&#8211;major</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]maxrecoveryrate</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;metadataprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;minor</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[raid]minrecoveryrate</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;mirrorlog</code>&nbsp;<code>core</code>|<code>disk</code> </p>
<p>&nbsp;<code>-m</code>|<code>&#8211;mirrors</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;monitor</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-n</code>|<code>&#8211;name</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nolocking</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nosync</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;noudevsync</code> </p>
<p>&nbsp;<code>-p</code>|<code>&#8211;permission</code>&nbsp;<code>rw</code>|<code>r</code> </p>
<p>&nbsp;<code>-M</code>|<code>&#8211;persistent</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poolmetadatasize</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poolmetadataspare</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-q</code>|<code>&#8211;quiet</code> </p>
<p>&nbsp;<code>-r</code>|<code>&#8211;readahead</code>&nbsp;<code>auto</code>|<code>none</code>|<i>Number</i> </p>
<p>&nbsp;<code>-R</code>|<code>&#8211;regionsize</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;reportformat</code>&nbsp;<code>basic</code>|<code>json</code> </p>
<p>&nbsp;<code>-k</code>|<code>&#8211;setactivationskip</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-L</code>|<code>&#8211;size</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<code>-s</code>|<code>&#8211;snapshot</code> </p>
<p>&nbsp;<code>-i</code>|<code>&#8211;stripes</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<code>-I</code>|<code>&#8211;stripesize</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<code>-t</code>|<code>&#8211;test</code> </p>
<p>&nbsp;<code>-T</code>|<code>&#8211;thin</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;thinpool</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;type</code>&nbsp;<code>linear</code>|<code>striped</code>|<code>snapshot</code>|<code>mirror</code>|<code>raid</code>|<code>thin</code>|<code>cache</code>|<code>vdo</code>|<code>thin-pool</code>|<code>cache-pool</code>|<code>vdo-pool</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;vdo</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;vdopool</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<code>-v</code>|<code>&#8211;verbose</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;version</code> </p>
<p>&nbsp;<code>-V</code>|<code>&#8211;virtualsize</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<code>-W</code>|<code>&#8211;wipesignatures</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-y</code>|<code>&#8211;yes</code> </p>
<p>&nbsp;<code>-Z</code>|<code>&#8211;zero</code>&nbsp;<code>y</code>|<code>n</code></p>
<h2>Description</h2>
<p>lvcreate creates a new LV in a VG. For standard LVs, this requires allocating logical extents from the VG&#8217;s free physical extents. If there is not enough free space, the VG can be extended with other PVs (<code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8)), or existing LVs can be reduced or removed (<code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8), <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8).) </p>
<p> To control which PVs a new LV will use, specify one or more PVs as position args at the end of the command line. lvcreate will allocate physical extents only from the specified PVs. </p>
<p> lvcreate can also create snapshots of existing LVs, e.g. for backup purposes. The data in a new snapshot LV represents the content of the original LV from the time the snapshot was created. </p>
<p> RAID LVs can be created by specifying an LV type when creating the LV (see <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7)). Different RAID levels require different numbers of unique PVs be available in the VG for allocation. </p>
<p> Thin pools (for thin provisioning) and cache pools (for caching) are represented by special LVs with types thin-pool and cache-pool (see <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) and <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7)). The pool LVs are not usable as standard block devices, but the LV names act as references to the pools. </p>
<p> Thin LVs are thinly provisioned from a thin pool, and are created with a virtual size rather than a physical size. A cache LV is the combination of a standard LV with a cache pool, used to cache active portions of the LV to improve performance. </p>
<p> VDO LVs are also provisioned volumes from a VDO pool, and are created with a virtual size rather than a physical size (see <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7)).</p>
<h3>Usage notes</h3>
<p>In the usage section below, <code>&#8211;size</code> <i>Size</i> can be replaced with <code>&#8211;extents</code> <i>Number</i>. See descriptions in the options section. </p>
<p> In the usage section below, <code>&#8211;name</code> is omitted from the required options, even though it is typically used. When the name is not specified, a new LV name is generated with the &quot;lvol&quot; prefix and a unique numeric suffix. </p>
<p> In the usage section below, when creating a pool and the name is omitted the new LV pool name is generated with the &quot;vpool&quot; for vdo-pools for prefix and a unique numeric suffix. </p>
<p> Pool name can be specified together with <i>VG</i> name i.e.: vg00/mythinpool.</p>
<h2>Usage</h2>
<p>Create a linear LV. </p>
<p> <code>lvcreate</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>&#8211;type</code> <code>linear</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a striped LV (infers &#8211;type striped). </p>
<p> <code>lvcreate</code> <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a raid1 or mirror LV (infers &#8211;type raid1|mirror). </p>
<p> <code>lvcreate</code> <code>-m</code>|<code>&#8211;mirrors</code> <i>Number</i> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;mirrorlog</code> <code>core</code>|<code>disk</code> ]<br />
 [ <code>&#8211;[raid]minrecoveryrate</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;[raid]maxrecoveryrate</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a raid LV (a specific raid level must be used, e.g. raid1). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>raid</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-m</code>|<code>&#8211;mirrors</code> <i>Number</i> ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;[raid]minrecoveryrate</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;[raid]maxrecoveryrate</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a raid10 LV. </p>
<p> <code>lvcreate</code> <code>-m</code>|<code>&#8211;mirrors</code> <i>Number</i> <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i></p>
<dl>
<dd>&nbsp;<code>-L</code>|<code>&#8211;size</code>&nbsp;<i>Size</i>[m|UNIT]&nbsp;<i>VG</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;[raid]minrecoveryrate</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;[raid]maxrecoveryrate</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a COW snapshot LV of an origin LV. </p>
<p> <code>lvcreate</code> <code>-s</code>|<code>&#8211;snapshot</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>LV</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>snapshot</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin pool. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>thin-pool</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;thinpool</code> <i>LV</i><i>_new</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a cache pool. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>cache-pool</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-H</code>|<code>&#8211;cache</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV in a thin pool (infers &#8211;type thin). </p>
<p> <code>lvcreate</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] <code>&#8211;thinpool</code> <i>LV</i><i>_thinpool</i> <i>VG</i> </p>
<dl>
<dd>[ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>&#8211;type</code> <code>thin</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a thin LV that is a snapshot of an existing thin LV<br />
 (infers &#8211;type thin). </p>
<p> <code>lvcreate</code> <code>-s</code>|<code>&#8211;snapshot</code> <i>LV</i><i>_thin</i> </p>
<dl>
<dd>[ <code>&#8211;type</code> <code>thin</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a thin LV that is a snapshot of an external origin LV. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>thin</code> <code>&#8211;thinpool</code> <i>LV</i><i>_thinpool</i> <i>LV</i> </p>
<dl>
<dd>[ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a LV that returns VDO when used. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>vdo</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;vdo</code> ]<br />
 [ <code>&#8211;vdopool</code> <i>LV</i><i>_new</i> ]<br />
 [ <code>&#8211;compression</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;deduplication</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV, first creating a thin pool for it,<br />
 where the new thin pool is named by the &#8211;thinpool arg. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>thin</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>-L</code>|<code>&#8211;size</code>&nbsp;<i>Size</i>[m|UNIT]&nbsp;<code>&#8211;thinpool</code>&nbsp;<i>LV</i><i>_new</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a cache LV, first creating a new origin LV,<br />
 then combining it with the existing cache pool named<br />
 by the &#8211;cachepool arg. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>cache</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>&#8211;cachepool</code>&nbsp;<i>LV</i><i>_cachepool</i>&nbsp;<i>VG</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-H</code>|<code>&#8211;cache</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Common options for command:</p>
<dl>
<dd>[ <code>-a</code>|<code>&#8211;activate</code> <code>y</code>|<code>n</code>|<code>ay</code> ]<br />
 [ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-C</code>|<code>&#8211;contiguous</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-K</code>|<code>&#8211;ignoreactivationskip</code> ]<br />
 [ <code>-j</code>|<code>&#8211;major</code> <i>Number</i> ]<br />
 [ <code>-n</code>|<code>&#8211;name</code> <i>String</i> ]<br />
 [ <code>-p</code>|<code>&#8211;permission</code> <code>rw</code>|<code>r</code> ]<br />
 [ <code>-M</code>|<code>&#8211;persistent</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i> ]<br />
 [ <code>-k</code>|<code>&#8211;setactivationskip</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-W</code>|<code>&#8211;wipesignatures</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;addtag</code> <i>Tag</i> ]<br />
 [ <code>&#8211;alloc</code> <code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> ]<br />
 [ <code>&#8211;ignoremonitoring</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ <code>&#8211;minor</code> <i>Number</i> ]<br />
 [ <code>&#8211;monitor</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;nosync</code> ]<br />
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
<dd>Controls the active state of the new LV. <code>y</code> makes the LV active, or available. New LVs are made active by default. <code>n</code> makes the LV inactive, or unavailable, only when possible. In some cases, creating an LV requires it to be active. For example, COW snapshots of an active origin LV can only be created in the active state (this does not apply to thin snapshots). The &#8211;zero option normally requires the LV to be active. If autoactivation <code>ay</code> is used, the LV is only activated if it matches an item in lvm.conf activation/auto_activation_volume_list. <code>ay</code> implies &#8211;zero n and &#8211;wipesignatures n. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information about activation options for shared VGs.</p>
<dt> <code>&#8211;addtag</code> <i>Tag</i></p>
<dd>
<dd>Adds a tag to a PV, VG or LV. This option can be repeated to add multiple tags at once. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tags.</p>
<dt> <code>&#8211;alloc</code> <code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code></p>
<dd>
<dd>Determines the allocation policy when a command needs to allocate Physical Extents (PEs) from the VG. Each VG and LV has an allocation policy which can be changed with vgchange/lvchange, or overriden on the command line. <code>normal</code> applies common sense rules such as not placing parallel stripes on the same PV. <code>inherit</code> applies the VG policy to an LV. <code>contiguous</code> requires new PEs be placed adjacent to existing PEs. <code>cling</code> places new PEs on the same PV as existing PEs in the same stripe of the LV. If there are sufficient PEs for an allocation, but normal does not use them, <code>anywhere</code> will use them even if it reduces performance, e.g. by placing two stripes on the same PV. Optional positional PV args on the command line can also be used to limit which PVs the command will use for allocation. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for more information about allocation.</p>
<dt> <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Specifies if metadata should be backed up automatically after a change. Enabling this is strongly advised! See <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) for more information.</p>
<dt> <code>-H</code>|<code>&#8211;cache</code></p>
<dd>
<dd>Specifies the command is handling a cache LV or cache pool. See &#8211;type cache and &#8211;type cache-pool. See <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information about LVM caching.</p>
<dt> <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code></p>
<dd>
<dd>Specifies the cache metadata format used by cache target.</p>
<dt> <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code></p>
<dd>
<dd>Specifies when writes to a cache LV should be considered complete. <code>writeback</code> considers a write complete as soon as it is stored in the cache pool. <code>writethough</code> considers a write complete only when it has been stored in both the cache pool and on the origin LV. While writethrough may be slower for writes, it is more resilient if something should happen to a device associated with the cache pool LV. With <code>passthrough</code>, all reads are served from the origin LV (all reads miss the cache) and all writes are forwarded to the origin LV; additionally, write hits cause cache block invalidates. See <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information.</p>
<dt> <code>&#8211;cachepolicy</code> <i>String</i></p>
<dd>
<dd>Specifies the cache policy for a cache LV. See <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information.</p>
<dt> <code>&#8211;cachepool</code> <i>LV</i></p>
<dd>
<dd>The name of a cache pool.</p>
<dt> <code>&#8211;cachesettings</code> <i>String</i></p>
<dd>
<dd>Specifies tunable values for a cache LV in &quot;Key = Value&quot; form. Repeat this option to specify multiple values. (The default values should usually be adequate.) The special string value <code>default</code> switches settings back to their default kernel values and removes them from the list of settings stored in LVM metadata. See <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information.</p>
<dt> <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>The size of chunks in a snapshot, cache pool or thin pool. For snapshots, the value must be a power of 2 between 4KiB and 512KiB and the default value is 4. For a cache pool the value must be between 32KiB and 1GiB and the default value is 64. For a thin pool the value must be between 64KiB and 1GiB and the default value starts with 64 and scales up to fit the pool metadata size within 128MiB, if the pool metadata size is not specified. The value must be a multiple of 64KiB. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) and <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) for more information.</p>
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
<dt> <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code></p>
<dd>
<dd>Specifies how the device-mapper thin pool layer in the kernel should handle discards. <code>ignore</code> causes the thin pool to ignore discards. <code>nopassdown</code> causes the thin pool to process discards itself to allow reuse of unneeded extents in the thin pool. <code>passdown</code> causes the thin pool to process discards itself (like nopassdown) and pass the discards to the underlying device. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information.</p>
<dt> <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>If set to no, the command will not attempt to use device-mapper. For testing and debugging.</p>
<dt> <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Specifies thin pool behavior when data space is exhausted. When yes, device-mapper will immediately return an error when a thin pool is full and an I/O request requires space. When no, device-mapper will queue these I/O requests for a period of time to allow the thin pool to be extended. Errors are returned if no space is available after the timeout. (Also see dm-thin-pool kernel module option no_space_timeout.) See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information.</p>
<dt> <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT]</p>
<dd>
<dd>Specifies the size of the new LV in logical extents. The &#8211;size and &#8211;extents options are alternate methods of specifying size. The total number of physical extents used will be greater when redundant data is needed for RAID levels. An alternate syntax allows the size to be determined indirectly as a percentage of the size of a related VG, LV, or set of PVs. The suffix <code>%VG</code> denotes the total size of the VG, the suffix <code>%FREE</code> the remaining free space in the VG, and the suffix <code>%PVS</code> the free space in the specified PVs. For a snapshot, the size can be expressed as a percentage of the total size of the origin LV with the suffix <code>%ORIGIN</code> (<code>100%ORIGIN</code> provides space for the whole origin). When expressed as a percentage, the size defines an upper limit for the number of logical extents in the new LV. The precise number of logical extents in the new LV is not determined until the command has completed.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display help text.</p>
<dt> <code>-K</code>|<code>&#8211;ignoreactivationskip</code></p>
<dd>
<dd>Ignore the &quot;activation skip&quot; LV flag during activation to allow LVs with the flag set to be activated.</p>
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
<dt> <code>&#8211;mirrorlog</code> <code>core</code>|<code>disk</code></p>
<dd>
<dd>Specifies the type of mirror log for LVs with the &quot;mirror&quot; type (does not apply to the &quot;raid1&quot; type.) <code>disk</code> is a persistent log and requires a small amount of storage space, usually on a separate device from the data being mirrored. <code>core</code> is not persistent; the log is kept only in memory. In this case, the mirror must be synchronized (by copying LV data from the first device to others) each time the LV is activated, e.g. after reboot. <code>mirrored</code> is a persistent log that is itself mirrored, but should be avoided. Instead, use the raid1 type for log redundancy.</p>
<dt> <code>-m</code>|<code>&#8211;mirrors</code> <i>Number</i></p>
<dd>
<dd>Specifies the number of mirror images in addition to the original LV image, e.g. &#8211;mirrors 1 means there are two images of the data, the original and one mirror image. Optional positional PV args on the command line can specify the devices the images should be placed on. There are two mirroring implementations: &quot;raid1&quot; and &quot;mirror&quot;. These are the names of the corresponding LV types, or &quot;segment types&quot;. Use the &#8211;type option to specify which to use (raid1 is default, and mirror is legacy) Use lvm.conf global/mirror_segtype_default and global/raid10_segtype_default to configure the default types. See the &#8211;nosync option for avoiding initial image synchronization. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
<dt> <code>&#8211;monitor</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Start (yes) or stop (no) monitoring an LV with dmeventd. dmeventd monitors kernel events for an LV, and performs automated maintenance for the LV in reponse to specific events. See <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) for more information.</p>
<dt> <code>-n</code>|<code>&#8211;name</code> <i>String</i></p>
<dd>
<dd>Specifies the name of a new LV. When unspecified, a default name of &quot;lvol#&quot; is generated, where # is a number generated by LVM.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;nosync</code></p>
<dd>
<dd>Causes the creation of mirror, raid1, raid4, raid5 and raid10 to skip the initial synchronization. In case of mirror, raid1 and raid10, any data written afterwards will be mirrored, but the original contents will not be copied. In case of raid4 and raid5, no parity blocks will be written, though any data written afterwards will cause parity blocks to be stored. This is useful for skipping a potentially long and resource intensive initial sync of an empty mirror/raid1/raid4/raid5 and raid10 LV. This option is not valid for raid6, because raid6 relies on proper parity (P and Q Syndromes) being created during initial synchronization in order to reconstruct proper user date in case of device failures. raid0 and raid0_meta do not provide any data copies or parity support and thus do not support initial synchronization.</p>
<dt> <code>&#8211;noudevsync</code></p>
<dd>
<dd>Disables udev synchronisation. The process will not wait for notification from udev. It will continue irrespective of any possible udev processing in the background. Only use this if udev is not running or has rules that ignore the devices LVM creates.</p>
<dt> <code>-p</code>|<code>&#8211;permission</code> <code>rw</code>|<code>r</code></p>
<dd>
<dd>Set access permission to read only <code>r</code> or read and write <code>rw</code>.</p>
<dt> <code>-M</code>|<code>&#8211;persistent</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>When yes, makes the specified minor number persistent.</p>
<dt> <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>Specifies the size of the new pool metadata LV.</p>
<dt> <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Enable or disable the automatic creation and management of a spare pool metadata LV in the VG. A spare metadata LV is reserved space that can be used when repairing a pool.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i></p>
<dd>
<dd>Sets read ahead sector count of an LV. <code>auto</code> is the default which allows the kernel to choose a suitable value automatically. <code>none</code> is equivalent to zero.</p>
<dt> <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>Size of each raid or mirror synchronization region. lvm.conf activation/raid_region_size can be used to configure a default.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
<dt> <code>-k</code>|<code>&#8211;setactivationskip</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Persistently sets (yes) or clears (no) the &quot;activation skip&quot; flag on an LV. An LV with this flag set is not activated unless the &#8211;ignoreactivationskip option is used by the activation command. This flag is set by default on new thin snapshot LVs. The flag is not applied to deactivation. The current value of the flag is indicated in the lvs lv_attr bits.</p>
<dt> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>Specifies the size of the new LV. The &#8211;size and &#8211;extents options are alternate methods of specifying size. The total number of physical extents used will be greater when redundant data is needed for RAID levels.</p>
<dt> <code>-s</code>|<code>&#8211;snapshot</code></p>
<dd>
<dd>Create a snapshot. Snapshots provide a &quot;frozen image&quot; of an origin LV. The snapshot LV can be used, e.g. for backups, while the origin LV continues to be used. This option can create a COW (copy on write) snapshot, or a thin snapshot (in a thin pool.) Thin snapshots are created when the origin is a thin LV and the size option is NOT specified. Thin snapshots share the same blocks in the thin pool, and do not allocate new space from the VG. Thin snapshots are created with the &quot;activation skip&quot; flag, see &#8211;setactivationskip. A thin snapshot of a non-thin &quot;external origin&quot; LV is created when a thin pool is specified. Unprovisioned blocks in the thin snapshot LV are read from the external origin LV. The external origin LV must be read-only. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information about LVM thin provisioning. COW snapshots are created when a size is specified. The size is allocated from space in the VG, and is the amount of space that can be used for saving COW blocks as writes occur to the origin or snapshot. The size chosen should depend upon the amount of writes that are expected; often 20% of the origin LV is enough. If COW space runs low, it can be extended with lvextend (shrinking is also allowed with lvreduce.) A small amount of the COW snapshot LV size is used to track COW block locations, so the full size is not available for COW data blocks. Use lvs to check how much space is used, and see &#8211;monitor to to automatically extend the size to avoid running out of space.</p>
<dt> <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i></p>
<dd>
<dd>Specifies the number of stripes in a striped LV. This is the number of PVs (devices) that a striped LV is spread across. Data that appears sequential in the LV is spread across multiple devices in units of the stripe size (see &#8211;stripesize). This does not change existing allocated space, but only applies to space being allocated by the command. When creating a RAID 4/5/6 LV, this number does not include the extra devices that are required for parity. The largest number depends on the RAID type (raid0: 64, raid10: 32, raid4/5: 63, raid6: 62), and when unspecified, the default depends on the RAID type (raid0: 2, raid10: 2, raid4/5: 3, raid6: 5.) To stripe a new raid LV across all PVs by default, see lvm.conf allocation/raid_stripe_all_devices.</p>
<dt> <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>The amount of data that is written to one device before moving to the next in a striped LV.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>-T</code>|<code>&#8211;thin</code></p>
<dd>
<dd>Specifies the command is handling a thin LV or thin pool. See &#8211;type thin, &#8211;type thin-pool, and &#8211;virtualsize. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information about LVM thin provisioning.</p>
<dt> <code>&#8211;thinpool</code> <i>LV</i></p>
<dd>
<dd>The name of a thin pool LV.</p>
<dt> <code>&#8211;type</code> <code>linear</code>|<code>striped</code>|<code>snapshot</code>|<code>mirror</code>|<code>raid</code>|<code>thin</code>|<code>cache</code>|<code>vdo</code>|<code>thin-pool</code>|<code>cache-pool</code>|<code>vdo-pool</code></p>
<dd>
<dd>The LV type, also known as &quot;segment type&quot; or &quot;segtype&quot;. See usage descriptions for the specific ways to use these types. For more information about redundancy and performance (<code>raid</code>&lt;N&gt;, <code>mirror</code>, <code>striped</code>, <code>linear</code>) see <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7). For thin provisioning (<code>thin</code>, <code>thin-pool</code>) see <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7). For performance caching (<code>cache</code>, <code>cache-pool</code>) see <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7). For copy-on-write snapshots (<code>snapshot</code>) see usage definitions. For VDO (<code>vdo</code>) see <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7). Several commands omit an explicit type option because the type is inferred from other options or shortcuts (e.g. &#8211;stripes, &#8211;mirrors, &#8211;snapshot, &#8211;virtualsize, &#8211;thin, &#8211;cache, &#8211;vdo). Use inferred types with care because it can lead to unexpected results.</p>
<dt> <code>&#8211;vdo</code></p>
<dd>
<dd>Specifies the command is handling VDO LV. See &#8211;type vdo. See <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7) for more information about VDO usage.</p>
<dt> <code>&#8211;vdopool</code> <i>LV</i></p>
<dd>
<dd>The name of a VDO pool LV. See <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7) for more information about VDO usage.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code> &#8230;</p>
<dd>
<dd>Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.</p>
<dt> <code>&#8211;version</code></p>
<dd>
<dd>Display version information.</p>
<dt> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>The virtual size of a new thin LV. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information about LVM thin provisioning. Using virtual size (-V) and actual size (-L) together creates a sparse LV. lvm.conf global/sparse_segtype_default determines the default segment type used to create a sparse LV. Anything written to a sparse LV will be returned when reading from it. Reading from other areas of the LV will return blocks of zeros. When using a snapshot to create a sparse LV, a hidden virtual device is created using the zero target, and the LV has the suffix _vorigin. Snapshots are less efficient than thin provisioning when creating large sparse LVs (GiB).</p>
<dt> <code>-W</code>|<code>&#8211;wipesignatures</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Controls detection and subsequent wiping of signatures on new LVs. There is a prompt for each signature detected to confirm its wiping (unless &#8211;yes is used to override confirmations.) When not specified, signatures are wiped whenever zeroing is done (see &#8211;zero). This behaviour can be configured with lvm.conf allocation/wipe_signatures_when_zeroing_new_lvs. If blkid wiping is used (lvm.conf allocation/use_blkid_wiping) and LVM is compiled with blkid wiping support, then the <a href="/docs/linux/man/8-blkid/">blkid</a>(8) library is used to detect the signatures (use blkid -k to list the signatures that are recognized). Otherwise, native LVM code is used to detect signatures (only MD RAID, swap and LUKS signatures are detected in this case.) The LV is not wiped if the read only flag is set.</p>
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</p>
<dt> <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Controls zeroing of the first 4KiB of data in the new LV. Default is <code>y</code>. Snapshot COW volumes are always zeroed. For thin pools, this controls zeroing of provisioned blocks. LV is not zeroed if the read only flag is set. Warning: trying to mount an unzeroed LV can cause the system to hang.</dl>
<h2>Variables</h2>
<dl>
<dt> <i>VG</i></p>
<dd>
<dd>Volume Group name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names. For lvcreate, the required VG positional arg may be omitted when the VG name is included in another option, e.g. &#8211;name VG/LV.</p>
<dt> <i>LV</i></p>
<dd>
<dd>Logical Volume name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names. An LV positional arg generally includes the VG name and LV name, e.g. VG/LV. LV followed by _&lt;type&gt; indicates that an LV of the given type is required. (raid represents raid&lt;N&gt; type)</p>
<dt> <i>PV</i></p>
<dd>
<dd>Physical Volume name, a device path under /dev. For commands managing physical extents, a PV positional arg generally accepts a suffix indicating a range (or multiple ranges) of physical extents (PEs). When the first PE is omitted, it defaults to the start of the device, and when the last PE is omitted it defaults to end. Start and end range (inclusive): <i>PV</i>[<code>:</code><i>PE</i><code>&#8211;</code><i>PE</i>]&#8230; Start and length range (counting from 0): <i>PV</i>[<code>:</code><i>PE</i><code>+</code><i>PE</i>]&#8230;</p>
<dt> <i>String</i></p>
<dd>
<dd>See the option description for information about the string content.</p>
<dt> <i>Size</i>[UNIT]</p>
<dd>
<dd>Size is an input number that accepts an optional unit. Input units are always treated as base two values, regardless of capitalization, e.g. &#8216;k&#8217; and &#8216;K&#8217; both refer to 1024. The default input unit is specified by letter, followed by |UNIT. UNIT represents other possible input units: <code>bBsSkKmMgGtTpPeE</code>. b|B is bytes, s|S is sectors of 512 bytes, k|K is kilobytes, m|M is megabytes, g|G is gigabytes, t|T is terabytes, p|P is petabytes, e|E is exabytes. (This should not be confused with the output control &#8211;units, where capital letters mean multiple of 1000.)</dl>
<h2>Environment Variables</h2>
<p>See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about environment variables used by lvm. For example, LVM_VG_NAME can generally be substituted for a required VG parameter.</p>
<h2>Advanced Usage</h2>
<p>Alternate command forms, advanced command usage, and listing of all valid syntax for completeness. </p>
<p> Create an LV that returns errors when used. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>error</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create an LV that returns zeros when read. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>zero</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a linear LV. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>linear</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a striped LV (also see lvcreate &#8211;stripes). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>striped</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a mirror LV (also see &#8211;type raid1). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>mirror</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-m</code>|<code>&#8211;mirrors</code> <i>Number</i> ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;mirrorlog</code> <code>core</code>|<code>disk</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a COW snapshot LV of an origin LV<br />
 (also see &#8211;snapshot). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>snapshot</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>LV</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-s</code>|<code>&#8211;snapshot</code> ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a sparse COW snapshot LV of a virtual origin LV<br />
 (also see &#8211;snapshot). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>snapshot</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>-V</code>|<code>&#8211;virtualsize</code>&nbsp;<i>Size</i>[m|UNIT]&nbsp;<i>VG</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-s</code>|<code>&#8211;snapshot</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a sparse COW snapshot LV of a virtual origin LV. </p>
<p> <code>lvcreate</code> <code>-s</code>|<code>&#8211;snapshot</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>-V</code>|<code>&#8211;virtualsize</code>&nbsp;<i>Size</i>[m|UNIT]&nbsp;<i>VG</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>snapshot</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin pool (infers &#8211;type thin-pool). </p>
<p> <code>lvcreate</code> <code>-T</code>|<code>&#8211;thin</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>thin-pool</code> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin pool named by the &#8211;thinpool arg<br />
 (infers &#8211;type thin-pool). </p>
<p> <code>lvcreate</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <code>&#8211;thinpool</code> <i>LV</i><i>_new</i> <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>thin-pool</code> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a cache pool named by the &#8211;cachepool arg<br />
 (variant, uses &#8211;cachepool in place of &#8211;name). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>cache-pool</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>&#8211;cachepool</code>&nbsp;<i>LV</i><i>_new</i>&nbsp;<i>VG</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-H</code>|<code>&#8211;cache</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV in a thin pool. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>thin</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>&#8211;thinpool</code>&nbsp;<i>LV</i><i>_thinpool</i>&nbsp;<i>VG</i></dl>
<dl>
<dd>[ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a thin LV in a thin pool named in the first arg<br />
 (variant, also see &#8211;thinpool for naming pool). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>thin</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] <i>LV</i><i>_thinpool</i> </p>
<dl>
<dd>[ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a thin LV in the thin pool named in the first arg<br />
 (variant, infers &#8211;type thin, also see &#8211;thinpool for<br />
 naming pool.) </p>
<p> <code>lvcreate</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] <i>LV</i><i>_thinpool</i> </p>
<dl>
<dd>[ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>&#8211;type</code> <code>thin</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a thin LV that is a snapshot of an existing thin LV. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>thin</code> <i>LV</i><i>_thin</i> </p>
<dl>
<dd>[ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a thin LV that is a snapshot of an existing thin LV<br />
 (infers &#8211;type thin). </p>
<p> <code>lvcreate</code> <code>-T</code>|<code>&#8211;thin</code> <i>LV</i><i>_thin</i> </p>
<dl>
<dd>[ <code>&#8211;type</code> <code>thin</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a thin LV that is a snapshot of an external origin LV<br />
 (infers &#8211;type thin). </p>
<p> <code>lvcreate</code> <code>-s</code>|<code>&#8211;snapshot</code> <code>&#8211;thinpool</code> <i>LV</i><i>_thinpool</i> <i>LV</i> </p>
<dl>
<dd>[ <code>&#8211;type</code> <code>thin</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Create a VDO LV with VDO pool. </p>
<p> <code>lvcreate</code> <code>&#8211;vdo</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;vdopool</code> <i>LV</i><i>_new</i> ]<br />
 [ <code>&#8211;compression</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;deduplication</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a VDO LV with VDO pool. </p>
<p> <code>lvcreate</code> <code>&#8211;vdopool</code> <i>LV</i><i>_new</i> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;vdo</code> ]<br />
 [ <code>&#8211;type</code> <code>vdo</code> ]<br />
 [ <code>&#8211;compression</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;deduplication</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV, first creating a thin pool for it,<br />
 where the new thin pool is named by the &#8211;thinpool arg<br />
 (variant, infers &#8211;type thin). </p>
<p> <code>lvcreate</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>&#8211;thinpool</code>&nbsp;<i>LV</i><i>_new</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV, first creating a thin pool for it,<br />
 where the new thin pool is named by the &#8211;thinpool arg<br />
 (variant, infers &#8211;type thin). </p>
<p> <code>lvcreate</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>&#8211;thinpool</code>&nbsp;<i>LV</i><i>_new</i>&nbsp;<i>VG</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV, first creating a thin pool for it,<br />
 where the new thin pool is named in the first arg,<br />
 or the new thin pool name is generated when the first<br />
 arg is a VG name. </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>thin</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>-L</code>|<code>&#8211;size</code>&nbsp;<i>Size</i>[m|UNIT]&nbsp;<i>VG</i>|<i>LV</i><i>_new</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV, first creating a thin pool for it,<br />
 where the new thin pool is named in the first arg,<br />
 or the new thin pool name is generated when the first<br />
 arg is a VG name (variant, infers &#8211;type thin). </p>
<p> <code>lvcreate</code> <code>-T</code>|<code>&#8211;thin</code> <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT]</p>
<dl>
<dd>&nbsp;<code>-L</code>|<code>&#8211;size</code>&nbsp;<i>Size</i>[m|UNIT]&nbsp;<i>VG</i>|<i>LV</i><i>_new</i></dl>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a thin LV, first creating a thin pool for it<br />
 (infers &#8211;type thin).<br />
 Create a sparse snapshot of a virtual origin LV<br />
 (infers &#8211;type snapshot).<br />
 Chooses &#8211;type thin or &#8211;type snapshot according to<br />
 config setting sparse_segtype_default. </p>
<p> <code>lvcreate</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-s</code>|<code>&#8211;snapshot</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>snapshot</code> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;errorwhenfull</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a cache LV, first creating a new origin LV,<br />
 then combining it with the existing cache pool named<br />
 by the &#8211;cachepool arg (variant, infers &#8211;type cache). </p>
<p> <code>lvcreate</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <code>&#8211;cachepool</code> <i>LV</i><i>_cachepool</i> <i>VG</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-H</code>|<code>&#8211;cache</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>cache</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Create a cache LV, first creating a new origin LV,<br />
 then combining it with the existing cache pool named<br />
 in the first arg (variant, also use &#8211;cachepool). </p>
<p> <code>lvcreate</code> <code>&#8211;type</code> <code>cache</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>LV</i><i>_cachepool</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-H</code>|<code>&#8211;cache</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> When LV is a cache pool, create a cache LV,<br />
 first creating a new origin LV, then combining it with<br />
 the existing cache pool named in the first arg<br />
 (variant, infers &#8211;type cache, also use &#8211;cachepool).<br />
 When LV is not a cache pool, convert the specified LV<br />
 to type cache after creating a new cache pool LV to use<br />
 (use lvconvert). </p>
<p> <code>lvcreate</code> <code>-H</code>|<code>&#8211;cache</code> <code>-L</code>|<code>&#8211;size</code> <i>Size</i>[m|UNIT] <i>LV</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> <i>Number</i>[PERCENT] ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211;</p>
<h2>Examples</h2>
<p>Create a striped LV with 3 stripes, a stripe size of 8KiB and a size of 100MiB. The LV name is chosen by lvcreate.<br />
 <code>lvcreate -i 3 -I 8 -L 100m vg00</code> </p>
<p> Create a raid1 LV with two images, and a useable size of 500 MiB. This operation requires two devices, one for each mirror image. RAID metadata (superblock and bitmap) is also included on the two devices.<br />
 <code>lvcreate &#8211;type raid1 -m1 -L 500m -n mylv vg00</code> </p>
<p> Create a mirror LV with two images, and a useable size of 500 MiB. This operation requires three devices: two for mirror images and one for a disk log.<br />
 <code>lvcreate &#8211;type mirror -m1 -L 500m -n mylv vg00</code> </p>
<p> Create a mirror LV with 2 images, and a useable size of 500 MiB. This operation requires 2 devices because the log is in memory.<br />
 <code>lvcreate &#8211;type mirror -m1 &#8211;mirrorlog core -L 500m -n mylv vg00</code> </p>
<p> Create a copy-on-write snapshot of an LV:<br />
 <code>lvcreate &#8211;snapshot &#8211;size 100m &#8211;name mysnap vg00/mylv</code> </p>
<p> Create a copy-on-write snapshot with a size sufficient for overwriting 20% of the size of the original LV.<br />
 <code>lvcreate -s -l 20%ORIGIN -n mysnap vg00/mylv</code> </p>
<p> Create a sparse LV with 1TiB of virtual space, and actual space just under 100MiB.<br />
 <code>lvcreate &#8211;snapshot &#8211;virtualsize 1t &#8211;size 100m &#8211;name mylv vg00</code> </p>
<p> Create a linear LV with a usable size of 64MiB on specific physical extents.<br />
 <code>lvcreate -L 64m -n mylv vg00 /dev/sda:0-7 /dev/sdb:0-7</code> </p>
<p> Create a RAID5 LV with a usable size of 5GiB, 3 stripes, a stripe size of 64KiB, using a total of 4 devices (including one for parity).<br />
 <code>lvcreate &#8211;type raid5 -L 5G -i 3 -I 64 -n mylv vg00</code> </p>
<p> Create a RAID5 LV using all of the free space in the VG and spanning all the PVs in the VG (note that the command will fail if there are more than 8 PVs in the VG, in which case <code>-i 7</code> must be used to get to the current maximum of 8 devices including parity for RaidLVs).<br />
 <code>lvcreate &#8211;config allocation/raid_stripe_all_devices=1</code></p>
<dl>
<dd><code>&#8211;type raid5 -l 100%FREE -n mylv vg00</code></dl>
<p> Create RAID10 LV with a usable size of 5GiB, using 2 stripes, each on a two-image mirror. (Note that the <code>-i</code> and <code>-m</code> arguments behave differently: <code>-i</code> specifies the total number of stripes, but <code>-m</code> specifies the number of images in addition to the first image).<br />
 <code>lvcreate &#8211;type raid10 -L 5G -i 2 -m 1 -n mylv vg00</code> </p>
<p> Create a 1TiB thin LV mythin, with 256GiB thinpool tpool0 in vg00.<br />
 <code>lvcreate &#8211;T &#8211;size 256G &#8211;name mythin vg00/tpool0</code> </p>
<p> Create a 1TiB thin LV, first creating a new thin pool for it, where the thin pool has 100MiB of space, uses 2 stripes, has a 64KiB stripe size, and 256KiB chunk size.<br />
 <code>lvcreate &#8211;type thin &#8211;name mylv &#8211;thinpool mypool</code></p>
<dl>
<dd><code>-V 1t -L 100m -i 2 -I 64 -c 256 vg00</code></dl>
<p> Create a thin snapshot of a thin LV (the size option must not be used, otherwise a copy-on-write snapshot would be created).<br />
 <code>lvcreate &#8211;snapshot &#8211;name mysnap vg00/thinvol</code> </p>
<p> Create a thin snapshot of the read-only inactive LV named &quot;origin&quot; which becomes an external origin for the thin snapshot LV.<br />
 <code>lvcreate &#8211;snapshot &#8211;name mysnap &#8211;thinpool mypool vg00/origin</code> </p>
<p> Create a cache pool from a fast physical device. The cache pool can then be used to cache an LV.<br />
 <code>lvcreate &#8211;type cache-pool -L 1G -n my_cpool vg00 /dev/fast1</code> </p>
<p> Create a cache LV, first creating a new origin LV on a slow physical device, then combining the new origin LV with an existing cache pool.<br />
 <code>lvcreate &#8211;type cache &#8211;cachepool my_cpool</code></p>
<dl>
<dd><code>-L 100G -n mylv vg00 /dev/slow1</code></dl>
<p> Create a VDO LV vdo0 with VDOPoolLV size of 10GiB and name vpool1.<br />
 <code>lvcreate &#8211;vdo &#8211;size 10G &#8211;name vdo0 vg00/vpool1</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
