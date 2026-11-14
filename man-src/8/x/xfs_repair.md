---
title: "xfs_repair(8)"
name: "xfs_repair"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_repair/"
description: "xfs_repair – repair an XFS filesystem"
---

<p>xfs_repair &#8211; repair an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_repair</code> [ <code>-dfLnPv</code> ] [ <code>-m</code> <i>maxmem</i> ] [ <code>-c</code><i> subopt</i><code>=</code><i>value</i> ] [ <code>-o</code> <i>subopt</i>[<code>=</code><i>value</i>] ] [ <code>-t</code> <i>interval</i> ] [ <code>-l</code> <i>logdev</i> ] [ <code>-r</code> <i>rtdev</i> ] <i>device</i><br />
 <code>xfs_repair -V</code></p>
<h2>Description</h2>
<p><code>xfs_repair</code> repairs corrupt or damaged XFS filesystems (see <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5)). The filesystem is specified using the <i>device</i> argument which should be the device name of the disk partition or volume containing the filesystem. If given the name of a block device, <code>xfs_repair</code> will attempt to find the raw device associated with the specified block device and will use the raw device instead. </p>
<p> Regardless, the filesystem to be repaired must be unmounted, otherwise, the resulting filesystem may be inconsistent or corrupt.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Specifies that the filesystem image to be processed is stored in a regular file at <i>device</i> (see the <code>mkfs.xfs -d</code> <i>file</i> option). This might happen if an image copy of a filesystem has been copied or written into an ordinary file. This option implies that any external log or realtime section is also in an ordinary file.</p>
<dt><code>-L</code></p>
<dd>Force Log Zeroing. Forces <code>xfs_repair</code> to zero the log even if it is dirty (contains metadata changes). When using this option the filesystem will likely appear to be corrupt, and can cause the loss of user files and/or data.</p>
<dt><code>-l</code><i> logdev</i></p>
<dd>Specifies the device special file where the filesystem&#8217;s external log resides. Only for those filesystems which use an external log. See the <code>mkfs.xfs -l</code> option, and refer to <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5) for a detailed description of the XFS log.</p>
<dt><code>-r</code><i> rtdev</i></p>
<dd>Specifies the device special file where the filesystem&#8217;s realtime section resides. Only for those filesystems which use a realtime section. See the <code>mkfs.xfs -r</code> option, and refer to <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5) for a detailed description of the XFS realtime section.</p>
<dt><code>-n</code></p>
<dd>No modify mode. Specifies that <code>xfs_repair</code> should not modify the filesystem but should only scan the filesystem and indicate what repairs would have been made.</p>
<dt><code>-P</code></p>
<dd>Disable prefetching of inode and directory blocks. Use this option if you find <code>xfs_repair</code> gets stuck and stops proceeding. Interrupting a stuck <code>xfs_repair</code> is safe.</p>
<dt><code>-m</code><i> maxmem</i></p>
<dd>Specifies the approximate maximum amount of memory, in megabytes, to use for <code>xfs_repair</code>. <code>xfs_repair</code> has its own internal block cache which will scale out up to the lesser of the process&#8217;s virtual address limit or about 75% of the system&#8217;s physical RAM. This option overrides these limits.</p>
<dd><code>NOTE:</code> These memory limits are only approximate and may use more than the specified limit.</p>
<dt><code>-c</code><i> subopt</i><code>=</code><i>value</i></p>
<dd>Change filesystem parameters. Refer to <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8) for information on changing filesystem parameters.</p>
<dt> <code>-o</code> <i>subopt</i>[<code>=</code><i>value</i>]</p>
<dd>
<dd>Override what the program might conclude about the filesystem if left to its own devices.</p>
<dd>The <i>subopt</i>ions supported are:</p>
<dl>
<dd>
<dl>
<dt><code>bhash=</code><i>bhashsize</i></p>
<dd>overrides the default buffer cache hash size. The total number of buffer cache entries are limited to 8 times this amount. The default size is set to use up the remainder of 75% of the system&#8217;s physical RAM size.</p>
<dt><code>ag_stride=</code><i>ags_per_concat_unit</i></p>
<dd>This creates additional processing threads to parallel process AGs that span multiple concat units. This can significantly reduce repair times on concat based filesystems.</p>
<dt><code>force_geometry</code></p>
<dd>Check the filesystem even if geometry information could not be validated. Geometry information can not be validated if only a single allocation group exists and thus we do not have a backup superblock available, or if there are two allocation groups and the two superblocks do not agree on the filesystem geometry. Only use this option if you validated the geometry yourself and know what you are doing. If In doubt run in no modify mode first.</dl>
</dl>
<dt><code>-t interval</code></p>
<dd>Modify reporting interval, specified in seconds. During long runs <code>xfs_repair</code> outputs its progress every 15 minutes. Reporting is only activated when ag_stride is enabled.</p>
<dt><code>-v</code></p>
<dd>Verbose output. May be specified multiple times to increase verbosity.</p>
<dt><code>-d</code></p>
<dd>Repair dangerously. Allow <code>xfs_repair</code> to repair an XFS filesystem mounted read only. This is typically done on a root filesystem from single user mode, immediately followed by a reboot.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<h3>Checks Performed</h3>
<p>Inconsistencies corrected include the following:</p>
<dl>
<dt>1.</p>
<dd>Inode and inode blockmap (addressing) checks: bad magic number in inode, bad magic numbers in inode blockmap blocks, extents out of order, incorrect number of records in inode blockmap blocks, blocks claimed that are not in a legal data area of the filesystem, blocks that are claimed by more than one inode.</p>
<dt>2.</p>
<dd>Inode allocation map checks: bad magic number in inode map blocks, inode state as indicated by map (free or in-use) inconsistent with state indicated by the inode, inodes referenced by the filesystem that do not appear in the inode allocation map, inode allocation map referencing blocks that do not appear to contain inodes.</p>
<dt>3.</p>
<dd>Size checks: number of blocks claimed by inode inconsistent with inode size, directory size not block aligned, inode size not consistent with inode format.</p>
<dt>4.</p>
<dd>Directory checks: bad magic numbers in directory blocks, incorrect number of entries in a directory block, bad freespace information in a directory leaf block, entry pointing to an unallocated (free) or out of range inode, overlapping entries, missing or incorrect dot and dotdot entries, entries out of hashvalue order, incorrect internal directory pointers, directory type not consistent with inode format and size.</p>
<dt>5.</p>
<dd>Pathname checks: files or directories not referenced by a pathname starting from the filesystem root, illegal pathname components.</p>
<dt>6.</p>
<dd>Link count checks: link counts that do not agree with the number of directory references to the inode.</p>
<dt>7.</p>
<dd>Freemap checks: blocks claimed free by the freemap but also claimed by an inode, blocks unclaimed by any inode but not appearing in the freemap.</p>
<dt>8.</p>
<dd>Super Block checks: total free block and/or free i-node count incorrect, filesystem geometry inconsistent, secondary and primary superblocks contradictory.</dl>
<p> Orphaned files and directories (allocated, in-use but unreferenced) are reconnected by placing them in the <i>lost+found</i> directory. The name assigned is the inode number.</p>
<h3>Disk Errors</h3>
<p><code>xfs_repair</code> aborts on most disk I/O errors. Therefore, if you are trying to repair a filesystem that was damaged due to a disk drive failure, steps should be taken to ensure that all blocks in the filesystem are readable and writable before attempting to use <code>xfs_repair</code> to repair the filesystem. A possible method is using <code><a href="/docs/linux/man/8-dd/">dd</a></code>(8) to copy the data onto a good disk.</p>
<h3>lost+found</h3>
<p>The directory <i>lost+found</i> does not have to already exist in the filesystem being repaired. If the directory does not exist, it is automatically created if required. If it already exists, it will be checked for consistency and if valid will be used for additional orphaned files. Invalid <i>lost+found</i> directories are removed and recreated. Existing files in a valid <i>lost+found</i> are not removed or renamed.</p>
<h3>Corrupted Superblocks</h3>
<p>XFS has both primary and secondary superblocks. <code>xfs_repair</code> uses information in the primary superblock to automatically find and validate the primary superblock against the secondary superblocks before proceeding. Should the primary be too corrupted to be useful in locating the secondary superblocks, the program scans the filesystem until it finds and validates some secondary superblocks. At that point, it generates a primary superblock.</p>
<h3>Quotas</h3>
<p>If quotas are in use, it is possible that <code>xfs_repair</code> will clear some or all of the filesystem quota information. If so, the program issues a warning just before it terminates. If all quota information is lost, quotas are disabled and the program issues a warning to that effect. </p>
<p> Note that <code>xfs_repair</code> does not check the validity of quota limits. It is recommended that you check the quota limit information manually after <code>xfs_repair</code>. Also, space usage information is automatically regenerated the next time the filesystem is mounted with quotas turned on, so the next quota mount of the filesystem may take some time.</p>
<h2>Diagnostics</h2>
<p><code>xfs_repair</code> issues informative messages as it proceeds indicating what it has found that is abnormal or any corrective action that it has taken. Most of the messages are completely understandable only to those who are knowledgeable about the structure of the filesystem. Some of the more common messages are explained here. Note that the language of the messages is slightly different if <code>xfs_repair</code> is run in no-modify mode because the program is not changing anything on disk. No-modify mode indicates what it would do to repair the filesystem if run without the no-modify flag. </p>
<p> <code>disconnected inode</code> <i>ino</i><code>,</code> <code>moving to lost+found</code></p>
<dl>
<dd>An inode numbered <i>ino</i> was not connected to the filesystem directory tree and was reconnected to the <i>lost+found</i> directory. The inode is assigned the name of its inode number (<i>ino</i>). If a <i>lost+found</i> directory does not exist, it is automatically created.</dl>
<p> <code>disconnected dir inode</code> <i>ino</i><code>,</code> <code>moving to lost+found</code></p>
<dl>
<dd>As above only the inode is a directory inode. If a directory inode is attached to <i>lost+found</i>, all of its children (if any) stay attached to the directory and therefore get automatically reconnected when the directory is reconnected.</dl>
<p> <code>imap claims in-use inode</code> <i>ino</i> <code>is free, correcting imap</code></p>
<dl>
<dd>The inode allocation map thinks that inode <i>ino</i> is free whereas examination of the inode indicates that the inode may be in use (although it may be disconnected). The program updates the inode allocation map.</dl>
<p> <code>imap claims free inode</code> <i>ino</i> <code>is in use, correcting imap</code></p>
<dl>
<dd>The inode allocation map thinks that inode <i>ino</i> is in use whereas examination of the inode indicates that the inode is not in use and therefore is free. The program updates the inode allocation map.</dl>
<p> <code>resetting inode</code> <i>ino</i> <code>nlinks from</code> <i>x</i> <code>to</code> <i>y</i></p>
<dl>
<dd>The program detected a mismatch between the number of valid directory entries referencing inode <i>ino</i> and the number of references recorded in the inode and corrected the the number in the inode.</dl>
<p> <i>fork-type</i> <code>fork in ino</code> <i>ino</i> <code>claims used block</code> <i>bno</i></p>
<dl>
<dd>Inode <i>ino</i> claims a block <i>bno</i> that is used (claimed) by either another inode or the filesystem itself for metadata storage. The <i>fork-type</i> is either <code>data</code> or <code>attr</code> indicating whether the problem lies in the portion of the inode that tracks regular data or the portion of the inode that stores XFS attributes. If the inode is a real-time (rt) inode, the message says so. Any inode that claims blocks used by the filesystem is deleted. If two or more inodes claim the same block, they are both deleted.</dl>
<p> <i>fork-type</i> <code>fork in ino</code> <i>ino</i> <code>claims dup extent &#8230;</code></p>
<dl>
<dd>Inode <i>ino</i> claims a block in an extent known to be claimed more than once. The offset in the inode, start and length of the extent is given. The message is slightly different if the inode is a real-time (rt) inode and the extent is therefore a real-time (rt) extent.</dl>
<p> <code>inode</code> <i>ino</i> <code>&#8211; bad extent &#8230;</code></p>
<dl>
<dd>An extent record in the blockmap of inode <i>ino</i> claims blocks that are out of the legal range of the filesystem. The message supplies the start, end, and file offset of the extent. The message is slightly different if the extent is a real-time (rt) extent.</dl>
<p> <code>bad</code> <i>fork-type</i> <code>fork in inode</code> <i>ino</i></p>
<dl>
<dd>There was something structurally wrong or inconsistent with the data structures that map offsets to filesystem blocks.</dl>
<p> <code>cleared inode</code> <i>ino</i></p>
<dl>
<dd>There was something wrong with the inode that was uncorrectable so the program freed the inode. This usually happens because the inode claims blocks that are used by something else or the inode itself is badly corrupted. Typically, this message is preceded by one or more messages indicating why the inode needed to be cleared.</dl>
<p> <code>bad attribute fork in inode</code> <i>ino</i>, <code>clearing attr fork</code></p>
<dl>
<dd>There was something wrong with the portion of the inode that stores XFS attributes (the attribute fork) so the program reset the attribute fork. As a result of this, all attributes on that inode are lost.</dl>
<p> <code>correcting nextents for inode</code> <i>ino</i>, <code>was</code> <i>x</i> <code>&#8211; counted</code> <i>y</i></p>
<dl>
<dd>The program found that the number of extents used to store the data in the inode is wrong and corrected the number. The message refers to nextents if the count is wrong on the number of extents used to store attribute information.</dl>
<p> <code>entry</code> <i>name</i> <code>in dir</code> <i>dir_ino</i> <code>not consistent with .. value</code> <code>(</code><i>xxxx</i><code>)</code> <code>in dir ino</code> <i>ino</i><code>,</code> <code>junking entry</code> <i>name</i> <code>in directory inode</code> <i>dir_ino</i></p>
<dl>
<dd>The entry <i>name</i> in directory inode <i>dir_ino</i> references a directory inode <i>ino</i>. However, the .. entry in directory <i>ino</i> does not point back to directory <i>dir_ino</i>, so the program deletes the entry <i>name</i> in directory inode <i>dir_ino</i>. If the directory inode <i>ino</i> winds up becoming a disconnected inode as a result of this, it is moved to <i>lost+found</i> later.</dl>
<p> <code>entry</code> <i>name</i> <code>in dir</code> <i>dir_ino</i> <code>references already connected dir ino</code> <i>ino</i><code>,</code> <code>junking entry</code> <i>name</i> <code>in directory inode</code> <i>dir_ino</i></p>
<dl>
<dd>The entry <i>name</i> in directory inode <i>dir_ino</i> points to a directory inode <i>ino</i> that is known to be a child of another directory. Therefore, the entry is invalid and is deleted. This message refers to an entry in a small directory. If this were a large directory, the last phrase would read &quot;will clear entry&quot;.</dl>
<p> <code>entry references free inode</code> <i>ino</i> <code>in directory</code> <i>dir_ino</i><code>,</code> <code>will clear entry</code></p>
<dl>
<dd>An entry in directory inode <i>dir_ino</i> references an inode <i>ino</i> that is known to be free. The entry is therefore invalid and is deleted. This message refers to a large directory. If the directory were small, the message would read &quot;junking entry &#8230;&quot;.</dl>
<h2>Exit Status</h2>
<p><code>xfs_repair -n</code> (no modify node) will return a status of 1 if filesystem corruption was detected and 0 if no filesystem corruption was detected. <code>xfs_repair</code> run without the -n option will always return a status code of 0.</p>
<h2>Bugs</h2>
<p>The filesystem to be checked and repaired must have been unmounted cleanly using normal system administration procedures (the <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command or system shutdown), not as a result of a crash or system reset. If the filesystem has not been unmounted cleanly, mount it and unmount it cleanly before running <code>xfs_repair</code>. </p>
<p> <code>xfs_repair</code> does not do a thorough job on XFS extended attributes. The structure of the attribute fork will be consistent, but only the contents of attribute forks that will fit into an inode are checked. This limitation will be fixed in the future. </p>
<p> The no-modify mode (<code>-n</code> option) is not completely accurate. It does not catch inconsistencies in the freespace and inode maps, particularly lost blocks or subtly corrupted maps (trees). </p>
<p> The no-modify mode can generate repeated warnings about the same problems because it cannot fix the problems as they are encountered. </p>
<p> If a filesystem fails to be repaired, a metadump image can be generated with <code><a href="/docs/linux/man/8-xfs_metadump/">xfs_metadump</a></code>(8) and be sent to an XFS maintainer to be analysed and <code>xfs_repair</code> fixed and/or improved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dd/">dd</a></code>(1), <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8), <code><a href="/docs/linux/man/8-xfs_metadump/">xfs_metadump</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
