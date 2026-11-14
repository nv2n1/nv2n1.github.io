---
title: "xfsctl(3)"
name: "xfsctl"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfsctl/"
description: "xfsctl – control XFS filesystems and individual files"
---

<p>xfsctl &#8211; control XFS filesystems and individual files</p>
<h2>C Synopsis</h2>
<p><code>#include &lt;xfs/xfs.h&gt;</code></p>
<dl>
<dt> <code>int xfsctl(const char *</code><i>path</i><code>, int </code><i>fd</i><code>, int </code><i>cmd</i><code>, void *</code><i>ptr</i><code>);</code></dl>
<p> <code>int platform_test_xfs_fd(int </code><i>fd</i><code>);</code></p>
<dd><code>int platform_test_xfs_path(const char *</code><i>path</i><code>);</code></p>
<h2>Description</h2>
<dd>Some functionality specific to the XFS filesystem is accessible to applications through platform-specific system call interfaces. These operations can be divided into two sections &#8211; operations that operate on individual files, and operations that operate on the filesystem itself. Care should be taken when issuing <code>xfsctl</code>() calls to ensure the target path and file descriptor (both must be supplied) do indeed represent a file from an XFS filesystem. The <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) and <code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2) system calls can be used to determine whether or not an arbitrary path or file descriptor belong to an XFS filesystem. These are not portable however, so the routines <code>platform_test_xfs_fd</code>() and <code>platform_test_xfs_path</code>() provide a platform-independent mechanism.</p>
<h3>File Operations</h3>
<p>In order to effect an operation on an individual file, the pathname and descriptor arguments passed to <code>xfsctl</code> identifies the file being operated on. The final argument described below refers to the final argument of <code>xfsctl</code>. All of the data structures and macros mentioned below are defined in the &lt;<i>xfs/xfs_fs.h</i>&gt; header file. <code>XFS_IOC_ALLOCSP</code><br />
 <code>XFS_IOC_ALLOCSP64</code><br />
 <code>XFS_IOC_FREESP</code></p>
<dl>
<dt><code>XFS_IOC_FREESP64</code></p>
<dd>Alter storage space associated with a section of the ordinary file specified. The section is specified by a variable of type <code>xfs_flock64_t</code>, pointed to by the final argument. The data type <code>xfs_flock64_t</code> contains the following members: <code>l_whence</code> is 0, 1, or 2 to indicate that the relative offset <code>l_start</code> will be measured from the start of the file, the current position, or the end of the file, respectively (i.e., <code>l_start</code> is the offset from the position specified in <code>l_whence</code>). If the offset specified is before the current end of file, any data previously written into this section is no longer accessible. If the offset specified is beyond the current end of file, the file is grown and filled with zeroes. The <code>l_len</code> field is currently ignored, and should be set to zero. <code>XFS_IOC_ALLOCSP</code>, <code>XFS_IOC_ALLOCSP64</code>, <code>XFS_IOC_FREESP</code> and <code>XFS_IOC_FREESP64</code> operations are all identical.</p>
<dt><code>XFS_IOC_FSSETDM</code></p>
<dd>Set the di_dmevmask and di_dmstate fields in an XFS on-disk inode. The only legitimate values for these fields are those previously returned in the <code>bs_dmevmask</code> and <code>bs_dmstate</code> fields of the bulkstat structure. The data referred to by the final argument is a <code>struct fsdmidata</code>. This structure&#8217;s members are <code>fsd_dmevmask</code> and <code>fsd_dmstate</code>. The di_dmevmask field is set to the value in <code>fsd_dmevmask</code>. The di_dmstate field is set to the value in <code>fsd_dmstate</code>. This command is restricted to root or to processes with device management capabilities. Its sole purpose is to allow backup and restore programs to restore the aforementioned critical on-disk inode fields.</p>
<dt><code>XFS_IOC_DIOINFO</code></p>
<dd>Get information required to perform direct I/O on the specified file descriptor. Direct I/O is performed directly to and from a user&#8217;s data buffer. Since the kernel&#8217;s buffer cache is no longer between the two, the user&#8217;s data buffer must conform to the same type of constraints as required for accessing a raw disk partition. The final argument points to a variable of type <code>struct dioattr</code>, which contains the following members: <code>d_mem</code> is the memory alignment requirement of the user&#8217;s data buffer. <code>d_miniosz</code> specifies block size, minimum I/O request size, and I/O alignment. The size of all I/O requests must be a multiple of this amount and the value of the seek pointer at the time of the I/O request must also be an integer multiple of this amount. <code>d_maxiosz</code> is the maximum I/O request size which can be performed on the file descriptor. If an I/O request does not meet these constraints, the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) will fail with EINVAL. All I/O requests are kept consistent with any data brought into the cache with an access through a non-direct I/O file descriptor.</p>
<dt><code>XFS_IOC_FSGETXATTR</code></p>
<dd>Get additional attributes associated with files in XFS file systems. The final argument points to a variable of type <code>struct fsxattr</code>, whose fields include: <code>fsx_xflags</code> (extended flag bits), <code>fsx_extsize</code> (nominal extent size in file system blocks), <code>fsx_nextents</code> (number of data extents in the file). A <code>fsx_extsize</code> value returned indicates that a preferred extent size was previously set on the file, a <code>fsx_extsize</code> of zero indicates that the defaults for that filesystem will be used. Currently the meaningful bits for the <code>fsx_xflags</code> field are:</p>
<dl>
<dd>
<dl>
<dt><font SIZE="-1">Bit 0 (0x1) &#8211; XFS_XFLAG_REALTIME</font></p>
<dd>The file is a realtime file.</p>
<dt><font SIZE="-1">Bit 1 (0x2) &#8211; XFS_XFLAG_PREALLOC</font></p>
<dd>The file has preallocated space.</p>
<dt><font SIZE="-1">Bit 3 (0x8) &#8211; XFS_XFLAG_IMMUTABLE</font></p>
<dd>The file is immutable &#8211; it cannot be modified, deleted or renamed, no link can be created to this file and no data can be written to the file. Only the superuser or a process possessing the CAP_LINUX_IMMUTABLE capability can set or clear this flag.</p>
<dt><font SIZE="-1">Bit 4 (0x10) &#8211; XFS_XFLAG_APPEND</font></p>
<dd>The file is append-only &#8211; it can only be open in append mode for writing. Only the superuser or a process possessing the CAP_LINUX_IMMUTABLE capability can set or clear this flag.</p>
<dt><font SIZE="-1">Bit 5 (0x20) &#8211; XFS_XFLAG_SYNC</font></p>
<dd>All writes to the file are synchronous.</p>
<dt><font SIZE="-1">Bit 6 (0x40) &#8211; XFS_XFLAG_NOATIME</font></p>
<dd>When the file is accessed, its atime record is not modified.</p>
<dt><font SIZE="-1">Bit 7 (0x80) &#8211; XFS_XFLAG_NODUMP</font></p>
<dd>The file should be skipped by backup utilities.</p>
<dt><font SIZE="-1">Bit 8 (0x100) &#8211; XFS_XFLAG_RTINHERIT</font></p>
<dd>Realtime inheritance bit &#8211; new files created in the directory will be automatically realtime, and new directories created in the directory will inherit the inheritance bit.</p>
<dt><font SIZE="-1">Bit 9 (0x200) &#8211; XFS_XFLAG_PROJINHERIT</font></p>
<dd>Project inheritance bit &#8211; new files and directories created in the directory will inherit the parents project ID. New directories also inherit the project inheritance bit.</p>
<dt><font SIZE="-1">Bit 10 (0x400) &#8211; XFS_XFLAG_NOSYMLINKS</font></p>
<dd>Can only be set on a directory and disallows creation of symbolic links in that directory.</p>
<dt><font SIZE="-1">Bit 11 (0x800) &#8211; XFS_XFLAG_EXTSIZE</font></p>
<dd>Extent size bit &#8211; if a basic extent size value is set on the file then the allocator will allocate in multiples of the set size for this file (see <code>XFS_IOC_FSSETXATTR</code> below).</p>
<dt><font SIZE="-1">Bit 12 (0x1000) &#8211; XFS_XFLAG_EXTSZINHERIT</font></p>
<dd>Extent size inheritance bit &#8211; new files and directories created in the directory will inherit the parents basic extent size value (see <code>XFS_IOC_FSSETXATTR</code> below). Can only be set on a directory.</p>
<dt><font SIZE="-1">Bit 13 (0x2000) &#8211; XFS_XFLAG_NODEFRAG</font></p>
<dd>No defragment file bit &#8211; the file should be skipped during a defragmentation operation. When applied to a directory, new files and directories created will inherit the no-defrag bit.</p>
<dt><font SIZE="-1">Bit 14 (0x4000) &#8211; XFS_XFLAG_FILESTREAM</font></p>
<dd>Filestream allocator bit &#8211; allows a directory to reserve an allocation group for exclusive use by files created within that directory. Files being written in other directories will not use the same allocation group and so files within different directories will not interleave extents on disk. The reservation is only active while files are being created and written into the directory.</p>
<dt><font SIZE="-1">Bit 31 (0x80000000) &#8211; XFS_XFLAG_HASATTR</font></p>
<dd>The file has extended attributes associated with it.</dl>
</dl>
</dl>
<dl>
<dt><code>XFS_IOC_FSGETXATTRA</code></p>
<dd>Identical to <code>XFS_IOC_FSGETXATTR</code> except that the <code>fsx_nextents</code> field contains the number of attribute extents in the file.</p>
<dt><code>XFS_IOC_FSSETXATTR</code></p>
<dd>Set additional attributes associated with files in XFS file systems. The final argument points to a variable of type <code>struct fsxattr</code>, but only the following fields are used in this call: <code>fsx_xflags</code>, <code>fsx_extsize</code> and <code>fsx_projid</code>. The <code>fsx_xflags</code> realtime file bit and the file&#8217;s extent size may be changed only when the file is empty, except in the case of a directory where the extent size can be set at any time (this value is only used for regular file allocations, so should only be set on a directory in conjunction with the XFS_XFLAG_EXTSZINHERIT flag).</p>
<dt><code>XFS_IOC_GETBMAP</code></p>
<dd>Get the block map for a segment of a file in an XFS file system. The final argument points to an arry of variables of type <code>struct getbmap</code>. All sizes and offsets in the structure are in units of 512 bytes. The structure fields include: <code>bmv_offset</code> (file offset of segment), <code>bmv_block</code> (starting block of segment), <code>bmv_length</code> (length of segment), <code>bmv_count</code> (number of array entries, including the first), and <code>bmv_entries</code> (number of entries filled in). The first structure in the array is a header, and the remaining structures in the array contain block map information on return. The header controls iterative calls to the <code>XFS_IOC_GETBMAP</code> command. The caller fills in the <code>bmv_offset</code> and <code>bmv_length</code> fields of the header to indicate the area of interest in the file, and fills in the <code>bmv_count</code> field to indicate the length of the array. If the <code>bmv_length</code> value is set to -1 then the length of the interesting area is the rest of the file. On return from a call, the header is updated so that the command can be reused to obtain more information, without re-initializing the structures. Also on return, the <code>bmv_entries</code> field of the header is set to the number of array entries actually filled in. The non-header structures will be filled in with <code>bmv_offset</code>, <code>bmv_block</code>, and <code>bmv_length</code>. If a region of the file has no blocks (is a hole in the file) then the <code>bmv_block</code> field is set to -1.</p>
<dt><code>XFS_IOC_GETBMAPA</code></p>
<dd>Identical to <code>XFS_IOC_GETBMAP</code> except that information about the attribute fork of the file is returned.  <code>XFS_IOC_RESVSP</code></p>
<dl>
<dt><code>XFS_IOC_RESVSP64</code></p>
<dd>This command is used to allocate space to a file. A range of bytes is specified using a pointer to a variable of type <code>xfs_flock64_t</code> in the final argument. The blocks are allocated, but not zeroed, and the file size does not change. If the XFS filesystem is configured to flag unwritten file extents, performance will be negatively affected when writing to preallocated space, since extra filesystem transactions are required to convert extent flags on the range of the file written. If <code><a href="/docs/linux/man/8-xfs_info/">xfs_info</a></code>(8) reports unwritten=1, then the filesystem was made to flag unwritten extents.  <code>XFS_IOC_UNRESVSP</code></p>
<dl>
<dt><code>XFS_IOC_UNRESVSP64</code></p>
<dd>This command is used to free space from a file. A range of bytes is specified using a pointer to a variable of type <code>xfs_flock64_t</code> in the final argument. Partial filesystem blocks are zeroed, and whole filesystem blocks are removed from the file. The file size does not change.</p>
<dt><code>XFS_IOC_ZERO_RANGE</code></p>
<dd>This command is used to convert a range of a file to zeros without issuing data IO. A range of bytes is specified using a pointer to a variable of type <code>xfs_flock64_t</code> in the final argument. Blocks are preallocated for regions that span holes in the file, and the entire range is converted to unwritten extents. This operation is a fast method of overwriting any from the range specified with zeros without removing any blocks or having to write zeros to disk. Any subsequent read in the given range will return zeros until new data is written. This functionality requires filesystems to support unwritten extents. If <code><a href="/docs/linux/man/8-xfs_info/">xfs_info</a></code>(8) reports unwritten=1, then the filesystem was made to flag unwritten extents.  </p>
<pre><code>XFS_IOC_PATH_TO_HANDLE</code>
<code>XFS_IOC_PATH_TO_FSHANDLE</code>
<code>XFS_IOC_FD_TO_HANDLE</code>
<code>XFS_IOC_OPEN_BY_HANDLE</code>
<code>XFS_IOC_READLINK_BY_HANDLE</code>
<code>XFS_IOC_ATTR_LIST_BY_HANDLE</code>
<code>XFS_IOC_ATTR_MULTI_BY_HANDLE</code></pre>
<dl>
<dt><code>XFS_IOC_FSSETDM_BY_HANDLE</code></p>
<dd>These are all interfaces that are used to implement various <i>libhandle</i> functions (see <code><a href="/docs/linux/man/3-open_by_handle/">open_by_handle</a></code>(3)). They are all subject to change and should not be called directly by applications.</dl>
<h3>Filesystem Operations</h3>
<p>In order to effect one of the following operations, the pathname and descriptor arguments passed to <code>xfsctl</code>() can be any open file in the XFS filesystem in question.</p>
<dl>
<dt><code>XFS_IOC_FSINUMBERS</code></p>
<dd>This interface is used to extract a list of valid inode numbers from an XFS filesystem. It is intended to be called iteratively, to obtain the entire set of inodes. The information is passed in and out via a structure of type <code>xfs_fsop_bulkreq_t</code> pointed to by the final argument. <code>lastip</code> is a pointer to a variable containing the last inode number returned, initially it should be zero. <code>icount</code> is the size of the array of structures specified by <code>ubuffer</code>. <code>ubuffer</code> is the address of an array of structures, of type <code>xfs_inogrp_t</code>. This structure has the following elements: <code>xi_startino</code> (starting inode number), <code>xi_alloccount</code> (count of bits set in xi_allocmask), and <code>xi_allocmask</code> (mask of allocated inodes in this group). The bitmask is 64 bits long, and the least significant bit corresponds to inode <code>xi_startino.</code> Each bit is set if the corresponding inode is in use. <code>ocount</code> is a pointer to a count of returned values, filled in by the call. An output <code>ocount</code> value of zero means that the inode table has been exhausted.</p>
<dt><code>XFS_IOC_FSBULKSTAT</code></p>
<dd>This interface is used to extract inode information (stat information) &quot;in bulk&quot; from a filesystem. It is intended to be called iteratively, to obtain information about the entire set of inodes in a filesystem. The information is passed in and out via a structure of type <code>xfs_fsop_bulkreq_t</code> pointed to by the final argument. <code>lastip</code> is a pointer to a variable containing the last inode number returned, initially it should be zero. <code>icount</code> indicates the size of the array of structures specified by <code>ubuffer.</code> <code>ubuffer</code> is the address of an array of structures of type <code>xfs_bstat_t</code>. Many of the elements in the structure are the same as for the stat structure. The structure has the following elements: <code>bs_ino</code> (inode number), <code>bs_mode</code> (type and mode), <code>bs_nlink</code> (number of links), <code>bs_uid</code> (user id), <code>bs_gid</code> (group id), <code>bs_rdev</code> (device value), <code>bs_blksize</code> (block size of the filesystem), <code>bs_size</code> (file size in bytes), <code>bs_atime</code> (access time), <code>bs_mtime</code> (modify time), <code>bs_ctime</code> (inode change time), <code>bs_blocks</code> (number of blocks used by the file), <code>bs_xflags</code> (extended flags), <code>bs_extsize</code> (extent size), <code>bs_extents</code> (number of extents), <code>bs_gen</code> (generation count), <code>bs_projid_lo</code> (project id &#8211; low word), <code>bs_projid_hi</code> (project id &#8211; high word, used when projid32bit feature is enabled), <code>bs_dmevmask</code> (DMIG event mask), <code>bs_dmstate</code> (DMIG state information), and <code>bs_aextents</code> (attribute extent count). <code>ocount</code> is a pointer to a count of returned values, filled in by the call. An output <code>ocount</code> value of zero means that the inode table has been exhausted.</p>
<dt><code>XFS_IOC_FSBULKSTAT_SINGLE</code></p>
<dd>This interface is a variant of the <code>XFS_IOC_FSBULKSTAT</code> interface, used to obtain information about a single inode. for an open file in the filesystem of interest. The same structure is used to pass information in and out of the kernel, except no output count parameter is used (should be initialized to zero). An error is returned if the inode number is invalid.  </p>
<pre><code>XFS_IOC_THAW</code>
<code>XFS_IOC_FREEZE</code>
<code>XFS_IOC_GET_RESBLKS</code>
<code>XFS_IOC_SET_RESBLKS</code>
<code>XFS_IOC_FSGROWFSDATA</code>
<code>XFS_IOC_FSGROWFSLOG</code>
<code>XFS_IOC_FSGROWFSRT</code></pre>
<dl>
<dt><code>XFS_IOC_FSCOUNTS</code></p>
<dd>These interfaces are used to implement various filesystem internal operations on XFS filesystems. For <code>XFS_IOC_FSGEOMETRY</code> (get filesystem mkfs time information), the output structure is of type <code>xfs_fsop_geom_t</code>. For <code>XFS_FS_COUNTS</code> (get filesystem dynamic global information), the output structure is of type <code>xfs_fsop_counts_t</code>. The remainder of these operations will not be described further as they are not of general use to applications. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2), <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/8-xfs_info/">xfs_info</a></code>(8). </p>
