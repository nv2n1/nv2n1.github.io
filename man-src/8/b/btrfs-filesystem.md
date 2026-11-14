---
title: "btrfs-filesystem(8)"
name: "btrfs-filesystem"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-filesystem/"
description: "btrfs-filesystem – command group that primarily does work on the whole filesystems"
---

<p>btrfs-filesystem &#8211; command group that primarily does work on the whole filesystems</p>
<h2>Synopsis</h2>
<p><code>btrfs filesystem</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs filesystem</code> is used to perform several whole filesystem level tasks, including all the regular filesystem operations like resizing, space stats, label setting/getting, and defragmentation. There are other whole filesystem tasks like scrub or balance that are grouped in separate commands.</p>
<h2>Subcommand</h2>
<p><code>df</code> [options] <i>&lt;path&gt;</i></p>
<dl>
<dd>Show a terse summary information about allocation of block group types of a given mount point. The original purpose of this command was a debugging helper. The output needs to be further interpreted and is not suitable for quick overview. </p>
<p> An example with description: </p>
<dl>
<dd>&bull; device size: <i>1.9TiB</i>, one device, no RAID</dl>
<dl>
<dd>&bull; filesystem size: <i>1.9TiB</i></dl>
<dl>
<dd>&bull; created with: <i>mkfs.btrfs -d single -m single</i></dl>
<dl>
<dd>
<pre>$ btrfs filesystem df /path
Data, single: total=1.15TiB, used=1.13TiB
System, single: total=32.00MiB, used=144.00KiB
Metadata, single: total=12.00GiB, used=6.45GiB
GlobalReserve, single: total=512.00MiB, used=0.00B</pre>
</dl>
<dl>
<dd>&bull; <i>Data</i>, <i>System</i> and <i>Metadata</i> are separate block group types. <i>GlobalReserve</i> is an artificial and internal emergency space, see below.</dl>
<dl>
<dd>&bull; <i>single</i> &#8212; the allocation profile, defined at mkfs time</dl>
<dl>
<dd>&bull; <i>total</i> &#8212; sum of space reserved for all allocation profiles of the given type, ie. all Data/single. Note that it&#8217;s not total size of filesystem.</dl>
<dl>
<dd>&bull; <i>used</i> &#8212; sum of used space of the above, ie. file extents, metadata blocks</dl>
<p> <i>GlobalReserve</i> is an artificial and internal emergency space. It is used eg. when the filesystem is full. Its <i>total</i> size is dynamic based on the filesystem size, usually not larger than 512MiB, <i>used</i> may fluctuate. </p>
<p> The GlobalReserve is a portion of Metadata. In case the filesystem metadata is exhausted, <i>GlobalReserve/total + Metadata/used = Metadata/total</i>. Otherwise there appears to be some unused space of Metadata. </p>
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
<dd>show sizes in TiB, or TB with &#8211;si </p>
<p> If conflicting options are passed, the last one takes precedence.</dl>
</dl>
<p> <code>defragment</code> [options] <i>&lt;file&gt;</i>|<i>&lt;dir&gt;</i> [<i>&lt;file&gt;</i>|<i>&lt;dir&gt;</i>&#8230;]</p>
<dl>
<dd>Defragment file data on a mounted filesystem. Requires kernel 2.6.33 and newer. </p>
<p> If <i>-r</i> is passed, files in dir will be defragmented recursively (not descending to subvolumes and mount points). The start position and the number of bytes to defragment can be specified by start and length using <i>-s</i> and <i>-l</i> options below. Extents bigger than value given by <i>-t</i> will be skipped, otherwise this value is used as a target extent size, but is only advisory and may not be reached if the free space is too fragmented. Use 0 to take the kernel default, which is 256kB but may change in the future. You can also turn on compression in defragment operations. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Defragmenting with Linux kernel versions &lt; 3.9 or &ge; 3.14-rc2 as well as with Linux stable kernel versions &ge; 3.10.31, &ge; 3.12.12 or &ge; 3.13.4 will break up the reflinks of COW data (for example files copied with <code>cp &#8211;reflink</code>, snapshots or de-duplicated data). This may cause considerable increase of space usage depending on the broken up reflinks. </p>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Directory arguments without <i>-r</i> do not defragment files recursively but will defragment certain internal trees (extent tree and the subvolume tree). This has been confusing and could be removed in the future. </p>
</dl>
<p> For <i>start</i>, <i>len</i>, <i>size</i> it is possible to append units designator: &#8216;K&#8217;, &#8216;M&#8217;, &#8216;G&#8217;, &#8216;T&#8217;, &#8216;P&#8217;, or &#8216;E&#8217;, which represent KiB, MiB, GiB, TiB, PiB, or EiB, respectively (case does not matter). </p>
<p> <code>Options</code> </p>
<p> -v</p>
<dl>
<dd>be verbose, print file names as they&#8217;re submitted for defragmentation</dl>
<p> -c[<i>&lt;algo&gt;</i>]</p>
<dl>
<dd>compress file contents while defragmenting. Optional argument selects the compression algorithm, <i>zlib</i> (default), <i>lzo</i> or <i>zstd</i>. Currently it&#8217;s not possible to select no compression. See also section <i>EXAMPLES</i>.</dl>
<p> -r</p>
<dl>
<dd>defragment files recursively in given directories, does not descend to subvolumes or mount points</dl>
<p> -f</p>
<dl>
<dd>flush data for each file before going to the next file. </p>
<p> This will limit the amount of dirty data to current file, otherwise the amount accumulates from several files and will increase system load. This can also lead to ENOSPC if there&#8217;s too much dirty data to write and it&#8217;s not possible to make the reservations for the new data (ie. how the COW design works).</dl>
<p> -s <i>&lt;start&gt;</i>[kKmMgGtTpPeE]</p>
<dl>
<dd>defragmentation will start from the given offset, default is beginning of a file</dl>
<p> -l <i>&lt;len&gt;</i>[kKmMgGtTpPeE]</p>
<dl>
<dd>defragment only up to <i>len</i> bytes, default is the file size</dl>
<p> -t <i>&lt;size&gt;</i>[kKmMgGtTpPeE]</p>
<dl>
<dd>target extent size, do not touch extents bigger than <i>size</i>, default: 32M </p>
<p> The value is only advisory and the final size of the extents may differ, depending on the state of the free space and fragmentation or other internal logic. Reasonable values are from tens to hundreds of megabytes.</dl>
</dl>
<p> <code>du</code> [options] <i>&lt;path&gt;</i> [<i>&lt;path&gt;</i>..]</p>
<dl>
<dd>Calculate disk usage of the target files using FIEMAP. For individual files, it will report a count of total bytes, and exclusive (not shared) bytes. We also calculate a <i>set shared</i> value which is described below. </p>
<p> Each argument to <i>btrfs filesystem du</i> will have a <i>set shared</i> value calculated for it. We define each <i>set</i> as those files found by a recursive search of an argument (recursion descends to subvolumes but not mount points). The <i>set shared</i> value then is a sum of all shared space referenced by the set. </p>
<p> <i>set shared</i> takes into account overlapping shared extents, hence it isn&#8217;t as simple as adding up shared extents. </p>
<p> <code>Options</code> </p>
<p> -s|&#8211;summarize</p>
<dl>
<dd>display only a total for each argument</dl>
<p> &#8211;raw</p>
<dl>
<dd>raw numbers in bytes, without the <i>B</i> suffix.</dl>
<p> &#8211;human-readable</p>
<dl>
<dd>print human friendly numbers, base 1024, this is the default</dl>
<p> &#8211;iec</p>
<dl>
<dd>select the 1024 base for the following options, according to the IEC standard.</dl>
<p> &#8211;si</p>
<dl>
<dd>select the 1000 base for the following options, according to the SI standard.</dl>
<p> &#8211;kbytes</p>
<dl>
<dd>show sizes in KiB, or kB with &#8211;si.</dl>
<p> &#8211;mbytes</p>
<dl>
<dd>show sizes in MiB, or MB with &#8211;si.</dl>
<p> &#8211;gbytes</p>
<dl>
<dd>show sizes in GiB, or GB with &#8211;si.</dl>
<p> &#8211;tbytes</p>
<dl>
<dd>show sizes in TiB, or TB with &#8211;si.</dl>
</dl>
<p> <code>label</code> [<i>&lt;device&gt;</i>|<i>&lt;mountpoint&gt;</i>] [<i>&lt;newlabel&gt;</i>]</p>
<dl>
<dd>Show or update the label of a filesystem. This works on a mounted filesystem or a filesystem image. </p>
<p> The <i>newlabel</i> argument is optional. Current label is printed if the argument is omitted. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 the maximum allowable length shall be less than 256 chars and must not contain a newline. The trailing newline is stripped automatically. </p>
</dl>
</dl>
<p> <code>resize</code> [<i>&lt;devid&gt;</i>:][+/-]<i>&lt;size&gt;</i>[kKmMgGtTpPeE]|[<i>&lt;devid&gt;</i>:]max <i>&lt;path&gt;</i></p>
<dl>
<dd>Resize a mounted filesystem identified by <i>path</i>. A particular device can be resized by specifying a <i>devid</i>. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If <i>path</i> is a file containing a BTRFS image then resize does not work as expected and does not resize the image. This would resize the underlying filesystem instead. </p>
</dl>
<p> The <i>devid</i> can be found in the output of <code>btrfs filesystem show</code> and defaults to 1 if not specified. The <i>size</i> parameter specifies the new size of the filesystem. If the prefix <i>+</i> or <i>&#8211;</i> is present the size is increased or decreased by the quantity <i>size</i>. If no units are specified, bytes are assumed for <i>size</i>. Optionally, the size parameter may be suffixed by one of the following unit designators: &#8216;K&#8217;, &#8216;M&#8217;, &#8216;G&#8217;, &#8216;T&#8217;, &#8216;P&#8217;, or &#8216;E&#8217;, which represent KiB, MiB, GiB, TiB, PiB, or EiB, respectively (case does not matter). </p>
<p> If <i>max</i> is passed, the filesystem will occupy all available space on the device respecting <i>devid</i> (remember, devid 1 by default). </p>
<p> The resize command does not manipulate the size of underlying partition. If you wish to enlarge/reduce a filesystem, you must make sure you can expand the partition before enlarging the filesystem and shrink the partition after reducing the size of the filesystem. This can done using <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) or <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8) to delete the existing partition and recreate it with the new desired size. When recreating the partition make sure to use the same starting partition offset as before. </p>
<p> Growing is usually instant as it only updates the size. However, shrinking could take a long time if there are data in the device area that&#8217;s beyond the new end. Relocation of the data takes time. </p>
<p> See also section <i>EXAMPLES</i>.</dl>
<p> <code>show</code> [options] [<i>&lt;path&gt;</i>|<i>&lt;uuid&gt;</i>|<i>&lt;device&gt;</i>|<i>&lt;label&gt;</i>]</p>
<dl>
<dd>Show the btrfs filesystem with some additional info about devices and space allocation. </p>
<p> If no option none of <i>path</i>/<i>uuid</i>/<i>device</i>/<i>label</i> is passed, information about all the BTRFS filesystems is shown, both mounted and unmounted. </p>
<p> <code>Options</code> </p>
<p> -m|&#8211;mounted</p>
<dl>
<dd>probe kernel for mounted BTRFS filesystems</dl>
<p> -d|&#8211;all-devices</p>
<dl>
<dd>scan all devices under /dev, otherwise the devices list is extracted from the /proc/partitions file. This is a fallback option if there&#8217;s no device node manager (like udev) available in the system.</dl>
<p> &#8211;raw</p>
<dl>
<dd>raw numbers in bytes, without the <i>B</i> suffix</dl>
<p> &#8211;human-readable</p>
<dl>
<dd>print human friendly numbers, base 1024, this is the default</dl>
<p> &#8211;iec</p>
<dl>
<dd>select the 1024 base for the following options, according to the IEC standard</dl>
<p> &#8211;si</p>
<dl>
<dd>select the 1000 base for the following options, according to the SI standard</dl>
<p> &#8211;kbytes</p>
<dl>
<dd>show sizes in KiB, or kB with &#8211;si</dl>
<p> &#8211;mbytes</p>
<dl>
<dd>show sizes in MiB, or MB with &#8211;si</dl>
<p> &#8211;gbytes</p>
<dl>
<dd>show sizes in GiB, or GB with &#8211;si</dl>
<p> &#8211;tbytes</p>
<dl>
<dd>show sizes in TiB, or TB with &#8211;si</dl>
</dl>
<p> <code>sync</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Force a sync of the filesystem at <i>path</i>. This is done via a special ioctl and will also trigger cleaning of deleted subvolumes. Besides that it&#8217;s equivalent to the <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1) command.</dl>
<p> <code>usage</code> [options] <i>&lt;path&gt;</i> [<i>&lt;path&gt;</i>&#8230;]</p>
<dl>
<dd>Show detailed information about internal filesystem usage. This is supposed to replace the <code>btrfs filesystem df</code> command in the long run. </p>
<p> The level of detail can differ if the command is run under a regular or the root user (due to use of restricted ioctl). For both there&#8217;s a summary section with information about space usage: </p>
<dl>
<dd>
<pre>$ btrfs filesystem usage /path
WARNING: cannot read detailed chunk info, RAID5/6 numbers will be incorrect, run as root
Overall:
 Device size: 1.82TiB
 Device allocated: 1.17TiB
 Device unallocated: 669.99GiB
 Device missing: 0.00B
 Used: 1.14TiB
 Free (estimated): 692.57GiB (min: 692.57GiB)
 Data ratio: 1.00
 Metadata ratio: 1.00
 Global reserve: 512.00MiB (used: 0.00B)</pre>
</dl>
<p> The root user will also see stats broken down by block group types: </p>
<dl>
<dd>
<pre>Data,single: Size:1.15TiB, Used:1.13TiB
 /dev/sdb 1.15TiB
Metadata,single: Size:12.00GiB, Used:6.45GiB
 /dev/sdb 12.00GiB
System,single: Size:32.00MiB, Used:144.00KiB
 /dev/sdb 32.00MiB
Unallocated:
 /dev/sdb 669.99GiB</pre>
</dl>
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
<p> -T</p>
<dl>
<dd>show data in tabular format </p>
<p> If conflicting options are passed, the last one takes precedence.</dl>
</dl>
<h2>Examples</h2>
<p><code>$ btrfs filesystem defrag -v -r dir/</code> Recursively defragment files under <i>dir/</i>, print files as they are processed. The file names will be printed in batches, similarly the amount of data triggered by defragmentation will be proportional to last N printed files. The system dirty memory throttling will slow down the defragmentation but there can still be a lot of IO load and the system may stall for a moment. <code>$ btrfs filesystem defrag -v -r -f dir/</code> Recursively defragment files under <i>dir/</i>, be verbose and wait until all blocks are flushed before processing next file. You can note slower progress of the output and lower IO load (proportional to currently defragmented file). <code>$ btrfs filesystem defrag -v -r -f -clzo dir/</code> Recursively defragment files under <i>dir/</i>, be verbose, wait until all blocks are flushed and force file compression. <code>$ btrfs filesystem defrag -v -r -t 64M dir/</code> Recursively defragment files under <i>dir/</i>, be verbose and try to merge extents to be about 64MiB. As stated above, the success rate depends on actual free space fragmentation and the final result is not guaranteed to meet the target even if run repeatedly. <code>$ btrfs filesystem resize -1G /path</code> <code>$ btrfs filesystem resize 1:-1G /path</code> Shrink size of the filesystem&#8217;s device id 1 by 1GiB. The first syntax expects a device with id 1 to exist, otherwise fails. The second is equivalent and more explicit. For a single-device filesystem it&#8217;s typically not necessary to specify the devid though. <code>$ btrfs filesystem resize max /path</code> <code>$ btrfs filesystem resize 1:max /path</code> Let&#8217;s assume that devid 1 exists and the filesystem does not occupy the whole block device, eg. it has been enlarged and we want to grow the filesystem. By simply using <i>max</i> as size we will achieve that.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 There are two ways to minimize the filesystem on a given device. The <code>btrfs inspect-internal min-dev-size</code> command, or iteratively shrink in steps. </p>
<h2>Exit Status</h2>
<p><code>btrfs filesystem</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), </p>
