---
title: "btrfs-balance(8)"
name: "btrfs-balance"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-balance/"
description: "btrfs-balance – balance block groups on a btrfs filesystem"
---

<p>btrfs-balance &#8211; balance block groups on a btrfs filesystem</p>
<h2>Synopsis</h2>
<p><code>btrfs balance</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p>The primary purpose of the balance feature is to spread block groups across all devices so they match constraints defined by the respective profiles. See <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) section <i>PROFILES</i> for more details. The scope of the balancing process can be further tuned by use of filters that can select the block groups to process. Balance works only on a mounted filesystem. The balance operation is cancellable by the user. The on-disk state of the filesystem is always consistent so an unexpected interruption (eg. system crash, reboot) does not corrupt the filesystem. The progress of the balance operation is temporarily stored as an internal state and will be resumed upon mount, unless the mount option <i>skip_balance</i> is specified.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 running balance without filters will take a lot of time as it basically rewrites the entire filesystem and needs to update all block pointers.  The filters can be used to perform following actions:</p>
<dl>
<dd>&bull; convert block group profiles (filter <i>convert</i>)</dl>
<dl>
<dd>&bull; make block group usage more compact (filter <i>usage</i>)</dl>
<dl>
<dd>&bull; perform actions only on a given device (filters <i>devid</i>, <i>drange</i>)</dl>
<p> The filters can be applied to a combination of block group types (data, metadata, system). Note that changing <i>system</i> needs the force option.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 the balance operation needs enough work space, ie. space that is completely unused in the filesystem, otherwise this may lead to ENOSPC reports. See the section <i>ENOSPC</i> for more details. </p>
<h2>Compatibility</h2>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The balance subcommand also exists under the <code>btrfs filesystem</code> namespace. This still works for backward compatibility but is deprecated and should not be used any more. </p>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> A short syntax <code>btrfs balance </code><i>&lt;path&gt;</i> works due to backward compatibility but is deprecated and should not be used any more. Use <code>btrfs balance start</code> command instead. </p>
</dl>
<h2>Performance Implications</h2>
<p>Balancing operations are very IO intensive and can also be quite CPU intensive, impacting other ongoing filesystem operations. Typically large amounts of data are copied from one location to another, with corresponding metadata updates. </p>
<p> Depending upon the block group layout, it can also be seek heavy. Performance on rotational devices is noticeably worse compared to SSDs or fast arrays.</p>
<h2>Subcommand</h2>
<p><code>cancel</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>cancels a running or paused balance, the command will block and wait until the current blockgroup being processed completes</dl>
<p> <code>pause</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>pause running balance operation, this will store the state of the balance progress and used filters to the filesystem</dl>
<p> <code>resume</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>resume interrupted balance, the balance status must be stored on the filesystem from previous run, eg. after it was forcibly interrupted and mounted again with <i>skip_balance</i></dl>
<p> <code>start</code> [options] <i>&lt;path&gt;</i></p>
<dl>
<dd>start the balance operation according to the specified filters, no filters will rewrite the entire filesystem. The process runs in the foreground. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 the balance command without filters will basically rewrite everything in the filesystem. The run time is potentially very long, depending on the filesystem size. To prevent starting a full balance by accident, the user is warned and has a few seconds to cancel the operation before it starts. The warning and delay can be skipped with <i>&#8211;full-balance</i> option. </p>
</dl>
<p> Please note that the filters must be written together with the <i>-d</i>, <i>-m</i> and <i>-s</i> options, because they&#8217;re optional and bare <i>-d</i> etc also work and mean no filters. </p>
<p> <code>Options</code> </p>
<p> -d[<i>&lt;filters&gt;</i>]</p>
<dl>
<dd>act on data block groups, see <code>FILTERS</code> section for details about <i>filters</i></dl>
<p> -m[<i>&lt;filters&gt;</i>]</p>
<dl>
<dd>act on metadata chunks, see <code>FILTERS</code> section for details about <i>filters</i></dl>
<p> -s[<i>&lt;filters&gt;</i>]</p>
<dl>
<dd>act on system chunks (requires <i>-f</i>), see <code>FILTERS</code> section for details about <i>filters</i>.</dl>
<p> -v</p>
<dl>
<dd>be verbose and print balance filter arguments</dl>
<p> -f</p>
<dl>
<dd>force a reduction of metadata integrity, eg. when going from <i>raid1</i> to <i>single</i></dl>
<p> &#8211;background|&#8211;bg</p>
<dl>
<dd>run the balance operation asynchronously in the background, uses <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) to start the process that calls the kernel ioctl</dl>
</dl>
<p> <code>status</code> [-v] <i>&lt;path&gt;</i></p>
<dl>
<dd>Show status of running or paused balance. </p>
<p> If <i>-v</i> option is given, output will be verbose.</dl>
<h2>Filters</h2>
<p>From kernel 3.3 onwards, btrfs balance can limit its action to a subset of the whole filesystem, and can be used to change the replication configuration (e.g. moving data from single to RAID1). This functionality is accessed through the <i>-d</i>, <i>-m</i> or <i>-s</i> options to btrfs balance start, which filter on data, metadata and system blocks respectively. </p>
<p> A filter has the following structure: <i>type</i>[=<i>params</i>][,<i>type</i>=&#8230;] </p>
<p> The available types are: </p>
<p> <code>profiles=</code><i>&lt;profiles&gt;</i></p>
<dl>
<dd>Balances only block groups with the given profiles. Parameters are a list of profile names separated by &quot;<i>|</i>&quot; (pipe).</dl>
<p> <code>usage=</code><i>&lt;percent&gt;</i>, <code>usage=</code><i>&lt;range&gt;</i></p>
<dl>
<dd>Balances only block groups with usage under the given percentage. The value of 0 is allowed and will clean up completely unused block groups, this should not require any new work space allocated. You may want to use <i>usage=0</i> in case balance is returning ENOSPC and your filesystem is not too full. </p>
<p> The argument may be a single value or a range. The single value <i>N</i> means <i>at most N percent used</i>, equivalent to <i>..N</i> range syntax. Kernels prior to 4.4 accept only the single value format. The minimum range boundary is inclusive, maximum is exclusive.</dl>
<p> <code>devid=</code><i>&lt;id&gt;</i></p>
<dl>
<dd>Balances only block groups which have at least one chunk on the given device. To list devices with ids use <code>btrfs filesystem show</code>.</dl>
<p> <code>drange=</code><i>&lt;range&gt;</i></p>
<dl>
<dd>Balance only block groups which overlap with the given byte range on any device. Use in conjunction with <i>devid</i> to filter on a specific device. The parameter is a range specified as <i>start..end</i>.</dl>
<p> <code>vrange=</code><i>&lt;range&gt;</i></p>
<dl>
<dd>Balance only block groups which overlap with the given byte range in the filesystem&#8217;s internal virtual address space. This is the address space that most reports from btrfs in the kernel log use. The parameter is a range specified as <i>start..end</i>.</dl>
<p> <code>convert=</code><i>&lt;profile&gt;</i></p>
<dl>
<dd>Convert each selected block group to the given profile name identified by parameters. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 starting with kernel 4.5, the <i>data</i> chunks can be converted to/from the <i>DUP</i> profile on a single device. </p>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 starting with kernel 4.6, all profiles can be converted to/from <i>DUP</i> on multi-device filesystems. </p>
</dl>
</dl>
<p> <code>limit=</code><i>&lt;number&gt;</i>, <code>limit=</code><i>&lt;range&gt;</i></p>
<dl>
<dd>Process only given number of chunks, after all filters are applied. This can be used to specifically target a chunk in connection with other filters (<i>drange</i>, <i>vrange</i>) or just simply limit the amount of work done by a single balance run. </p>
<p> The argument may be a single value or a range. The single value <i>N</i> means <i>at most N chunks</i>, equivalent to <i>..N</i> range syntax. Kernels prior to 4.4 accept only the single value format. The range minimum and maximum are inclusive.</dl>
<p> <code>stripes=</code><i>&lt;range&gt;</i></p>
<dl>
<dd>Balance only block groups which have the given number of stripes. The parameter is a range specified as <i>start..end</i>. Makes sense for block group profiles that utilize striping, ie. RAID0/10/5/6. The range minimum and maximum are inclusive.</dl>
<p> <code>soft</code></p>
<dl>
<dd>Takes no parameters. Only has meaning when converting between profiles. When doing convert from one profile to another and soft mode is on, chunks that already have the target profile are left untouched. This is useful e.g. when half of the filesystem was converted earlier but got cancelled. </p>
<p> The soft mode switch is (like every other filter) per-type. For example, this means that we can convert metadata chunks the &quot;hard&quot; way while converting data chunks selectively with soft switch.</dl>
<p> Profile names, used in <i>profiles</i> and <i>convert</i> are one of: <i>raid0</i>, <i>raid1</i>, <i>raid10</i>, <i>raid5</i>, <i>raid6</i>, <i>dup</i>, <i>single</i>. The mixed data/metadata profiles can be converted in the same way, but it&#8217;s conversion between mixed and non-mixed is not implemented. For the constraints of the profiles please refer to <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), section <i>PROFILES</i>.</p>
<h2>Enospc</h2>
<p>The way balance operates, it usually needs to temporarily create a new block group and move the old data there, before the old block group can be removed. For that it needs the work space, otherwise it fails for ENOSPC reasons. This is not the same ENOSPC as if the free space is exhausted. This refers to the space on the level of block groups, which are bigger parts of the filesystem that contain many file extents. </p>
<p> The free work space can be calculated from the output of the <code>btrfs filesystem show</code> command: </p>
<dl>
<dd>
<pre> Label: 'BTRFS' uuid: 8a9d72cd-ead3-469d-b371-9c7203276265
 Total devices 2 FS bytes used 77.03GiB
 devid 1 size 53.90GiB used 51.90GiB path /dev/sdc2
 devid 2 size 53.90GiB used 51.90GiB path /dev/sde1</pre>
</dl>
<p> <i>size</i> &#8211; <i>used</i> = <i>free work space</i> <i>53.90GiB</i> &#8211; <i>51.90GiB</i> = <i>2.00GiB</i> </p>
<p> An example of a filter that does not require workspace is <i>usage=0</i>. This will scan through all unused block groups of a given type and will reclaim the space. After that it might be possible to run other filters. </p>
<p> <code>CONVERSIONS ON MULTIPLE DEVICES</code> </p>
<p> Conversion to profiles based on striping (RAID0, RAID5/6) require the work space on each device. An interrupted balance may leave partially filled block groups that consume the work space.</p>
<h2>Examples</h2>
<p>A more comprehensive example when going from one to multiple devices, and back, can be found in section <i>TYPICAL USECASES</i> of <code><a href="/docs/linux/man/8-btrfs-device/">btrfs-device</a></code>(8).</p>
<h3>Making Block Group Layout More Compact</h3>
<p>The layout of block groups is not normally visible; most tools report only summarized numbers of free or used space, but there are still some hints provided. </p>
<p> Let&#8217;s use the following real life example and start with the output: </p>
<dl>
<dd>
<pre>$ btrfs filesystem df /path
Data, single: total=75.81GiB, used=64.44GiB
System, RAID1: total=32.00MiB, used=20.00KiB
Metadata, RAID1: total=15.87GiB, used=8.84GiB
GlobalReserve, single: total=512.00MiB, used=0.00B</pre>
</dl>
<p> Roughly calculating for data, <i>75G &#8211; 64G = 11G</i>, the used/total ratio is about <i>85%</i>. How can we can interpret that: </p>
<dl>
<dd>&bull; chunks are filled by 85% on average, ie. the <i>usage</i> filter with anything smaller than 85 will likely not affect anything</dl>
<dl>
<dd>&bull; in a more realistic scenario, the space is distributed unevenly, we can assume there are completely used chunks and the remaining are partially filled</dl>
<p> Compacting the layout could be used on both. In the former case it would spread data of a given chunk to the others and removing it. Here we can estimate that roughly 850 MiB of data have to be moved (85% of a 1 GiB chunk). </p>
<p> In the latter case, targeting the partially used chunks will have to move less data and thus will be faster. A typical filter command would look like: </p>
<dl>
<dd>
<pre># btrfs balance start -dusage=50 /path
Done, had to relocate 2 out of 97 chunks
$ btrfs filesystem df /path
Data, single: total=74.03GiB, used=64.43GiB
System, RAID1: total=32.00MiB, used=20.00KiB
Metadata, RAID1: total=15.87GiB, used=8.84GiB
GlobalReserve, single: total=512.00MiB, used=0.00B</pre>
</dl>
<p> As you can see, the <i>total</i> amount of data is decreased by just 1 GiB, which is an expected result. Let&#8217;s see what will happen when we increase the estimated usage filter. </p>
<dl>
<dd>
<pre># btrfs balance start -dusage=85 /path
Done, had to relocate 13 out of 95 chunks
$ btrfs filesystem df /path
Data, single: total=68.03GiB, used=64.43GiB
System, RAID1: total=32.00MiB, used=20.00KiB
Metadata, RAID1: total=15.87GiB, used=8.85GiB
GlobalReserve, single: total=512.00MiB, used=0.00B</pre>
</dl>
<p> Now the used/total ratio is about 94% and we moved about <i>74G &#8211; 68G = 6G</i> of data to the remaining blockgroups, ie. the 6GiB are now free of filesystem structures, and can be reused for new data or metadata block groups. </p>
<p> We can do a similar exercise with the metadata block groups, but this should not typically be necessary, unless the used/total ratio is really off. Here the ratio is roughly 50% but the difference as an absolute number is &quot;a few gigabytes&quot;, which can be considered normal for a workload with snapshots or reflinks updated frequently. </p>
<dl>
<dd>
<pre># btrfs balance start -musage=50 /path
Done, had to relocate 4 out of 89 chunks
$ btrfs filesystem df /path
Data, single: total=68.03GiB, used=64.43GiB
System, RAID1: total=32.00MiB, used=20.00KiB
Metadata, RAID1: total=14.87GiB, used=8.85GiB
GlobalReserve, single: total=512.00MiB, used=0.00B</pre>
</dl>
<p> Just 1 GiB decrease, which possibly means there are block groups with good utilization. Making the metadata layout more compact would in turn require updating more metadata structures, ie. lots of IO. As running out of metadata space is a more severe problem, it&#8217;s not necessary to keep the utilization ratio too high. For the purpose of this example, let&#8217;s see the effects of further compaction: </p>
<dl>
<dd>
<pre># btrfs balance start -musage=70 /path
Done, had to relocate 13 out of 88 chunks
$ btrfs filesystem df .
Data, single: total=68.03GiB, used=64.43GiB
System, RAID1: total=32.00MiB, used=20.00KiB
Metadata, RAID1: total=11.97GiB, used=8.83GiB
GlobalReserve, single: total=512.00MiB, used=0.00B</pre>
</dl>
<h3>Getting Rid Of Completely Unused Block Groups</h3>
<p>Normally the balance operation needs a work space, to temporarily move the data before the old block groups gets removed. If there&#8217;s no work space, it ends with <i>no space left</i>. </p>
<p> There&#8217;s a special case when the block groups are completely unused, possibly left after removing lots of files or deleting snapshots. Removing empty block groups is automatic since 3.18. The same can be achieved manually with a notable exception that this operation does not require the work space. Thus it can be used to reclaim unused block groups to make it available. </p>
<dl>
<dd>
<pre># btrfs balance start -dusage=0 /path</pre>
</dl>
<p> This should lead to decrease in the <i>total</i> numbers in the <code>btrfs filesystem df</code> output.</p>
<h2>Exit Status</h2>
<p>Unless indicated otherwise below, all <code>btrfs balance</code> subcommands return a zero exit status if they succeed, and non zero in case of failure. </p>
<p> The <code>pause</code>, <code>cancel</code>, and <code>resume</code> subcommands exit with a status of <code>2</code> if they fail because a balance operation was not running. </p>
<p> The <code>status</code> subcommand exits with a status of <code>0</code> if a balance operation is not running, <code>1</code> if the command-line usage is incorrect or a balance operation is still running, and <code>2</code> on other errors.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-device/">btrfs-device</a></code>(8) </p>
