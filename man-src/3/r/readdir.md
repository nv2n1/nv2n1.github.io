---
title: "readdir(3)"
name: "readdir"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readdir/"
description: "readdir – read a directory"
---

<p>readdir &#8211; read a directory</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;dirent.h&gt;

struct dirent *readdir(DIR *dirp);</code></pre>
<h2>Description</h2>
<p>The <code>readdir</code>() function returns a pointer to a <i>dirent</i> structure representing the next directory entry in the directory stream pointed to by <i>dirp</i>. It returns NULL on reaching the end of the directory stream or if an error occurred. In the glibc implementation, the <i>dirent</i> structure is defined as follows: </p>
<pre><code>struct dirent {
    ino_t d_ino;             /* Inode number */
    off_t d_off;             /* Not an offset; see below */
    unsigned short d_reclen; /* Length of this record */
    unsigned char d_type;    /* Type of file; not supported
                                by all filesystem types */
    char d_name[256];        /* Null-terminated filename */
};</code></pre>
<p> The only fields in the <i>dirent</i> structure that are mandated by POSIX.1 are <i>d_name</i> and <i>d_ino</i>. The other fields are unstandardized, and not present on all systems; see NOTES below for some further details. The fields of the <i>dirent</i> structure are as follows:</p>
<dl>
<dt><i>d_ino</i></p>
<dd>This is the inode number of the file.</p>
<dt><i>d_off</i></p>
<dd>The value returned in <i>d_off</i> is the same as would be returned by calling <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3) at the current position in the directory stream. Be aware that despite its type and name, the <i>d_off</i> field is seldom any kind of directory offset on modern filesystems. Applications should treat this field as an opaque value, making no assumptions about its contents; see also <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3).</p>
<dt><i>d_reclen</i></p>
<dd>This is the size (in bytes) of the returned record. This may not match the size of the structure definition shown above; see NOTES.</p>
<dt><i>d_type</i></p>
<dd>This field contains a value indicating the file type, making it possible to avoid the expense of calling <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) if further actions depend on the type of the file.</p>
<dd>When a suitable feature test macro is defined (<code>_DEFAULT_SOURCE</code> on glibc versions since 2.19, or <code>_BSD_SOURCE</code> on glibc versions 2.19 and earlier), glibc defines the following macro constants for the value returned in <i>d_type</i>:</p>
<dl>
<dd>
<dl>
<dt><code>DT_BLK</code></p>
<dd>This is a block device.</p>
<dt><code>DT_CHR</code></p>
<dd>This is a character device.</p>
<dt><code>DT_DIR</code></p>
<dd>This is a directory.</p>
<dt><code>DT_FIFO</code></p>
<dd>This is a named pipe (FIFO).</p>
<dt><code>DT_LNK</code></p>
<dd>This is a symbolic link.</p>
<dt><code>DT_REG</code></p>
<dd>This is a regular file.</p>
<dt><code>DT_SOCK</code></p>
<dd>This is a UNIX domain socket.</p>
<dt><code>DT_UNKNOWN</code></p>
<dd>The file type could not be determined.</dl>
</dl>
<dd>Currently, only some filesystems (among them: Btrfs, ext2, ext3, and ext4) have full support for returning the file type in <i>d_type</i>. All applications must properly handle a return of <code>DT_UNKNOWN</code>.</p>
<dt><i>d_name</i></p>
<dd>This field contains the null terminated filename. <i>See NOTES</i>.</dl>
<p> The data returned by <code>readdir</code>() may be overwritten by subsequent calls to <code>readdir</code>() for the same directory stream.</p>
<h2>Return Value</h2>
<p>On success, <code>readdir</code>() returns a pointer to a <i>dirent</i> structure. (This structure may be statically allocated; do not attempt to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) it.) </p>
<p> If the end of the directory stream is reached, NULL is returned and <i>errno</i> is not changed. If an error occurs, NULL is returned and <i>errno</i> is set appropriately. To distinguish end of stream from an error, set <i>errno</i> to zero before calling <code>readdir</code>() and then check the value of <i>errno</i> if NULL is returned.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd>Invalid directory stream descriptor <i>dirp</i>.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>readdir</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:dirstream
</td>
</tr>
</table>
<p> In the current POSIX.1 specification (POSIX.1-2008), <code>readdir</code>() is not required to be thread-safe. However, in modern implementations (including the glibc implementation), concurrent calls to <code>readdir</code>() that specify different directory streams are thread-safe. In cases where multiple threads must read from the same directory stream, using <code>readdir</code>() with external synchronization is still preferable to the use of the deprecated <code><a href="/docs/linux/man/3-readdir_r/">readdir_r</a></code>(3) function. It is expected that a future version of POSIX.1 will require that <code>readdir</code>() be thread-safe when concurrently employed on different directory streams.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>Notes</h2>
<p>A directory stream is opened using <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3). </p>
<p> The order in which filenames are read by successive calls to <code>readdir</code>() depends on the filesystem implementation; it is unlikely that the names will be sorted in any fashion. </p>
<p> Only the fields <i>d_name</i> and (as an XSI extension) <i>d_ino</i> are specified in POSIX.1. Other than Linux, the <i>d_type</i> field is available mainly only on BSD systems. The remaining fields are available on many, but not all systems. Under glibc, programs can check for the availability of the fields not defined in POSIX.1 by testing whether the macros <code>_DIRENT_HAVE_D_NAMLEN</code>, <code>_DIRENT_HAVE_D_RECLEN</code>, <code>_DIRENT_HAVE_D_OFF</code>, or <code>_DIRENT_HAVE_D_TYPE</code> are defined.</p>
<h3>The d_name field</h3>
<p>The <i>dirent</i> structure definition shown above is taken from the glibc headers, and shows the <i>d_name</i> field with a fixed size. </p>
<p> <i>Warning</i>: applications should avoid any dependence on the size of the <i>d_name</i> field. POSIX defines it as <i>char d_name[],</i> a character array of unspecified size, with at most <code>NAME_MAX</code> characters preceding the terminating null byte (&#8216;
