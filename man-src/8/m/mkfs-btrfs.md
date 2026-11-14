---
title: "mkfs-btrfs(8)"
name: "mkfs-btrfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-btrfs/"
description: "mkfs.btrfs – create a btrfs filesystem"
---

<p>mkfs.btrfs &#8211; create a btrfs filesystem</p>
<h2>Synopsis</h2>
<p><code>mkfs.btrfs</code> [options] <i>&lt;device&gt;</i> [<i>&lt;device&gt;</i>&#8230;]</p>
<h2>Description</h2>
<p><code>mkfs.btrfs</code> is used to create the btrfs filesystem on a single or multiple devices. <i>&lt;device&gt;</i> is typically a block device but can be a file-backed image as well. Multiple devices are grouped by UUID of the filesystem. </p>
<p> Before mounting such filesystem, the kernel module must know all the devices either via preceding execution of <code>btrfs device scan</code> or using the <code>device</code> mount option. See section <code>MULTIPLE DEVICES</code> for more details.</p>
<h2>Options</h2>
<p><code>-b|&#8211;byte-count </code><i>&lt;size&gt;</i></p>
<dl>
<dd>Specify the size of the filesystem. If this option is not used, then mkfs.btrfs uses the entire device space for the filesystem.</dl>
<p> <code>-d|&#8211;data </code><i>&lt;profile&gt;</i></p>
<dl>
<dd>Specify the profile for the data block groups. Valid values are <i>raid0</i>, <i>raid1</i>, <i>raid5</i>, <i>raid6</i>, <i>raid10</i> or <i>single</i> or dup (case does not matter). </p>
<p> See <i>DUP PROFILES ON A SINGLE DEVICE</i> for more.</dl>
<p> <code>-m|&#8211;metadata </code><i>&lt;profile&gt;</i></p>
<dl>
<dd>Specify the profile for the metadata block groups. Valid values are <i>raid0</i>, <i>raid1</i>, <i>raid5</i>, <i>raid6</i>, <i>raid10</i>, <i>single</i> or <i>dup</i>, (case does not matter). </p>
<p> A single device filesystem will default to <i>DUP</i>, unless a SSD is detected. Then it will default to <i>single</i>. The detection is based on the value of <code>/sys/block/DEV/queue/rotational</code>, where <i>DEV</i> is the short name of the device. </p>
<p> Note that the rotational status can be arbitrarily set by the underlying block device driver and may not reflect the true status (network block device, memory-backed SCSI devices etc). Use the options <i>&#8211;data/&#8211;metadata</i> to avoid confusion. </p>
<p> See <i>DUP PROFILES ON A SINGLE DEVICE</i> for more details.</dl>
<p> <code>-M|&#8211;mixed</code></p>
<dl>
<dd>Normally the data and metadata block groups are isolated. The <i>mixed</i> mode will remove the isolation and store both types in the same block group type. This helps to utilize the free space regardless of the purpose and is suitable for small devices. The separate allocation of block groups leads to a situation where the space is reserved for the other block group type, is not available for allocation and can lead to ENOSPC state. </p>
<p> The recommended size for the mixed mode is for filesystems less than 1GiB. The soft recommendation is to use it for filesystems smaller than 5GiB. The mixed mode may lead to degraded performance on larger filesystems, but is otherwise usable, even on multiple devices. </p>
<p> The <i>nodesize</i> and <i>sectorsize</i> must be equal, and the block group types must match. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 versions up to 4.2.x forced the mixed mode for devices smaller than 1GiB. This has been removed in 4.3+ as it caused some usability issues. </p>
</dl>
</dl>
<p> <code>-l|&#8211;leafsize </code><i>&lt;size&gt;</i></p>
<dl>
<dd>Alias for &#8211;nodesize. Deprecated.</dl>
<p> <code>-n|&#8211;nodesize </code><i>&lt;size&gt;</i></p>
<dl>
<dd>Specify the nodesize, the tree block size in which btrfs stores metadata. The default value is 16KiB (16384) or the page size, whichever is bigger. Must be a multiple of the sectorsize and a power of 2, but not larger than 64KiB (65536). Leafsize always equals nodesize and the options are aliases. </p>
<p> Smaller node size increases fragmentation but leads to taller b-trees which in turn leads to lower locking contention. Higher node sizes give better packing and less fragmentation at the cost of more expensive memory operations while updating the metadata blocks. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 versions up to 3.11 set the nodesize to 4k. </p>
</dl>
</dl>
<p> <code>-s|&#8211;sectorsize </code><i>&lt;size&gt;</i></p>
<dl>
<dd>Specify the sectorsize, the minimum data block allocation unit. </p>
<p> The default value is the page size and is autodetected. If the sectorsize differs from the page size, the created filesystem may not be mountable by the kernel. Therefore it is not recommended to use this option unless you are going to mount it on a system with the appropriate page size.</dl>
<p> <code>-L|&#8211;label </code><i>&lt;string&gt;</i></p>
<dl>
<dd>Specify a label for the filesystem. The <i>string</i> should be less than 256 bytes and must not contain newline characters.</dl>
<p> <code>-K|&#8211;nodiscard</code></p>
<dl>
<dd>Do not perform whole device TRIM operation on devices that are capable of that. This does not affect discard/trim operation when the filesystem is mounted. Please see the mount option <i>discard</i> for that in <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5).</dl>
<p> <code>-r|&#8211;rootdir </code><i>&lt;rootdir&gt;</i></p>
<dl>
<dd>Populate the toplevel subvolume with files from <i>rootdir</i>. This does not require root permissions to write the new files or to mount the filesystem. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This option may enlarge the image or file to ensure it&#8217;s big enough to contain the files from <i>rootdir</i>. Since version 4.14.1 the filesystem size is not minimized. Please see option <i>&#8211;shrink</i> if you need that functionality. </p>
</dl>
</dl>
<p> <code>&#8211;shrink</code></p>
<dl>
<dd>Shrink the filesystem to its minimal size, only works with <i>&#8211;rootdir</i> option. </p>
<p> If the destination is a regular file, this option will also truncate the file to the minimal size. Otherwise it will reduce the filesystem available space. Extra space will not be usable unless the filesystem is mounted and resized using <i>btrfs filesystem resize</i>. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 prior to version 4.14.1, the shrinking was done automatically. </p>
</dl>
</dl>
<p> <code>-O|&#8211;features </code><i>&lt;feature1&gt;</i><code>[,</code><i>&lt;feature2&gt;</i><code>&#8230;]</code></p>
<dl>
<dd>A list of filesystem features turned on at mkfs time. Not all features are supported by old kernels. To disable a feature, prefix it with <i>^</i>. </p>
<p> See section <code>FILESYSTEM FEATURES</code> for more details. To see all available features that mkfs.btrfs supports run: </p>
<p> <code>mkfs.btrfs -O list-all</code></dl>
<p> <code>-f|&#8211;force</code></p>
<dl>
<dd>Forcibly overwrite the block devices when an existing filesystem is detected. By default, mkfs.btrfs will utilize <i>libblkid</i> to check for any known filesystem on the devices. Alternatively you can use the <code>wipefs</code> utility to clear the devices.</dl>
<p> <code>-q|&#8211;quiet</code></p>
<dl>
<dd>Print only error or warning messages. Options &#8211;features or &#8211;help are unaffected.</dl>
<p> <code>-U|&#8211;uuid </code><i>&lt;UUID&gt;</i></p>
<dl>
<dd>Create the filesystem with the given <i>UUID</i>. The UUID must not exist on any filesystem currently present.</dl>
<p> <code>-V|&#8211;version</code></p>
<dl>
<dd>Print the <code>mkfs.btrfs</code> version and exit.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Print help.</dl>
<p> <code>-A|&#8211;alloc-start </code><i>&lt;offset&gt;</i></p>
<dl>
<dd><code>deprecated, will be removed</code> (An option to help debugging chunk allocator.) Specify the (physical) offset from the start of the device at which allocations start. The default value is zero.</dl>
<h2>Size Units</h2>
<p>The default unit is <i>byte</i>. All size parameters accept suffixes in the 1024 base. The recognized suffixes are: <i>k</i>, <i>m</i>, <i>g</i>, <i>t</i>, <i>p</i>, <i>e</i>, both uppercase and lowercase.</p>
<h2>Multiple Devices</h2>
<p>Before mounting a multiple device filesystem, the kernel module must know the association of the block devices that are attached to the filesystem UUID. </p>
<p> There is typically no action needed from the user. On a system that utilizes a udev-like daemon, any new block device is automatically registered. The rules call <code>btrfs device scan</code>. </p>
<p> The same command can be used to trigger the device scanning if the btrfs kernel module is reloaded (naturally all previous information about the device registration is lost). </p>
<p> Another possibility is to use the mount options <code>device</code> to specify the list of devices to scan at the time of mount. </p>
<dl>
<dd>
<pre># mount -o device=/dev/sdb,device=/dev/sdc /dev/sda /mnt</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> that this means only scanning, if the devices do not exist in the system, mount will fail anyway. This can happen on systems without initramfs/initrd and root partition created with RAID1/10/5/6 profiles. The mount action can happen before all block devices are discovered. The waiting is usually done on the initramfs/initrd systems. </p>
</dl>
<p> As of kernel 4.14, RAID5/6 is still considered experimental and shouldn&#8217;t be employed for production use.</p>
<h2>Filesystem Features</h2>
<p>Features that can be enabled during creation time. See also <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5) section <i>FILESYSTEM FEATURES</i>. </p>
<p> <code>mixed-bg</code></p>
<dl>
<dd>(kernel support since 2.6.37) </p>
<p> mixed data and metadata block groups, also set by option <i>&#8211;mixed</i></dl>
<p> <code>extref</code></p>
<dl>
<dd>(default since btrfs-progs 3.12, kernel support since 3.7) </p>
<p> increased hardlink limit per file in a directory to 65536, older kernels supported a varying number of hardlinks depending on the sum of all file name sizes that can be stored into one metadata block</dl>
<p> <code>raid56</code></p>
<dl>
<dd>(kernel support since 3.9) </p>
<p> extended format for RAID5/6, also enabled if raid5 or raid6 block groups are selected</dl>
<p> <code>skinny-metadata</code></p>
<dl>
<dd>(default since btrfs-progs 3.18, kernel support since 3.10) </p>
<p> reduced-size metadata for extent references, saves a few percent of metadata</dl>
<p> <code>no-holes</code></p>
<dl>
<dd>(kernel support since 3.14) </p>
<p> improved representation of file extents where holes are not explicitly stored as an extent, saves a few percent of metadata if sparse files are used</dl>
<h2>Block Groups, Chunks, Raid</h2>
<p>The highlevel organizational units of a filesystem are block groups of three types: data, metadata and system. </p>
<p> <code>DATA</code></p>
<dl>
<dd>store data blocks and nothing else</dl>
<p> <code>METADATA</code></p>
<dl>
<dd>store internal metadata in b-trees, can store file data if they fit into the inline limit</dl>
<p> <code>SYSTEM</code></p>
<dl>
<dd>store structures that describe the mapping between the physical devices and the linear logical space representing the filesystem</dl>
<p> Other terms commonly used: </p>
<p> <code>block group</code>, <code>chunk</code></p>
<dl>
<dd>a logical range of space of a given profile, stores data, metadata or both; sometimes the terms are used interchangeably </p>
<p> A typical size of metadata block group is 256MiB (filesystem smaller than 50GiB) and 1GiB (larger than 50GiB), for data it&#8217;s 1GiB. The system block group size is a few megabytes.</dl>
<p> <code>RAID</code></p>
<dl>
<dd>a block group profile type that utilizes RAID-like features on multiple devices: striping, mirroring, parity</dl>
<p> <code>profile</code></p>
<dl>
<dd>when used in connection with block groups refers to the allocation strategy and constraints, see the section <i>PROFILES</i> for more details</dl>
<h2>Profiles</h2>
<p>There are the following block group types available: </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center ROWSPAN=2>
<p> <code>Profile</code> </td>
<td ALIGN=center COLSPAN=3>
<p> <code>Redundancy</code> </td>
<td ALIGN=center ROWSPAN=2>
<p> <code>Min/max devices</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>Copies</code> </td>
<td ALIGN=center>
<p> <code>Parity</code> </td>
<td ALIGN=center>
<p> <code>Striping</code> </td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> single </td>
<td ALIGN=center>
<p> 1 </td>
<td ALIGN=center>
</td>
<td ALIGN=center>
</td>
<td ALIGN=center>
<p> 1/any
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> DUP </td>
<td ALIGN=center>
<p> 2 / 1 device </td>
<td ALIGN=center>
</td>
<td ALIGN=center>
</td>
<td ALIGN=center>
<p> 1/any (see note 1)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> RAID0 </td>
<td ALIGN=center>
</td>
<td ALIGN=center>
</td>
<td ALIGN=center>
<p> 1 to N </td>
<td ALIGN=center>
<p> 2/any
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> RAID1 </td>
<td ALIGN=center>
<p> 2 </td>
<td ALIGN=center>
</td>
<td ALIGN=center>
</td>
<td ALIGN=center>
<p> 2/any
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> RAID10 </td>
<td ALIGN=center>
<p> 2 </td>
<td ALIGN=center>
</td>
<td ALIGN=center>
<p> 1 to N </td>
<td ALIGN=center>
<p> 4/any
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> RAID5 </td>
<td ALIGN=center>
<p> 1 </td>
<td ALIGN=center>
<p> 1 </td>
<td ALIGN=center>
<p> 2 to N &#8211; 1 </td>
<td ALIGN=center>
<p> 2/any (see note 2)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> RAID6 </td>
<td ALIGN=center>
<p> 1 </td>
<td ALIGN=center>
<p> 2 </td>
<td ALIGN=center>
<p> 3 to N &#8211; 2 </td>
<td ALIGN=center>
<p> 3/any (see note 3)
</td>
</tr>
</table>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> It&#8217;s not recommended to build btrfs with RAID0/1/10/5/6 profiles on partitions from the same device. Neither redundancy nor performance will be improved. </p>
</dl>
<p> <i>Note 1:</i> DUP may exist on more than 1 device if it starts on a single device and another one is added. Since version 4.5.1, <code>mkfs.btrfs</code> will let you create DUP on multiple devices. </p>
<p> <i>Note 2:</i> It&#8217;s not recommended to use 2 devices with RAID5. In that case, parity stripe will contain the same data as the data stripe, making RAID5 degraded to RAID1 with more overhead. </p>
<p> <i>Note 3:</i> It&#8217;s also not recommended to use 3 devices with RAID6, unless you want to get effectively 3 copies in a RAID1-like manner (but not exactly that). N-copies RAID1 is not implemented.</p>
<h2>Dup Profiles On A Single Device</h2>
<p>The mkfs utility will let the user create a filesystem with profiles that write the logical blocks to 2 physical locations. Whether there are really 2 physical copies highly depends on the underlying device type. </p>
<p> For example, a SSD drive can remap the blocks internally to a single copy&#8212;thus deduplicating them. This negates the purpose of increased redundancy and just wastes filesystem space without providing the expected level of redundancy. </p>
<p> The duplicated data/metadata may still be useful to statistically improve the chances on a device that might perform some internal optimizations. The actual details are not usually disclosed by vendors. For example we could expect that not all blocks get deduplicated. This will provide a non-zero probability of recovery compared to a zero chance if the single profile is used. The user should make the tradeoff decision. The deduplication in SSDs is thought to be widely available so the reason behind the mkfs default is to not give a false sense of redundancy. </p>
<p> As another example, the widely used USB flash or SD cards use a translation layer between the logical and physical view of the device. The data lifetime may be affected by frequent plugging. The memory cells could get damaged, hopefully not destroying both copies of particular data in case of DUP. </p>
<p> The wear levelling techniques can also lead to reduced redundancy, even if the device does not do any deduplication. The controllers may put data written in a short timespan into the same physical storage unit (cell, block etc). In case this unit dies, both copies are lost. BTRFS does not add any artificial delay between metadata writes. </p>
<p> The traditional rotational hard drives usually fail at the sector level. </p>
<p> In any case, a device that starts to misbehave and repairs from the DUP copy should be replaced! <code>DUP is not backup</code>.</p>
<h2>Known Issues</h2>
<p><code>SMALL FILESYSTEMS AND LARGE NODESIZE</code> </p>
<p> The combination of small filesystem size and large nodesize is not recommended in general and can lead to various ENOSPC-related issues during mount time or runtime. </p>
<p> Since mixed block group creation is optional, we allow small filesystem instances with differing values for <i>sectorsize</i> and <i>nodesize</i> to be created and could end up in the following situation: </p>
<dl>
<dd>
<pre># mkfs.btrfs -f -n 65536 /dev/loop0
btrfs-progs v3.19-rc2-405-g976307c
See <a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a> for more information.</pre>
</dl>
<dl>
<dd>
<pre>Performing full device TRIM (512.00MiB) ...
Label: (null)
UUID: 49fab72e-0c8b-466b-a3ca-d1bfe56475f0
Node size: 65536
Sector size: 4096
Filesystem size: 512.00MiB
Block group profiles:
 Data: single 8.00MiB
 Metadata: DUP 40.00MiB
 System: DUP 12.00MiB
SSD detected: no
Incompat features: extref, skinny-metadata
Number of devices: 1
Devices:
 ID SIZE PATH
 1 512.00MiB /dev/loop0</pre>
</dl>
<dl>
<dd>
<pre># mount /dev/loop0 /mnt/
mount: mount /dev/loop0 on /mnt failed: No space left on device</pre>
</dl>
<p> The ENOSPC occurs during the creation of the UUID tree. This is caused by large metadata blocks and space reservation strategy that allocates more than can fit into the filesystem.</p>
<h2>Availability</h2>
<p><code>mkfs.btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8), <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) </p>
