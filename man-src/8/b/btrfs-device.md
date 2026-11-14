---
title: "btrfs-device(8)"
name: "btrfs-device"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-device/"
description: "btrfs-device – manage devices of btrfs filesystems"
---

<p>btrfs-device &#8211; manage devices of btrfs filesystems</p>
<h2>Synopsis</h2>
<p><code>btrfs device</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p>The <code>btrfs device</code> command group is used to manage devices of the btrfs filesystems.</p>
<h2>Device Management</h2>
<p>Btrfs filesystem can be created on top of single or multiple block devices. Data and metadata are organized in allocation profiles with various redundancy policies. There&#8217;s some similarity with traditional RAID levels, but this could be confusing to users familiar with the traditional meaning. Due to the similarity, the RAID terminology is widely used in the documentation. See <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) for more details and the exact profile capabilities and constraints. </p>
<p> The device management works on a mounted filesystem. Devices can be added, removed or replaced, by commands provided by <code>btrfs device</code> and <code>btrfs replace</code>. </p>
<p> The profiles can be also changed, provided there&#8217;s enough workspace to do the conversion, using the <code>btrfs balance</code> command and namely the filter <i>convert</i>. </p>
<p> Profile</p>
<dl>
<dd>A profile describes an allocation policy based on the redundancy/replication constraints in connection with the number of devices. The profile applies to data and metadata block groups separately.</dl>
<p> RAID level</p>
<dl>
<dd>Where applicable, the level refers to a profile that matches constraints of the standard RAID levels. At the moment the supported ones are: RAID0, RAID1, RAID10, RAID5 and RAID6.</dl>
<p> See the section <code>TYPICAL USECASES</code> for some examples.</p>
<h2>Subcommand</h2>
<p><code>add</code> [-Kf] <i>&lt;device&gt;</i> [<i>&lt;device&gt;</i>&#8230;] <i>&lt;path&gt;</i></p>
<dl>
<dd>Add device(s) to the filesystem identified by <i>&lt;path&gt;</i>. </p>
<p> If applicable, a whole device discard (TRIM) operation is performed prior to adding the device. A device with existing filesystem detected by <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8) will prevent device addition and has to be forced. Alternatively the filesystem can be wiped from the device using eg. the <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) tool. </p>
<p> The operation is instant and does not affect existing data. The operation merely adds the device to the filesystem structures and creates some block groups headers. </p>
<p> <code>Options</code> </p>
<p> -K|&#8211;nodiscard</p>
<dl>
<dd>do not perform discard (TRIM) by default</dl>
<p> -f|&#8211;force</p>
<dl>
<dd>force overwrite of existing filesystem on the given disk(s)</dl>
</dl>
<p> <code>remove</code> <i>&lt;device&gt;</i>|<i>&lt;devid&gt;</i> [<i>&lt;device&gt;</i>|<i>&lt;devid&gt;</i>&#8230;] <i>&lt;path&gt;</i></p>
<dl>
<dd>Remove device(s) from a filesystem identified by <i>&lt;path&gt;</i> </p>
<p> Device removal must satisfy the profile constraints, otherwise the command fails. The filesystem must be converted to profile(s) that would allow the removal. This can typically happen when going down from 2 devices to 1 and using the RAID1 profile. See the <code>TYPICAL USECASES</code> section below. </p>
<p> The operation can take long as it needs to move all data from the device. </p>
<p> It is possible to delete the device that was used to mount the filesystem. The device entry in the mount table will be replaced by another device name with the lowest device id. </p>
<p> If the filesystem is mounted in degraded mode (-o degraded), special term <i>missing</i> can be used for <i>device</i>. In that case, the first device that is described by the filesystem metadata, but not present at the mount time will be removed. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 In most cases, there is only one missing device in degraded mode, otherwise mount fails. If there are two or more devices missing (e.g. possible in RAID6), you need specify <i>missing</i> as many times as the number of missing devices to remove all of them. </p>
</dl>
</dl>
<p> <code>delete</code> <i>&lt;device&gt;</i>|<i>&lt;devid&gt;</i> [<i>&lt;device&gt;</i>|<i>&lt;devid&gt;</i>&#8230;] <i>&lt;path&gt;</i></p>
<dl>
<dd>Alias of remove kept for backward compatibility</dl>
<p> <code>ready</code> <i>&lt;device&gt;</i></p>
<dl>
<dd>Wait until all devices of a multiple-device filesystem are scanned and registered within the kernel module. This is to provide a way for automatic filesystem mounting tools to wait before the mount can start. The device scan is only one of the preconditions and the mount can fail for other reasons. Normal users usually do not need this command and may safely ignore it.</dl>
<p> <code>scan</code> [options] [<i>&lt;device&gt;</i> [<i>&lt;device&gt;</i>&#8230;]]</p>
<dl>
<dd>Scan devices for a btrfs filesystem and register them with the kernel module. This allows mounting multiple-device filesystem by specifying just one from the whole group. </p>
<p> If no devices are passed, all block devices that blkid reports to contain btrfs are scanned. </p>
<p> The options <i>&#8211;all-devices</i> or <i>-d</i> can be used as a fallback in case blkid is not available. If used, behavior is the same as if no devices are passed. </p>
<p> The command can be run repeatedly. Devices that have been already registered remain as such. Reloading the kernel module will drop this information. There&#8217;s an alternative way of mounting multiple-device filesystem without the need for prior scanning. See the mount option <i>device</i>. </p>
<p> <code>Options</code> </p>
<p> -d|&#8211;all-devices</p>
<dl>
<dd>Enumerate and register all devices, use as a fallback in case blkid is not available.</dl>
<p> -u|&#8211;forget</p>
<dl>
<dd>Unregister a given device or all stale devices if no path is given, the device must be unmounted otherwise it&#8217;s an error.</dl>
</dl>
<p> <code>stats</code> [options] <i>&lt;path&gt;</i>|<i>&lt;device&gt;</i></p>
<dl>
<dd>Read and print the device IO error statistics for all devices of the given filesystem identified by <i>&lt;path&gt;</i> or for a single <i>&lt;device&gt;</i>. The filesystem must be mounted. See section <code>DEVICE STATS</code> for more information about the reported statistics and the meaning. </p>
<p> <code>Options</code> </p>
<p> -z|&#8211;reset</p>
<dl>
<dd>Print the stats and reset the values to zero afterwards.</dl>
<p> -c|&#8211;check</p>
<dl>
<dd>Check if the stats are all zeros and return 0 if it is so. Set bit 6 of the return code if any of the statistics is no-zero. The error values is 65 if reading stats from at least one device failed, otherwise it&#8217;s 64.</dl>
</dl>
<p> <code>usage</code> [options] <i>&lt;path&gt;</i> [<i>&lt;path&gt;</i>&#8230;]</p>
<dl>
<dd>Show detailed information about internal allocations in devices. </p>
<p> <code>Options</code> </p>
<p> -b|&#8211;raw</p>
<dl>
<dd>raw numbers in bytes, without the <i>B</i> suffix</dl>
<p> -h|&#8211;human-readable</p>
<dl>
<dd>print human friendly numbers, base 1024, this is the default</dl>
<p> -H</p>
<dl>
<dd>print human friendly numbers, base 1000</dl>
<p> &#8211;iec</p>
<dl>
<dd>select the 1024 base for the following options, according to the IEC standard</dl>
<p> &#8211;si</p>
<dl>
<dd>select the 1000 base for the following options, according to the SI standard</dl>
<p> -k|&#8211;kbytes</p>
<dl>
<dd>show sizes in KiB, or kB with &#8211;si</dl>
<p> -m|&#8211;mbytes</p>
<dl>
<dd>show sizes in MiB, or MB with &#8211;si</dl>
<p> -g|&#8211;gbytes</p>
<dl>
<dd>show sizes in GiB, or GB with &#8211;si</dl>
<p> -t|&#8211;tbytes</p>
<dl>
<dd>show sizes in TiB, or TB with &#8211;si</dl>
</dl>
<p> If conflicting options are passed, the last one takes precedence.</p>
<h2>Typical Usecases</h2>
<h3>Starting With A Single-Device Filesystem</h3>
<p>Assume we&#8217;ve created a filesystem on a block device <i>/dev/sda</i> with profile <i>single/single</i> (data/metadata), the device size is 50GiB and we&#8217;ve used the whole device for the filesystem. The mount point is <i>/mnt</i>. </p>
<p> The amount of data stored is 16GiB, metadata have allocated 2GiB. </p>
<p> <font SIZE="+1"> <code>ADD NEW DEVICE</code></p>
<dl>
<dd>We want to increase the total size of the filesystem and keep the profiles. The size of the new device <i>/dev/sdb</i> is 100GiB. </p>
<dl>
<dd></font></p>
<pre>$ btrfs device add /dev/sdb /mnt</pre>
</dl>
<p> The amount of free data space increases by less than 100GiB, some space is allocated for metadata.</dl>
<p> <font SIZE="+1"> <code>CONVERT TO RAID1</code></p>
<dl>
<dd>Now we want to increase the redundancy level of both data and metadata, but we&#8217;ll do that in steps. Note, that the device sizes are not equal and we&#8217;ll use that to show the capabilities of split data/metadata and independent profiles. </p>
<p> The constraint for RAID1 gives us at most 50GiB of usable space and exactly 2 copies will be stored on the devices. </p>
<p> First we&#8217;ll convert the metadata. As the metadata occupy less than 50GiB and there&#8217;s enough workspace for the conversion process, we can do: </p>
<dl>
<dd></font></p>
<pre>$ btrfs balance start -mconvert=raid1 /mnt</pre>
</dl>
<p> This operation can take a while, because all metadata have to be moved and all block pointers updated. Depending on the physical locations of the old and new blocks, the disk seeking is the key factor affecting performance. </p>
<p> You&#8217;ll note that the system block group has been also converted to RAID1, this normally happens as the system block group also holds metadata (the physical to logical mappings). </p>
<p> What changed: </p>
<dl>
<dd>&bull; available data space decreased by 3GiB, usable roughly (50 &#8211; 3) + (100 &#8211; 3) = 144 GiB</dl>
<dl>
<dd>&bull; metadata redundancy increased</dl>
<p> IOW, the unequal device sizes allow for combined space for data yet improved redundancy for metadata. If we decide to increase redundancy of data as well, we&#8217;re going to lose 50GiB of the second device for obvious reasons. </p>
<dl>
<dd>
<pre>$ btrfs balance start -dconvert=raid1 /mnt</pre>
</dl>
<p> The balance process needs some workspace (ie. a free device space without any data or metadata block groups) so the command could fail if there&#8217;s too much data or the block groups occupy the whole first device. </p>
<p> The device size of <i>/dev/sdb</i> as seen by the filesystem remains unchanged, but the logical space from 50-100GiB will be unused.</dl>
<p> <font SIZE="+1"> <code>REMOVE DEVICE</code></p>
<dl>
<dd>Device removal must satisfy the profile constraints, otherwise the command fails. For example: </p>
<dl>
<dd></font></p>
<pre>$ btrfs device remove /dev/sda /mnt
ERROR: error removing device '/dev/sda': unable to go below two devices on raid1</pre>
</dl>
<p> In order to remove a device, you need to convert the profile in this case: </p>
<dl>
<dd>
<pre>$ btrfs balance start -mconvert=dup -dconvert=single /mnt
$ btrfs device remove /dev/sda /mnt</pre>
</dl>
</dl>
<h2>Device Stats</h2>
<p>The device stats keep persistent record of several error classes related to doing IO. The current values are printed at mount time and updated during filesystem lifetime or from a scrub run. </p>
<dl>
<dd>
<pre>$ btrfs device stats /dev/sda3
[/dev/sda3].write_io_errs 0
[/dev/sda3].read_io_errs 0
[/dev/sda3].flush_io_errs 0
[/dev/sda3].corruption_errs 0
[/dev/sda3].generation_errs 0</pre>
</dl>
<p> write_io_errs</p>
<dl>
<dd>Failed writes to the block devices, means that the layers beneath the filesystem were not able to satisfy the write request.</dl>
<p> read_io_errors</p>
<dl>
<dd>Read request analogy to write_io_errs.</dl>
<p> flush_io_errs</p>
<dl>
<dd>Number of failed writes with the <i>FLUSH</i> flag set. The flushing is a method of forcing a particular order between write requests and is crucial for implementing crash consistency. In case of btrfs, all the metadata blocks must be permanently stored on the block device before the superblock is written.</dl>
<p> corruption_errs</p>
<dl>
<dd>A block checksum mismatched or a corrupted metadata header was found.</dl>
<p> generation_errs</p>
<dl>
<dd>The block generation does not match the expected value (eg. stored in the parent node).</dl>
<h2>Exit Status</h2>
<p><code>btrfs device</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure. </p>
<p> If the <i>-s</i> option is used, <code>btrfs device stats</code> will add 64 to the exit status if any of the error counters is non-zero.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-replace/">btrfs-replace</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-balance/">btrfs-balance</a></code>(8) </p>
