---
title: "statx(2)"
name: "statx"
section: "2"
letter: "s"
url: "/docs/linux/man/2-statx/"
description: "statx – get file status (extended)"
---

<h2 class="name">NAME</h2>
<p> statx &#8211; get file status (extended) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
int statx(int dirfd, const char *pathname, int flags,
          unsigned int mask, struct statx *statxbuf);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function returns information about a file, storing it in the buffer pointed to by <i>statxbuf</i>. The returned buffer is a structure of the following type: </p>
<p> struct statx {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mask of bits indicating<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;filled fields&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_blksize;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Block size for filesystem I/O&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 stx_attributes;&nbsp;<wbr>&nbsp;/*&nbsp;Extra file attribute indicators&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_nlink;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of hard links&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User ID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Group ID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 stx_mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File type and mode&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 stx_ino;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inode number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 stx_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Total size in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 stx_blocks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of 512B blocks allocated&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 stx_attributes_mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mask to show what&#8217;s supported<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in stx_attributes&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The following fields are file timestamps&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct statx_timestamp stx_atime;&nbsp;<wbr>&nbsp;/*&nbsp;Last access&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct statx_timestamp stx_btime;&nbsp;<wbr>&nbsp;/*&nbsp;Creation&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct statx_timestamp stx_ctime;&nbsp;<wbr>&nbsp;/*&nbsp;Last status change&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct statx_timestamp stx_mtime;&nbsp;<wbr>&nbsp;/*&nbsp;Last modification&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If this file represents a device, then the next two<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fields contain the ID of the device&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_rdev_major;&nbsp;<wbr>&nbsp;/*&nbsp;Major ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_rdev_minor;&nbsp;<wbr>&nbsp;/*&nbsp;Minor ID&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The next two fields contain the ID of the device<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;containing the filesystem where the file resides&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_dev_major;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Major ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 stx_dev_minor;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Minor ID&nbsp;*/ }; </p>
<p> The file timestamps are structures of the following type: </p>
<p> struct statx_timestamp {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64 tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Seconds since the Epoch&nbsp;(UNIX time)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Nanoseconds since tv_sec&nbsp;*/ }; </p>
<p> (Note that reserved space and padding is omitted.)</p>
<h3>Invoking <code>statx</code>():</h3>
<p> To access a file&#8217;s status, no permissions are required on the file itself, but in the case of <code>statx</code>() with a pathname, execute (search) permission is required on all of the directories in <i>pathname</i> that lead to the file. </p>
<p> <code>statx</code>() uses <i>pathname</i>, <i>dirfd</i>, and <i>flags</i> to identify the target file in one of the following ways:</p>
<dl>
<dt>An absolute pathname</p>
<dd> If <i>pathname</i> begins with a slash, then it is an absolute pathname that identifies the target file. In this case, <i>dirfd</i> is ignored.</p>
<dt>A relative pathname</p>
<dd> If <i>pathname</i> is a string that begins with a character other than a slash and <i>dirfd</i> is <code>AT_FDCWD</code>, then <i>pathname</i> is a relative pathname that is interpreted relative to the process&#8217;s current working directory.</p>
<dt>A directory-relative pathname</p>
<dd> If <i>pathname</i> is a string that begins with a character other than a slash and <i>dirfd</i> is a file descriptor that refers to a directory, then <i>pathname</i> is a relative pathname that is interpreted relative to the directory referred to by <i>dirfd</i>.</p>
<dt>By file descriptor</p>
<dd> If <i>pathname</i> is an empty string and the <code>AT_EMPTY_PATH</code> flag is specified in <i>flags</i> (see below), then the target file is the one referred to by the file descriptor <i>dirfd</i>.</dl>
<p> <i>flags</i> can be used to influence a pathname-based lookup. A value for <i>flags</i> is constructed by ORing together zero or more of the following constants:</p>
<dl>
<dt><code>AT_EMPTY_PATH</code></p>
<dd> If <i>pathname</i> is an empty string, operate on the file referred to by <i>dirfd</i> (which may have been obtained using the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_PATH</code> flag). In this case, <i>dirfd</i> can refer to any type of file, not just a directory.</p>
<dt>
<dd> If <i>dirfd</i> is <code>AT_FDCWD</code>, the call operates on the current working directory.</p>
<dt>
<dd> This flag is Linux-specific; define <code>_GNU_SOURCE</code> to obtain its definition.</p>
<dt><code>AT_NO_AUTOMOUNT</code></p>
<dd> Don&#8217;t automount the terminal (&quot;basename&quot;) component of <i>pathname</i> if it is a directory that is an automount point. This allows the caller to gather attributes of an automount point (rather than the location it would mount). This flag can be used in tools that scan directories to prevent mass-automounting of a directory of automount points. The <code>AT_NO_AUTOMOUNT</code> flag has no effect if the mount point has already been mounted over. This flag is Linux-specific; define <code>_GNU_SOURCE</code> to obtain its definition.</p>
<dt><code>AT_SYMLINK_NOFOLLOW</code></p>
<dd> If <i>pathname</i> is a symbolic link, do not dereference it: instead return information about the link itself, like <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2).</dl>
<p> <i>flags</i> can also be used to control what sort of synchronization the kernel will do when querying a file on a remote filesystem. This is done by ORing in one of the following values:</p>
<dl>
<dt><code>AT_STATX_SYNC_AS_STAT</code></p>
<dd> Do whatever <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) does. This is the default and is very much filesystem-specific.</p>
<dt><code>AT_STATX_FORCE_SYNC</code></p>
<dd> Force the attributes to be synchronized with the server. This may require that a network filesystem perform a data writeback to get the timestamps correct.</p>
<dt><code>AT_STATX_DONT_SYNC</code></p>
<dd> Don&#8217;t synchronize anything, but rather just take whatever the system has cached if possible. This may mean that the information returned is approximate, but, on a network filesystem, it may not involve a round trip to the server &#8211; even if no lease is held.</dl>
<p> The <i>mask</i> argument to <code>statx</code>() is used to tell the kernel which fields the caller is interested in. <i>mask</i> is an ORed combination of the following constants: </p>
<table>
<tr VALIGN=top>
<td><code>STATX_TYPE</code></td>
<td>Want stx_mode &amp; S_IFMT
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_MODE</code></td>
<td>Want stx_mode &amp; ~S_IFMT
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_NLINK</code></td>
<td>Want stx_nlink
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_UID</code></td>
<td>Want stx_uid
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_GID</code></td>
<td>Want stx_gid
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_ATIME</code></td>
<td>Want stx_atime
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_MTIME</code></td>
<td>Want stx_mtime
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_CTIME</code></td>
<td>Want stx_ctime
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_INO</code></td>
<td>Want stx_ino
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_SIZE</code></td>
<td>Want stx_size
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_BLOCKS</code></td>
<td>Want stx_blocks
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_BASIC_STATS</code></td>
<td>[All of the above]
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_BTIME</code></td>
<td>Want stx_btime
</td>
</tr>
<tr VALIGN=top>
<td><code>STATX_ALL</code></td>
<td>[All currently available fields]
</td>
</tr>
</table>
<p> Note that, in general, the kernel does <i>not</i> reject values in <i>mask</i> other than the above. (For an exception, see <code>EINVAL</code> in errors.) Instead, it simply informs the caller which values are supported by this kernel and filesystem via the <i>statx.stx_mask</i> field. Therefore, <i>do not</i> simply set <i>mask</i> to <code>UINT_MAX</code> (all bits set), as one or more bits may, in the future, be used to specify an extension to the buffer.</p>
<h3>The returned information</h3>
<p> The status information for the target file is returned in the <i>statx</i> structure pointed to by <i>statxbuf</i>. Included in this is <i>stx_mask</i> which indicates what other information has been returned. <i>stx_mask</i> has the same format as the <i>mask</i> argument and bits are set in it to indicate which fields have been filled in. </p>
<p> It should be noted that the kernel may return fields that weren&#8217;t requested and may fail to return fields that were requested, depending on what the backing filesystem supports. (Fields that are given values despite being unrequested can just be ignored.) In either case, <i>stx_mask</i> will not be equal <i>mask</i>. </p>
<p> If a filesystem does not support a field or if it has an unrepresentable value (for instance, a file with an exotic type), then the mask bit corresponding to that field will be cleared in <i>stx_mask</i> even if the user asked for it and a dummy value will be filled in for compatibility purposes if one is available (e.g., a dummy UID and GID may be specified to mount under some circumstances). </p>
<p> A filesystem may also fill in fields that the caller didn&#8217;t ask for if it has values for them available and the information is available at no extra cost. If this happens, the corresponding bits will be set in <i>stx_mask</i>. </p>
<p> <i>Note</i>: for performance and simplicity reasons, different fields in the <i>statx</i> structure may contain state information from different moments during the execution of the system call. For example, if <i>stx_mode</i> or <i>stx_uid</i> is changed by another process by calling <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2) or <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code>stat</code>() might return the old <i>stx_mode</i> together with the new <i>stx_uid</i>, or the old <i>stx_uid</i> together with the new <i>stx_mode</i>. </p>
<p> Apart from <i>stx_mask</i> (which is described above), the fields in the <i>statx</i> structure are:</p>
<dl>
<dt><i>stx_blksize</i></p>
<dd> The &quot;preferred&quot; block size for efficient filesystem I/O. (Writing to a file in smaller chunks may cause an inefficient read-modify-rewrite.)</p>
<dt><i>stx_attributes</i></p>
<dd> Further status information about the file (see below for more information).</p>
<dt><i>stx_nlink</i></p>
<dd> The number of hard links on a file.</p>
<dt><i>stx_uid</i></p>
<dd> This field contains the user ID of the owner of the file.</p>
<dt><i>stx_gid</i></p>
<dd> This field contains the ID of the group owner of the file.</p>
<dt><i>stx_mode</i></p>
<dd> The file type and mode. See <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7) for details.</p>
<dt><i>stx_ino</i></p>
<dd> The inode number of the file.</p>
<dt><i>stx_size</i></p>
<dd> The size of the file (if it is a regular file or a symbolic link) in bytes. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.</p>
<dt><i>stx_blocks</i></p>
<dd> The number of blocks allocated to the file on the medium, in 512-byte units. (This may be smaller than <i>stx_size</i>/512 when the file has holes.)</p>
<dt><i>stx_attributes_mask</i></p>
<dd> A mask indicating which bits in <i>stx_attributes</i> are supported by the VFS and the filesystem.</p>
<dt><i>stx_atime</i></p>
<dd> The file&#8217;s last access timestamp.</p>
<dt><i>stx_btime</i></p>
<dd> The file&#8217;s creation timestamp.</p>
<dt><i>stx_ctime</i></p>
<dd> The file&#8217;s last status change timestamp.</p>
<dt><i>stx_mtime</i></p>
<dd> The file&#8217;s last modification timestamp.</p>
<dt><i>stx_dev_major</i> and <i>stx_dev_minor</i></p>
<dd> The device on which this file (inode) resides.</p>
<dt><i>stx_rdev_major</i> and <i>stx_rdev_minor</i></p>
<dd> The device that this file (inode) represents if the file is of block or character device type.</dl>
<p> For further information on the above fields, see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7).</p>
<h3>File attributes</h3>
<p> The <i>stx_attributes</i> field contains a set of ORed flags that indicate additional attributes of the file. Note that any attribute that is not indicated as supported by <i>stx_attributes_mask</i> has no usable value here. The bits in <i>stx_attributes_mask</i> correspond bit-by-bit to <i>stx_attributes</i>. </p>
<p> The flags are as follows:</p>
<dl>
<dt><code>STATX_ATTR_COMPRESSED</code></p>
<dd> The file is compressed by the filesystem and may take extra resources to access.</p>
<dt><code>STATX_ATTR_IMMUTABLE</code></p>
<dd> The file cannot be modified: it cannot be deleted or renamed, no hard links can be created to this file and no data can be written to it. See <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1).</p>
<dt><code>STATX_ATTR_APPEND</code></p>
<dd> The file can only be opened in append mode for writing. Random access writing is not permitted. See <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1).</p>
<dt><code>STATX_ATTR_NODUMP</code></p>
<dd> File is not a candidate for backup when a backup program such as <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8) is run. See <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1).</p>
<dt><code>STATX_ATTR_ENCRYPTED</code></p>
<dd> A key is required for the file to be encrypted by the filesystem.</p>
<dt><code>STATX_ATTR_VERITY</code> (since Linux 5.5)</p>
<dd> The file has fs-verity enabled. It cannot be written to, and all reads from it will be verified against a cryptographic hash that covers the entire file (e.g., via a Merkle tree).</p>
<dt><code>STATX_ATTR_DAX</code> (since Linux 5.8)</p>
<dd> The file is in the DAX (cpu direct access) state. DAX state attempts to minimize software cache effects for both I/O and memory mappings of this file. It requires a file system which has been configured to support DAX.</p>
<dt>
<dd> DAX generally assumes all accesses are via CPU load / store instructions which can minimize overhead for small accesses, but may adversely affect CPU utilization for large transfers.</p>
<dt>
<dd> File I/O is done directly to/from user-space buffers and memory mapped I/O may be performed with direct memory mappings that bypass the kernel page cache.</p>
<dt>
<dd> While the DAX property tends to result in data being transferred synchronously, it does not give the same guarantees as the <code>O_SYNC</code> flag (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)), where data and the necessary metadata are transferred together.</p>
<dt>
<dd> A DAX file may support being mapped with the <code>MAP_SYNC</code> flag, which enables a program to use CPU cache flush instructions to persist CPU store operations without an explicit <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2). See <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for more information.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied for one of the directories in the path prefix of <i>pathname</i>. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> or <i>statxbuf</i> is NULL or points to a location outside the process&#8217;s accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flag specified in <i>flags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> Reserved flag specified in <i>mask</i>. (Currently, there is one such flag, designated by the constant <code>STATX__RESERVED</code>, with the value 0x80000000U.)</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links encountered while traversing the pathname.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> A component of <i>pathname</i> does not exist, or <i>pathname</i> is an empty string and <code>AT_EMPTY_PATH</code> was not specified in <i>flags</i>.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory (i.e., kernel memory).</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of the path prefix of <i>pathname</i> is not a directory or <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>statx</code>() was added to Linux in kernel 4.11; library support was added in glibc 2.28.</p>
<h2>CONFORMING TO</h2>
<p> <code>statx</code>() is Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-stat/">stat</a></code>(1), <code><a href="/docs/linux/man/2-access/">access</a></code>(2), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
<dt><a href="#lbAH">RETURN VALUE</a></p>
<dd>
<dt><a href="#lbAI">ERRORS</a></p>
<dd>
<dt><a href="#lbAJ">VERSIONS</a></p>
<dd>
<dt><a href="#lbAK">CONFORMING TO</a></p>
<dd>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAM">COLOPHON</a></p>
<dd></dl>
