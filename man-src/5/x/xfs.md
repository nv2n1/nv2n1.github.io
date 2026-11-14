---
title: "xfs(5)"
name: "xfs"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xfs/"
description: "xfs – layout, mount options, and supported file attributes for the XFS filesystem"
---

<p>xfs &#8211; layout, mount options, and supported file attributes for the XFS filesystem</p>
<h2>Description</h2>
<p>An XFS filesystem can reside on a regular disk partition or on a logical volume. An XFS filesystem has up to three parts: a data section, a log section, and a realtime section. Using the default <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) options, the realtime section is absent, and the log area is contained within the data section. The log section can be either separate from the data section or contained within it. The filesystem sections are divided into a certain number of <i>blocks</i>, whose size is specified at <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) time with the <code>-b</code> option. </p>
<p> The data section contains all the filesystem metadata (inodes, directories, indirect blocks) as well as the user file data for ordinary (non-realtime) files and the log area if the log is <i>internal</i> to the data section. The data section is divided into a number of <i>allocation groups</i>. The number and size of the allocation groups are chosen by <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) so that there is normally a small number of equal-sized groups. The number of allocation groups controls the amount of parallelism available in file and block allocation. It should be increased from the default if there is sufficient memory and a lot of allocation activity. The number of allocation groups should not be set very high, since this can cause large amounts of CPU time to be used by the filesystem, especially when the filesystem is nearly full. More allocation groups are added (of the original size) when <code><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></code>(8) is run. </p>
<p> The log section (or area, if it is internal to the data section) is used to store changes to filesystem metadata while the filesystem is running until those changes are made to the data section. It is written sequentially during normal operation and read only during mount. When mounting a filesystem after a crash, the log is read to complete operations that were in progress at the time of the crash. </p>
<p> The realtime section is used to store the data of realtime files. These files had an attribute bit set through <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) after file creation, before any data was written to the file. The realtime section is divided into a number of <i>extents</i> of fixed size (specified at <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) time). Each file in the realtime section has an extent size that is a multiple of the realtime section extent size. </p>
<p> Each allocation group contains several data structures. The first sector contains the superblock. For allocation groups after the first, the superblock is just a copy and is not updated after <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8). The next three sectors contain information for block and inode allocation within the allocation group. Also contained within each allocation group are data structures to locate free blocks and inodes; these are located through the header structures. </p>
<p> Each XFS filesystem is labeled with a Universal Unique Identifier (UUID). The UUID is stored in every allocation group header and is used to help distinguish one XFS filesystem from another, therefore you should avoid using <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) or other block-by-block copying programs to copy XFS filesystems. If two XFS filesystems on the same machine have the same UUID, <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8) may become confused when doing incremental and resumed dumps. <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8) and <code><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></code>(8) are recommended for making copies of XFS filesystems.</p>
<h2>Operations</h2>
<p>Some functionality specific to the XFS filesystem is accessible to applications through the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) and by-handle (see <code><a href="/docs/linux/man/3-open_by_handle/">open_by_handle</a></code>(3)) interfaces.</p>
<h2>Mount Options</h2>
<p>The following XFS-specific mount options may be used when mounting an XFS filesystem. Other generic options may be used as well; refer to the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) manual page for more details.</p>
<dl>
<dt><code>allocsize=size</code></p>
<dd>Sets the buffered I/O end-of-file preallocation size when doing delayed allocation writeout. Valid values for this option are page size (typically 4KiB) through to 1GiB, inclusive, in power-of-2 increments. </p>
<p> The default behavior is for dynamic end-of-file preallocation size, which uses a set of heuristics to optimise the preallocation size based on the current allocation patterns within the file and the access patterns to the file. Specifying a fixed allocsize value turns off the dynamic behavior.</p>
<dt><code>attr2</code>|<code>noattr2</code></p>
<dd>The options enable/disable an &quot;opportunistic&quot; improvement to be made in the way inline extended attributes are stored on-disk. When the new form is used for the first time when attr2 is selected (either when setting or removing extended attributes) the on-disk superblock feature bit field will be updated to reflect this format being in use. </p>
<p> The default behavior is determined by the on-disk feature bit indicating that attr2 behavior is active. If either mount option it set, then that becomes the new default used by the filesystem. </p>
<p> CRC enabled filesystems always use the attr2 format, and so will reject the noattr2 mount option if it is set.</p>
<dt><code>discard</code>|<code>nodiscard</code></p>
<dd>Enable/disable the issuing of commands to let the block device reclaim space freed by the filesystem. This is useful for SSD devices, thinly provisioned LUNs and virtual machine images, but may have a performance impact. </p>
<p> Note: It is currently recommended that you use the fstrim application to discard unused blocks rather than the discard mount option because the performance impact of this option is quite severe. For this reason, nodiscard is the default.</p>
<dt><code>grpid</code>|<code>bsdgroups</code>|<code>nogrpid</code>|<code>sysvgroups</code></p>
<dd>These options define what group ID a newly created file gets. When grpid is set, it takes the group ID of the directory in which it is created; otherwise it takes the fsgid of the current process, unless the directory has the setgid bit set, in which case it takes the gid from the parent directory, and also gets the setgid bit set if it is a directory itself.</p>
<dt><code>filestreams</code></p>
<dd>Make the data allocator use the filestreams allocation mode across the entire filesystem rather than just on directories configured to use it.</p>
<dt><code>ikeep</code>|<code>noikeep</code></p>
<dd>When ikeep is specified, XFS does not delete empty inode clusters and keeps them around on disk. When noikeep is specified, empty inode clusters are returned to the free space pool. noikeep is the default.</p>
<dt><code>inode32</code>|<code>inode64</code></p>
<dd>When inode32 is specified, it indicates that XFS limits inode creation to locations which will not result in inode numbers with more than 32 bits of significance. </p>
<p> When inode64 is specified, it indicates that XFS is allowed to create inodes at any location in the filesystem, including those which will result in inode numbers occupying more than 32 bits of significance. </p>
<p> inode32 is provided for backwards compatibility with older systems and applications, since 64 bits inode numbers might cause problems for some applications that cannot handle large inode numbers. If applications are in use which do not handle inode numbers bigger than 32 bits, the inode32 option should be specified. </p>
<p> For kernel v3.7 and later, inode64 is the default.</p>
<dt><code>largeio</code>|<code>nolargeio</code></p>
<dd>If &quot;nolargeio&quot; is specified, the optimal I/O reported in st_blksize by <a href="/docs/linux/man/2-stat/">stat</a>(2) will be as small as possible to allow user applications to avoid inefficient read/modify/write I/O. This is typically the page size of the machine, as this is the granularity of the page cache. </p>
<p> If &quot;largeio&quot; specified, a filesystem that was created with a &quot;swidth&quot; specified will return the &quot;swidth&quot; value (in bytes) in st_blksize. If the filesystem does not have a &quot;swidth&quot; specified but does specify an &quot;allocsize&quot; then &quot;allocsize&quot; (in bytes) will be returned instead. Otherwise the behavior is the same as if &quot;nolargeio&quot; was specified. nolargeio is the default.</p>
<dt><code>logbufs=value</code></p>
<dd>Set the number of in-memory log buffers. Valid numbers range from 2-8 inclusive. </p>
<p> The default value is 8 buffers. </p>
<p> If the memory cost of 8 log buffers is too high on small systems, then it may be reduced at some cost to performance on metadata intensive workloads. The logbsize option below controls the size of each buffer and so is also relevant to this case.</p>
<dt><code>logbsize=value</code></p>
<dd>Set the size of each in-memory log buffer. The size may be specified in bytes, or in kibibytes (KiB) with a &quot;k&quot; suffix. Valid sizes for version 1 and version 2 logs are 16384 (value=16k) and 32768 (value=32k). Valid sizes for version 2 logs also include 65536 (value=64k), 131072 (value=128k) and 262144 (value=256k). The logbsize must be an integer multiple of the log stripe unit configured at mkfs time. </p>
<p> The default value for version 1 logs is 32768, while the default value for version 2 logs is max(32768, log_sunit).</p>
<dt><code>logdev=device</code> and <code>rtdev=device</code></p>
<dd>Use an external log (metadata journal) and/or real-time device. An XFS filesystem has up to three parts: a data section, a log section, and a real-time section. The real-time section is optional, and the log section can be separate from the data section or contained within it.</p>
<dt><code>noalign</code></p>
<dd>Data allocations will not be aligned at stripe unit boundaries. This is only relevant to filesystems created with non-zero data alignment parameters (sunit, swidth) by mkfs.</p>
<dt><code>norecovery</code></p>
<dd>The filesystem will be mounted without running log recovery. If the filesystem was not cleanly unmounted, it is likely to be inconsistent when mounted in &quot;norecovery&quot; mode. Some files or directories may not be accessible because of this. Filesystems mounted &quot;norecovery&quot; must be mounted read-only or the mount will fail.</p>
<dt><code>nouuid</code></p>
<dd>Don&#8217;t check for double mounted file systems using the file system uuid. This is useful to mount LVM snapshot volumes, and often used in combination with &quot;norecovery&quot; for mounting read-only snapshots.</p>
<dt><code>noquota</code></p>
<dd>Forcibly turns off all quota accounting and enforcement within the filesystem.</p>
<dt><code>uquota/usrquota/quota/uqnoenforce/qnoenforce</code></p>
<dd>User disk quota accounting enabled, and limits (optionally) enforced. Refer to <a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a>(8) for further details.</p>
<dt><code>gquota/grpquota/gqnoenforce</code></p>
<dd>Group disk quota accounting enabled and limits (optionally) enforced. Refer to <a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a>(8) for further details.</p>
<dt><code>pquota/prjquota/pqnoenforce</code></p>
<dd>Project disk quota accounting enabled and limits (optionally) enforced. Refer to <a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a>(8) for further details.</p>
<dt><code>sunit=value</code> and <code>swidth=value</code></p>
<dd>Used to specify the stripe unit and width for a RAID device or a stripe volume. &quot;value&quot; must be specified in 512-byte block units. These options are only relevant to filesystems that were created with non-zero data alignment parameters. </p>
<p> The sunit and swidth parameters specified must be compatible with the existing filesystem alignment characteristics. In general, that means the only valid changes to sunit are increasing it by a power-of-2 multiple. Valid swidth values are any integer multiple of a valid sunit value. </p>
<p> Typically the only time these mount options are necessary if after an underlying RAID device has had it&#8217;s geometry modified, such as adding a new disk to a RAID5 lun and reshaping it.</p>
<dt><code>swalloc</code></p>
<dd>Data allocations will be rounded up to stripe width boundaries when the current end of file is being extended and the file size is larger than the stripe width size.</p>
<dt><code>wsync</code></p>
<dd>When specified, all filesystem namespace operations are executed synchronously. This ensures that when the namespace operation (create, unlink, etc) completes, the change to the namespace is on stable storage. This is useful in HA setups where failover must not result in clients seeing inconsistent namespace presentation during or after a failover event.</dl>
<h2>Removed Mount Options</h2>
<p>The following mount options have been removed from the kernel, and will yield mount failures if specified. Mount options are deprecated for a significant period time prior to removal. </p>
<table>
<tr VALIGN=top>
<td><code>Name</code></td>
<td>Removed
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8212;-</code></td>
<td>&#8212;&#8212;-
</td>
</tr>
<tr VALIGN=top>
<td><code>delaylog/nodelaylog</code></td>
<td>v4.0
</td>
</tr>
<tr VALIGN=top>
<td><code>ihashsize</code></td>
<td>v4.0
</td>
</tr>
<tr VALIGN=top>
<td><code>irixsgid</code></td>
<td>v4.0
</td>
</tr>
<tr VALIGN=top>
<td><code>osyncisdsync/osyncisosync</code></td>
<td>v4.0
</td>
</tr>
<tr VALIGN=top>
<td><code>barrier/nobarrier</code></td>
<td>v4.19
</td>
</tr>
</table>
<h2>File Attributes</h2>
<p>The XFS filesystem supports setting the following file attributes on Linux systems using the <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) utility: </p>
<p> <code>a</code> &#8211; append only </p>
<p> <code>A</code> &#8211; no atime updates </p>
<p> <code>d</code> &#8211; no dump </p>
<p> <code>i</code> &#8211; immutable </p>
<p> <code>S</code> &#8211; synchronous updates </p>
<p> For descriptions of these attribute flags, please refer to the <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) man page.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-xfs_info/">xfs_info</a></code>(8), <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8), <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8), <code><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></code>(8). </p>
