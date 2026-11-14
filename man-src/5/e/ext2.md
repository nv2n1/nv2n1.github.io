---
title: "ext2(5)"
name: "ext2"
section: "5"
letter: "e"
url: "/docs/linux/man/5-ext2/"
description: "ext2 – the second extended file system ext3 – the third extended file system ext4 – the fourth extended file system"
---

<p>ext2 &#8211; the second extended file system<br />
 ext3 &#8211; the third extended file system<br />
 ext4 &#8211; the fourth extended file system</p>
<h2>Description</h2>
<p>The second, third, and fourth extended file systems, or ext2, ext3, and ext4 as they are commonly known, are Linux file systems that have historically been the default file system for many Linux distributions. They are general purpose file systems that have been designed for extensibility and backwards compatibility. In particular, file systems previously intended for use with the ext2 and ext3 file systems can be mounted using the ext4 file system driver, and indeed in many modern Linux distributions, the ext4 file system driver has been configured to handle mount requests for ext2 and ext3 file systems.</p>
<h2>File System Features</h2>
<p>A file system formatted for ext2, ext3, or ext4 can have some collection of the following file system feature flags enabled. Some of these features are not supported by all implementations of the ext2, ext3, and ext4 file system drivers, depending on Linux kernel version in use. On other operating systems, such as the GNU/HURD or FreeBSD, only a very restrictive set of file system features may be supported in their implementations of ext2.</p>
<dl>
<dt><code>64bit</code></p>
<dd>Enables the file system to be larger than 2^32 blocks. This feature is set automatically, as needed, but it can be useful to specify this feature explicitly if the file system might need to be resized larger than 2^32 blocks, even if it was smaller than that threshold when it was originally created. Note that some older kernels and older versions of e2fsprogs will not support file systems with this ext4 feature enabled.</p>
<dt><code>bigalloc</code></p>
<dd>This ext4 feature enables clustered block allocation, so that the unit of allocation is a power of two number of blocks. That is, each bit in the what had traditionally been known as the block allocation bitmap now indicates whether a cluster is in use or not, where a cluster is by default composed of 16 blocks. This feature can decrease the time spent on doing block allocation and brings smaller fragmentation, especially for large files. The size can be specified using the <code>mke2fs -C</code> option.</p>
<dd><code>Warning:</code> The bigalloc feature is still under development, and may not be fully supported with your kernel or may have various bugs. Please see the web page <a rel="nofollow" href="http://ext4.wiki.kernel.org/index.php/Bigalloc">http://ext4.wiki.kernel.org/index.php/Bigalloc</a> for details. May clash with delayed allocation (see <code>nodelalloc</code> mount option).</p>
<dd>This feature requires that the <code>extent</code> feature be enabled.</p>
<dt><code>casefold</code></p>
<dd>This ext4 feature provides file system level character encoding support for directories with the casefold (+F) flag enabled. This feature is name-preserving on the disk, but it allows applications to lookup for a file in the file system using an encoding equivalent version of the file name.</p>
<dt><code>dir_index</code></p>
<dd>Use hashed b-trees to speed up name lookups in large directories. This feature is supported by ext3 and ext4 file systems, and is ignored by ext2 file systems.</p>
<dt><code>dir_nlink</code></p>
<dd>Normally, ext4 allows an inode to have no more than 65,000 hard links. This applies to regular files as well as directories, which means that there can be no more than 64,998 subdirectories in a directory (because each of the &#8216;.&#8217; and &#8216;..&#8217; entries, as well as the directory entry for the directory in its parent directory counts as a hard link). This feature lifts this limit by causing ext4 to use a link count of 1 to indicate that the number of hard links to a directory is not known when the link count might exceed the maximum count limit.</p>
<dt><code>ea_inode</code></p>
<dd>Normally, a file&#8217;s extended attributes and associated metadata must fit within the inode or the inode&#8217;s associated extended attribute block. This feature allows the value of each extended attribute to be placed in the data blocks of a separate inode if necessary, increasing the limit on the size and number of extended attributes per file.</p>
<dt><code>encrypt</code></p>
<dd>Enables support for file-system level encryption of data blocks and file names. The inode metadata (timestamps, file size, user/group ownership, etc.) is <i>not</i> encrypted.</p>
<dd>This feature is most useful on file systems with multiple users, or where not all files should be encrypted. In many use cases, especially on single-user systems, encryption at the block device layer using dm-crypt may provide much better security.</p>
<dt><code>ext_attr</code></p>
<dd>This feature enables the use of extended attributes. This feature is supported by ext2, ext3, and ext4.</p>
<dt><code>extent</code></p>
<dd>This ext4 feature allows the mapping of logical block numbers for a particular inode to physical blocks on the storage device to be stored using an extent tree, which is a more efficient data structure than the traditional indirect block scheme used by the ext2 and ext3 file systems. The use of the extent tree decreases metadata block overhead, improves file system performance, and decreases the needed to run <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) on the file system. (Note: both <code>extent</code> and <code>extents</code> are accepted as valid names for this feature for historical/backwards compatibility reasons.)</p>
<dt><code>extra_isize</code></p>
<dd>This ext4 feature reserves a specific amount of space in each inode for extended metadata such as nanosecond timestamps and file creation time, even if the current kernel does not currently need to reserve this much space. Without this feature, the kernel will reserve the amount of space for features it currently needs, and the rest may be consumed by extended attributes. </p>
<p> For this feature to be useful the inode size must be 256 bytes in size or larger.</p>
<dt><code>filetype</code></p>
<dd>This feature enables the storage of file type information in directory entries. This feature is supported by ext2, ext3, and ext4.</p>
<dt><code>flex_bg</code></p>
<dd>This ext4 feature allows the per-block group metadata (allocation bitmaps and inode tables) to be placed anywhere on the storage media. In addition, <code>mke2fs</code> will place the per-block group metadata together starting at the first block group of each &quot;flex_bg group&quot;. The size of the flex_bg group can be specified using the <code>-G</code> option.</p>
<dt><code>has_journal</code></p>
<dd>Create a journal to ensure file system consistency even across unclean shutdowns. Setting the file system feature is equivalent to using the <code>-j</code> option with <code>mke2fs</code> or <code>tune2fs.</code> This feature is supported by ext3 and ext4, and ignored by the ext2 file system driver.</p>
<dt><code>huge_file</code></p>
<dd>This ext4 feature allows files to be larger than 2 terabytes in size.</p>
<dt><code>inline_data</code></p>
<dd>Allow data to be stored in the inode and extended attribute area.</p>
<dt><code>journal_dev</code></p>
<dd>This feature is enabled on the superblock found on an external journal device. The block size for the external journal must be the same as the file system which uses it.</p>
<dd>The external journal device can be used by a file system by specifying the <code>-J</code> <code>device=</code>&lt;external-device&gt; option to <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) or <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a>(8)</code>.</p>
<dt><code>large_dir</code></p>
<dd>This feature increases the limit on the number of files per directory by raising the maximum size of directories and, for hashed b-tree directories (see <code>dir_index</code>), the maximum height of the hashed b-tree used to store the directory entries.</p>
<dt><code>large_file</code></p>
<dd>This feature flag is set automatically by modern kernels when a file larger than 2 gigabytes is created. Very old kernels could not handle large files, so this feature flag was used to prohibit those kernels from mounting file systems that they could not understand.</p>
<dt><code>metadata_csum</code></p>
<dd>This ext4 feature enables metadata checksumming. This feature stores checksums for all of the file system metadata (superblock, group descriptor blocks, inode and block bitmaps, directories, and extent tree blocks). The checksum algorithm used for the metadata blocks is different than the one used for group descriptors with the <code>uninit_bg</code> feature. These two features are incompatible and <code>metadata_csum</code> will be used preferentially instead of <code>uninit_bg</code>.</p>
<dt><code>metadata_csum_seed</code></p>
<dd>This feature allows the file system to store the metadata checksum seed in the superblock, which allows the administrator to change the UUID of a file system using the <code>metadata_csum</code> feature while it is mounted.</p>
<dt><code>meta_bg</code></p>
<dd>This ext4 feature allows file systems to be resized on-line without explicitly needing to reserve space for growth in the size of the block group descriptors. This scheme is also used to resize file systems which are larger than 2^32 blocks. It is not recommended that this feature be set when a file system is created, since this alternate method of storing the block group descriptors will slow down the time needed to mount the file system, and newer kernels can automatically set this feature as necessary when doing an online resize and no more reserved space is available in the resize inode.</p>
<dt><code>mmp</code></p>
<dd>This ext4 feature provides multiple mount protection (MMP). MMP helps to protect the file system from being multiply mounted and is useful in shared storage environments.</p>
<dt><code>project</code></p>
<dd>This ext4 feature provides project quota support. With this feature, the project ID of inode will be managed when the file system is mounted.</p>
<dt><code>quota</code></p>
<dd>Create quota inodes (inode #3 for userquota and inode #4 for group quota) and set them in the superblock. With this feature, the quotas will be enabled automatically when the file system is mounted.</p>
<dd>Causes the quota files (i.e., user.quota and group.quota which existed in the older quota design) to be hidden inodes.</p>
<dt><code>resize_inode</code></p>
<dd>This file system feature indicates that space has been reserved so that the block group descriptor table can be extended while resizing a mounted file system. The online resize operation is carried out by the kernel, triggered by <code><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></code>(8). By default <code>mke2fs</code> will attempt to reserve enough space so that the file system may grow to 1024 times its initial size. This can be changed using the <code>resize</code> extended option.</p>
<dd>This feature requires that the <code>sparse_super</code> or <code>sparse_super2</code> feature be enabled.</p>
<dt><code>sparse_super</code></p>
<dd>This file system feature is set on all modern ext2, ext3, and ext4 file systems. It indicates that backup copies of the superblock and block group descriptors are present only in a few block groups, not all of them.</p>
<dt><code>sparse_super2</code></p>
<dd>This feature indicates that there will only be at most two backup superblocks and block group descriptors. The block groups used to store the backup superblock(s) and blockgroup descriptor(s) are stored in the superblock, but typically, one will be located at the beginning of block group #1, and one in the last block group in the file system. This feature is essentially a more extreme version of sparse_super and is designed to allow a much larger percentage of the disk to have contiguous blocks available for data files.</p>
<dt><code>stable_inodes</code></p>
<dd>Marks the file system&#8217;s inode numbers and UUID as stable. <code><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></code>(8) will not allow shrinking a file system with this feature, nor will <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8) allow changing its UUID. This feature allows the use of specialized encryption settings that make use of the inode numbers and UUID. Note that the <code>encrypt</code> feature still needs to be enabled separately. <code>stable_inodes</code> is a &quot;compat&quot; feature, so old kernels will allow it.</p>
<dt><code>uninit_bg</code></p>
<dd>This ext4 file system feature indicates that the block group descriptors will be protected using checksums, making it safe for <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) to create a file system without initializing all of the block groups. The kernel will keep a high watermark of unused inodes, and initialize inode tables and blocks lazily. This feature speeds up the time to check the file system using <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), and it also speeds up the time required for <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) to create the file system.</p>
<dt><code>verity</code></p>
<dd>Enables support for verity protected files. Verity files are readonly, and their data is transparently verified against a Merkle tree hidden past the end of the file. Using the Merkle tree&#8217;s root hash, a verity file can be efficiently authenticated, independent of the file&#8217;s size.</p>
<dd>This feature is most useful for authenticating important read-only files on read-write file systems. If the file system itself is read-only, then using dm-verity to authenticate the entire block device may provide much better security.</dl>
<h2>Mount Options</h2>
<p>This section describes mount options which are specific to ext2, ext3, and ext4. Other generic mount options may be used as well; see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for details.</p>
<h2>Mount options for ext2</h2>
<p>The `ext2&#8242; file system is the standard Linux file system. Since Linux 2.5.46, for most mount options the default is determined by the file system superblock. Set them with <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8).</p>
<dl>
<dt><code>acl</code>|<code>noacl</code></p>
<dd>Support POSIX Access Control Lists (or not). See the <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) manual page.</p>
<dt><code>bsddf</code>|<code>minixdf</code></p>
<dd>Set the behavior for the <i>statfs</i> system call. The <code>minixdf</code> behavior is to return in the <i>f_blocks</i> field the total number of blocks of the file system, while the <code>bsddf</code> behavior (which is the default) is to subtract the overhead blocks used by the ext2 file system and not available for file storage. Thus </p>
<p> % mount /k -o minixdf; df /k; umount /k </p>
<table>
<tr VALIGN=top>
<td>File System&nbsp;<wbr>&nbsp;</td>
<td>1024-blocks&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>Used&nbsp;<wbr>&nbsp;</td>
<td>Available&nbsp;<wbr>&nbsp;</td>
<td>Capacity&nbsp;<wbr>&nbsp;</td>
<td>Mounted on
</td>
</tr>
<tr VALIGN=top>
<td>/dev/sda6</td>
<td ALIGN=center>2630655</td>
<td ALIGN=right>86954</td>
<td ALIGN=center>2412169</td>
<td ALIGN=center>3%</td>
<td>/k
</td>
</tr>
</table>
<p> % mount /k -o bsddf; df /k; umount /k </p>
<table>
<tr VALIGN=top>
<td>File System&nbsp;<wbr>&nbsp;</td>
<td>1024-blocks&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>Used&nbsp;<wbr>&nbsp;</td>
<td>Available&nbsp;<wbr>&nbsp;</td>
<td>Capacity&nbsp;<wbr>&nbsp;</td>
<td>Mounted on
</td>
</tr>
<tr VALIGN=top>
<td>/dev/sda6</td>
<td ALIGN=center>2543714</td>
<td ALIGN=right>13</td>
<td ALIGN=center>2412169</td>
<td ALIGN=center>0%</td>
<td>/k
</td>
</tr>
</table>
<p> (Note that this example shows that one can add command line options to the options given in <i>/etc/fstab</i>.)</p>
<dt><code>check=none</code> or <code>nocheck</code></p>
<dd>No checking is done at mount time. This is the default. This is fast. It is wise to invoke <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) every now and then, e.g. at boot time. The non-default behavior is unsupported (check=normal and check=strict options have been removed). Note that these mount options don&#8217;t have to be supported if ext4 kernel driver is used for ext2 and ext3 file systems.</p>
<dt><code>debug</code></p>
<dd>Print debugging info upon each (re)mount.</p>
<dt><code>errors=</code>{<code>continue</code>|<code>remount-ro</code>|<code>panic</code>}</p>
<dd>Define the behavior when an error is encountered. (Either ignore errors and just mark the file system erroneous and continue, or remount the file system read-only, or panic and halt the system.) The default is set in the file system superblock, and can be changed using <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8).</p>
<dt><code>grpid</code>|<code>bsdgroups</code> and <code>nogrpid</code>|<code>sysvgroups</code></p>
<dd>These options define what group id a newly created file gets. When <code>grpid</code> is set, it takes the group id of the directory in which it is created; otherwise (the default) it takes the fsgid of the current process, unless the directory has the setgid bit set, in which case it takes the gid from the parent directory, and also gets the setgid bit set if it is a directory itself.</p>
<dt><code>grpquota</code>|<code>noquota</code>|<code>quota</code>|<code>usrquota</code></p>
<dd>The usrquota (same as quota) mount option enables user quota support on the file system. grpquota enables group quotas support. You need the quota utilities to actually enable and manage the quota system.</p>
<dt><code>nouid32</code></p>
<dd>Disables 32-bit UIDs and GIDs. This is for interoperability with older kernels which only store and expect 16-bit values.</p>
<dt><code>oldalloc</code> or <code>orlov</code></p>
<dd>Use old allocator or Orlov allocator for new inodes. Orlov is default.</p>
<dt><code>resgid=</code>,<i>n</i> and <code>resuid=</code>,<i>n</i></p>
<dd>The ext2 file system reserves a certain percentage of the available space (by default 5%, see <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) and <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8)). These options determine who can use the reserved blocks. (Roughly: whoever has the specified uid, or belongs to the specified group.)</p>
<dt><code>sb=</code><i>n</i></p>
<dd>Instead of using the normal superblock, use an alternative superblock specified by <i>n</i>. This option is normally used when the primary superblock has been corrupted. The location of backup superblocks is dependent on the file system&#8217;s blocksize, the number of blocks per group, and features such as <code>sparse_super</code>.</p>
<dd>Additional backup superblocks can be determined by using the <code>mke2fs</code> program using the <code>-n</code> option to print out where the superblocks exist, supposing <code>mke2fs</code> is supplied with arguments that are consistent with the file system&#8217;s layout (e.g. blocksize, blocks per group, <code>sparse_super</code>, etc.).</p>
<dd>The block number here uses 1 k units. Thus, if you want to use logical block 32768 on a file system with 4 k blocks, use &quot;sb=131072&quot;.</p>
<dt><code>user_xattr</code>|<code>nouser_xattr</code></p>
<dd>Support &quot;user.&quot; extended attributes (or not). </p>
</dl>
<h2>Mount options for ext3</h2>
<p>The ext3 file system is a version of the ext2 file system which has been enhanced with journaling. It supports the same options as ext2 as well as the following additions:</p>
<dl>
<dt><code>journal_dev=devnum</code>/<code>journal_path=path</code></p>
<dd>When the external journal device&#8217;s major/minor numbers have changed, these options allow the user to specify the new journal location. The journal device is identified either through its new major/minor numbers encoded in devnum, or via a path to the device.</p>
<dt><code>norecovery</code>/<code>noload</code></p>
<dd>Don&#8217;t load the journal on mounting. Note that if the file system was not unmounted cleanly, skipping the journal replay will lead to the file system containing inconsistencies that can lead to any number of problems.</p>
<dt><code>data=</code>{<code>journal</code>|<code>ordered</code>|<code>writeback</code>}</p>
<dd>Specifies the journaling mode for file data. Metadata is always journaled. To use modes other than <code>ordered</code> on the root file system, pass the mode to the kernel as boot parameter, e.g. <i>rootflags=data=journal</i>.</p>
<dl>
<dd>
<dl>
<dt><code>journal</code></p>
<dd>All data is committed into the journal prior to being written into the main file system.</p>
<dt><code>ordered</code></p>
<dd>This is the default mode. All data is forced directly out to the main file system prior to its metadata being committed to the journal.</p>
<dt><code>writeback</code></p>
<dd>Data ordering is not preserved &#8211; data may be written into the main file system after its metadata has been committed to the journal. This is rumoured to be the highest-throughput option. It guarantees internal file system integrity, however it can allow old data to appear in files after a crash and journal recovery.</dl>
</dl>
<dt><code>data_err=ignore</code></p>
<dd>Just print an error message if an error occurs in a file data buffer in ordered mode.</p>
<dt><code>data_err=abort</code></p>
<dd>Abort the journal if an error occurs in a file data buffer in ordered mode.</p>
<dt><code>barrier=0</code> / <code>barrier=1</code></p>
<dd>This disables / enables the use of write barriers in the jbd code. barrier=0 disables, barrier=1 enables (default). This also requires an IO stack which can support barriers, and if jbd gets an error on a barrier write, it will disable barriers again with a warning. Write barriers enforce proper on-disk ordering of journal commits, making volatile disk write caches safe to use, at some performance penalty. If your disks are battery-backed in one way or another, disabling barriers may safely improve performance.</p>
<dt><code>commit=</code><i>nrsec</i></p>
<dd>Start a journal commit every <i>nrsec</i> seconds. The default value is 5 seconds. Zero means default.</p>
<dt><code>user_xattr</code></p>
<dd>Enable Extended User Attributes. See the <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5) manual page.</p>
<dt><code>jqfmt=</code>{<code>vfsold</code>|<code>vfsv0</code>|<code>vfsv1</code>}</p>
<dd>Apart from the old quota system (as in ext2, jqfmt=vfsold aka version 1 quota) ext3 also supports journaled quotas (version 2 quota). jqfmt=vfsv0 or jqfmt=vfsv1 enables journaled quotas. Journaled quotas have the advantage that even after a crash no quota check is required. When the <code>quota</code> file system feature is enabled, journaled quotas are used automatically, and this mount option is ignored.</p>
<dt><code>usrjquota=aquota.user</code>|<code>grpjquota=aquota.group</code></p>
<dd>For journaled quotas (jqfmt=vfsv0 or jqfmt=vfsv1), the mount options usrjquota=aquota.user and grpjquota=aquota.group are required to tell the quota system which quota database files to use. When the <code>quota</code> file system feature is enabled, journaled quotas are used automatically, and this mount option is ignored. </p>
</dl>
<h2>Mount options for ext4</h2>
<p>The ext4 file system is an advanced level of the ext3 file system which incorporates scalability and reliability enhancements for supporting large file system. </p>
<p> The options <code>journal_dev, journal_path, norecovery, noload, data, commit, orlov,</code> <code>oldalloc, [no]user_xattr, [no]acl, bsddf, minixdf, debug, errors,</code> <code>data_err, grpid, bsdgroups, nogrpid, sysvgroups, resgid, resuid, sb,</code> <code>quota, noquota, nouid32, grpquota, usrquota, usrjquota, grpjquota,</code> <code>and jqfmt are backwardly compatible with ext3 or ext2.</code></p>
<dl>
<dt><code>journal_checksum | nojournal_checksum</code></p>
<dd>The journal_checksum option enables checksumming of the journal transactions. This will allow the recovery code in e2fsck and the kernel to detect corruption in the kernel. It is a compatible change and will be ignored by older kernels.</p>
<dt><code>journal_async_commit</code></p>
<dd>Commit block can be written to disk without waiting for descriptor blocks. If enabled older kernels cannot mount the device. This will enable &#8216;journal_checksum&#8217; internally.</p>
<dt><code>barrier=0</code> / <code>barrier=1</code> / <code>barrier</code> / <code>nobarrier</code></p>
<dd>These mount options have the same effect as in ext3. The mount options &quot;barrier&quot; and &quot;nobarrier&quot; are added for consistency with other ext4 mount options. </p>
<p> The ext4 file system enables write barriers by default.</p>
<dt><code>inode_readahead_blks=</code><i>n</i></p>
<dd>This tuning parameter controls the maximum number of inode table blocks that ext4&#8217;s inode table readahead algorithm will pre-read into the buffer cache. The value must be a power of 2. The default value is 32 blocks.</p>
<dt><code>stripe=</code><i>n</i></p>
<dd>Number of file system blocks that mballoc will try to use for allocation size and alignment. For RAID5/6 systems this should be the number of data disks * RAID chunk size in file system blocks.</p>
<dt><code>delalloc</code></p>
<dd>Deferring block allocation until write-out time.</p>
<dt><code>nodelalloc</code></p>
<dd>Disable delayed allocation. Blocks are allocated when data is copied from user to page cache.</p>
<dt><code>max_batch_time=</code><i>usec</i></p>
<dd>Maximum amount of time ext4 should wait for additional file system operations to be batch together with a synchronous write operation. Since a synchronous write operation is going to force a commit and then a wait for the I/O complete, it doesn&#8217;t cost much, and can be a huge throughput win, we wait for a small amount of time to see if any other transactions can piggyback on the synchronous write. The algorithm used is designed to automatically tune for the speed of the disk, by measuring the amount of time (on average) that it takes to finish committing a transaction. Call this time the &quot;commit time&quot;. If the time that the transaction has been running is less than the commit time, ext4 will try sleeping for the commit time to see if other operations will join the transaction. The commit time is capped by the max_batch_time, which defaults to 15000&nbsp;&micro;s (15 ms). This optimization can be turned off entirely by setting max_batch_time to 0.</p>
<dt><code>min_batch_time=</code><i>usec</i></p>
<dd>This parameter sets the commit time (as described above) to be at least min_batch_time. It defaults to zero microseconds. Increasing this parameter may improve the throughput of multi-threaded, synchronous workloads on very fast disks, at the cost of increasing latency.</p>
<dt><code>journal_ioprio=</code><i>prio</i></p>
<dd>The I/O priority (from 0 to 7, where 0 is the highest priority) which should be used for I/O operations submitted by kjournald2 during a commit operation. This defaults to 3, which is a slightly higher priority than the default I/O priority.</p>
<dt><code>abort</code></p>
<dd>Simulate the effects of calling ext4_abort() for debugging purposes. This is normally used while remounting a file system which is already mounted.</p>
<dt><code>auto_da_alloc</code>|<code>noauto_da_alloc</code></p>
<dd>Many broken applications don&#8217;t use fsync() when replacing existing files via patterns such as </p>
<p> fd = open(&quot;foo.new&quot;)/write(fd,&#8230;)/close(fd)/ rename(&quot;foo.new&quot;, &quot;foo&quot;) </p>
<p> or worse yet </p>
<p> fd = open(&quot;foo&quot;, O_TRUNC)/write(fd,&#8230;)/close(fd). </p>
<p> If auto_da_alloc is enabled, ext4 will detect the replace-via-rename and replace-via-truncate patterns and force that any delayed allocation blocks are allocated such that at the next journal commit, in the default data=ordered mode, the data blocks of the new file are forced to disk before the rename() operation is committed. This provides roughly the same level of guarantees as ext3, and avoids the &quot;zero-length&quot; problem that can happen when a system crashes before the delayed allocation blocks are forced to disk.</p>
<dt><code>noinit_itable</code></p>
<dd>Do not initialize any uninitialized inode table blocks in the background. This feature may be used by installation CD&#8217;s so that the install process can complete as quickly as possible; the inode table initialization process would then be deferred until the next time the file system is mounted.</p>
<dt><code>init_itable=n</code></p>
<dd>The lazy itable init code will wait n times the number of milliseconds it took to zero out the previous block group&#8217;s inode table. This minimizes the impact on system performance while the file system&#8217;s inode table is being initialized.</p>
<dt><code>discard</code>/<code>nodiscard</code></p>
<dd>Controls whether ext4 should issue discard/TRIM commands to the underlying block device when blocks are freed. This is useful for SSD devices and sparse/thinly-provisioned LUNs, but it is off by default until sufficient testing has been done.</p>
<dt><code>block_validity</code>/<code>noblock_validity</code></p>
<dd>This option enables/disables the in-kernel facility for tracking file system metadata blocks within internal data structures. This allows multi-block allocator and other routines to quickly locate extents which might overlap with file system metadata blocks. This option is intended for debugging purposes and since it negatively affects the performance, it is off by default.</p>
<dt><code>dioread_lock</code>/<code>dioread_nolock</code></p>
<dd>Controls whether or not ext4 should use the DIO read locking. If the dioread_nolock option is specified ext4 will allocate uninitialized extent before buffer write and convert the extent to initialized after IO completes. This approach allows ext4 code to avoid using inode mutex, which improves scalability on high speed storages. However this does not work with data journaling and dioread_nolock option will be ignored with kernel warning. Note that dioread_nolock code path is only used for extent-based files. Because of the restrictions this options comprises it is off by default (e.g. dioread_lock).</p>
<dt><code>max_dir_size_kb=n</code></p>
<dd>This limits the size of the directories so that any attempt to expand them beyond the specified limit in kilobytes will cause an ENOSPC error. This is useful in memory-constrained environments, where a very large directory can cause severe performance problems or even provoke the Out Of Memory killer. (For example, if there is only 512 MB memory available, a 176 MB directory may seriously cramp the system&#8217;s style.)</p>
<dt><code>i_version</code></p>
<dd>Enable 64-bit inode version support. This option is off by default.</p>
<dt><code>nombcache</code></p>
<dd>This option disables use of mbcache for extended attribute deduplication. On systems where extended attributes are rarely or never shared between files, use of mbcache for deduplication adds unnecessary computational overhead.</p>
<dt><code>prjquota</code></p>
<dd>The prjquota mount option enables project quota support on the file system. You need the quota utilities to actually enable and manage the quota system. This mount option requires the <code>project</code> file system feature. </p>
</dl>
<h2>File Attributes</h2>
<p>The ext2, ext3, and ext4 file systems support setting the following file attributes on Linux systems using the <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) utility: </p>
<p> <code>a</code> &#8211; append only </p>
<p> <code>A</code> &#8211; no atime updates </p>
<p> <code>d</code> &#8211; no dump </p>
<p> <code>D</code> &#8211; synchronous directory updates </p>
<p> <code>i</code> &#8211; immutable </p>
<p> <code>S</code> &#8211; synchronous updates </p>
<p> <code>u</code> &#8211; undeletable </p>
<p> In addition, the ext3 and ext4 file systems support the following flag: </p>
<p> <code>j</code> &#8211; data journaling </p>
<p> Finally, the ext4 file system also supports the following flag: </p>
<p> <code>e</code> &#8211; extents format </p>
<p> For descriptions of these attribute flags, please refer to the <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) man page.</p>
<h2>Kernel Support</h2>
<p>This section lists the file system driver (e.g., ext2, ext3, ext4) and upstream kernel version where a particular file system feature was supported. Note that in some cases the feature was present in earlier kernel versions, but there were known, serious bugs. In other cases the feature may still be considered in an experimental state. Finally, note that some distributions may have backported features into older kernels; in particular the kernel versions in certain &quot;enterprise distributions&quot; can be extremely misleading.</p>
<dl>
<dt><code>filetype</code></p>
<dd>ext2, 2.2.0</p>
<dt><code>sparse_super</code></p>
<dd>ext2, 2.2.0</p>
<dt><code>large_file</code></p>
<dd>ext2, 2.2.0</p>
<dt><code>has_journal</code></p>
<dd>ext3, 2.4.15</p>
<dt><code>ext_attr</code></p>
<dd>ext2/ext3, 2.6.0</p>
<dt><code>dir_index</code></p>
<dd>ext3, 2.6.0</p>
<dt><code>resize_inode</code></p>
<dd>ext3, 2.6.10 (online resizing)</p>
<dt><code>64bit</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>dir_nlink</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>extent</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>extra_isize</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>flex_bg</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>huge_file</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>meta_bg</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>uninit_bg</code></p>
<dd>ext4, 2.6.28</p>
<dt><code>mmp</code></p>
<dd>ext4, 3.0</p>
<dt><code>bigalloc</code></p>
<dd>ext4, 3.2</p>
<dt><code>quota</code></p>
<dd>ext4, 3.6</p>
<dt><code>inline_data</code></p>
<dd>ext4, 3.8</p>
<dt><code>sparse_super2</code></p>
<dd>ext4, 3.16</p>
<dt><code>metadata_csum</code></p>
<dd>ext4, 3.18</p>
<dt><code>encrypt</code></p>
<dd>ext4, 4.1</p>
<dt><code>metadata_csum_seed</code></p>
<dd>ext4, 4.4</p>
<dt><code>project</code></p>
<dd>ext4, 4.5</p>
<dt><code>ea_inode</code></p>
<dd>ext4, 4.13</p>
<dt><code>large_dir</code></p>
<dd>ext4, 4.13</p>
<dt><code>casefold</code></p>
<dd>ext4, 5.2</p>
<dt><code>verity</code></p>
<dd>ext4, 5.4</p>
<dt><code>stable_inodes</code></p>
<dd>ext4, 5.5</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/5-mke2fs-conf/">mke2fs.conf</a></code>(5), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8), <code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) </p>
