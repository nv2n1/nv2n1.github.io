---
title: "archivemount(1)"
name: "archivemount"
section: "1"
letter: "a"
url: "/docs/linux/man/1-archivemount/"
description: "archivemount – mounts an archive for access as a file system"
---

<h2>NAME</h2>
<p> archivemount &#8211; mounts an archive for access as a file system</p>
<h2>SYNOPSIS</h2>
<p> <code>archivemount</code> [<code>-hVdfs</code>] [<code>-o</code> <i>options</i>] <i>archivepath</i> <i>mountpoint</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>archivemount</code> command mounts the file tree contained in the archive <i>archivepath</i> on the directory <i>mountpoint</i>. The archive&#8217;s contents can subsequently be accessed inside <i>mountpoint</i> as a file system. The <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command performs the corresponding unmount operation. </p>
<p> <code>archivemount</code> is known to work under both linux and Mac OS X (via MacFUSE). </p>
<h2>EXAMPLE SESSION</h2>
<p> Consider the gzipped tar archive &#8220;files.tgz&#8221; containing files &#8220;file1&#8221; and &#8220;file2&#8221;, and an empty directory &#8220;mnt&#8221;. </p>
<pre><code>
$ ls
        files.tgz mnt /
    $ archivemount files.tgz mnt
        $ ls mnt
            file1 file2
                [... Perform desired read / write operations on the archive via mnt / ...] $ umount mnt
                    [... Any changes are saved to the archive...]
</code></pre>
<h2>ARCHIVE FORMATS</h2>
<p> Archive format support is provided by the <code>libarchive</code>(3) library. Read operations are supported for:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> old-style tar archives,</dd>
<dt>&bull;</dt>
<dd> most variants of the POSIX &#8220;ustar&#8221; format,</dd>
<dt>&bull;</dt>
<dd> the POSIX &#8220;pax interchange&#8221; format,</dd>
<dt>&bull;</dt>
<dd> GNU-format tar archives,</dd>
<dt>&bull;</dt>
<dd> most common cpio archive formats,</dd>
<dt>&bull;</dt>
<dd> ISO9660 CD images (with or without RockRidge extensions),</dd>
<dt>&bull;</dt>
<dd> Zip archives.</dd></dl>
</dl>
<p> Archives compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), or <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1) are automatically detected and transparently decompressed. </p>
<p> The following formats can be written:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> POSIX-standard &#8220;ustar&#8221; archives,</dd>
<dt>&bull;</dt>
<dd> POSIX &#8220;pax interchange format&#8221; archives,</dd>
<dt>&bull;</dt>
<dd> POSIX octet-oriented cpio archives,</dd>
<dt>&bull;</dt>
<dd> two different variants of shar archives.</dd></dl>
</dl>
<p> Before writing, the original archive is renamed with a &#8220;.orig&#8221; extension appended to it. More detail about the read/write support can be found in the <code>libarchive</code>(3) documentation. </p>
<h2>OPTIONS</h2>
<p> <code>archivemount</code> is built upon the FUSE (Filesystem in Userspace) library, and the complete set of available options depends upon the specific FUSE implementation. Execute <code>archivemount -h</code> to retrieve a definitive list. </p>
<h3>general options</h3>
<dl>
<dt><code>-o</code> opt,[opt&#8230;]</dt>
<dd> mount options</dd>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> print help</dd>
<dt><code>-V</code> <code>&#8211;version</code></dt>
<dd> print version </dd>
</dl>
<h3>archivemount mount options</h3>
<dl>
<dt><code>-o</code> readonly</dt>
<dd> disable write support</dd>
<dt><code>-o</code> nobackup</dt>
<dd> remove archive file backups</dd>
<dt><code>-o</code> subtree=&lt;regex&gt;</dt>
<dd> mount only subtree of archive, strip subtree part from path </dd>
</dl>
<h3>FUSE mount options</h3>
<p> These options are available to linux users using standard FUSE. </p>
<dl>
<dt><code>-d</code> <code>-o</code> debug</dt>
<dd> enable debug output (implies <code>-f</code>)</dd>
<dt><code>-f</code></dt>
<dd> foreground operation</dd>
<dt><code>-s</code></dt>
<dd> disable multi-threaded operation</dd>
<dt><code>-o</code> allow_other</dt>
<dd> allow access to other users</dd>
<dt><code>-o</code> allow_root</dt>
<dd> allow access to root</dd>
<dt><code>-o</code> nonempty</dt>
<dd> allow mounts over non-empty file/dir</dd>
<dt> <code>-o</code> default_permissions</dt>
<dd>enable permission checking by kernel</dd>
<dt><code>-o</code> fsname=NAME</dt>
<dd> set filesystem name</dd>
<dt><code>-o</code> subtype=NAME</dt>
<dd> set filesystem type</dd>
<dt><code>-o</code> large_read</dt>
<dd> issue large read requests (2.4 only)</dd>
<dt><code>-o</code> max_read=N</dt>
<dd> set maximum size of read requests</dd>
<dt><code>-o</code> hard_remove</dt>
<dd> immediate removal (don&#8217;t hide files)</dd>
<dt><code>-o</code> use_ino</dt>
<dd> let filesystem set inode numbers</dd>
<dt><code>-o</code> readdir_ino</dt>
<dd> try to fill in d_ino in readdir</dd>
<dt><code>-o</code> direct_io</dt>
<dd> use direct I/O</dd>
<dt><code>-o</code> kernel_cache</dt>
<dd> cache files in kernel</dd>
<dt><code>-o</code> [no]auto_cache</dt>
<dd> enable caching based on modification times</dd>
<dt><code>-o</code> umask=M</dt>
<dd> set file permissions (octal)</dd>
<dt><code>-o</code> uid=N</dt>
<dd> set file owner</dd>
<dt><code>-o</code> gid=N</dt>
<dd> set file group</dd>
<dt><code>-o</code> entry_timeout=T</dt>
<dd> cache timeout for names (1.0s)</dd>
<dt><code>-o</code> negative_timeout=T</dt>
<dd> cache timeout for deleted names (0.0s)</dd>
<dt><code>-o</code> attr_timeout=T</dt>
<dd> cache timeout for attributes (1.0s)</dd>
<dt><code>-o</code> ac_attr_timeout=T</dt>
<dd> auto cache timeout for attributes (attr_timeout)</dd>
<dt><code>-o</code> intr</dt>
<dd> allow requests to be interrupted</dd>
<dt><code>-o</code> intr_signal=NUM</dt>
<dd> signal to send on interrupt (10)</dd>
<dt><code>-o</code> modules=M1[:M2&#8230;]</dt>
<dd> names of modules to push onto filesystem stack</dd>
<dt><code>-o</code> max_write=N</dt>
<dd> set maximum size of write requests</dd>
<dt><code>-o</code> max_readahead=N</dt>
<dd> set maximum readahead</dd>
<dt><code>-o</code> async_read</dt>
<dd> perform reads asynchronously (default)</dd>
<dt><code>-o</code> sync_read</dt>
<dd> perform reads synchronously</dd>
<dt><code>-o</code> atomic_o_trunc</dt>
<dd> enable atomic open+truncate support </dd>
</dl>
<h3>MacFUSE mount options</h3>
<p> These options are available to Mac users using MacFUSE. </p>
<dl>
<dt><code>-o</code> allow_other</dt>
<dd> allow access to others besides the user who mounted the file system</dd>
<dt><code>-o</code> allow_recursion</dt>
<dd> allow a mount point that itself resides on a MacFUSE volume (by default, such mounting is disallowed)</dd>
<dt><code>-o</code> allow_root</dt>
<dd> allow access to root (can&#8217;t be used with allow_other)</dd>
<dt><code>-o</code> auto_xattr</dt>
<dd> handle extended attributes entirely through ._ files</dd>
<dt><code>-o</code> blocksize=SIZE</dt>
<dd> specify block size in bytes of &quot;storage&quot;</dd>
<dt><code>-o</code> case_insensitive</dt>
<dd> enable case-insensitive mode</dd>
<dt><code>-o</code> daemon_timeout=T</dt>
<dd> timeout in seconds for kernel calls to daemon</dd>
<dt><code>-o</code> debug</dt>
<dd> turn on debug information printing</dd>
<dt><code>-o</code> default_permissions</dt>
<dd> let the kernel handle permission checks locally</dd>
<dt><code>-o</code> defer_permissions</dt>
<dd> defer permission checks to file operations themselves</dd>
<dt><code>-o</code> direct_io</dt>
<dd> use alternative (direct) path for kernel-user I/O</dd>
<dt><code>-o</code> extended_security</dt>
<dd> turn on Mac OS X extended security (ACLs)</dd>
<dt><code>-o</code> fsid=FSID</dt>
<dd> set the second 32-bit component of the fsid</dd>
<dt><code>-o</code> fsname=NAME</dt>
<dd> set the file system&#8217;s name</dd>
<dt><code>-o</code> fssubtype=NUM</dt>
<dd> set the file system&#8217;s fssubtype identifier</dd>
<dt><code>-o</code> fstypename=NAME</dt>
<dd> set the file system&#8217;s type name</dd>
<dt><code>-o</code> iosize=SIZE</dt>
<dd> specify maximum I/O size in bytes</dd>
<dt><code>-o</code> jail_symlinks</dt>
<dd> contain symbolic links within the mount</dd>
<dt><code>-o</code> kill_on_unmount</dt>
<dd> kernel will send a signal (SIGKILL by default) to the daemon after unmount finishes</dd>
<dt><code>-o</code> local</dt>
<dd> mark the volume as &#8220;local&#8221; (default is &#8220;nonlocal&#8221;)</dd>
<dt><code>-o</code> negative_vncache</dt>
<dd> enable vnode name caching of non-existent objects</dd>
<dt><code>-o</code> volname=NAME</dt>
<dd> set the file system&#8217;s volume name </dd>
<dt><code>-o</code> noalerts</dt>
<dd> disable all graphical alerts (if any) in MacFUSE Core</dd>
<dt><code>-o</code> noappledouble</dt>
<dd> ignore Apple Double (._) and .DS_Store files entirely</dd>
<dt><code>-o</code> noapplexattr</dt>
<dd> ignore all &#8220;com.apple.*&#8221; extended attributes</dd>
<dt><code>-o</code> nobrowse</dt>
<dd> mark the volume as non-browsable by the Finder</dd>
<dt><code>-o</code> nolocalcaches</dt>
<dd> meta option equivalent to noreadahead,noubc,novncache</dd>
<dt><code>-o</code> noping_diskarb</dt>
<dd> do not ping Disk Arbitration (pings by default)</dd>
<dt><code>-o</code> noreadahead</dt>
<dd> disable I/O read-ahead behavior for this file system</dd>
<dt><code>-o</code> nosynconclose</dt>
<dd> disable sync-on-close behavior (enabled by default)</dd>
<dt><code>-o</code> nosyncwrites</dt>
<dd> disable synchronous-writes behavior (dangerous)</dd>
<dt><code>-o</code> noubc</dt>
<dd> disable the unified buffer cache for this file system</dd>
<dt><code>-o</code> novncache</dt>
<dd> disable the vnode name cache for this file system </dd>
<dt><code>-o</code> hard_remove</dt>
<dd> immediate removal (don&#8217;t hide files)</dd>
<dt><code>-o</code> use_ino</dt>
<dd> let filesystem set inode numbers</dd>
<dt><code>-o</code> readdir_ino</dt>
<dd> try to fill in d_ino in readdir</dd>
<dt><code>-o</code> direct_io</dt>
<dd> use direct I/O</dd>
<dt><code>-o</code> kernel_cache</dt>
<dd> cache files in kernel</dd>
<dt><code>-o</code> [no]auto_cache</dt>
<dd> enable caching based on modification times</dd>
<dt><code>-o</code> umask=M</dt>
<dd> set file permissions (octal)</dd>
<dt><code>-o</code> uid=N</dt>
<dd> set file owner</dd>
<dt><code>-o</code> gid=N</dt>
<dd> set file group</dd>
<dt><code>-o</code> entry_timeout=T</dt>
<dd> cache timeout for names (1.0s)</dd>
<dt><code>-o</code> negative_timeout=T</dt>
<dd> cache timeout for deleted names (0.0s)</dd>
<dt><code>-o</code> attr_timeout=T</dt>
<dd> cache timeout for attributes (1.0s)</dd>
<dt><code>-o</code> ac_attr_timeout=T</dt>
<dd> auto cache timeout for attributes (attr_timeout)</dd>
<dt><code>-o</code> intr</dt>
<dd> allow requests to be interrupted</dd>
<dt><code>-o</code> intr_signal=NUM</dt>
<dd> signal to send on interrupt (30)</dd>
<dt><code>-o</code> modules=M1[:M2&#8230;]</dt>
<dd> names of modules to push onto filesystem stack </dd>
<dt><code>-o</code> max_write=N</dt>
<dd> set maximum size of write requests</dd>
<dt><code>-o</code> max_readahead=N</dt>
<dd> set maximum readahead</dd>
<dt><code>-o</code> async_read</dt>
<dd> perform reads asynchronously (default)</dd>
<dt><code>-o</code> sync_read</dt>
<dd> perform reads synchronously </dd>
</dl>
<h3>Module options</h3>
<dl>
<dt>[subdir]</dt>
<dd>
</dd><dt><code>-o</code> subdir=DIR</dt>
<dd> prepend this directory to all paths (mandatory)</dd>
<dt><code>-o</code> [no]rellinks</dt>
<dd> transform absolute symlinks to relative</dd>
<dt>[iconv]</dt>
<dd>
</dd><dt><code>-o</code> from_code=CHARSET</dt>
<dd> original encoding of file names (default: UTF-8)</dd>
<dt><code>-o</code> to_code=CHARSET</dt>
<dd> new encoding of the file names (default: ISO-8859-2) </dd>
</dl>
<h2>LICENSE</h2>
<p> This sofware is free software; you can redistribute it and/or modify it under the terms of the GNU Library General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Library General Public License for more details. </p>
<p> You should have received a copy of the GNU Library General Public License along with this software; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA </p>
<h2>KNOWN BUGS</h2>
<p> This is beta software and should be treated as such. Bug reports to the AUTHORS listed below would be appreciated. </p>
<p> archivemount is forced to run a single-thread mode for now. Support for stable multithreading is planned in a future release. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1), <code><a href="/docs/linux/man/1-cpio/">cpio</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code>libarchive</code>(3), <code>pax</code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), and <code><a href="/docs/linux/man/1-zip/">zip</a></code>(1) </p>
<p> &#8220;Filesystem in Userspace&#8221;: <a rel="nofollow" href="http://fuse.sourceforge.net/">http://fuse.sourceforge.net/</a> </p>
<p> &#8220;MacFUSE&#8221;: <a rel="nofollow" href="http://code.google.com/p/macfuse/">http://code.google.com/p/macfuse/</a> </p>
<h2>AUTHORS</h2>
<p> Archivemount is written and maintained by Andre Landwehr &lt;andrel [at] cybernoia.de&gt;. </p>
<p> This man page was written by Tom Duck &lt;tom.duck [at] dal.ca&gt; with material drawn from the page for <code>libarchive</code>(3). </p>
<h2>Index</h2>
