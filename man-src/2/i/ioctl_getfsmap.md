---
title: "ioctl_getfsmap(2)"
name: "ioctl_getfsmap"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_getfsmap/"
description: "ioctl_getfsmap – retrieve the physical layout of the filesystem"
---

<h2 class="name">NAME</h2>
<p> ioctl_getfsmap &#8211; retrieve the physical layout of the filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/ioctl.h&gt;</code><br />
 <code>#include &lt;linux/fs.h&gt;</code><br />
 <code>#include &lt;linux/fsmap.h&gt;</code> </p>
<p> <code>int ioctl(int </code><i>fd</i><code>, FS_IOC_GETFSMAP, struct fsmap_head * </code><i>arg</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation retrieves physical extent mappings for a filesystem. This information can be used to discover which files are mapped to a physical block, examine free space, or find known bad blocks, among other things. </p>
<p> The sole argument to this operation should be a pointer to a single <i>struct fsmap_head</i>: </p>
<p> struct fsmap {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 fmr_device;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Device ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 fmr_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mapping flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 fmr_physical;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Device offset of segment&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 fmr_owner;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Owner ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 fmr_offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File offset of segment&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 fmr_length;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Length of segment&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 fmr_reserved[3];&nbsp;/*&nbsp;Must be zero&nbsp;*/ }; </p>
<p> struct fsmap_head {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 fmh_iflags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Control flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 fmh_oflags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Output flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 fmh_count;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of entries in array incl. input&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 fmh_entries;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of entries filled in&nbsp;(output)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 fmh_reserved[6];&nbsp;<wbr>&nbsp;/*&nbsp;Must be zero&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fsmap fmh_keys[2];&nbsp;<wbr>&nbsp;/*&nbsp;Low and high keys for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the mapping search&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fsmap fmh_recs[];&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Returned records&nbsp;*/ }; </p>
<p> The two <i>fmh_keys</i> array elements specify the lowest and highest reverse-mapping key for which the application would like physical mapping information. A reverse mapping key consists of the tuple (device, block, owner, offset). The owner and offset fields are part of the key because some filesystems support sharing physical blocks between multiple files and therefore may return multiple mappings for a given physical block. </p>
<p> Filesystem mappings are copied into the <i>fmh_recs</i> array, which immediately follows the header data.</p>
<h3>Fields of struct fsmap_head</h3>
<p> The <i>fmh_iflags</i> field is a bit mask passed to the kernel to alter the output. No flags are currently defined, so the caller must set this value to zero. </p>
<p> The <i>fmh_oflags</i> field is a bit mask of flags set by the kernel concerning the returned mappings. If <code>FMH_OF_DEV_T</code> is set, then the <i>fmr_device</i> field represents a <i>dev_t</i> structure containing the major and minor numbers of the block device. </p>
<p> The <i>fmh_count</i> field contains the number of elements in the array being passed to the kernel. If this value is 0, <i>fmh_entries</i> will be set to the number of records that would have been returned had the array been large enough; no mapping information will be returned. </p>
<p> The <i>fmh_entries</i> field contains the number of elements in the <i>fmh_recs</i> array that contain useful information. </p>
<p> The <i>fmh_reserved</i> fields must be set to zero.</p>
<h3>Keys</h3>
<p> The two key records in <i>fsmap_head.fmh_keys</i> specify the lowest and highest extent records in the keyspace that the caller wants returned. A filesystem that can share blocks between files likely requires the tuple (<i>device</i>, <i>physical</i>, <i>owner</i>, <i>offset</i>, <i>flags</i>) to uniquely index any filesystem mapping record. Classic non-sharing filesystems might be able to identify any record with only (<i>device</i>, <i>physical</i>, <i>flags</i>). For example, if the low key is set to (8:0, 36864, 0, 0, 0), the filesystem will only return records for extents starting at or above 36 KiB on disk. If the high key is set to (8:0, 1048576, 0, 0, 0), only records below 1 MiB will be returned. The format of <i>fmr_device</i> in the keys must match the format of the same field in the output records, as defined below. By convention, the field <i>fsmap_head.fmh_keys[0]</i> must contain the low key and <i>fsmap_head.fmh_keys[1]</i> must contain the high key for the request. </p>
<p> For convenience, if <i>fmr_length</i> is set in the low key, it will be added to <i>fmr_block</i> or <i>fmr_offset</i> as appropriate. The caller can take advantage of this subtlety to set up subsequent calls by copying <i>fsmap_head.fmh_recs[fsmap_head.fmh_entries &#8211; 1]</i> into the low key. The function <i>fsmap_advance</i> (defined in <i>linux/fsmap.h</i>) provides this functionality.</p>
<h3>Fields of struct fsmap</h3>
<p> The <i>fmr_device</i> field uniquely identifies the underlying storage device. If the <code>FMH_OF_DEV_T</code> flag is set in the header&#8217;s <i>fmh_oflags</i> field, this field contains a <i>dev_t</i> from which major and minor numbers can be extracted. If the flag is not set, this field contains a value that must be unique for each unique storage device. </p>
<p> The <i>fmr_physical</i> field contains the disk address of the extent in bytes. </p>
<p> The <i>fmr_owner</i> field contains the owner of the extent. This is an inode number unless <code>FMR_OF_SPECIAL_OWNER</code> is set in the <i>fmr_flags</i> field, in which case the value is determined by the filesystem. See the section below about owner values for more details. </p>
<p> The <i>fmr_offset</i> field contains the logical address in the mapping record in bytes. This field has no meaning if the <code>FMR_OF_SPECIAL_OWNER</code> or <code>FMR_OF_EXTENT_MAP</code> flags are set in <i>fmr_flags</i>. </p>
<p> The <i>fmr_length</i> field contains the length of the extent in bytes. </p>
<p> The <i>fmr_flags</i> field is a bit mask of extent state flags. The bits are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>FMR_OF_PREALLOC</code></p>
<dd> The extent is allocated but not yet written.</p>
<dt><code>FMR_OF_ATTR_FORK</code></p>
<dd> This extent contains extended attribute data.</p>
<dt><code>FMR_OF_EXTENT_MAP</code></p>
<dd> This extent contains extent map information for the owner.</p>
<dt><code>FMR_OF_SHARED</code></p>
<dd> Parts of this extent may be shared.</p>
<dt><code>FMR_OF_SPECIAL_OWNER</code></p>
<dd> The <i>fmr_owner</i> field contains a special value instead of an inode number.</p>
<dt><code>FMR_OF_LAST</code></p>
<dd> This is the last record in the data set.</dl>
</dl>
<p> The <i>fmr_reserved</i> field will be set to zero.</p>
<h3>Owner values</h3>
<p> Generally, the value of the <i>fmr_owner</i> field for non-metadata extents should be an inode number. However, filesystems are under no obligation to report inode numbers; they may instead report <code>FMR_OWN_UNKNOWN</code> if the inode number cannot easily be retrieved, if the caller lacks sufficient privilege, if the filesystem does not support stable inode numbers, or for any other reason. If a filesystem wishes to condition the reporting of inode numbers based on process capabilities, it is strongly urged that the <code>CAP_SYS_ADMIN</code> capability be used for this purpose.</p>
<dl>
<dt>The following special owner values are generic to all filesystems:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>FMR_OWN_FREE</code></p>
<dd> Free space.</p>
<dt><code>FMR_OWN_UNKNOWN</code></p>
<dd> This extent is in use but its owner is not known or not easily retrieved.</p>
<dt><code>FMR_OWN_METADATA</code></p>
<dd> This extent is filesystem metadata.</dl>
</dl>
</dl>
<p> XFS can return the following special owner values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>XFS_FMR_OWN_FREE</code></p>
<dd> Free space.</p>
<dt><code>XFS_FMR_OWN_UNKNOWN</code></p>
<dd> This extent is in use but its owner is not known or not easily retrieved.</p>
<dt><code>XFS_FMR_OWN_FS</code></p>
<dd> Static filesystem metadata which exists at a fixed address. These are the AG superblock, the AGF, the AGFL, and the AGI headers.</p>
<dt><code>XFS_FMR_OWN_LOG</code></p>
<dd> The filesystem journal.</p>
<dt><code>XFS_FMR_OWN_AG</code></p>
<dd> Allocation group metadata, such as the free space btrees and the reverse mapping btrees.</p>
<dt><code>XFS_FMR_OWN_INOBT</code></p>
<dd> The inode and free inode btrees.</p>
<dt><code>XFS_FMR_OWN_INODES</code></p>
<dd> Inode records.</p>
<dt><code>XFS_FMR_OWN_REFC</code></p>
<dd> Reference count information.</p>
<dt><code>XFS_FMR_OWN_COW</code></p>
<dd> This extent is being used to stage a copy-on-write.</p>
<dt><code>XFS_FMR_OWN_DEFECTIVE:</code></p>
<dd> This extent has been marked defective either by the filesystem or the underlying device.</dl>
</dl>
<p> ext4 can return the following special owner values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>EXT4_FMR_OWN_FREE</code></p>
<dd> Free space.</p>
<dt><code>EXT4_FMR_OWN_UNKNOWN</code></p>
<dd> This extent is in use but its owner is not known or not easily retrieved.</p>
<dt><code>EXT4_FMR_OWN_FS</code></p>
<dd> Static filesystem metadata which exists at a fixed address. This is the superblock and the group descriptors.</p>
<dt><code>EXT4_FMR_OWN_LOG</code></p>
<dd> The filesystem journal.</p>
<dt><code>EXT4_FMR_OWN_INODES</code></p>
<dd> Inode records.</p>
<dt><code>EXT4_FMR_OWN_BLKBM</code></p>
<dd> Block bit map.</p>
<dt><code>EXT4_FMR_OWN_INOBM</code></p>
<dd> Inode bit map.</dl>
</dl>
<h2>RETURN VALUE</h2>
<p> On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> The error placed in <i>errno</i> can be one of, but is not limited to, the following:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not open for reading.</p>
<dt><code>EBADMSG</code></p>
<dd> The filesystem has detected a checksum error in the metadata.</p>
<dt><code>EFAULT</code></p>
<dd> The pointer passed in was not mapped to a valid memory address.</p>
<dt><code>EINVAL</code></p>
<dd> The array is not long enough, the keys do not point to a valid part of the filesystem, the low key points to a higher point in the filesystem&#8217;s physical storage address space than the high key, or a nonzero value was passed in one of the fields that must be zero.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to process the request.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The filesystem does not support this command.</p>
<dt><code>EUCLEAN</code></p>
<dd> The filesystem metadata is corrupt and needs repair.</dl>
<h2>VERSIONS</h2>
<p> The <code>FS_IOC_GETFSMAP</code> operation first appeared in Linux 4.12.</p>
<h2>CONFORMING TO</h2>
<p> This API is Linux-specific. Not all filesystems support it.</p>
<h2>EXAMPLES</h2>
<p> See <i>io/fsmap.c</i> in the <i>xfsprogs</i> distribution for a sample program.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
