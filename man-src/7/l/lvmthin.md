---
title: "lvmthin(7)"
name: "lvmthin"
section: "7"
letter: "l"
url: "/docs/linux/man/7-lvmthin/"
description: "lvmthin — LVM thin provisioning"
---

<p>lvmthin &#8212; LVM thin provisioning</p>
<h2>Description</h2>
<p>Blocks in a standard <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) Logical Volume (LV) are allocated when the LV is created, but blocks in a thin provisioned LV are allocated as they are written. Because of this, a thin provisioned LV is given a virtual size, and can then be much larger than physically available storage. The amount of physical storage provided for thin provisioned LVs can be increased later as the need arises. Blocks in a standard LV are allocated (during creation) from the Volume Group (VG), but blocks in a thin LV are allocated (during use) from a special &quot;thin pool LV&quot;. The thin pool LV contains blocks of physical storage, and blocks in thin LVs just reference blocks in the thin pool LV. A thin pool LV must be created before thin LVs can be created within it. A thin pool LV is created by combining two standard LVs: a large data LV that will hold blocks for thin LVs, and a metadata LV that will hold metadata. The metadata tracks which data blocks belong to each thin LV. Snapshots of thin LVs are efficient because the data blocks common to a thin LV and any of its snapshots are shared. Snapshots may be taken of thin LVs or of other thin snapshots. Blocks common to recursive snapshots are also shared in the thin pool. There is no limit to or degradation from sequences of snapshots. As thin LVs or snapshot LVs are written to, they consume data blocks in the thin pool. As free data blocks in the pool decrease, more free blocks may need to be supplied. This is done by extending the thin pool data LV with additional physical space from the VG. Removing thin LVs or snapshots from the thin pool can also free blocks in the thin pool. However, removing LVs is not always an effective way of freeing space in a thin pool because the amount is limited to the number of blocks not shared with other LVs in the pool. Incremental block allocation from thin pools can cause thin LVs to become fragmented. Standard LVs generally avoid this problem by allocating all the blocks at once during creation. </p>
<h2>Thin Terms</h2>
<dl>
<dt>ThinDataLV</p>
<dd>thin data LV<br />
 large LV created in a VG<br />
 used by thin pool to store ThinLV blocks </p>
<dt>ThinMetaLV</p>
<dd>thin metadata LV<br />
 small LV created in a VG<br />
 used by thin pool to track data block usage </p>
<dt>ThinPoolLV</p>
<dd>thin pool LV<br />
 combination of ThinDataLV and ThinMetaLV<br />
 contains ThinLVs and SnapLVs </p>
<dt>ThinLV</p>
<dd>thin LV<br />
 created from ThinPoolLV<br />
 appears blank after creation </p>
<dt>SnapLV</p>
<dd>snapshot LV<br />
 created from ThinPoolLV<br />
 appears as a snapshot of another LV after creation </p>
</dl>
<h2>Thin Usage</h2>
<p>The primary method for using lvm thin provisioning:</p>
<h3>1. create ThinDataLV</h3>
<p>Create an LV that will hold thin pool data. </p>
<p> <code>lvcreate -n ThinDataLV -L LargeSize VG</code> </p>
<p> <i>Example</i><br />
 # lvcreate -n pool0 -L 10G vg</p>
<h3>2. create ThinMetaLV</h3>
<p>Create an LV that will hold thin pool metadata. </p>
<p> <code>lvcreate -n ThinMetaLV -L SmallSize VG</code> </p>
<p> <i>Example</i><br />
 # lvcreate -n pool0meta -L 1G vg </p>
<p> # lvs<br />
&nbsp;<wbr>&nbsp;LV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VG Attr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;LSize<br />
&nbsp;<wbr>&nbsp;pool0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;vg -wi-a&#8212;&#8211; 10.00g<br />
&nbsp;<wbr>&nbsp;pool0meta vg -wi-a&#8212;&#8211; 1.00g</p>
<h3>3. create ThinPoolLV</h3>
<pre>Combine the data and metadata LVs into a thin pool LV.
ThinDataLV is renamed to hidden ThinPoolLV_tdata.
ThinMetaLV is renamed to hidden ThinPoolLV_tmeta.
The new ThinPoolLV takes the previous name of ThinDataLV.</pre>
<p><code>lvconvert &#8211;type thin-pool &#8211;poolmetadata VG/ThinMetaLV VG/ThinDataLV</code> </p>
<p> <i>Example</i><br />
 # lvconvert &#8211;type thin-pool &#8211;poolmetadata vg/pool0meta vg/pool0 </p>
<p> # lvs vg/pool0<br />
&nbsp;<wbr>&nbsp;LV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VG Attr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;LSize&nbsp;<wbr>&nbsp;Pool Origin Data%&nbsp;Meta%<br />
&nbsp;<wbr>&nbsp;pool0 vg twi-a-tz&#8211; 10.00g&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00 </p>
<p> # lvs -a<br />
&nbsp;<wbr>&nbsp;LV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VG Attr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;LSize<br />
&nbsp;<wbr>&nbsp;pool0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;vg twi-a-tz&#8211; 10.00g<br />
&nbsp;<wbr>&nbsp;[pool0_tdata]&nbsp;vg Twi-ao&#8212;- 10.00g<br />
&nbsp;<wbr>&nbsp;[pool0_tmeta]&nbsp;vg ewi-ao&#8212;- 1.00g</p>
<h3>4. create ThinLV</h3>
<pre>Create a new thin LV from the thin pool LV.
The thin LV is created with a virtual size.
Multiple new thin LVs may be created in the thin pool.
Thin LV names must be unique in the VG.
The '--type thin' option is inferred from the virtual size option.
The --thinpool argument specifies which thin pool will
contain the ThinLV.</pre>
<p><code>lvcreate -n ThinLV -V VirtualSize &#8211;thinpool ThinPoolLV VG</code> </p>
<p> <i>Example</i><br />
 Create a thin LV in a thin pool:<br />
 # lvcreate -n thin1 -V 1T &#8211;thinpool pool0 vg </p>
<p> Create another thin LV in the same thin pool:<br />
 # lvcreate -n thin2 -V 1T &#8211;thinpool pool0 vg </p>
<p> # lvs vg/thin1 vg/thin2<br />
&nbsp;<wbr>&nbsp;LV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VG Attr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;LSize Pool&nbsp;<wbr>&nbsp;Origin Data%<br />
&nbsp;<wbr>&nbsp;thin1 vg Vwi-a-tz&#8211; 1.00t pool0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00<br />
&nbsp;<wbr>&nbsp;thin2 vg Vwi-a-tz&#8211; 1.00t pool0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00</p>
<h3>5. create SnapLV</h3>
<p>Create snapshots of an existing ThinLV or SnapLV.<br />
 Do not specify <code>-L</code>, <code>&#8211;size</code> when creating a thin snapshot.<br />
 A size argument will cause an old COW snapshot to be created. </p>
<p> <code>lvcreate -n SnapLV &#8211;snapshot VG/ThinLV</code><br />
 <code>lvcreate -n SnapLV &#8211;snapshot VG/PrevSnapLV</code> </p>
<p> <i>Example</i><br />
 Create first snapshot of an existing ThinLV:<br />
 # lvcreate -n thin1s1 -s vg/thin1 </p>
<p> Create second snapshot of the same ThinLV:<br />
 # lvcreate -n thin1s2 -s vg/thin1 </p>
<p> Create a snapshot of the first snapshot:<br />
 # lvcreate -n thin1s1s1 -s vg/thin1s1 </p>
<p> # lvs vg/thin1s1 vg/thin1s2 vg/thin1s1s1<br />
&nbsp;<wbr>&nbsp;LV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VG Attr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;LSize Pool&nbsp;<wbr>&nbsp;Origin<br />
&nbsp;<wbr>&nbsp;thin1s1&nbsp;<wbr>&nbsp;<wbr>&nbsp;vg Vwi&#8212;tz-k 1.00t pool0 thin1<br />
&nbsp;<wbr>&nbsp;thin1s2&nbsp;<wbr>&nbsp;<wbr>&nbsp;vg Vwi&#8212;tz-k 1.00t pool0 thin1<br />
&nbsp;<wbr>&nbsp;thin1s1s1 vg Vwi&#8212;tz-k 1.00t pool0 thin1s1</p>
<h3>6. activate SnapLV</h3>
<p>Thin snapshots are created with the persistent &quot;activation skip&quot; flag, indicated by the &quot;k&quot; attribute. Use -K with lvchange or vgchange to activate thin snapshots with the &quot;k&quot; attribute. </p>
<p> <code>lvchange -ay -K VG/SnapLV</code> </p>
<p> <i>Example</i><br />
 # lvchange -ay -K vg/thin1s1 </p>
<p> # lvs vg/thin1s1<br />
&nbsp;<wbr>&nbsp;LV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VG Attr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;LSize Pool&nbsp;<wbr>&nbsp;Origin<br />
&nbsp;<wbr>&nbsp;thin1s1 vg Vwi-a-tz-k 1.00t pool0 thin1</p>
<h2>Thin Topics</h2>
<p><code>Automatic pool metadata LV</code><br />
 <code>Specify devices for data and metadata LVs</code><br />
 <code>Tolerate device failures using raid</code><br />
 <code>Spare metadata LV</code><br />
 <code>Metadata check and repair</code><br />
 <code>Activation of thin snapshots</code><br />
 <code>Removing thin pool LVs, thin LVs and snapshots</code><br />
 <code>Manually manage free data space of thin pool LV</code><br />
 <code>Manually manage free metadata space of a thin pool LV</code><br />
 <code>Using fstrim to increase free space in a thin pool LV</code><br />
 <code>Automatically extend thin pool LV</code><br />
 <code>Data space exhaustion</code><br />
 <code>Metadata space exhaustion</code><br />
 <code>Automatic extend settings</code><br />
 <code>Zeroing</code><br />
 <code>Discard</code><br />
 <code>Chunk size</code><br />
 <code>Size of pool metadata LV</code><br />
 <code>Create a thin snapshot of an external, read only LV</code><br />
 <code>Convert a standard LV to a thin LV with an external origin</code><br />
 <code>Single step thin pool LV creation</code><br />
 <code>Single step thin pool LV and thin LV creation</code><br />
 <code>Merge thin snapshots</code><br />
 <code>XFS on snapshots</code></p>
<h3>Automatic pool metadata LV</h3>
<p>A thin data LV can be converted to a thin pool LV without specifying a thin pool metadata LV. LVM automatically creates a metadata LV from the same VG. </p>
<p> <code>lvcreate -n ThinDataLV -L LargeSize VG</code><br />
 <code>lvconvert &#8211;type thin-pool VG/ThinDataLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvcreate -n pool0 -L 10G vg
# lvconvert --type thin-pool vg/pool0
# lvs -a
 pool0 vg twi-a-tz-- 10.00g
 [pool0_tdata] vg Twi-ao---- 10.00g
 [pool0_tmeta] vg ewi-ao---- 16.00m</pre>
<h3>Specify devices for data and metadata LVs</h3>
<p>The data and metadata LVs in a thin pool are best created on separate physical devices. To do that, specify the device name(s) at the end of the lvcreate line. It can be especially helpful to use fast devices for the metadata LV. </p>
<p> <code>lvcreate -n ThinDataLV -L LargeSize VG LargePV</code><br />
 <code>lvcreate -n ThinMetaLV -L SmallSize VG SmallPV</code><br />
 <code>lvconvert &#8211;type thin-pool &#8211;poolmetadata VG/ThinMetaLV VG/ThinDataLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvcreate -n pool0 -L 10G vg /dev/sdA
# lvcreate -n pool0meta -L 1G vg /dev/sdB
# lvconvert --type thin-pool --poolmetadata vg/pool0meta vg/pool0</pre>
<p><code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_metadata_require_separate_pvs</code><br />
 controls the default PV usage for thin pool creation.</p>
<h3>Tolerate device failures using raid</h3>
<p>To tolerate device failures, use raid for the pool data LV and pool metadata LV. This is especially recommended for pool metadata LVs. </p>
<p> <code>lvcreate &#8211;type raid1 -m 1 -n ThinMetaLV -L SmallSize VG PVA PVB</code><br />
 <code>lvcreate &#8211;type raid1 -m 1 -n ThinDataLV -L LargeSize VG PVC PVD</code><br />
 <code>lvconvert &#8211;type thin-pool &#8211;poolmetadata VG/ThinMetaLV VG/ThinDataLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvcreate --type raid1 -m 1 -n pool0 -L 10G vg /dev/sdA /dev/sdB
# lvcreate --type raid1 -m 1 -n pool0meta -L 1G vg /dev/sdC /dev/sdD
# lvconvert --type thin-pool --poolmetadata vg/pool0meta vg/pool0</pre>
<h3>Spare metadata LV</h3>
<p>The first time a thin pool LV is created, lvm will create a spare metadata LV in the VG. This behavior can be controlled with the option &#8211;poolmetadataspare y|n. (Future thin pool creations will also attempt to create the pmspare LV if none exists.) </p>
<p> To create the pmspare (&quot;pool metadata spare&quot;) LV, lvm first creates an LV with a default name, e.g. lvol0, and then converts this LV to a hidden LV with the _pmspare suffix, e.g. lvol0_pmspare. </p>
<p> One pmspare LV is kept in a VG to be used for any thin pool. </p>
<p> The pmspare LV cannot be created explicitly, but may be removed explicitly. </p>
<p> <i>Example</i> </p>
<pre># lvcreate -n pool0 -L 10G vg
# lvcreate -n pool0meta -L 1G vg
# lvconvert --type thin-pool --poolmetadata vg/pool0meta vg/pool0
# lvs -a
 [lvol0_pmspare] vg ewi-------
 pool0 vg twi---tz--
 [pool0_tdata] vg Twi-------
 [pool0_tmeta] vg ewi-------</pre>
<p>The &quot;Metadata check and repair&quot; section describes the use of the pmspare LV.</p>
<h3>Metadata check and repair</h3>
<p>If thin pool metadata is damaged, it may be repairable. Checking and repairing thin pool metadata is analagous to running fsck/repair on a file system. </p>
<p> When a thin pool LV is activated, lvm runs the thin_check command to check the correctness of the metadata on the pool metadata LV. </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_check_executable</code><br />
 can be set to an empty string (&quot;&quot;) to disable the thin_check step. This is not recommended. </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_check_options</code><br />
 controls the command options used for the thin_check command. </p>
<p> If the thin_check command finds a problem with the metadata, the thin pool LV is not activated, and the thin pool metadata needs to be repaired. </p>
<p> Simple repair commands are not always successful. Advanced repair may require editing thin pool metadata and lvm metadata. Newer versions of the kernel and lvm tools may be more successful at repair. Report the details of damaged thin metadata to get the best advice on recovery. </p>
<p> Command to repair a thin pool:<br />
 <code>lvconvert &#8211;repair VG/ThinPoolLV</code> </p>
<p> Repair performs the following steps: </p>
<p> 1. Creates a new, repaired copy of the metadata.<br />
 lvconvert runs the thin_repair command to read damaged metadata from the existing pool metadata LV, and writes a new repaired copy to the VG&#8217;s pmspare LV. </p>
<p> 2. Replaces the thin pool metadata LV.<br />
 If step 1 is successful, the thin pool metadata LV is replaced with the pmspare LV containing the corrected metadata. The previous thin pool metadata LV, containing the damaged metadata, becomes visible with the new name ThinPoolLV_tmetaN (where N is 0,1,&#8230;). </p>
<p> If the repair works, the thin pool LV and its thin LVs can be activated, and the LV containing the damaged thin pool metadata can be removed. It may be useful to move the new metadata LV (previously pmspare) to a better PV. </p>
<p> If the repair does not work, the thin pool LV and its thin LVs are lost. </p>
<p> If metadata is manually restored with thin_repair directly, the pool metadata LV can be manually swapped with another LV containing new metadata: </p>
<p> <code>lvconvert &#8211;thinpool VG/ThinPoolLV &#8211;poolmetadata VG/NewThinMetaLV</code></p>
<h3>Activation of thin snapshots</h3>
<p>When a thin snapshot LV is created, it is by default given the &quot;activation skip&quot; flag. This flag is indicated by the &quot;k&quot; attribute displayed by lvs: </p>
<pre># lvs vg/thin1s1
 LV VG Attr LSize Pool Origin
 thin1s1 vg Vwi---tz-k 1.00t pool0 thin1</pre>
<p>This flag causes the snapshot LV to be skipped, i.e. not activated, by normal activation commands. The skipping behavior does not apply to deactivation commands. </p>
<p> A snapshot LV with the &quot;k&quot; attribute can be activated using the -K (or &#8211;ignoreactivationskip) option in addition to the standard -ay (or &#8211;activate y) option. </p>
<p> Command to activate a thin snapshot LV:<br />
 <code>lvchange -ay -K VG/SnapLV</code> </p>
<p> The persistent &quot;activation skip&quot; flag can be turned off during lvcreate, or later with lvchange using the -kn (or &#8211;setactivationskip n) option. It can be turned on again with -ky (or &#8211;setactivationskip y). </p>
<p> When the &quot;activation skip&quot; flag is removed, normal activation commands will activate the LV, and the -K activation option is not needed. </p>
<p> Command to create snapshot LV without the activation skip flag:<br />
 <code>lvcreate -kn -n SnapLV -s VG/ThinLV</code> </p>
<p> Command to remove the activation skip flag from a snapshot LV:<br />
 <code>lvchange -kn VG/SnapLV</code> </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>auto_set_activation_skip</code><br />
 controls the default activation skip setting used by lvcreate.</p>
<h3>Removing thin pool LVs, thin LVs and snapshots</h3>
<p>Removing a thin LV and its related snapshots returns the blocks it used to the thin pool LV. These blocks will be reused for other thin LVs and snapshots. </p>
<p> Removing a thin pool LV removes both the data LV and metadata LV and returns the space to the VG. </p>
<p> lvremove of thin pool LVs, thin LVs and snapshots cannot be reversed with vgcfgrestore. </p>
<p> vgcfgbackup does not back up thin pool metadata.</p>
<h3>Manually manage free data space of thin pool LV</h3>
<p>The available free space in a thin pool LV can be displayed with the lvs command. Free space can be added by extending the thin pool LV. </p>
<p> Command to extend thin pool data space:<br />
 <code>lvextend -L Size VG/ThinPoolLV</code> </p>
<p> <i>Example</i> </p>
<pre>1. A thin pool LV is using 26.96% of its data blocks.
# lvs
 LV VG Attr LSize Pool Origin Data%
 pool0 vg twi-a-tz-- 10.00g 26.96
2. Double the amount of physical space in the thin pool LV.
# lvextend -L+10G vg/pool0
3. The percentage of used data blocks is half the previous value.
# lvs
 LV VG Attr LSize Pool Origin Data%
 pool0 vg twi-a-tz-- 20.00g 13.48</pre>
<p>Other methods of increasing free data space in a thin pool LV include removing a thin LV and its related snapsots, or running fstrim on the file system using a thin LV.</p>
<h3>Manually manage free metadata space of a thin pool LV</h3>
<p>The available metadata space in a thin pool LV can be displayed with the lvs -o+metadata_percent command. </p>
<p> Command to extend thin pool metadata space:<br />
 <code>lvextend &#8211;poolmetadatasize Size VG/ThinPoolLV</code> </p>
<p> <i>Example</i><br />
 1. A thin pool LV is using 12.40% of its metadata blocks. </p>
<pre># lvs -oname,size,data_percent,metadata_percent vg/pool0
 LV LSize Data% Meta%
 pool0 20.00g 13.48 12.40</pre>
<p>2. Display a thin pool LV with its component thin data LV and thin metadata LV. </p>
<pre># lvs -a -oname,attr,size vg
 LV Attr LSize
 pool0 twi-a-tz-- 20.00g
 [pool0_tdata] Twi-ao---- 20.00g
 [pool0_tmeta] ewi-ao---- 12.00m</pre>
<p>3. Double the amount of physical space in the thin metadata LV. </p>
<pre># lvextend --poolmetadatasize +12M vg/pool0</pre>
<p>4. The percentage of used metadata blocks is half the previous value. </p>
<pre># lvs -a -oname,size,data_percent,metadata_percent vg
 LV LSize Data% Meta%
 pool0 20.00g 13.48 6.20
 [pool0_tdata] 20.00g
 [pool0_tmeta] 24.00m</pre>
<h3>Using fstrim to increase free space in a thin pool LV</h3>
<p>Removing files in a file system on top of a thin LV does not generally add free space back to the thin pool. Manually running the fstrim command can return space back to the thin pool that had been used by removed files. fstrim uses discards and will not work if the thin pool LV has discards mode set to ignore. </p>
<p> <i>Example</i><br />
 A thin pool has 10G of physical data space, and a thin LV has a virtual size of 100G. Writing a 1G file to the file system reduces the free space in the thin pool by 10% and increases the virtual usage of the file system by 1%. Removing the 1G file restores the virtual 1% to the file system, but does not restore the physical 10% to the thin pool. The fstrim command restores the physical space to the thin pool. </p>
<pre># lvs -a -oname,attr,size,pool_lv,origin,data_percent,metadata_percent vg
LV Attr LSize Pool Origin Data% Meta%
pool0 twi-a-tz-- 10.00g 47.01 21.03
thin1 Vwi-aotz-- 100.00g pool0 2.70
# df -h /mnt/X
Filesystem Size Used Avail Use% Mounted on
/dev/mapper/vg-thin1 99G 1.1G 93G 2% /mnt/X
# dd if=/dev/zero of=/mnt/X/1Gfile bs=4096 count=262144; sync
# lvs
pool0 vg twi-a-tz-- 10.00g 57.01 25.26
thin1 vg Vwi-aotz-- 100.00g pool0 3.70
# df -h /mnt/X
/dev/mapper/vg-thin1 99G 2.1G 92G 3% /mnt/X
# rm /mnt/X/1Gfile
# lvs
pool0 vg twi-a-tz-- 10.00g 57.01 25.26
thin1 vg Vwi-aotz-- 100.00g pool0 3.70
# df -h /mnt/X
/dev/mapper/vg-thin1 99G 1.1G 93G 2% /mnt/X
# fstrim -v /mnt/X
# lvs
pool0 vg twi-a-tz-- 10.00g 47.01 21.03
thin1 vg Vwi-aotz-- 100.00g pool0 2.70</pre>
<p>The &quot;Discard&quot; section covers an option for automatically freeing data space in a thin pool.</p>
<h3>Automatically extend thin pool LV</h3>
<p>The lvm daemon dmeventd (lvm2-monitor) monitors the data usage of thin pool LVs and extends them when the usage reaches a certain level. The necessary free space must exist in the VG to extend thin pool LVs. Monitoring and extension of thin pool LVs are controlled independently. </p>
<p> <i>monitoring</i> </p>
<p> When a thin pool LV is activated, dmeventd will begin monitoring it by default. </p>
<p> Command to start or stop dmeventd monitoring a thin pool LV:<br />
 <code>lvchange &#8211;monitor {y|n} VG/ThinPoolLV</code> </p>
<p> The current dmeventd monitoring status of a thin pool LV can be displayed with the command lvs -o+seg_monitor. </p>
<p> <i>autoextend</i> </p>
<p> dmeventd should be configured to extend thin pool LVs before all data space is used. Warnings are emitted through syslog when the use of a thin pool reaches 80%, 85%, 90% and 95%. (See the section &quot;Data space exhaustion&quot; for the effects of not extending a thin pool LV.) The point at which dmeventd extends thin pool LVs, and the amount are controlled with two configuration settings: </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_autoextend_threshold</code><br />
 is a percentage full value that defines when the thin pool LV should be extended. Setting this to 100 disables automatic extention. The minimum value is 50. </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_autoextend_percent</code><br />
 defines how much extra data space should be added to the thin pool LV from the VG, in percent of its current size. </p>
<p> <i>disabling</i> </p>
<p> There are multiple ways that extension of thin pools could be prevented: </p>
<dl>
<dt>&bull;</p>
<dd>If the dmeventd daemon is not running, no monitoring or automatic extension will occur. </p>
<dt>&bull;</p>
<dd>Even when dmeventd is running, all monitoring can be disabled with the lvm.conf monitoring setting. </p>
<dt>&bull;</p>
<dd>To activate or create a thin pool LV without interacting with dmeventd, the &#8211;ignoremonitoring option can be used. With this option, the command will not ask dmeventd to monitor the thin pool LV. </p>
<dt>&bull;</p>
<dd>Setting thin_pool_autoextend_threshould to 100 disables automatic extension of thin pool LVs, even if they are being monitored by dmeventd. </p>
</dl>
<p> <i>Example</i><br />
 If thin_pool_autoextend_threshold is 70 and thin_pool_autoextend_percent is 20, whenever a pool exceeds 70% usage, it will be extended by another 20%. For a 1G pool, using 700M will trigger a resize to 1.2G. When the usage exceeds 840M, the pool will be extended to 1.44G, and so on.</p>
<h3>Data space exhaustion</h3>
<p>When properly managed, thin pool data space should be extended before it is all used (see the section &quot;Automatically extend thin pool LV&quot;). If thin pool data space is already exhausted, it can still be extended (see the section &quot;Manually manage free data space of thin pool LV&quot;.) </p>
<p> The behavior of a full thin pool is configurable with the &#8211;errorwhenfull y|n option to lvcreate or lvchange. The errorwhenfull setting applies only to writes; reading thin LVs can continue even when data space is exhausted. </p>
<p> Command to change the handling of a full thin pool:<br />
 <code>lvchange &#8211;errorwhenfull {y|n} VG/ThinPoolLV</code> </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>error_when_full</code><br />
 controls the default error when full behavior. </p>
<p> The current setting of a thin pool LV can be displayed with the command: lvs -o+lv_when_full. </p>
<p> The errorwhenfull setting does not effect the monitoring and autoextend settings, and the monitoring/autoextend settings do not effect the errorwhenfull setting. It is only when monitoring/autoextend are not effective that the thin pool becomes full and the errorwhenfull setting is applied. </p>
<p> <i>errorwhenfull n</i> </p>
<p> This is the default. Writes to thin LVs are accepted and queued, with the expectation that pool data space will be extended soon. Once data space is extended, the queued writes will be processed, and the thin pool will return to normal operation. </p>
<p> While waiting to be extended, the thin pool will queue writes for up to 60 seconds (the default). If data space has not been extended after this time, the queued writes will return an error to the caller, e.g. the file system. This can result in file system corruption for non-journaled file systems that may require repair. When a thin pool returns errors for writes to a thin LV, any file system is subject to losing unsynced user data. </p>
<p> The 60 second timeout can be changed or disabled with the dm-thin-pool kernel module option <code>no_space_timeout.</code> This option sets the number of seconds that thin pools will queue writes. If set to 0, writes will not time out. Disabling timeouts can result in the system running out of resources, memory exhaustion, hung tasks, and deadlocks. (The timeout applies to all thin pools on the system.) </p>
<p> <i>errorwhenfull y</i> </p>
<p> Writes to thin LVs immediately return an error, and no writes are queued. In the case of a file system, this can result in corruption that may require fs repair (the specific consequences depend on the thin LV user.) </p>
<p> <i>data percent</i> </p>
<p> When data space is exhausted, the lvs command displays 100 under Data% for the thin pool LV: </p>
<pre># lvs vg/pool0
 LV VG Attr LSize Pool Origin Data%
 pool0 vg twi-a-tz-- 512.00m 100.00</pre>
<p><i>causes</i> </p>
<p> A thin pool may run out of data space for any of the following reasons: </p>
<dl>
<dt>&bull;</p>
<dd>Automatic extension of the thin pool is disabled, and the thin pool is not manually extended. (Disabling automatic extension is not recommended.) </p>
<dt>&bull;</p>
<dd>The dmeventd daemon is not running and the thin pool is not manually extended. (Disabling dmeventd is not recommended.) </p>
<dt>&bull;</p>
<dd>Automatic extension of the thin pool is too slow given the rate of writes to thin LVs in the pool. (This can be addressed by tuning the thin_pool_autoextend_threshold and thin_pool_autoextend_percent. See &quot;Automatic extend settings&quot;.) </p>
<dt>&bull;</p>
<dd>The VG does not have enough free blocks to extend the thin pool. </p>
</dl>
<h3>Metadata space exhaustion</h3>
<p>If thin pool metadata space is exhausted (or a thin pool metadata operation fails), errors will be returned for IO operations on thin LVs. </p>
<p> When metadata space is exhausted, the lvs command displays 100 under Meta% for the thin pool LV: </p>
<pre># lvs -o lv_name,size,data_percent,metadata_percent vg/pool0
 LV LSize Data% Meta%
 pool0 100.00</pre>
<p>The same reasons for thin pool data space exhaustion apply to thin pool metadata space. </p>
<p> Metadata space exhaustion can lead to inconsistent thin pool metadata and inconsistent file systems, so the response requires offline checking and repair. </p>
<p> 1. Deactivate the thin pool LV, or reboot the system if this is not possible. </p>
<p> 2. Repair thin pool with lvconvert &#8211;repair. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;See&nbsp;&quot;Metadata check and repair&quot;. </p>
<p> 3. Extend pool metadata space with lvextend &#8211;poolmetadatasize. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;See&nbsp;&quot;Manually manage free metadata space of a thin pool LV&quot;. </p>
<p> 4. Check and repair file system.</p>
<h3>Automatic extend settings</h3>
<p>Thin pool LVs can be extended according to preset values. The presets determine if the LV should be extended based on how full it is, and if so by how much. When dmeventd monitors thin pool LVs, it uses lvextend with these presets. (See &quot;Automatically extend thin pool LV&quot;.) </p>
<p> Command to extend a thin pool data LV using presets:<br />
 <code>lvextend &#8211;use-policies VG/ThinPoolLV</code> </p>
<p> The command uses these settings: </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_autoextend_threshold</code><br />
 autoextend the LV when its usage exceeds this percent. </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_autoextend_percent</code><br />
 autoextend the LV by this much additional space. </p>
<p> To see the default values of these settings, run: </p>
<p> <code>lvmconfig &#8211;type default &#8211;withcomment</code></p>
<dl>
<dd><code>activation/thin_pool_autoextend_threshold</code></dl>
<p> <code>lvmconfig &#8211;type default &#8211;withcomment</code></p>
<dl>
<dd><code>activation/thin_pool_autoextend_percent</code></dl>
<p> To change these values globally, edit <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5). </p>
<p> To change these values on a per-VG or per-LV basis, attach a &quot;profile&quot; to the VG or LV. A profile is a collection of config settings, saved in a local text file (using the lvm.conf format). lvm looks for profiles in the profile_dir directory, e.g. /etc/lvm/profile/. Once attached to a VG or LV, lvm will process the VG or LV using the settings from the attached profile. A profile is named and referenced by its file name. </p>
<p> To use a profile to customize the lvextend settings for an LV: </p>
<dl>
<dt>&bull;</p>
<dd>Create a file containing settings, saved in profile_dir. For the profile_dir location, run:<br />
 <code>lvmconfig config/profile_dir</code> </p>
<dt>&bull;</p>
<dd>Attach the profile to an LV, using the command:<br />
 <code>lvchange &#8211;metadataprofile ProfileName VG/ThinPoolLV</code> </p>
<dt>&bull;</p>
<dd>Extend the LV using the profile settings:<br />
 <code>lvextend &#8211;use-policies VG/ThinPoolLV</code> </p>
</dl>
<p> <i>Example</i> </p>
<pre># lvmconfig config/profile_dir
profile_dir=&quot;/etc/lvm/profile&quot;
# cat /etc/lvm/profile/pool0extend.profile
activation {
 thin_pool_autoextend_threshold=50
 thin_pool_autoextend_percent=10
}
# lvchange --metadataprofile pool0extend vg/pool0
# lvextend --use-policies vg/pool0</pre>
<p><i>Notes</i></p>
<dl>
<dt>&bull;</p>
<dd>A profile is attached to a VG or LV by name, where the name references a local file in profile_dir. If the VG is moved to another machine, the file with the profile also needs to be moved. </p>
<dt>&bull;</p>
<dd>Only certain settings can be used in a VG or LV profile, see:<br />
 <code>lvmconfig &#8211;type profilable-metadata.</code> </p>
<dt>&bull;</p>
<dd>An LV without a profile of its own will inherit the VG profile. </p>
<dt>&bull;</p>
<dd>Remove a profile from an LV using the command:<br />
 <code>lvchange &#8211;detachprofile VG/ThinPoolLV.</code> </p>
<dt>&bull;</p>
<dd>Commands can also have profiles applied to them. The settings that can be applied to a command are different than the settings that can be applied to a VG or LV. See lvmconfig &#8211;type profilable-command. To apply a profile to a command, write a profile, save it in the profile directory, and run the command using the option: &#8211;commandprofile ProfileName. </p>
</dl>
<h3>Zeroing</h3>
<p>When a thin pool provisions a new data block for a thin LV, the new block is first overwritten with zeros. The zeroing mode is indicated by the &quot;z&quot; attribute displayed by lvs. The option -Z (or &#8211;zero) can be added to commands to specify the zeroing mode. </p>
<p> Command to set the zeroing mode when creating a thin pool LV:<br />
 <code>lvconvert &#8211;type thin-pool -Z{y|n}</code> </p>
<dl>
<dd><code>&#8211;poolmetadata VG/ThinMetaLV VG/ThinDataLV</code></dl>
<p> Command to change the zeroing mode of an existing thin pool LV:<br />
 <code>lvchange -Z{y|n} VG/ThinPoolLV</code> </p>
<p> If zeroing mode is changed from &quot;n&quot; to &quot;y&quot;, previously provisioned blocks are not zeroed. </p>
<p> Provisioning of large zeroed chunks impacts performance. </p>
<p> <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_zero</code><br />
 controls the default zeroing mode used when creating a thin pool.</p>
<h3>Discard</h3>
<p>The discard behavior of a thin pool LV determines how discard requests are handled. Enabling discard under a file system may adversely affect the file system performance (see the section on fstrim for an alternative.) Possible discard behaviors: </p>
<p> ignore: Ignore any discards that are received. </p>
<p> nopassdown: Process any discards in the thin pool itself and allow the no longer needed extents to be overwritten by new data. </p>
<p> passdown: Process discards in the thin pool (as with nopassdown), and pass the discards down the the underlying device. This is the default mode. </p>
<p> Command to display the current discard mode of a thin pool LV:<br />
 <code>lvs -o+discards VG/ThinPoolLV</code> </p>
<p> Command to set the discard mode when creating a thin pool LV:<br />
 <code>lvconvert &#8211;discards {ignore|nopassdown|passdown}</code> </p>
<dl>
<dd><code>&#8211;type thin-pool &#8211;poolmetadata VG/ThinMetaLV VG/ThinDataLV</code></dl>
<p> Command to change the discard mode of an existing thin pool LV:<br />
 <code>lvchange &#8211;discards {ignore|nopassdown|passdown} VG/ThinPoolLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvs -o name,discards vg/pool0
pool0 passdown
# lvchange --discards ignore vg/pool0</pre>
<p><code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_discards</code><br />
 controls the default discards mode used when creating a thin pool.</p>
<h3>Chunk size</h3>
<p>The size of data blocks managed by a thin pool can be specified with the &#8211;chunksize option when the thin pool LV is created. The default unit is KiB. The value must be a multiple of 64KiB between 64KiB and 1GiB. </p>
<p> When a thin pool is used primarily for the thin provisioning feature, a larger value is optimal. To optimize for many snapshots, a smaller value reduces copying time and consumes less space. </p>
<p> Command to display the thin pool LV chunk size:<br />
 <code>lvs -o+chunksize VG/ThinPoolLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvs -o name,chunksize
 pool0 64.00k</pre>
<p><code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>thin_pool_chunk_size</code><br />
 controls the default chunk size used when creating a thin pool. </p>
<p> The default value is shown by:<br />
 <code>lvmconfig &#8211;type default allocation/thin_pool_chunk_size</code></p>
<h3>Size of pool metadata LV</h3>
<p>The amount of thin metadata depends on how many blocks are shared between thin LVs (i.e. through snapshots). A thin pool with many snapshots may need a larger metadata LV. Thin pool metadata LV sizes can be from 2MiB to 16GiB. </p>
<p> When using lvcreate to create what will become a thin metadata LV, the size is specified with the -L&#8211;size option. </p>
<p> When an LVM command automatically creates a thin metadata LV, the size is specified with the &#8211;poolmetadatasize option. When this option is not given, LVM automatically chooses a size based on the data size and chunk size. </p>
<p> It can be hard to predict the amount of metadata space that will be needed, so it is recommended to start with a size of 1GiB which should be enough for all practical purposes. A thin pool metadata LV can later be manually or automatically extended if needed.</p>
<h3>Create a thin snapshot of an external, read only LV</h3>
<p>Thin snapshots are typically taken of other thin LVs or other thin snapshot LVs within the same thin pool. It is also possible to take thin snapshots of external, read only LVs. Writes to the snapshot are stored in the thin pool, and the external LV is used to read unwritten parts of the thin snapshot. </p>
<p> <code>lvcreate -n SnapLV -s VG/ExternalOriginLV &#8211;thinpool VG/ThinPoolLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvchange -an vg/lve
# lvchange --permission r vg/lve
# lvcreate -n snaplve -s vg/lve --thinpool vg/pool0
# lvs vg/lve vg/snaplve
 LV VG Attr LSize Pool Origin Data%
 lve vg ori------- 10.00g
 snaplve vg Vwi-a-tz-- 10.00g pool0 lve 0.00</pre>
<h3>Convert a standard LV to a thin LV with an external origin</h3>
<p>A new thin LV can be created and given the name of an existing standard LV. At the same time, the existing LV is converted to a read only external LV with a new name. Unwritten portions of the thin LV are read from the external LV. The new name given to the existing LV can be specified with &#8211;originname, otherwise the existing LV will be given a default name, e.g. lvol#. </p>
<p> Convert ExampleLV into a read only external LV with the new name NewExternalOriginLV, and create a new thin LV that is given the previous name of ExampleLV. </p>
<p> <code>lvconvert &#8211;type thin &#8211;thinpool VG/ThinPoolLV</code> </p>
<dl>
<dd><code>&#8211;originname NewExternalOriginLV VG/ExampleLV</code></dl>
<p> <i>Example</i> </p>
<pre># lvcreate -n lv_example -L 10G vg
# lvs
 lv_example vg -wi-a----- 10.00g
# lvconvert --type thin --thinpool vg/pool0
 --originname lv_external --thin vg/lv_example
# lvs
 LV VG Attr LSize Pool Origin
 lv_example vg Vwi-a-tz-- 10.00g pool0 lv_external
 lv_external vg ori------- 10.00g</pre>
<h3>Single step thin pool LV creation</h3>
<p>A thin pool LV can be created with a single lvcreate command, rather than using lvconvert on existing LVs. This one command creates a thin data LV, a thin metadata LV, and combines the two into a thin pool LV. </p>
<p> <code>lvcreate &#8211;type thin-pool -L LargeSize -n ThinPoolLV VG</code> </p>
<p> <i>Example</i> </p>
<pre># lvcreate --type thin-pool -L8M -n pool0 vg
# lvs vg/pool0
 LV VG Attr LSize Pool Origin Data%
 pool0 vg twi-a-tz-- 8.00m 0.00
# lvs -a
 pool0 vg twi-a-tz-- 8.00m
 [pool0_tdata] vg Twi-ao---- 8.00m
 [pool0_tmeta] vg ewi-ao---- 8.00m</pre>
<h3>Single step thin pool LV and thin LV creation</h3>
<p>A thin pool LV and a thin LV can be created with a single lvcreate command. This one command creates a thin data LV, a thin metadata LV, combines the two into a thin pool LV, and creates a thin LV in the new pool.<br />
 -L LargeSize specifies the physical size of the thin pool LV.<br />
 -V VirtualSize specifies the virtual size of the thin LV. </p>
<p> <code>lvcreate &#8211;type thin -V VirtualSize -L LargeSize</code></p>
<dl>
<dd><code>-n ThinLV &#8211;thinpool VG/ThinPoolLV</code></dl>
<p> Equivalent to:<br />
 <code>lvcreate &#8211;type thin-pool -L LargeSize VG/ThinPoolLV</code><br />
 <code>lvcreate -n ThinLV -V VirtualSize &#8211;thinpool VG/ThinPoolLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvcreate -L8M -V2G -n thin1 --thinpool vg/pool0
# lvs -a
 pool0 vg twi-a-tz-- 8.00m
 [pool0_tdata] vg Twi-ao---- 8.00m
 [pool0_tmeta] vg ewi-ao---- 8.00m
 thin1 vg Vwi-a-tz-- 2.00g pool0</pre>
<h3>Merge thin snapshots</h3>
<p>A thin snapshot can be merged into its origin thin LV using the lvconvert &#8211;merge command. The result of a snapshot merge is that the origin thin LV takes the content of the snapshot LV, and the snapshot LV is removed. Any content that was unique to the origin thin LV is lost after the merge. </p>
<p> Because a merge changes the content of an LV, it cannot be done while the LVs are open, e.g. mounted. If a merge is initiated while the LVs are open, the effect of the merge is delayed until the origin thin LV is next activated. </p>
<p> <code>lvconvert &#8211;merge VG/SnapLV</code> </p>
<p> <i>Example</i> </p>
<pre># lvs vg
 LV VG Attr LSize Pool Origin
 pool0 vg twi-a-tz-- 10.00g
 thin1 vg Vwi-a-tz-- 100.00g pool0
 thin1s1 vg Vwi-a-tz-k 100.00g pool0 thin1
# lvconvert --merge vg/thin1s1
# lvs vg
 LV VG Attr LSize Pool Origin
 pool0 vg twi-a-tz-- 10.00g
 thin1 vg Vwi-a-tz-- 100.00g pool0</pre>
<p><i>Example</i> </p>
<pre>Delayed merging of open LVs.
# lvs vg
 LV VG Attr LSize Pool Origin
 pool0 vg twi-a-tz-- 10.00g
 thin1 vg Vwi-aotz-- 100.00g pool0
 thin1s1 vg Vwi-aotz-k 100.00g pool0 thin1
# df
/dev/mapper/vg-thin1 100G 33M 100G 1% /mnt/X
/dev/mapper/vg-thin1s1 100G 33M 100G 1% /mnt/Xs
# ls /mnt/X
file1 file2 file3
# ls /mnt/Xs
file3 file4 file5
# lvconvert --merge vg/thin1s1
Logical volume vg/thin1s1 contains a filesystem in use.
Delaying merge since snapshot is open.
Merging of thin snapshot thin1s1 will occur on next activation.
# umount /mnt/X
# umount /mnt/Xs
# lvs -a vg
 LV VG Attr LSize Pool Origin
 pool0 vg twi-a-tz-- 10.00g
 [pool0_tdata] vg Twi-ao---- 10.00g
 [pool0_tmeta] vg ewi-ao---- 1.00g
 thin1 vg Owi-a-tz-- 100.00g pool0
 [thin1s1] vg Swi-a-tz-k 100.00g pool0 thin1
# lvchange -an vg/thin1
# lvchange -ay vg/thin1
# mount /dev/vg/thin1 /mnt/X
# ls /mnt/X
file3 file4 file5</pre>
<h3>XFS on snapshots</h3>
<p>Mounting an XFS file system on a new snapshot LV requires attention to the file system&#8217;s log state and uuid. On the snapshot LV, the xfs log will contain a dummy transaction, and the xfs uuid will match the uuid from the file system on the origin LV. </p>
<p> If the snapshot LV is writable, mounting will recover the log to clear the dummy transaction, but will require skipping the uuid check: </p>
<p> mount /dev/VG/SnapLV /mnt -o nouuid </p>
<p> After the first mount with the above approach, the UUID can subsequently be changed using: </p>
<p> xfs_admin -U generate /dev/VG/SnapLV<br />
 mount /dev/VG/SnapLV /mnt </p>
<p> Once the UUID has been changed, the mount command will no longer require the nouuid option. </p>
<p> If the snapshot LV is readonly, the log recovery and uuid check need to be skipped while mounting readonly: </p>
<p> mount /dev/VG/SnapLV /mnt -o ro,nouuid,norecovery</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5), <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8), <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8), <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8), <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8), <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8), <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8), <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8), <code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8) <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8) </p>
