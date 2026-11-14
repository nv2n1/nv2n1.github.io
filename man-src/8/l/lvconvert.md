---
title: "lvconvert(8)"
name: "lvconvert"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvconvert/"
description: "lvconvert – Change logical volume layout"
---

<p>lvconvert &#8211; Change logical volume layout</p>
<h2>Synopsis</h2>
<p><code>lvconvert</code> <i>option_args</i> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>position_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;alloc</code>&nbsp;<code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> </p>
<p>&nbsp;<code>-b</code>|<code>&#8211;background</code> </p>
<p>&nbsp;<code>-H</code>|<code>&#8211;cache</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachemetadataformat</code>&nbsp;<code>auto</code>|<code>1</code>|<code>2</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachemode</code>&nbsp;<code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachepolicy</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachepool</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachesettings</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;cachevol</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<code>-c</code>|<code>&#8211;chunksize</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;commandprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;compression</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;config</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-d</code>|<code>&#8211;debug</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;deduplication</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;discards</code>&nbsp;<code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;driverloaded</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-f</code>|<code>&#8211;force</code> </p>
<p>&nbsp;<code>-h</code>|<code>&#8211;help</code> </p>
<p>&nbsp;<code>-i</code>|<code>&#8211;interval</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockopt</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;longhelp</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;merge</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;mergemirrors</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;mergesnapshot</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;mergethin</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;metadataprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;mirrorlog</code>&nbsp;<code>core</code>|<code>disk</code> </p>
<p>&nbsp;<code>-m</code>|<code>&#8211;mirrors</code>&nbsp;[<code>+</code>|<code>&#8211;</code>]<i>Number</i> </p>
<p>&nbsp;<code>-n</code>|<code>&#8211;name</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nolocking</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;noudevsync</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;originname</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poolmetadata</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poolmetadatasize</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poolmetadataspare</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-q</code>|<code>&#8211;quiet</code> </p>
<p>&nbsp;<code>-r</code>|<code>&#8211;readahead</code>&nbsp;<code>auto</code>|<code>none</code>|<i>Number</i> </p>
<p>&nbsp;<code>-R</code>|<code>&#8211;regionsize</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;repair</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;replace</code>&nbsp;<i>PV</i> </p>
<p>&nbsp;<code>-s</code>|<code>&#8211;snapshot</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;splitcache</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;splitmirrors</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;splitsnapshot</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;startpoll</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;stripes</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<code>-I</code>|<code>&#8211;stripesize</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;swapmetadata</code> </p>
<p>&nbsp;<code>-t</code>|<code>&#8211;test</code> </p>
<p>&nbsp;<code>-T</code>|<code>&#8211;thin</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;thinpool</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;trackchanges</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;type</code>&nbsp;<code>linear</code>|<code>striped</code>|<code>snapshot</code>|<code>mirror</code>|<code>raid</code>|<code>thin</code>|<code>cache</code>|<code>vdo</code>|<code>thin-pool</code>|<code>cache-pool</code>|<code>vdo-pool</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;uncache</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;usepolicies</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;vdopool</code>&nbsp;<i>LV</i> </p>
<p>&nbsp;<code>-v</code>|<code>&#8211;verbose</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;version</code> </p>
<p>&nbsp;<code>-V</code>|<code>&#8211;virtualsize</code>&nbsp;<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<code>-y</code>|<code>&#8211;yes</code> </p>
<p>&nbsp;<code>-Z</code>|<code>&#8211;zero</code>&nbsp;<code>y</code>|<code>n</code></p>
<h2>Description</h2>
<p>lvconvert changes the LV type and includes utilities for LV data maintenance. The LV type controls data layout and redundancy. The LV type is also called the segment type or segtype. </p>
<p> To display the current LV type, run the command: </p>
<p> <code>lvs -o name,segtype</code> <i>LV</i> </p>
<p> In some cases, an LV is a single device mapper (dm) layer above physical devices. In other cases, hidden LVs (dm devices) are layered between the visible LV and physical devices. LVs in the middle layers are called sub LVs. A command run on a visible LV sometimes operates on a sub LV rather than the specified LV. In other cases, a sub LV must be specified directly on the command line. </p>
<p> Sub LVs can be displayed with the command: </p>
<p> <code>lvs -a</code> </p>
<p> The <code>linear</code> type is equivalent to the <code>striped</code> type when one stripe exists. In that case, the types can sometimes be used interchangably. </p>
<p> In most cases, the <code>mirror</code> type is deprecated and the <code>raid1</code> type should be used. They are both implementations of mirroring. </p>
<p> Striped raid types are <code>raid0/raid0_meta</code>, <code>raid5</code> (an alias for raid5_ls), <code>raid6</code> (an alias for raid6_zr) and <code>raid10</code> (an alias for raid10_near). </p>
<p> As opposed to mirroring, raid5 and raid6 stripe data and calculate parity blocks. The parity blocks can be used for data block recovery in case devices fail. A maximum number of one device in a raid5 LV may fail, and two in case of raid6. Striped raid types typically rotate the parity and data blocks for performance reasons, thus avoiding contention on a single device. Specific arrangements of parity and data blocks (layouts) can be used to optimize I/O performance, or to convert between raid levels. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information. </p>
<p> Layouts of raid5 rotating parity blocks can be: left-asymmetric (raid5_la), left-symmetric (raid5_ls with alias raid5), right-asymmetric (raid5_ra), right-symmetric (raid5_rs) and raid5_n, which doesn&#8217;t rotate parity blocks. Layouts of raid6 are: zero-restart (raid6_zr with alias raid6), next-restart (raid6_nr), and next-continue (raid6_nc). </p>
<p> Layouts including _n allow for conversion between raid levels (raid5_n to raid6 or raid5_n to striped/raid0/raid0_meta). Additionally, special raid6 layouts for raid level conversions between raid5 and raid6 are: raid6_ls_6, raid6_rs_6, raid6_la_6 and raid6_ra_6. Those correspond to their raid5 counterparts (e.g. raid5_rs can be directly converted to raid6_rs_6 and vice-versa). </p>
<p> raid10 (an alias for raid10_near) is currently limited to one data copy and even number of sub LVs. This is a mirror group layout, thus a single sub LV may fail per mirror group without data loss. </p>
<p> Striped raid types support converting the layout, their stripesize and their number of stripes. </p>
<p> The striped raid types combined with raid1 allow for conversion from linear-&gt; striped/raid0/raid0_meta and vice-versa by e.g. linear &lt;-&gt; raid1 &lt;-&gt; raid5_n (then adding stripes) &lt;-&gt; striped/raid0/raid0_meta.</p>
<h2>Usage</h2>
<p>Convert LV to linear. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>linear</code> <i>LV</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert LV to striped. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>striped</code> <i>LV</i> </p>
<dl>
<dd>[ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ <code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert LV to type mirror (also see type raid1), </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>mirror</code> <i>LV</i> </p>
<dl>
<dd>[ <code>-m</code>|<code>&#8211;mirrors</code> [<code>+</code>|<code>&#8211;</code>]<i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ <code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>&#8211;mirrorlog</code> <code>core</code>|<code>disk</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert LV to raid or change raid layout<br />
 (a specific raid level must be used, e.g. raid1). </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>raid</code> <i>LV</i> </p>
<dl>
<dd>[ <code>-m</code>|<code>&#8211;mirrors</code> [<code>+</code>|<code>&#8211;</code>]<i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ <code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert LV to raid1 or mirror, or change number of mirror images. </p>
<p> <code>lvconvert</code> <code>-m</code>|<code>&#8211;mirrors</code> [<code>+</code>|<code>&#8211;</code>]<i>Number</i> <i>LV</i> </p>
<dl>
<dd>[ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ <code>&#8211;mirrorlog</code> <code>core</code>|<code>disk</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert raid LV to change number of stripe images. </p>
<p> <code>lvconvert</code> <code>&#8211;stripes</code> <i>Number</i> <i>LV</i><i>_raid</i> </p>
<dl>
<dd>[ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert raid LV to change the stripe size. </p>
<p> <code>lvconvert</code> <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] <i>LV</i><i>_raid</i> </p>
<dl>
<dd>[ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Split images from a raid1 or mirror LV and use them to create a new LV. </p>
<p> <code>lvconvert</code> <code>&#8211;splitmirrors</code> <i>Number</i> <code>-n</code>|<code>&#8211;name</code> <i>LV</i><i>_new</i> <i>LV</i><i>_cache_mirror_raid1</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Split images from a raid1 LV and track changes to origin for later merge. </p>
<p> <code>lvconvert</code> <code>&#8211;splitmirrors</code> <i>Number</i> <code>&#8211;trackchanges</code> <i>LV</i><i>_cache_raid1</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Merge LV images that were split from a raid1 LV. </p>
<p> <code>lvconvert</code> <code>&#8211;mergemirrors</code> <i>VG</i>|<i>LV</i><i>_linear_raid</i>|<i>Tag</i> &#8230; </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Convert LV to a thin LV, using the original LV as an external origin. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>thin</code> <code>&#8211;thinpool</code> <i>LV</i> <i>LV</i><i>_linear_striped_thin_cache_raid</i> </p>
<dl>
<dd>[ <code>-T</code>|<code>&#8211;thin</code> ]<br />
 [ <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;originname</code> <i>LV</i><i>_new</i> ]<br />
 [ <code>&#8211;poolmetadata</code> <i>LV</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Attach a cache pool to an LV, converts the LV to type cache. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>cache</code> <code>&#8211;cachepool</code> <i>LV</i> <i>LV</i><i>_linear_striped_thinpool_vdo_vdopool_vdopooldata_raid</i> </p>
<dl>
<dd>[ <code>-H</code>|<code>&#8211;cache</code> ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;poolmetadata</code> <i>LV</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Attach a writecache to an LV, converts the LV to type writecache. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>writecache</code> <code>&#8211;cachevol</code> <i>LV</i> <i>LV</i><i>_linear_striped_raid</i> </p>
<dl>
<dd>[ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Attach a cache to an LV, converts the LV to type cache. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>cache</code> <code>&#8211;cachevol</code> <i>LV</i> <i>LV</i><i>_linear_striped_thinpool_raid</i> </p>
<dl>
<dd>[ <code>-H</code>|<code>&#8211;cache</code> ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Convert LV to type thin-pool. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>thin-pool</code> <i>LV</i><i>_linear_striped_cache_raid</i> </p>
<dl>
<dd>[ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>&#8211;discards</code> <code>passdown</code>|<code>nopassdown</code>|<code>ignore</code> ]<br />
 [ <code>&#8211;poolmetadata</code> <i>LV</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert LV to type cache-pool. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>cache-pool</code> <i>LV</i><i>_linear_striped_raid</i> </p>
<dl>
<dd>[ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;poolmetadata</code> <i>LV</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert LV to type vdopool. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>vdo-pool</code> <i>LV</i><i>_linear_striped_cache_raid</i> </p>
<dl>
<dd>[ <code>-n</code>|<code>&#8211;name</code> <i>LV</i><i>_new</i> ]<br />
 [ <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;compression</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;deduplication</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Detach a cache from an LV. </p>
<p> <code>lvconvert</code> <code>&#8211;splitcache</code> <i>LV</i><i>_thinpool_cache_cachepool_vdopool_writecache</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Merge thin LV into its origin LV. </p>
<p> <code>lvconvert</code> <code>&#8211;mergethin</code> <i>LV</i><i>_thin</i> &#8230; </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Merge COW snapshot LV into its origin. </p>
<p> <code>lvconvert</code> <code>&#8211;mergesnapshot</code> <i>LV</i><i>_snapshot</i> &#8230; </p>
<dl>
<dd>[ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Combine a former COW snapshot (second arg) with a former<br />
 origin LV (first arg) to reverse a splitsnapshot command. </p>
<p> <code>lvconvert</code> <code>&#8211;type</code> <code>snapshot</code> <i>LV</i> <i>LV</i><i>_linear_striped</i> </p>
<dl>
<dd>[ <code>-s</code>|<code>&#8211;snapshot</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Replace failed PVs in a raid or mirror LV.<br />
 Repair a thin pool.<br />
 Repair a cache pool. </p>
<p> <code>lvconvert</code> <code>&#8211;repair</code> <i>LV</i><i>_thinpool_cache_cachepool_mirror_raid</i> </p>
<dl>
<dd>[ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ <code>&#8211;usepolicies</code> ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Replace specific PV(s) in a raid LV with another PV. </p>
<p> <code>lvconvert</code> <code>&#8211;replace</code> <i>PV</i> <i>LV</i><i>_raid</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Poll LV to continue conversion. </p>
<p> <code>lvconvert</code> <code>&#8211;startpoll</code> <i>LV</i><i>_mirror_raid</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Common options for command:</p>
<dl>
<dd>[ <code>-b</code>|<code>&#8211;background</code> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>&#8211;alloc</code> <code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]</dl>
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
<dt> <code>&#8211;alloc</code> <code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code></p>
<dd>
<dd>Determines the allocation policy when a command needs to allocate Physical Extents (PEs) from the VG. Each VG and LV has an allocation policy which can be changed with vgchange/lvchange, or overriden on the command line. <code>normal</code> applies common sense rules such as not placing parallel stripes on the same PV. <code>inherit</code> applies the VG policy to an LV. <code>contiguous</code> requires new PEs be placed adjacent to existing PEs. <code>cling</code> places new PEs on the same PV as existing PEs in the same stripe of the LV. If there are sufficient PEs for an allocation, but normal does not use them, <code>anywhere</code> will use them even if it reduces performance, e.g. by placing two stripes on the same PV. Optional positional PV args on the command line can also be used to limit which PVs the command will use for allocation. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for more information about allocation.</p>
<dt> <code>-b</code>|<code>&#8211;background</code></p>
<dd>
<dd>If the operation requires polling, this option causes the command to return before the operation is complete, and polling is done in the background.</p>
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
<dt> <code>&#8211;cachevol</code> <i>LV</i></p>
<dd>
<dd>The name of a cache volume.</p>
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
<dt> <code>-f</code>|<code>&#8211;force</code> &#8230;</p>
<dd>
<dd>Override various checks, confirmations and protections. Use with extreme caution.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display help text.</p>
<dt> <code>-i</code>|<code>&#8211;interval</code> <i>Number</i></p>
<dd>
<dd>Report progress at regular intervals.</p>
<dt> <code>&#8211;lockopt</code> <i>String</i></p>
<dd>
<dd>Used to pass options for special cases to lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;longhelp</code></p>
<dd>
<dd>Display long help text.</p>
<dt> <code>&#8211;merge</code></p>
<dd>
<dd>An alias for &#8211;mergethin, &#8211;mergemirrors, or &#8211;mergesnapshot, depending on the type of LV.</p>
<dt> <code>&#8211;mergemirrors</code></p>
<dd>
<dd>Merge LV images that were split from a raid1 LV. See &#8211;splitmirrors with &#8211;trackchanges.</p>
<dt> <code>&#8211;mergesnapshot</code></p>
<dd>
<dd>Merge COW snapshot LV into its origin. When merging a snapshot, if both the origin and snapshot LVs are not open, the merge will start immediately. Otherwise, the merge will start the first time either the origin or snapshot LV are activated and both are closed. Merging a snapshot into an origin that cannot be closed, for example a root filesystem, is deferred until the next time the origin volume is activated. When merging starts, the resulting LV will have the origin&#8217;s name, minor number and UUID. While the merge is in progress, reads or writes to the origin appear as being directed to the snapshot being merged. When the merge finishes, the merged snapshot is removed. Multiple snapshots may be specified on the command line or a @tag may be used to specify multiple snapshots be merged to their respective origin.</p>
<dt> <code>&#8211;mergethin</code></p>
<dd>
<dd>Merge thin LV into its origin LV. The origin thin LV takes the content of the thin snapshot, and the thin snapshot LV is removed. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information.</p>
<dt> <code>&#8211;metadataprofile</code> <i>String</i></p>
<dd>
<dd>The metadata profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;mirrorlog</code> <code>core</code>|<code>disk</code></p>
<dd>
<dd>Specifies the type of mirror log for LVs with the &quot;mirror&quot; type (does not apply to the &quot;raid1&quot; type.) <code>disk</code> is a persistent log and requires a small amount of storage space, usually on a separate device from the data being mirrored. <code>core</code> is not persistent; the log is kept only in memory. In this case, the mirror must be synchronized (by copying LV data from the first device to others) each time the LV is activated, e.g. after reboot. <code>mirrored</code> is a persistent log that is itself mirrored, but should be avoided. Instead, use the raid1 type for log redundancy.</p>
<dt> <code>-m</code>|<code>&#8211;mirrors</code> [<code>+</code>|<code>&#8211;</code>]<i>Number</i></p>
<dd>
<dd>Specifies the number of mirror images in addition to the original LV image, e.g. &#8211;mirrors 1 means there are two images of the data, the original and one mirror image. Optional positional PV args on the command line can specify the devices the images should be placed on. There are two mirroring implementations: &quot;raid1&quot; and &quot;mirror&quot;. These are the names of the corresponding LV types, or &quot;segment types&quot;. Use the &#8211;type option to specify which to use (raid1 is default, and mirror is legacy) Use lvm.conf global/mirror_segtype_default and global/raid10_segtype_default to configure the default types. The plus prefix <code>+</code> can be used, in which case the number is added to the current number of images, or the minus prefix <code>&#8211;</code> can be used, in which case the number is subtracted from the current number of images. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
<dt> <code>-n</code>|<code>&#8211;name</code> <i>String</i></p>
<dd>
<dd>Specifies the name of a new LV. When unspecified, a default name of &quot;lvol#&quot; is generated, where # is a number generated by LVM.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;noudevsync</code></p>
<dd>
<dd>Disables udev synchronisation. The process will not wait for notification from udev. It will continue irrespective of any possible udev processing in the background. Only use this if udev is not running or has rules that ignore the devices LVM creates.</p>
<dt> <code>&#8211;originname</code> <i>LV</i></p>
<dd>
<dd>Specifies the name to use for the external origin LV when converting an LV to a thin LV. The LV being converted becomes a read-only external origin with this name.</p>
<dt> <code>&#8211;poolmetadata</code> <i>LV</i></p>
<dd>
<dd>The name of a an LV to use for storing pool metadata.</p>
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
<dt> <code>&#8211;repair</code></p>
<dd>
<dd>Replace failed PVs in a raid or mirror LV, or run a repair utility on a thin pool. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) and <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information.</p>
<dt> <code>&#8211;replace</code> <i>PV</i></p>
<dd>
<dd>Replace a specific PV in a raid LV with another PV. The new PV to use can be optionally specified after the LV. Multiple PVs can be replaced by repeating this option. See <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) for more information.</p>
<dt> <code>-s</code>|<code>&#8211;snapshot</code></p>
<dd>
<dd>Combine a former COW snapshot LV with a former origin LV to reverse a previous &#8211;splitsnapshot command.</p>
<dt> <code>&#8211;splitcache</code></p>
<dd>
<dd>Separates a cache pool from a cache LV, and keeps the unused cache pool LV. Before the separation, the cache is flushed. Also see &#8211;uncache.</p>
<dt> <code>&#8211;splitmirrors</code> <i>Number</i></p>
<dd>
<dd>Splits the specified number of images from a raid1 or mirror LV and uses them to create a new LV. If &#8211;trackchanges is also specified, changes to the raid1 LV are tracked while the split LV remains detached. If &#8211;name is specified, then the images are permanently split from the original LV and changes are not tracked.</p>
<dt> <code>&#8211;splitsnapshot</code></p>
<dd>
<dd>Separates a COW snapshot from its origin LV. The LV that is split off contains the chunks that differ from the origin LV along with metadata describing them. This LV can be wiped and then destroyed with lvremove.</p>
<dt> <code>&#8211;startpoll</code></p>
<dd>
<dd>Start polling an LV to continue processing a conversion.</p>
<dt> <code>&#8211;stripes</code> <i>Number</i></p>
<dd>
<dd>Specifies the number of stripes in a striped LV. This is the number of PVs (devices) that a striped LV is spread across. Data that appears sequential in the LV is spread across multiple devices in units of the stripe size (see &#8211;stripesize). This does not apply to existing allocated space, only newly allocated space can be striped.</p>
<dt> <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>The amount of data that is written to one device before moving to the next in a striped LV.</p>
<dt> <code>&#8211;swapmetadata</code></p>
<dd>
<dd>Extracts the metadata LV from a pool and replaces it with another specified LV. The extracted LV is preserved and given the name of the LV that replaced it. Use for repair only. When the metadata LV is swapped out of the pool, it can be activated directly and used with thin provisioning tools: <code><a href="/docs/linux/man/8-cache_dump/">cache_dump</a></code>(8), <code><a href="/docs/linux/man/8-cache_repair/">cache_repair</a></code>(8), <code><a href="/docs/linux/man/8-cache_restore/">cache_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8).</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>-T</code>|<code>&#8211;thin</code></p>
<dd>
<dd>Specifies the command is handling a thin LV or thin pool. See &#8211;type thin, &#8211;type thin-pool, and &#8211;virtualsize. See <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) for more information about LVM thin provisioning.</p>
<dt> <code>&#8211;thinpool</code> <i>LV</i></p>
<dd>
<dd>The name of a thin pool LV.</p>
<dt> <code>&#8211;trackchanges</code></p>
<dd>
<dd>Can be used with &#8211;splitmirrors on a raid1 LV. This causes changes to the original raid1 LV to be tracked while the split images remain detached. This is a temporary state that allows the read-only detached image to be merged efficiently back into the raid1 LV later. Only the regions with changed data are resynchronized during merge. While a raid1 LV is tracking changes, operations on it are limited to merging the split image (see &#8211;mergemirrors) or permanently splitting the image (see &#8211;splitmirrors with &#8211;name.</p>
<dt> <code>&#8211;type</code> <code>linear</code>|<code>striped</code>|<code>snapshot</code>|<code>mirror</code>|<code>raid</code>|<code>thin</code>|<code>cache</code>|<code>vdo</code>|<code>thin-pool</code>|<code>cache-pool</code>|<code>vdo-pool</code></p>
<dd>
<dd>The LV type, also known as &quot;segment type&quot; or &quot;segtype&quot;. See usage descriptions for the specific ways to use these types. For more information about redundancy and performance (<code>raid</code>&lt;N&gt;, <code>mirror</code>, <code>striped</code>, <code>linear</code>) see <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7). For thin provisioning (<code>thin</code>, <code>thin-pool</code>) see <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7). For performance caching (<code>cache</code>, <code>cache-pool</code>) see <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7). For copy-on-write snapshots (<code>snapshot</code>) see usage definitions. For VDO (<code>vdo</code>) see <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7). Several commands omit an explicit type option because the type is inferred from other options or shortcuts (e.g. &#8211;stripes, &#8211;mirrors, &#8211;snapshot, &#8211;virtualsize, &#8211;thin, &#8211;cache, &#8211;vdo). Use inferred types with care because it can lead to unexpected results.</p>
<dt> <code>&#8211;uncache</code></p>
<dd>
<dd>Separates a cache pool from a cache LV, and deletes the unused cache pool LV. Before the separation, the cache is flushed. Also see &#8211;splitcache.</p>
<dt> <code>&#8211;usepolicies</code></p>
<dd>
<dd>Perform an operation according to the policy configured in lvm.conf or a profile.</p>
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
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</p>
<dt> <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>For snapshots, this controls zeroing of the first 4KiB of data in the snapshot. If the LV is read-only, the snapshot will not be zeroed. For thin pools, this controls zeroing of provisioned blocks. Provisioning of large zeroed chunks negatively impacts performance.</dl>
<h2>Variables</h2>
<dl>
<dt> <i>VG</i></p>
<dd>
<dd>Volume Group name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names.</p>
<dt> <i>LV</i></p>
<dd>
<dd>Logical Volume name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names. An LV positional arg generally includes the VG name and LV name, e.g. VG/LV. LV followed by _&lt;type&gt; indicates that an LV of the given type is required. (raid represents raid&lt;N&gt; type)</p>
<dt> <i>PV</i></p>
<dd>
<dd>Physical Volume name, a device path under /dev. For commands managing physical extents, a PV positional arg generally accepts a suffix indicating a range (or multiple ranges) of physical extents (PEs). When the first PE is omitted, it defaults to the start of the device, and when the last PE is omitted it defaults to end. Start and end range (inclusive): <i>PV</i>[<code>:</code><i>PE</i><code>&#8211;</code><i>PE</i>]&#8230; Start and length range (counting from 0): <i>PV</i>[<code>:</code><i>PE</i><code>+</code><i>PE</i>]&#8230;</p>
<dt> <i>Tag</i></p>
<dd>
<dd>Tag name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tag names and using tags in place of a VG, LV or PV.</p>
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
<p> Change the region size of an LV. </p>
<p> <code>lvconvert</code> <code>-R</code>|<code>&#8211;regionsize</code> <i>Size</i>[m|UNIT] <i>LV</i><i>_raid</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Change the type of mirror log used by a mirror LV. </p>
<p> <code>lvconvert</code> <code>&#8211;mirrorlog</code> <code>core</code>|<code>disk</code> <i>LV</i><i>_mirror</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Convert LV to a thin LV, using the original LV as an external origin<br />
 (infers &#8211;type thin). </p>
<p> <code>lvconvert</code> <code>-T</code>|<code>&#8211;thin</code> <code>&#8211;thinpool</code> <i>LV</i> <i>LV</i><i>_linear_striped_thin_cache_raid</i> </p>
<dl>
<dd>[ <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;type</code> <code>thin</code> ]<br />
 [ <code>&#8211;originname</code> <i>LV</i><i>_new</i> ]<br />
 [ <code>&#8211;poolmetadata</code> <i>LV</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Attach a cache pool to an LV (infers &#8211;type cache). </p>
<p> <code>lvconvert</code> <code>-H</code>|<code>&#8211;cache</code> <code>&#8211;cachepool</code> <i>LV</i> <i>LV</i><i>_linear_striped_thinpool_vdo_vdopool_vdopooldata_raid</i> </p>
<dl>
<dd>[ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-r</code>|<code>&#8211;readahead</code> <code>auto</code>|<code>none</code>|<i>Number</i> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>cache</code> ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;poolmetadata</code> <i>LV</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;poolmetadataspare</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Attach a cache to an LV, converts the LV to type cache. </p>
<p> <code>lvconvert</code> <code>-H</code>|<code>&#8211;cache</code> <code>&#8211;cachevol</code> <i>LV</i> <i>LV</i><i>_linear_striped_thinpool_raid</i> </p>
<dl>
<dd>[ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;cachemetadataformat</code> <code>auto</code>|<code>1</code>|<code>2</code> ]<br />
 [ <code>&#8211;cachemode</code> <code>writethrough</code>|<code>writeback</code>|<code>passthrough</code> ]<br />
 [ <code>&#8211;cachepolicy</code> <i>String</i> ]<br />
 [ <code>&#8211;cachesettings</code> <i>String</i> ]<br />
 [ <code>&#8211;poolmetadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Convert LV to type vdopool. </p>
<p> <code>lvconvert</code> <code>&#8211;vdopool</code> <i>LV</i><i>_linear_striped_cache_raid</i> </p>
<dl>
<dd>[ <code>-n</code>|<code>&#8211;name</code> <i>LV</i><i>_new</i> ]<br />
 [ <code>-V</code>|<code>&#8211;virtualsize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;type</code> <code>vdo-pool</code> ]<br />
 [ <code>&#8211;compression</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;deduplication</code> <code>y</code>|<code>n</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Detach and delete a cache from an LV. </p>
<p> <code>lvconvert</code> <code>&#8211;uncache</code> <i>LV</i><i>_thinpool_cache_vdopool_writecache</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Swap metadata LV in a thin pool or cache pool (for repair only). </p>
<p> <code>lvconvert</code> <code>&#8211;swapmetadata</code> <code>&#8211;poolmetadata</code> <i>LV</i> <i>LV</i><i>_thinpool_cachepool</i> </p>
<dl>
<dd>[ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Merge LV that was split from a mirror (variant, use &#8211;mergemirrors).<br />
 Merge thin LV into its origin LV (variant, use &#8211;mergethin).<br />
 Merge COW snapshot LV into its origin (variant, use &#8211;mergesnapshot). </p>
<p> <code>lvconvert</code> <code>&#8211;merge</code> <i>VG</i>|<i>LV</i><i>_linear_striped_snapshot_thin_raid</i>|<i>Tag</i> &#8230; </p>
<dl>
<dd>[ <code>-i</code>|<code>&#8211;interval</code> <i>Number</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Separate a COW snapshot from its origin LV. </p>
<p> <code>lvconvert</code> <code>&#8211;splitsnapshot</code> <i>LV</i><i>_snapshot</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Combine a former COW snapshot (second arg) with a former<br />
 origin LV (first arg) to reverse a splitsnapshot command. </p>
<p> <code>lvconvert</code> <code>-s</code>|<code>&#8211;snapshot</code> <i>LV</i> <i>LV</i><i>_linear_striped</i> </p>
<dl>
<dd>[ <code>-c</code>|<code>&#8211;chunksize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;type</code> <code>snapshot</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Poll LV to continue conversion (also see &#8211;startpoll)<br />
 or waits till conversion/mirror syncing is finished </p>
<p> <code>lvconvert</code> <i>LV</i><i>_mirror_raid</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211;</p>
<h2>Notes</h2>
<p>This previous command syntax would perform two different operations:<br />
 <code>lvconvert &#8211;thinpool</code> <i>LV1</i> <code>&#8211;poolmetadata</code> <i>LV2</i><br />
 If LV1 was not a thin pool, the command would convert LV1 to a thin pool, optionally using a specified LV for metadata. But, if LV1 was already a thin pool, the command would swap the current metadata LV with LV2 (for repair purposes.) </p>
<p> In the same way, this previous command syntax would perform two different operations:<br />
 <code>lvconvert &#8211;cachepool</code> <i>LV1</i> <code>&#8211;poolmetadata</code> <i>LV2</i><br />
 If LV1 was not a cache pool, the command would convert LV1 to a cache pool, optionally using a specified LV for metadata. But, if LV1 was already a cache pool, the command would swap the current metadata LV with LV2 (for repair purposes.)</p>
<h2>Examples</h2>
<p>Convert a linear LV to a two-way mirror LV.<br />
 <code>lvconvert &#8211;type mirror &#8211;mirrors 1 vg/lvol1</code> </p>
<p> Convert a linear LV to a two-way RAID1 LV.<br />
 <code>lvconvert &#8211;type raid1 &#8211;mirrors 1 vg/lvol1</code> </p>
<p> Convert a mirror LV to use an in-memory log.<br />
 <code>lvconvert &#8211;mirrorlog core vg/lvol1</code> </p>
<p> Convert a mirror LV to use a disk log.<br />
 <code>lvconvert &#8211;mirrorlog disk vg/lvol1</code> </p>
<p> Convert a mirror or raid1 LV to a linear LV.<br />
 <code>lvconvert &#8211;type linear vg/lvol1</code> </p>
<p> Convert a mirror LV to a raid1 LV with the same number of images.<br />
 <code>lvconvert &#8211;type raid1 vg/lvol1</code> </p>
<p> Convert a linear LV to a two-way mirror LV, allocating new extents from specific PV ranges.<br />
 <code>lvconvert &#8211;mirrors 1 vg/lvol1 /dev/sda:0-15 /dev/sdb:0-15</code> </p>
<p> Convert a mirror LV to a linear LV, freeing physical extents from a specific PV.<br />
 <code>lvconvert &#8211;type linear vg/lvol1 /dev/sda</code> </p>
<p> Split one image from a mirror or raid1 LV, making it a new LV.<br />
 <code>lvconvert &#8211;splitmirrors 1 &#8211;name lv_split vg/lvol1</code> </p>
<p> Split one image from a raid1 LV, and track changes made to the raid1 LV while the split image remains detached.<br />
 <code>lvconvert &#8211;splitmirrors 1 &#8211;trackchanges vg/lvol1</code> </p>
<p> Merge an image (that was previously created with &#8211;splitmirrors and &#8211;trackchanges) back into the original raid1 LV.<br />
 <code>lvconvert &#8211;mergemirrors vg/lvol1_rimage_1</code> </p>
<p> Replace PV /dev/sdb1 with PV /dev/sdf1 in a raid1/4/5/6/10 LV.<br />
 <code>lvconvert &#8211;replace /dev/sdb1 vg/lvol1 /dev/sdf1</code> </p>
<p> Replace 3 PVs /dev/sd[b-d]1 with PVs /dev/sd[f-h]1 in a raid1 LV.<br />
 <code>lvconvert &#8211;replace /dev/sdb1 &#8211;replace /dev/sdc1 &#8211;replace /dev/sdd1</code></p>
<dl>
<dd><code>vg/lvol1 /dev/sd[fgh]1</code></dl>
<p> Replace the maximum of 2 PVs /dev/sd[bc]1 with PVs /dev/sd[gh]1 in a raid6 LV.<br />
 <code>lvconvert &#8211;replace /dev/sdb1 &#8211;replace /dev/sdc1 vg/lvol1 /dev/sd[gh]1</code> </p>
<p> Convert an LV into a thin LV in the specified thin pool. The existing LV is used as an external read-only origin for the new thin LV.<br />
 <code>lvconvert &#8211;type thin &#8211;thinpool vg/tpool1 vg/lvol1</code> </p>
<p> Convert an LV into a thin LV in the specified thin pool. The existing LV is used as an external read-only origin for the new thin LV, and is renamed &quot;external&quot;.<br />
 <code>lvconvert &#8211;type thin &#8211;thinpool vg/tpool1</code></p>
<dl>
<dd><code>&#8211;originname external vg/lvol1</code></dl>
<p> Convert an LV to a cache pool LV using another specified LV for cache pool metadata.<br />
 <code>lvconvert &#8211;type cache-pool &#8211;poolmetadata vg/poolmeta1 vg/lvol1</code> </p>
<p> Convert an LV to a cache LV using the specified cache pool and chunk size.<br />
 <code>lvconvert &#8211;type cache &#8211;cachepool vg/cpool1 -c 128 vg/lvol1</code> </p>
<p> Detach and keep the cache pool from a cache LV.<br />
 <code>lvconvert &#8211;splitcache vg/lvol1</code> </p>
<p> Detach and remove the cache pool from a cache LV.<br />
 <code>lvconvert &#8211;uncache vg/lvol1</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
