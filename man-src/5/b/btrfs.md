---
title: "btrfs(5)"
name: "btrfs"
section: "5"
letter: "b"
url: "/docs/linux/man/5-btrfs/"
description: "btrfs-man5 – topics about the BTRFS filesystem (mount options, supported file attributes and other)"
---

<p>btrfs-man5 &#8211; topics about the BTRFS filesystem (mount options, supported file attributes and other)</p>
<h2>Description</h2>
<p>This document describes topics related to BTRFS that are not specific to the tools. Currently covers:</p>
<dl>
<dd>1. mount options</dl>
<dl>
<dd>2. filesystem features</dl>
<dl>
<dd>3. checksum algorithms</dl>
<dl>
<dd>4. filesystem limits</dl>
<dl>
<dd>5. bootloader support</dl>
<dl>
<dd>6. file attributes</dl>
<dl>
<dd>7. control device</dl>
<h2>Mount Options</h2>
<p>This section describes mount options specific to BTRFS. For the generic mount options please refer to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) manpage. The options are sorted alphabetically (discarding the <i>no</i> prefix). </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> most mount options apply to the whole filesystem and only options in the first mounted subvolume will take effect. This is due to lack of implementation and may change in the future. This means that (for example) you can&#8217;t set per-subvolume <i>nodatacow</i>, <i>nodatasum</i>, or <i>compress</i> using mount options. This should eventually be fixed, but it has proved to be difficult to implement correctly within the Linux VFS framework. </p>
</dl>
<p> <code>acl</code>, <code>noacl</code></p>
<dl>
<dd>(default: on) </p>
<p> Enable/disable support for Posix Access Control Lists (ACLs). See the <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) manual page for more information about ACLs. </p>
<p> The support for ACL is build-time configurable (BTRFS_FS_POSIX_ACL) and mount fails if <i>acl</i> is requested but the feature is not compiled in. </p>
</dl>
<p> <code>autodefrag</code>, <code>noautodefrag</code></p>
<dl>
<dd>(since: 3.0, default: off) </p>
<p> Enable automatic file defragmentation. When enabled, small random writes into files (in a range of tens of kilobytes, currently it&#8217;s 64K) are detected and queued up for the defragmentation process. Not well suited for large database workloads. </p>
<p> The read latency may increase due to reading the adjacent blocks that make up the range for defragmentation, successive write will merge the blocks in the new location. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> Defragmenting with Linux kernel versions &lt; 3.9 or &ge; 3.14-rc2 as well as with Linux stable kernel versions &ge; 3.10.31, &ge; 3.12.12 or &ge; 3.13.4 will break up the reflinks of COW data (for example files copied with <code>cp &#8211;reflink</code>, snapshots or de-duplicated data). This may cause considerable increase of space usage depending on the broken up reflinks. </p>
</dl>
</dl>
<p> <code>barrier</code>, <code>nobarrier</code></p>
<dl>
<dd>(default: on) </p>
<p> Ensure that all IO write operations make it through the device cache and are stored permanently when the filesystem is at its consistency checkpoint. This typically means that a flush command is sent to the device that will synchronize all pending data and ordinary metadata blocks, then writes the superblock and issues another flush. </p>
<p> The write flushes incur a slight hit and also prevent the IO block scheduler to reorder requests in a more effective way. Disabling barriers gets rid of that penalty but will most certainly lead to a corrupted filesystem in case of a crash or power loss. The ordinary metadata blocks could be yet unwritten at the time the new superblock is stored permanently, expecting that the block pointers to metadata were stored permanently before. </p>
<p> On a device with a volatile battery-backed write-back cache, the <i>nobarrier</i> option will not lead to filesystem corruption as the pending blocks are supposed to make it to the permanent storage. </p>
</dl>
<p> <code>check_int</code>, <code>check_int_data</code>, <code>check_int_print_mask=</code><i>value</i></p>
<dl>
<dd>(since: 3.0, default: off) </p>
<p> These debugging options control the behavior of the integrity checking module (the BTRFS_FS_CHECK_INTEGRITY config option required). The main goal is to verify that all blocks from a given transaction period are properly linked. </p>
<p> <i>check_int</i> enables the integrity checker module, which examines all block write requests to ensure on-disk consistency, at a large memory and CPU cost. </p>
<p> <i>check_int_data</i> includes extent data in the integrity checks, and implies the <i>check_int</i> option. </p>
<p> <i>check_int_print_mask</i> takes a bitmask of BTRFSIC_PRINT_MASK_* values as defined in <i>fs/btrfs/check-integrity.c</i>, to control the integrity checker module behavior. </p>
<p> See comments at the top of <i>fs/btrfs/check-integrity.c</i> for more information. </p>
</dl>
<p> <code>clear_cache</code></p>
<dl>
<dd>Force clearing and rebuilding of the disk space cache if something has gone wrong. See also: <i>space_cache</i>. </p>
</dl>
<p> <code>commit=</code><i>seconds</i></p>
<dl>
<dd>(since: 3.12, default: 30) </p>
<p> Set the interval of periodic transaction commit when data are synchronized to permanent storage. Higher interval values lead to larger amount of unwritten data, which has obvious consequences when the system crashes. The upper bound is not forced, but a warning is printed if it&#8217;s more than 300 seconds (5 minutes). Use with care. </p>
</dl>
<p> <code>compress</code>, <code>compress=</code><i>type[:level]</i>, <code>compress-force</code>, <code>compress-force=</code><i>type[:level]</i></p>
<dl>
<dd>(default: off, level support since: 5.1) </p>
<p> Control BTRFS file data compression. Type may be specified as <i>zlib</i>, <i>lzo</i>, <i>zstd</i> or <i>no</i> (for no compression, used for remounting). If no type is specified, <i>zlib</i> is used. If <i>compress-force</i> is specified, then compression will always be attempted, but the data may end up uncompressed if the compression would make them larger. </p>
<p> Both <i>zlib</i> and <i>zstd</i> (since version 5.1) expose the compression level as a tunable knob with higher levels trading speed and memory (<i>zstd</i>) for higher compression ratios. This can be set by appending a colon and the desired level. Zlib accepts the range [1, 9] and zstd accepts [1, 15]. If no level is set, both currently use a default level of 3. The value 0 is an alias for the defaul level. </p>
<p> Otherwise some simple heuristics are applied to detect an incompressible file. If the first blocks written to a file are not compressible, the whole file is permanently marked to skip compression. As this is too simple, the <i>compress-force</i> is a workaround that will compress most of the files at the cost of some wasted CPU cycles on failed attempts. Since kernel 4.15, a set of heuristic algorithms have been improved by using frequency sampling, repeated pattern detection and Shannon entropy calculation to avoid that. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If compression is enabled, <i>nodatacow</i> and <i>nodatasum</i> are disabled. </p>
</dl>
</dl>
<p> <code>datacow</code>, <code>nodatacow</code></p>
<dl>
<dd>(default: on) </p>
<p> Enable data copy-on-write for newly created files. <i>Nodatacow</i> implies <i>nodatasum</i>, and disables <i>compression</i>. All files created under <i>nodatacow</i> are also set the NOCOW file attribute (see <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1)). </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If <i>nodatacow</i> or <i>nodatasum</i> are enabled, compression is disabled. </p>
</dl>
<p> Updates in-place improve performance for workloads that do frequent overwrites, at the cost of potential partial writes, in case the write is interrupted (system crash, device failure). </p>
</dl>
<p> <code>datasum</code>, <code>nodatasum</code></p>
<dl>
<dd>(default: on) </p>
<p> Enable data checksumming for newly created files. <i>Datasum</i> implies <i>datacow</i>, ie. the normal mode of operation. All files created under <i>nodatasum</i> inherit the &quot;no checksums&quot; property, however there&#8217;s no corresponding file attribute (see <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1)). </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If <i>nodatacow</i> or <i>nodatasum</i> are enabled, compression is disabled. </p>
</dl>
<p> There is a slight performance gain when checksums are turned off, the corresponding metadata blocks holding the checksums do not need to updated. The cost of checksumming of the blocks in memory is much lower than the IO, modern CPUs feature hardware support of the checksumming algorithm. </p>
</dl>
<p> <code>degraded</code></p>
<dl>
<dd>(default: off) </p>
<p> Allow mounts with less devices than the RAID profile constraints require. A read-write mount (or remount) may fail when there are too many devices missing, for example if a stripe member is completely missing from RAID0. </p>
<p> Since 4.14, the constraint checks have been improved and are verified on the chunk level, not an the device level. This allows degraded mounts of filesystems with mixed RAID profiles for data and metadata, even if the device number constraints would not be satisfied for some of the profiles. </p>
<p> Example: metadata &#8212; raid1, data &#8212; single, devices &#8212; /dev/sda, /dev/sdb </p>
<p> Suppose the data are completely stored on <i>sda</i>, then missing <i>sdb</i> will not prevent the mount, even if 1 missing device would normally prevent (any) <i>single</i> profile to mount. In case some of the data chunks are stored on <i>sdb</i>, then the constraint of single/data is not satisfied and the filesystem cannot be mounted. </p>
</dl>
<p> <code>device=</code><i>devicepath</i></p>
<dl>
<dd>Specify a path to a device that will be scanned for BTRFS filesystem during mount. This is usually done automatically by a device manager (like udev) or using the <code>btrfs device scan</code> command (eg. run from the initial ramdisk). In cases where this is not possible the <i>device</i> mount option can help. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> booting eg. a RAID1 system may fail even if all filesystem&#8217;s <i>device</i> paths are provided as the actual device nodes may not be discovered by the system at that point. </p>
</dl>
</dl>
<p> <code>discard</code>, <code>nodiscard</code></p>
<dl>
<dd>(default: off) </p>
<p> Enable discarding of freed file blocks. This is useful for SSD devices, thinly provisioned LUNs, or virtual machine images; however, every storage layer must support discard for it to work. if the backing device does not support asynchronous queued TRIM, then this operation can severely degrade performance, because a synchronous TRIM operation will be attempted instead. Queued TRIM requires newer than SATA revision 3.1 chipsets and devices. </p>
<p> If it is not necessary to immediately discard freed blocks, then the <code>fstrim</code> tool can be used to discard all free blocks in a batch. Scheduling a TRIM during a period of low system activity will prevent latent interference with the performance of other operations. Also, a device may ignore the TRIM command if the range is too small, so running a batch discard has a greater probability of actually discarding the blocks. </p>
</dl>
<p> <code>enospc_debug</code>, <code>noenospc_debug</code></p>
<dl>
<dd>(default: off) </p>
<p> Enable verbose output for some ENOSPC conditions. It&#8217;s safe to use but can be noisy if the system reaches near-full state. </p>
</dl>
<p> <code>fatal_errors=</code><i>action</i></p>
<dl>
<dd>(since: 3.4, default: bug) </p>
<p> Action to take when encountering a fatal error. </p>
<p> <code>bug</code></p>
<dl>
<dd><i>BUG()</i> on a fatal error, the system will stay in the crashed state and may be still partially usable, but reboot is required for full operation </p>
</dl>
<p> <code>panic</code></p>
<dl>
<dd><i>panic()</i> on a fatal error, depending on other system configuration, this may be followed by a reboot. Please refer to the documentation of kernel boot parameters, eg. <i>panic</i>, <i>oops</i> or <i>crashkernel</i>. </p>
</dl>
</dl>
<p> <code>flushoncommit</code>, <code>noflushoncommit</code></p>
<dl>
<dd>(default: off) </p>
<p> This option forces any data dirtied by a write in a prior transaction to commit as part of the current commit, effectively a full filesystem sync. </p>
<p> This makes the committed state a fully consistent view of the file system from the application&#8217;s perspective (i.e. it includes all completed file system operations). This was previously the behavior only when a snapshot was created. </p>
<p> When off, the filesystem is consistent but buffered writes may last more than one transaction commit. </p>
</dl>
<p> <code>fragment=</code><i>type</i></p>
<dl>
<dd>(depends on compile-time option BTRFS_DEBUG, since: 4.4, default: off) </p>
<p> A debugging helper to intentionally fragment given <i>type</i> of block groups. The type can be <i>data</i>, <i>metadata</i> or <i>all</i>. This mount option should not be used outside of debugging environments and is not recognized if the kernel config option <i>BTRFS_DEBUG</i> is not enabled. </p>
</dl>
<p> <code>inode_cache</code>, <code>noinode_cache</code></p>
<dl>
<dd>(since: 3.0, default: off) </p>
<p> Enable free inode number caching. Not recommended to use unless files on your filesystem get assigned inode numbers that are approaching 264. Normally, new files in each subvolume get assigned incrementally (plus one from the last time) and are not reused. The mount option turns on caching of the existing inode numbers and reuse of inode numbers of deleted files. </p>
<p> This option may slow down your system at first run, or after mounting without the option. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Defaults to off due to a potential overflow problem when the free space checksums don&#8217;t fit inside a single page. </p>
</dl>
<p> Don&#8217;t use this option unless you really need it. The inode number limit on 64bit system is 264, which is practically enough for the whole filesystem lifetime. Due to implementation of linux VFS layer, the inode numbers on 32bit systems are only 32 bits wide. This lowers the limit significantly and makes it possible to reach it. In such case, this mount option will help. Alternatively, files with high inode numbers can be copied to a new subvolume which will effectively start the inode numbers from the beginning again. </p>
</dl>
<p> <code>logreplay</code>, <code>nologreplay</code></p>
<dl>
<dd>(default: on, even read-only) </p>
<p> Enable/disable log replay at mount time. See also <i>treelog</i>. Note that <i>nologreplay</i> is the same as <i>norecovery</i>. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> currently, the tree log is replayed even with a read-only mount! To disable that behaviour, mount also with <i>nologreplay</i>. </p>
</dl>
</dl>
<p> <code>max_inline=</code><i>bytes</i></p>
<dl>
<dd>(default: min(2048, page size) ) </p>
<p> Specify the maximum amount of space, that can be inlined in a metadata B-tree leaf. The value is specified in bytes, optionally with a K suffix (case insensitive). In practice, this value is limited by the filesystem block size (named <i>sectorsize</i> at mkfs time), and memory page size of the system. In case of sectorsize limit, there&#8217;s some space unavailable due to leaf headers. For example, a 4k sectorsize, maximum size of inline data is about 3900 bytes. </p>
<p> Inlining can be completely turned off by specifying 0. This will increase data block slack if file sizes are much smaller than block size but will reduce metadata consumption in return. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> the default value has changed to 2048 in kernel 4.6. </p>
</dl>
</dl>
<p> <code>metadata_ratio=</code><i>value</i></p>
<dl>
<dd>(default: 0, internal logic) </p>
<p> Specifies that 1 metadata chunk should be allocated after every <i>value</i> data chunks. Default behaviour depends on internal logic, some percent of unused metadata space is attempted to be maintained but is not always possible if there&#8217;s not enough space left for chunk allocation. The option could be useful to override the internal logic in favor of the metadata allocation if the expected workload is supposed to be metadata intense (snapshots, reflinks, xattrs, inlined files). </p>
</dl>
<p> <code>norecovery</code></p>
<dl>
<dd>(since: 4.5, default: off) </p>
<p> Do not attempt any data recovery at mount time. This will disable <i>logreplay</i> and avoids other write operations. Note that this option is the same as <i>nologreplay</i>. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The opposite option <i>recovery</i> used to have different meaning but was changed for consistency with other filesystems, where <i>norecovery</i> is used for skipping log replay. BTRFS does the same and in general will try to avoid any write operations. </p>
</dl>
</dl>
<p> <code>rescan_uuid_tree</code></p>
<dl>
<dd>(since: 3.12, default: off) </p>
<p> Force check and rebuild procedure of the UUID tree. This should not normally be needed. </p>
</dl>
<p> <code>skip_balance</code></p>
<dl>
<dd>(since: 3.3, default: off) </p>
<p> Skip automatic resume of an interrupted balance operation. The operation can later be resumed with <code>btrfs balance resume</code>, or the paused state can be removed with <code>btrfs balance cancel</code>. The default behaviour is to resume an interrupted balance immediately after a volume is mounted. </p>
</dl>
<p> <code>space_cache</code>, <code>space_cache=</code><i>version</i>, <code>nospace_cache</code></p>
<dl>
<dd>(<i>nospace_cache</i> since: 3.2, <i>space_cache=v1</i> and <i>space_cache=v2</i> since 4.5, default: <i>space_cache=v1</i>) </p>
<p> Options to control the free space cache. The free space cache greatly improves performance when reading block group free space into memory. However, managing the space cache consumes some resources, including a small amount of disk space. </p>
<p> There are two implementations of the free space cache. The original one, referred to as <i>v1</i>, is the safe default. The <i>v1</i> space cache can be disabled at mount time with <i>nospace_cache</i> without clearing. </p>
<p> On very large filesystems (many terabytes) and certain workloads, the performance of the <i>v1</i> space cache may degrade drastically. The <i>v2</i> implementation, which adds a new B-tree called the free space tree, addresses this issue. Once enabled, the <i>v2</i> space cache will always be used and cannot be disabled unless it is cleared. Use <i>clear_cache,space_cache=v1</i> or <i>clear_cache,nospace_cache</i> to do so. If <i>v2</i> is enabled, kernels without <i>v2</i> support will only be able to mount the filesystem in read-only mode. The <code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8) command currently only has read-only support for <i>v2</i>. A read-write command may be run on a <i>v2</i> filesystem by clearing the cache, running the command, and then remounting with <i>space_cache=v2</i>. </p>
<p> If a version is not explicitly specified, the default implementation will be chosen, which is <i>v1</i>. </p>
</dl>
<p> <code>ssd</code>, <code>ssd_spread</code>, <code>nossd</code>, <code>nossd_spread</code></p>
<dl>
<dd>(default: SSD autodetected) </p>
<p> Options to control SSD allocation schemes. By default, BTRFS will enable or disable SSD optimizations depending on status of a device with respect to rotational or non-rotational type. This is determined by the contents of <i>/sys/block/DEV/queue/rotational</i>). If it is 0, the <i>ssd</i> option is turned on. The option <i>nossd</i> will disable the autodetection. </p>
<p> The optimizations make use of the absence of the seek penalty that&#8217;s inherent for the rotational devices. The blocks can be typically written faster and are not offloaded to separate threads. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Since 4.14, the block layout optimizations have been dropped. This used to help with first generations of SSD devices. Their FTL (flash translation layer) was not effective and the optimization was supposed to improve the wear by better aligning blocks. This is no longer true with modern SSD devices and the optimization had no real benefit. Furthermore it caused increased fragmentation. The layout tuning has been kept intact for the option <i>ssd_spread</i>. </p>
</dl>
<p> The <i>ssd_spread</i> mount option attempts to allocate into bigger and aligned chunks of unused space, and may perform better on low-end SSDs. <i>ssd_spread</i> implies <i>ssd</i>, enabling all other SSD heuristics as well. The option <i>nossd</i> will disable all SSD options while <i>nossd_spread</i> only disables <i>ssd_spread</i>. </p>
</dl>
<p> <code>subvol=</code><i>path</i></p>
<dl>
<dd>Mount subvolume from <i>path</i> rather than the toplevel subvolume. The <i>path</i> is always treated as relative to the toplevel subvolume. This mount option overrides the default subvolume set for the given filesystem. </p>
</dl>
<p> <code>subvolid=</code><i>subvolid</i></p>
<dl>
<dd>Mount subvolume specified by a <i>subvolid</i> number rather than the toplevel subvolume. You can use <code>btrfs subvolume list</code> of <code>btrfs subvolume show</code> to see subvolume ID numbers. This mount option overrides the default subvolume set for the given filesystem. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> if both <i>subvolid</i> and <i>subvol</i> are specified, they must point at the same subvolume, otherwise the mount will fail. </p>
</dl>
</dl>
<p> <code>thread_pool=</code><i>number</i></p>
<dl>
<dd>(default: min(NRCPUS + 2, 8) ) </p>
<p> The number of worker threads to start. NRCPUS is number of on-line CPUs detected at the time of mount. Small number leads to less parallelism in processing data and metadata, higher numbers could lead to a performance hit due to increased locking contention, process scheduling, cache-line bouncing or costly data transfers between local CPU memories. </p>
</dl>
<p> <code>treelog</code>, <code>notreelog</code></p>
<dl>
<dd>(default: on) </p>
<p> Enable the tree logging used for <i>fsync</i> and <i>O_SYNC</i> writes. The tree log stores changes without the need of a full filesystem sync. The log operations are flushed at sync and transaction commit. If the system crashes between two such syncs, the pending tree log operations are replayed during mount. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> currently, the tree log is replayed even with a read-only mount! To disable that behaviour, also mount with <i>nologreplay</i>. </p>
</dl>
<p> The tree log could contain new files/directories, these would not exist on a mounted filesystem if the log is not replayed. </p>
</dl>
<p> <code>usebackuproot</code>, <code>nousebackuproot</code></p>
<dl>
<dd>(since: 4.6, default: off) </p>
<p> Enable autorecovery attempts if a bad tree root is found at mount time. Currently this scans a backup list of several previous tree roots and tries to use the first readable. This can be used with read-only mounts as well. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> This option has replaced <i>recovery</i>. </p>
</dl>
</dl>
<p> <code>user_subvol_rm_allowed</code></p>
<dl>
<dd>(default: off) </p>
<p> Allow subvolumes to be deleted by their respective owner. Otherwise, only the root user can do that. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> historically, any user could create a snapshot even if he was not owner of the source subvolume, the subvolume deletion has been restricted for that reason. The subvolume creation has been restricted but this mount option is still required. This is a usability issue. Since 4.18, the <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) syscall can delete an empty subvolume just like an ordinary directory. Whether this is possible can be detected at runtime, see <i>rmdir_subvol</i> feature in <i>FILESYSTEM FEATURES</i>. </p>
</dl>
</dl>
<h3>Deprecated Mount Options</h3>
<p>List of mount options that have been removed, kept for backward compatibility. </p>
<p> <code>alloc_start=</code><i>bytes</i></p>
<dl>
<dd>(default: 1M, minimum: 1M, deprecated since: 4.13) </p>
<p> Debugging option to force all block allocations above a certain byte threshold on each block device. The value is specified in bytes, optionally with a K, M, or G suffix (case insensitive). </p>
</dl>
<p> <code>recovery</code></p>
<dl>
<dd>(since: 3.2, default: off, deprecated since: 4.5) </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> this option has been replaced by <i>usebackuproot</i> and should not be used but will work on 4.5+ kernels. </p>
</dl>
</dl>
<p> <code>subvolrootid=</code><i>objectid</i></p>
<dl>
<dd>(irrelevant since: 3.2, formally deprecated since: 3.10) </p>
<p> A workaround option from times (pre 3.2) when it was not possible to mount a subvolume that did not reside directly under the toplevel subvolume. </p>
</dl>
<h3>Notes On Generic Mount Options</h3>
<p>Some of the general mount options from <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) that affect BTRFS and are worth mentioning. </p>
<p> <code>noatime</code></p>
<dl>
<dd>under read intensive work-loads, specifying <i>noatime</i> significantly improves performance because no new access time information needs to be written. Without this option, the default is <i>relatime</i>, which only reduces the number of inode atime updates in comparison to the traditional <i>strictatime</i>. The worst case for atime updates under <i>relatime</i> occurs when many files are read whose atime is older than 24 h and which are freshly snapshotted. In that case the atime is updated <i>and</i> COW happens &#8211; for each file &#8211; in bulk. See also m[blue]<code><a rel="nofollow" href="https://lwn.net/Articles/499293/">https://lwn.net/Articles/499293/</a></code>m[] &#8211; <i>Atime and btrfs: a bad combination? (LWN, 2012-05-31)</i>. </p>
<p> Note that <i>noatime</i> may break applications that rely on atime uptimes like the venerable Mutt (unless you use maildir mailboxes). </p>
</dl>
<h2>Filesystem Features</h2>
<p>The basic set of filesystem features gets extended over time. The backward compatibility is maintained and the features are optional, need to be explicitly asked for so accidental use will not create incompatibilities. </p>
<p> There are several classes and the respective tools to manage the features: </p>
<p> at mkfs time only</p>
<dl>
<dd>This is namely for core structures, like the b-tree nodesize or checksum algorithm, see <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) for more details. </p>
</dl>
<p> after mkfs, on an unmounted filesystem</p>
<dl>
<dd>Features that may optimize internal structures or add new structures to support new functionality, see <code><a href="/docs/linux/man/8-btrfstune/">btrfstune</a></code>(8). The command <code>btrfs inspect-internal dump-super device</code> will dump a superblock, you can map the value of <i>incompat_flags</i> to the features listed below </p>
</dl>
<p> after mkfs, on a mounted filesystem</p>
<dl>
<dd>The features of a filesystem (with a given UUID) are listed in <code>/sys/fs/btrfs/UUID/features/</code>, one file per feature. The status is stored inside the file. The value <i>1</i> is for enabled and active, while <i>0</i> means the feature was enabled at mount time but turned off afterwards. </p>
<p> Whether a particular feature can be turned on a mounted filesystem can be found in the directory <code>/sys/fs/btrfs/features/</code>, one file per feature. The value <i>1</i> means the feature can be enabled. </p>
</dl>
<p> List of features (see also <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) section <i>FILESYSTEM FEATURES</i>): </p>
<p> <code>big_metadata</code></p>
<dl>
<dd>(since: 3.4) </p>
<p> the filesystem uses <i>nodesize</i> for metadata blocks, this can be bigger than the page size </p>
</dl>
<p> <code>compress_lzo</code></p>
<dl>
<dd>(since: 2.6.38) </p>
<p> the <i>lzo</i> compression has been used on the filesystem, either as a mount option or via <code>btrfs filesystem defrag</code>. </p>
</dl>
<p> <code>compress_zstd</code></p>
<dl>
<dd>(since: 4.14) </p>
<p> the <i>zstd</i> compression has been used on the filesystem, either as a mount option or via <code>btrfs filesystem defrag</code>. </p>
</dl>
<p> <code>default_subvol</code></p>
<dl>
<dd>(since: 2.6.34) </p>
<p> the default subvolume has been set on the filesystem </p>
</dl>
<p> <code>extended_iref</code></p>
<dl>
<dd>(since: 3.7) </p>
<p> increased hardlink limit per file in a directory to 65536, older kernels supported a varying number of hardlinks depending on the sum of all file name sizes that can be stored into one metadata block </p>
</dl>
<p> <code>metadata_uuid</code></p>
<dl>
<dd>(since: 5.0) </p>
<p> the main filesystem UUID is the metadata_uuid, which stores the new UUID only in the superblock while all metadata blocks still have the UUID set at mkfs time, see <code><a href="/docs/linux/man/8-btrfstune/">btrfstune</a></code>(8) for more </p>
</dl>
<p> <code>mixed_backref</code></p>
<dl>
<dd>(since: 2.6.31) </p>
<p> the last major disk format change, improved backreferences, now default </p>
</dl>
<p> <code>mixed_groups</code></p>
<dl>
<dd>(since: 2.6.37) </p>
<p> mixed data and metadata block groups, ie. the data and metadata are not separated and occupy the same block groups, this mode is suitable for small volumes as there are no constraints how the remaining space should be used (compared to the split mode, where empty metadata space cannot be used for data and vice versa) </p>
<p> on the other hand, the final layout is quite unpredictable and possibly highly fragmented, which means worse performance </p>
</dl>
<p> <code>no_holes</code></p>
<dl>
<dd>(since: 3.14) </p>
<p> improved representation of file extents where holes are not explicitly stored as an extent, saves a few percent of metadata if sparse files are used </p>
</dl>
<p> <code>raid56</code></p>
<dl>
<dd>(since: 3.9) </p>
<p> the filesystem contains or contained a raid56 profile of block groups </p>
</dl>
<p> <code>rmdir_subvol</code></p>
<dl>
<dd>(since: 4.18) </p>
<p> indicate that <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) syscall can delete an empty subvolume just like an ordinary directory. Note that this feature only depends on the kernel version. </p>
</dl>
<p> <code>skinny_metadata</code></p>
<dl>
<dd>(since: 3.10) </p>
<p> reduced-size metadata for extent references, saves a few percent of metadata </p>
</dl>
<h3>Swapfile Support</h3>
<p>The swapfile is supported since kernel 5.0. Use <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) to activate the swapfile. There are some limitations of the implementation in btrfs and linux swap subystem: </p>
<dl>
<dd>&bull; </p>
<p> filesystem &#8211; must be only single device</dl>
<dl>
<dd>&bull; </p>
<p> swapfile &#8211; the containing subvolume cannot be snapshotted</dl>
<dl>
<dd>&bull; </p>
<p> swapfile &#8211; must be preallocated</dl>
<dl>
<dd>&bull; </p>
<p> swapfile &#8211; must be nodatacow (ie. also nodatasum)</dl>
<dl>
<dd>&bull; </p>
<p> swapfile &#8211; must not be compressed</dl>
<p> The limitations come namely from the COW-based design and mapping layer of blocks that allows the advanced features like relocation and multi-device filesystems. However, the swap subsystem expects simpler mapping and no background changes of the file blocks once they&#8217;ve been attached to swap. </p>
<p> With active swapfiles, the following whole-filesystem operations will skip swapfile extents or may fail: </p>
<dl>
<dd>&bull; </p>
<p> balance &#8211; block groups with swapfile extents are skipped and reported, the rest will be processed normally</dl>
<dl>
<dd>&bull; </p>
<p> resize grow &#8211; unaffected</dl>
<dl>
<dd>&bull; </p>
<p> resize shrink &#8211; works as long as the extents are outside of the shrunk range</dl>
<dl>
<dd>&bull; </p>
<p> device add &#8211; a new device does not interfere with existing swapfile and this operation will work, though no new swapfile can be activated afterwards</dl>
<dl>
<dd>&bull; </p>
<p> device delete &#8211; if the device has been added as above, it can be also deleted</dl>
<dl>
<dd>&bull; </p>
<p> device replace &#8211; ditto</dl>
<p> When there are no active swapfiles and a whole-filesystem exclusive operation is running (ie. balance, device delete, shrink), the swapfiles cannot be temporarily activated. The operation must finish first. </p>
<dl>
<dd>
<pre># truncate -s 0 swapfile
# chattr +C swapfile
# fallocate -l 2G swapfile
# chmod 0600 swapfile
# mkswap swapfile
# swapon swapfile</pre>
</dl>
<h2>Checksum Algorithms</h2>
<p>There are several checksum algorithms supported. The default and backward compatible is <i>crc32c</i>. Since kernel 5.5 there are three more with different characteristics and trade-offs regarding speed and strength. The following list may help you to decide which one to select. </p>
<p> <code>CRC32C</code> (32bit digest)</p>
<dl>
<dd>default, best backward compatibility, very fast, modern CPUs have instruction-level support, not collision-resistant but still good error detection capabilities </p>
</dl>
<p> <code>XXHASH</code> (64bit digest)</p>
<dl>
<dd>can be used as CRC32C successor, very fast, optimized for modern CPUs utilizing instruction pipelining, good collision resistance and error detection </p>
</dl>
<p> <code>SHA256</code> (256bit digest)</p>
<dl>
<dd>a cryptographic-strength hash, relatively slow but with possible CPU instruction acceleration or specialized hardware cards, FIPS certified and in wide use </p>
</dl>
<p> <code>BLAKE2b</code> (256bit digest)</p>
<dl>
<dd>a cryptographic-strength hash, relatively fast with possible CPU acceleration using SIMD extensions, not standardized but based on BLAKE which was a SHA3 finalist, in wide use, the algorithm used is BLAKE2b-256 that&#8217;s optimized for 64bit platforms </p>
</dl>
<p> The <i>digest size</i> affects overall size of data block checksums stored in the filesystem. The metadata blocks have a fixed area up to 256bits (32 bytes), so there&#8217;s no increase. Each data block has a separate checksum stored, with additional overhead of the b-tree leaves. </p>
<p> Approximate relative performance of the algorithms, measured against CRC32C using reference software implementations on a 3.5GHz intel CPU: </p>
<p> [ cols=&quot;^,&gt;,&gt;&quot;,width=&quot;50%&quot; ] </p>
<table BORDER>
<tr VALIGN=top>
<td>
<p> <code>Digest</code> </td>
<td>
<p> <code>Cycles/4KiB</code> </td>
<td>
<p> <code>Ratio</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> CRC32C </td>
<td>
<p> 1700 </td>
<td>
<p> 1.00
</td>
</tr>
<tr VALIGN=top>
<td>
<p> XXHASH </td>
<td>
<p> 2500 </td>
<td>
<p> 1.44
</td>
</tr>
<tr VALIGN=top>
<td>
<p> SHA256 </td>
<td>
<p> 105000 </td>
<td>
<p> 61
</td>
</tr>
<tr VALIGN=top>
<td>
<p> BLAKE2b </td>
<td>
<p> 22000 </td>
<td>
<p> 13
</td>
</tr>
</table>
<h2>Filesystem Limits</h2>
<p>maximum file name length</p>
<dl>
<dd>255 </p>
</dl>
<p> maximum symlink target length</p>
<dl>
<dd>depends on the <i>nodesize</i> value, for 4k it&#8217;s 3949 bytes, for larger nodesize it&#8217;s 4095 due to the system limit PATH_MAX </p>
<p> The symlink target may not be a valid path, ie. the path name components can exceed the limits (NAME_MAX), there&#8217;s no content validation at <code><a href="/docs/linux/man/3-symlink/">symlink</a></code>(3) creation. </p>
</dl>
<p> maximum number of inodes</p>
<dl>
<dd>264 but depends on the available metadata space as the inodes are created dynamically </p>
</dl>
<p> inode numbers</p>
<dl>
<dd>minimum number: 256 (for subvolumes), regular files and directories: 257 </p>
</dl>
<p> maximum file length</p>
<dl>
<dd>inherent limit of btrfs is 264 (16 EiB) but the linux VFS limit is 263 (8 EiB) </p>
</dl>
<p> maximum number of subvolumes</p>
<dl>
<dd>the subvolume ids can go up to 264 but the number of actual subvolumes depends on the available metadata space, the space consumed by all subvolume metadata includes bookkeeping of shared extents can be large (MiB, GiB) </p>
</dl>
<p> maximum number of hardlinks of a file in a directory</p>
<dl>
<dd>65536 when the <code>extref</code> feature is turned on during mkfs (default), roughly 100 otherwise </p>
</dl>
<h2>Bootloader Support</h2>
<p>GRUB2 (m[blue]<code><a rel="nofollow" href="https://www.gnu.org/software/grub">https://www.gnu.org/software/grub</a></code>m[]) has the most advanced support of booting from BTRFS with respect to features. </p>
<p> EXTLINUX (from the m[blue]<code><a rel="nofollow" href="https://syslinux.org">https://syslinux.org</a></code>m[] project) can boot but does not support all features. Please check the upstream documentation before you use it.</p>
<h2>File Attributes</h2>
<p>The btrfs filesystem supports setting the following file attributes using the <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) utility: </p>
<p> <code>a</code></p>
<dl>
<dd><i>append only</i>, new writes are always written at the end of the file </p>
</dl>
<p> <code>A</code></p>
<dl>
<dd><i>no atime updates</i> </p>
</dl>
<p> <code>c</code></p>
<dl>
<dd><i>compress data</i>, all data written after this attribute is set will be compressed. Please note that compression is also affected by the mount options or the parent directory attributes. </p>
<p> When set on a directory, all newly created files will inherit this attribute. </p>
</dl>
<p> <code>C</code></p>
<dl>
<dd><i>no copy-on-write</i>, file modifications are done in-place </p>
<p> When set on a directory, all newly created files will inherit this attribute. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> due to implementation limitations, this flag can be set/unset only on empty files. </p>
</dl>
</dl>
<p> <code>d</code></p>
<dl>
<dd><i>no dump</i>, makes sense with 3rd party tools like <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8), on BTRFS the attribute can be set/unset but no other special handling is done </p>
</dl>
<p> <code>D</code></p>
<dl>
<dd><i>synchronous directory updates</i>, for more details search <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for <i>O_SYNC</i> and <i>O_DSYNC</i> </p>
</dl>
<p> <code>i</code></p>
<dl>
<dd><i>immutable</i>, no file data and metadata changes allowed even to the root user as long as this attribute is set (obviously the exception is unsetting the attribute) </p>
</dl>
<p> <code>S</code></p>
<dl>
<dd><i>synchronous updates</i>, for more details search <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for <i>O_SYNC</i> and <i>O_DSYNC</i> </p>
</dl>
<p> <code>X</code></p>
<dl>
<dd><i>no compression</i>, permanently turn off compression on the given file. Any compression mount options will not affect this file. </p>
<p> When set on a directory, all newly created files will inherit this attribute. </p>
</dl>
<p> No other attributes are supported. For the complete list please refer to the <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) manual page.</p>
<h2>Control Device</h2>
<p>There&#8217;s a character special device <code>/dev/btrfs-control</code> with major and minor numbers 10 and 234 (the device can be found under the <i>misc</i> category). </p>
<dl>
<dd>
<pre>$ ls -l /dev/btrfs-control
crw------- 1 root root 10, 234 Jan 1 12:00 /dev/btrfs-control</pre>
</dl>
<p> The device accepts some ioctl calls that can perform following actions on the filesystem module: </p>
<dl>
<dd>&bull; </p>
<p> scan devices for btrfs filesystem (ie. to let multi-device filesystems mount automatically) and register them with the kernel module</dl>
<dl>
<dd>&bull; </p>
<p> similar to scan, but also wait until the device scanning process is finished for a given filesystem</dl>
<dl>
<dd>&bull; </p>
<p> get the supported features (can be also found under <i>/sys/fs/btrfs/features</i>)</dl>
<p> The device is usually created by a system device node manager (eg. udev), but can be created manually: </p>
<dl>
<dd>
<pre># mknod --mode=600 c 10 234 /dev/btrfs-control</pre>
</dl>
<p> The control device is not strictly required but the device scanning will not work and a workaround would need to be used to mount a multi-device filesystem. The mount option <i>device</i> can trigger the device scanning during mount.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-acl/">acl</a></code>(5), <code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8), <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), <code><a href="/docs/linux/man/8-fstrim/">fstrim</a></code>(8), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) </p>
