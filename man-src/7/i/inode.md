---
title: "inode(7)"
name: "inode"
section: "7"
letter: "i"
url: "/docs/linux/man/7-inode/"
description: "inode – file inode information"
---

<p>inode &#8211; file inode information</p>
<h2>Description</h2>
<p>Each file has an inode containing metadata about the file. An application can retrieve this metadata using <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) (or related calls), which returns a <i>stat</i> structure, or <code><a href="/docs/linux/man/2-statx/">statx</a></code>(2), which returns a <i>statx</i> structure. The following is a list of the information typically found in, or associated with, the file inode, with the names of the corresponding structure fields returned by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) and <code><a href="/docs/linux/man/2-statx/">statx</a></code>(2):</p>
<dl>
<dt>Device where inode resides</p>
<dd><i>stat.st_dev</i>; <i>statx.stx_dev_minor</i> and <i>statx.stx_dev_major</i></p>
<dd>Each inode (as well as the associated file) resides in a filesystem that is hosted on a device. That device is identified by the combination of its major ID (which identifies the general class of device) and minor ID (which identifies a specific instance in the general class).</p>
<dt>Inode number</p>
<dd><i>stat.st_ino</i>; <i>statx.stx_ino</i></p>
<dd>Each file in a filesystem has a unique inode number. Inode numbers are guaranteed to be unique only within a filesystem (i.e., the same inode numbers may be used by different filesystems, which is the reason that hard links may not cross filesystem boundaries). This field contains the file&#8217;s inode number.</p>
<dt>File type and mode</p>
<dd><i>stat.st_mode</i>; <i>statx.stx_mode</i></p>
<dd>See the discussion of file type and mode, below.</p>
<dt>Link count</p>
<dd><i>stat.st_nlink</i>; <i>statx.stx_nlink</i></p>
<dd>This field contains the number of hard links to the file. Additional links to an existing file are created using <code><a href="/docs/linux/man/2-link/">link</a></code>(2).</p>
<dt>User ID</p>
<dd><i>st_uid</i> <i>stat.st_uid</i>; <i>statx.stx_uid</i></p>
<dd>This field records the user ID of the owner of the file. For newly created files, the file user ID is the effective user ID of the creating process. The user ID of a file can be changed using <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2).</p>
<dt>Group ID</p>
<dd><i>stat.st_gid</i>; <i>statx.stx_gid</i></p>
<dd>The inode records the ID of the group owner of the file. For newly created files, the file group ID is either the group ID of the parent directory or the effective group ID of the creating process, depending on whether or not the set-group-ID bit is set on the parent directory (see below). The group ID of a file can be changed using <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2).</p>
<dt>Device represented by this inode</p>
<dd><i>stat.st_rdev</i>; <i>statx.stx_rdev_minor</i> and <i>statx.stx_rdev_major</i></p>
<dd>If this file (inode) represents a device, then the inode records the major and minor ID of that device.</p>
<dt>File size</p>
<dd><i>stat.st_size</i>; <i>statx.stx_size</i></p>
<dd>This field gives the size of the file (if it is a regular file or a symbolic link) in bytes. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.</p>
<dt>Preferred block size for I/O</p>
<dd><i>stat.st_blksize</i>; <i>statx.stx_blksize</i></p>
<dd>This field gives the &quot;preferred&quot; blocksize for efficient filesystem I/O. (Writing to a file in smaller chunks may cause an inefficient read-modify-rewrite.)</p>
<dt>Number of blocks allocated to the file</p>
<dd><i>stat.st_blocks</i>; <i>statx.stx_size</i></p>
<dd>This field indicates the number of blocks allocated to the file, 512-byte units, (This may be smaller than <i>st_size</i>/512 when the file has holes.)</p>
<dd>The POSIX.1 standard notes that the unit for the <i>st_blocks</i> member of the <i>stat</i> structure is not defined by the standard. On many implementations it is 512 bytes; on a few systems, a different unit is used, such as 1024. Furthermore, the unit may differ on a per-filesystem basis.</p>
<dt>Last access timestamp (atime)</p>
<dd><i>stat.st_atime</i>; <i>statx.stx_atime</i></p>
<dd>This is the file&#8217;s last access timestamp. It is changed by file accesses, for example, by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), and <code><a href="/docs/linux/man/2-read/">read</a></code>(2) (of more than zero bytes). Other interfaces, such as <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), may or may not update the atime timestamp</p>
<dd>Some filesystem types allow mounting in such a way that file and/or directory accesses do not cause an update of the atime timestamp. (See <i>noatime</i>, <i>nodiratime</i>, and <i>relatime</i> in <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), and related information in <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2).) In addition, the atime timestamp is not updated if a file is opened with the <code>O_NOATIME</code> flag; see <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt>File creation (birth) timestamp (btime)</p>
<dd>(not returned in the <i>stat</i> structure); <i>statx.stx_btime</i></p>
<dd>The file&#8217;s creation timestamp. This is set on file creation and not changed subsequently.</p>
<dd>The btime timestamp was not historically present on UNIX systems and is not currently supported by most Linux filesystems.</p>
<dt>Last modification timestamp (mtime)</p>
<dd><i>stat.st_mtime</i>; <i>statx.stx_mtime</i></p>
<dd>This is the file&#8217;s last modification timestamp. It is changed by file modifications, for example, by <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) (of more than zero bytes). Moreover, the mtime timestamp of a directory is changed by the creation or deletion of files in that directory. The mtime timestamp is <i>not</i> changed for changes in owner, group, hard link count, or mode.</p>
<dt>Last status change timestamp (ctime)</p>
<dd><i>stat.st_ctime</i>; <i>statx.stx_ctime</i></p>
<dd>This is the file&#8217;s last status change timestamp. It is changed by writing or by setting inode information (i.e., owner, group, link count, mode, etc.).</dl>
<p> The timestamp fields report time measured with a zero point at the <i>Epoch</i>, 1970-01-02 00:00:00 +0000, UTC (see <code><a href="/docs/linux/man/7-time/">time</a></code>(7)). Nanosecond timestamps are supported on XFS, JFS, Btrfs, and ext4 (since Linux 2.6.23). Nanosecond timestamps are not supported in ext2, ext3, and Reiserfs. In order to return timestamps with nanosecond precision, the timestamp fields in the <i>stat</i> and <i>statx</i> structures are defined as structures that include a nanosecond component. See <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) and <code><a href="/docs/linux/man/2-statx/">statx</a></code>(2) for details. On filesystems that do not support subsecond timestamps, the nanosecond fields in the <i>stat</i> and <i>statx</i> structures are returned with the value 0.</p>
<h3>The file type and mode</h3>
<p>The <i>stat.st_mode</i> field (for <code><a href="/docs/linux/man/2-statx/">statx</a></code>(2), the <i>statx.stx_mode</i> field) contains the file type and mode. POSIX refers to the <i>stat.st_mode</i> bits corresponding to the mask <code>S_IFMT</code> (see below) as the <i>file type</i>, the 12 bits corresponding to the mask 07777 as the <i>file mode bits</i> and the least significant 9 bits (0777) as the <i>file permission bits</i>. The following mask values are defined for the file type: </p>
<table>
<tr VALIGN=top>
<td><code>S_IFMT</code></td>
<td>0170000</td>
<td>bit mask for the file type bit field
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IFSOCK</code></td>
<td>0140000</td>
<td>socket
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IFLNK</code></td>
<td>0120000</td>
<td>symbolic link
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IFREG</code></td>
<td>0100000</td>
<td>regular file
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IFBLK</code></td>
<td>0060000</td>
<td>block device
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IFDIR</code></td>
<td>0040000</td>
<td>directory
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IFCHR</code></td>
<td>0020000</td>
<td>character device
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IFIFO</code></td>
<td>0010000</td>
<td>FIFO
</td>
</tr>
</table>
<p> Thus, to test for a regular file (for example), one could write: </p>
<pre><code>stat(pathname, &amp;sb);
if ((sb.st_mode &amp; S_IFMT) == S_IFREG) {
    /* Handle regular file */
}</code></pre>
<p> Because tests of the above form are common, additional macros are defined by POSIX to allow the test of the file type in <i>st_mode</i> to be written more concisely:</p>
<dl>
<dd>
<dl>
<dt><code>S_ISREG</code>(m)</p>
<dd>is it a regular file?</p>
<dt><code>S_ISDIR</code>(m)</p>
<dd>directory?</p>
<dt><code>S_ISCHR</code>(m)</p>
<dd>character device?</p>
<dt><code>S_ISBLK</code>(m)</p>
<dd>block device?</p>
<dt><code>S_ISFIFO</code>(m)</p>
<dd>FIFO (named pipe)?</p>
<dt><code>S_ISLNK</code>(m)</p>
<dd>symbolic link? (Not in POSIX.1-1996.)</p>
<dt><code>S_ISSOCK</code>(m)</p>
<dd>socket? (Not in POSIX.1-1996.)</dl>
</dl>
<p> The preceding code snippet could thus be rewritten as: </p>
<pre><code>stat(pathname, &amp;sb);
if (S_ISREG(sb.st_mode)) {
    /* Handle regular file */
}</code></pre>
<p> The definitions of most of the above file type test macros are provided if any of the following feature test macros is defined: <code>_BSD_SOURCE</code> (in glibc 2.19 and earlier), <code>_SVID_SOURCE</code> (in glibc 2.19 and earlier), or <code>_DEFAULT_SOURCE</code> (in glibc 2.20 and later). In addition, definitions of all of the above macros except <code>S_IFSOCK</code> and <code>S_ISSOCK</code>() are provided if <code>_XOPEN_SOURCE</code> is defined. The definition of <code>S_IFSOCK</code> can also be exposed either by defining <code>_XOPEN_SOURCE</code> with a value of 500 or greater or (since glibc 2.24) by defining both <code>_XOPEN_SOURCE</code> and <code>_XOPEN_SOURCE_EXTENDED</code>. The definition of <code>S_ISSOCK</code>() is exposed if any of the following feature test macros is defined: <code>_BSD_SOURCE</code> (in glibc 2.19 and earlier), <code>_DEFAULT_SOURCE</code> (in glibc 2.20 and later), <code>_XOPEN_SOURCE</code> with a value of 500 or greater, <code>_POSIX_C_SOURCE</code> with a value of 200112L or greater, or (since glibc 2.24) by defining both <code>_XOPEN_SOURCE</code> and <code>_XOPEN_SOURCE_EXTENDED</code>. The following mask values are defined for the file mode component of the <i>st_mode</i> field: </p>
<table>
<tr VALIGN=top>
<td><code>S_ISUID</code></td>
<td> 04000</td>
<td>set-user-ID bit (see <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2))
</td>
</tr>
<tr VALIGN=top>
<td><code>S_ISGID</code></td>
<td> 02000</td>
<td>set-group-ID bit (see below)
</td>
</tr>
<tr VALIGN=top>
<td><code>S_ISVTX</code></td>
<td> 01000</td>
<td>sticky bit (see below)
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IRWXU</code></td>
<td> 00700</td>
<td>owner has read, write, and execute permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IRUSR</code></td>
<td> 00400</td>
<td>owner has read permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IWUSR</code></td>
<td> 00200</td>
<td>owner has write permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IXUSR</code></td>
<td> 00100</td>
<td>owner has execute permission
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IRWXG</code></td>
<td> 00070</td>
<td>group has read, write, and execute permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IRGRP</code></td>
<td> 00040</td>
<td>group has read permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IWGRP</code></td>
<td> 00020</td>
<td>group has write permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IXGRP</code></td>
<td> 00010</td>
<td>group has execute permission
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IRWXO</code></td>
<td> 00007</td>
<td> others (not in group) have read, write, and execute permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IROTH</code></td>
<td> 00004</td>
<td>others have read permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IWOTH</code></td>
<td> 00002</td>
<td>others have write permission
</td>
</tr>
<tr VALIGN=top>
<td><code>S_IXOTH</code></td>
<td> 00001</td>
<td>others have execute permission
</td>
</tr>
</table>
<p> The set-group-ID bit (<code>S_ISGID</code>) has several special uses. For a directory, it indicates that BSD semantics are to be used for that directory: files created there inherit their group ID from the directory, not from the effective group ID of the creating process, and directories created there will also get the <code>S_ISGID</code> bit set. For an executable file, the set-group-ID bit causes the effective group ID of a process that executes the file to change as described in <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). For a file that does not have the group execution bit (<code>S_IXGRP</code>) set, the set-group-ID bit indicates mandatory file/record locking. The sticky bit (<code>S_ISVTX</code>) on a directory means that a file in that directory can be renamed or deleted only by the owner of the file, by the owner of the directory, and by a privileged process.</p>
<h2>Conforming To</h2>
<p>If you need to obtain the definition of the <i>blkcnt_t</i> or <i>blksize_t</i> types from <i>&lt;sys/stat.h&gt;</i>, then define <code>_XOPEN_SOURCE</code> with the value 500 or greater (before including <i>any</i> header files). </p>
<p> POSIX.1-1990 did not describe the <code>S_IFMT</code>, <code>S_IFSOCK</code>, <code>S_IFLNK</code>, <code>S_IFREG</code>, <code>S_IFBLK</code>, <code>S_IFDIR</code>, <code>S_IFCHR</code>, <code>S_IFIFO</code>, <code>S_ISVTX</code> constants, but instead specified the use of the macros <code>S_ISDIR</code>(), and so on. The <code>S_IF*</code> constants are present in POSIX.1-2001 and later. </p>
<p> The <code>S_ISLNK</code>() and <code>S_ISSOCK</code>() macros were not in POSIX.1-1996, but both are present in POSIX.1-2001; the former is from SVID 4, the latter from SUSv2. </p>
<p> UNIX V7 (and later systems) had <code>S_IREAD</code>, <code>S_IWRITE</code>, <code>S_IEXEC</code>, where POSIX prescribes the synonyms <code>S_IRUSR</code>, <code>S_IWUSR</code>, <code>S_IXUSR</code>.</p>
<h2>Notes</h2>
<p>For pseudofiles that are autogenerated by the kernel, the file size (<i>stat.st_size</i>; <i>statx.stx_size</i>) reported by the kernel is not accurate. For example, the value 0 is returned for many files under the <i>/proc</i> directory, while various files under <i>/sys</i> report a size of 4096 bytes, even though the file content is smaller. For such files, one should simply try to read as many bytes as possible (and append &#8216;
