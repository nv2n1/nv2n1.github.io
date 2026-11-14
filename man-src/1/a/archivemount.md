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
<p> Archive format support is provided by the <code><a href="/docs/linux/man/3-libarchive/">libarchive</a></code>(3) library. Read operations are supported for:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> old-style tar archives,</p>
<dt>&bull;</p>
<dd> most variants of the POSIX &#8220;ustar&#8221; format,</p>
<dt>&bull;</p>
<dd> the POSIX &#8220;pax interchange&#8221; format,</p>
<dt>&bull;</p>
<dd> GNU-format tar archives,</p>
<dt>&bull;</p>
<dd> most common cpio archive formats,</p>
<dt>&bull;</p>
<dd> ISO9660 CD images (with or without RockRidge extensions),</p>
<dt>&bull;</p>
<dd> Zip archives.</dl>
</dl>
<p> Archives compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), or <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1) are automatically detected and transparently decompressed. </p>
<p> The following formats can be written:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> POSIX-standard &#8220;ustar&#8221; archives,</p>
<dt>&bull;</p>
<dd> POSIX &#8220;pax interchange format&#8221; archives,</p>
<dt>&bull;</p>
<dd> POSIX octet-oriented cpio archives,</p>
<dt>&bull;</p>
<dd> two different variants of shar archives.</dl>
</dl>
<p> Before writing, the original archive is renamed with a &#8220;.orig&#8221; extension appended to it. More detail about the read/write support can be found in the <code><a href="/docs/linux/man/3-libarchive/">libarchive</a></code>(3) documentation. </p>
<h2>OPTIONS</h2>
<p> <code>archivemount</code> is built upon the FUSE (Filesystem in Userspace) library, and the complete set of available options depends upon the specific FUSE implementation. Execute <code>archivemount -h</code> to retrieve a definitive list. </p>
<h3>general options</h3>
<dl>
<dt><code>-o</code> opt,[opt&#8230;]</p>
<dd> mount options</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> print help</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> print version </p>
</dl>
<h3>archivemount mount options</h3>
<dl>
<dt><code>-o</code> readonly</p>
<dd> disable write support</p>
<dt><code>-o</code> nobackup</p>
<dd> remove archive file backups</p>
<dt><code>-o</code> subtree=&lt;regex&gt;</p>
<dd> mount only subtree of archive, strip subtree part from path </p>
</dl>
<h3>FUSE mount options</h3>
<p> These options are available to linux users using standard FUSE. </p>
<dl>
<dt><code>-d</code> <code>-o</code> debug</p>
<dd> enable debug output (implies <code>-f</code>)</p>
<dt><code>-f</code></p>
<dd> foreground operation</p>
<dt><code>-s</code></p>
<dd> disable multi-threaded operation</p>
<dt><code>-o</code> allow_other</p>
<dd> allow access to other users</p>
<dt><code>-o</code> allow_root</p>
<dd> allow access to root</p>
<dt><code>-o</code> nonempty</p>
<dd> allow mounts over non-empty file/dir</p>
<dt> <code>-o</code> default_permissions</p>
<dd>enable permission checking by kernel</p>
<dt><code>-o</code> fsname=NAME</p>
<dd> set filesystem name</p>
<dt><code>-o</code> subtype=NAME</p>
<dd> set filesystem type</p>
<dt><code>-o</code> large_read</p>
<dd> issue large read requests (2.4 only)</p>
<dt><code>-o</code> max_read=N</p>
<dd> set maximum size of read requests</p>
<dt><code>-o</code> hard_remove</p>
<dd> immediate removal (don&#8217;t hide files)</p>
<dt><code>-o</code> use_ino</p>
<dd> let filesystem set inode numbers</p>
<dt><code>-o</code> readdir_ino</p>
<dd> try to fill in d_ino in readdir</p>
<dt><code>-o</code> direct_io</p>
<dd> use direct I/O</p>
<dt><code>-o</code> kernel_cache</p>
<dd> cache files in kernel</p>
<dt><code>-o</code> [no]auto_cache</p>
<dd> enable caching based on modification times</p>
<dt><code>-o</code> umask=M</p>
<dd> set file permissions (octal)</p>
<dt><code>-o</code> uid=N</p>
<dd> set file owner</p>
<dt><code>-o</code> gid=N</p>
<dd> set file group</p>
<dt><code>-o</code> entry_timeout=T</p>
<dd> cache timeout for names (1.0s)</p>
<dt><code>-o</code> negative_timeout=T</p>
<dd> cache timeout for deleted names (0.0s)</p>
<dt><code>-o</code> attr_timeout=T</p>
<dd> cache timeout for attributes (1.0s)</p>
<dt><code>-o</code> ac_attr_timeout=T</p>
<dd> auto cache timeout for attributes (attr_timeout)</p>
<dt><code>-o</code> intr</p>
<dd> allow requests to be interrupted</p>
<dt><code>-o</code> intr_signal=NUM</p>
<dd> signal to send on interrupt (10)</p>
<dt><code>-o</code> modules=M1[:M2&#8230;]</p>
<dd> names of modules to push onto filesystem stack</p>
<dt><code>-o</code> max_write=N</p>
<dd> set maximum size of write requests</p>
<dt><code>-o</code> max_readahead=N</p>
<dd> set maximum readahead</p>
<dt><code>-o</code> async_read</p>
<dd> perform reads asynchronously (default)</p>
<dt><code>-o</code> sync_read</p>
<dd> perform reads synchronously</p>
<dt><code>-o</code> atomic_o_trunc</p>
<dd> enable atomic open+truncate support </p>
</dl>
<h3>MacFUSE mount options</h3>
<p> These options are available to Mac users using MacFUSE. </p>
<dl>
<dt><code>-o</code> allow_other</p>
<dd> allow access to others besides the user who mounted the file system</p>
<dt><code>-o</code> allow_recursion</p>
<dd> allow a mount point that itself resides on a MacFUSE volume (by default, such mounting is disallowed)</p>
<dt><code>-o</code> allow_root</p>
<dd> allow access to root (can&#8217;t be used with allow_other)</p>
<dt><code>-o</code> auto_xattr</p>
<dd> handle extended attributes entirely through ._ files</p>
<dt><code>-o</code> blocksize=SIZE</p>
<dd> specify block size in bytes of &quot;storage&quot;</p>
<dt><code>-o</code> case_insensitive</p>
<dd> enable case-insensitive mode</p>
<dt><code>-o</code> daemon_timeout=T</p>
<dd> timeout in seconds for kernel calls to daemon</p>
<dt><code>-o</code> debug</p>
<dd> turn on debug information printing</p>
<dt><code>-o</code> default_permissions</p>
<dd> let the kernel handle permission checks locally</p>
<dt><code>-o</code> defer_permissions</p>
<dd> defer permission checks to file operations themselves</p>
<dt><code>-o</code> direct_io</p>
<dd> use alternative (direct) path for kernel-user I/O</p>
<dt><code>-o</code> extended_security</p>
<dd> turn on Mac OS X extended security (ACLs)</p>
<dt><code>-o</code> fsid=FSID</p>
<dd> set the second 32-bit component of the fsid</p>
<dt><code>-o</code> fsname=NAME</p>
<dd> set the file system&#8217;s name</p>
<dt><code>-o</code> fssubtype=NUM</p>
<dd> set the file system&#8217;s fssubtype identifier</p>
<dt><code>-o</code> fstypename=NAME</p>
<dd> set the file system&#8217;s type name</p>
<dt><code>-o</code> iosize=SIZE</p>
<dd> specify maximum I/O size in bytes</p>
<dt><code>-o</code> jail_symlinks</p>
<dd> contain symbolic links within the mount</p>
<dt><code>-o</code> kill_on_unmount</p>
<dd> kernel will send a signal (SIGKILL by default) to the daemon after unmount finishes</p>
<dt><code>-o</code> local</p>
<dd> mark the volume as &#8220;local&#8221; (default is &#8220;nonlocal&#8221;)</p>
<dt><code>-o</code> negative_vncache</p>
<dd> enable vnode name caching of non-existent objects</p>
<dt><code>-o</code> volname=NAME</p>
<dd> set the file system&#8217;s volume name </p>
<dt><code>-o</code> noalerts</p>
<dd> disable all graphical alerts (if any) in MacFUSE Core</p>
<dt><code>-o</code> noappledouble</p>
<dd> ignore Apple Double (._) and .DS_Store files entirely</p>
<dt><code>-o</code> noapplexattr</p>
<dd> ignore all &#8220;com.apple.*&#8221; extended attributes</p>
<dt><code>-o</code> nobrowse</p>
<dd> mark the volume as non-browsable by the Finder</p>
<dt><code>-o</code> nolocalcaches</p>
<dd> meta option equivalent to noreadahead,noubc,novncache</p>
<dt><code>-o</code> noping_diskarb</p>
<dd> do not ping Disk Arbitration (pings by default)</p>
<dt><code>-o</code> noreadahead</p>
<dd> disable I/O read-ahead behavior for this file system</p>
<dt><code>-o</code> nosynconclose</p>
<dd> disable sync-on-close behavior (enabled by default)</p>
<dt><code>-o</code> nosyncwrites</p>
<dd> disable synchronous-writes behavior (dangerous)</p>
<dt><code>-o</code> noubc</p>
<dd> disable the unified buffer cache for this file system</p>
<dt><code>-o</code> novncache</p>
<dd> disable the vnode name cache for this file system </p>
<dt><code>-o</code> hard_remove</p>
<dd> immediate removal (don&#8217;t hide files)</p>
<dt><code>-o</code> use_ino</p>
<dd> let filesystem set inode numbers</p>
<dt><code>-o</code> readdir_ino</p>
<dd> try to fill in d_ino in readdir</p>
<dt><code>-o</code> direct_io</p>
<dd> use direct I/O</p>
<dt><code>-o</code> kernel_cache</p>
<dd> cache files in kernel</p>
<dt><code>-o</code> [no]auto_cache</p>
<dd> enable caching based on modification times</p>
<dt><code>-o</code> umask=M</p>
<dd> set file permissions (octal)</p>
<dt><code>-o</code> uid=N</p>
<dd> set file owner</p>
<dt><code>-o</code> gid=N</p>
<dd> set file group</p>
<dt><code>-o</code> entry_timeout=T</p>
<dd> cache timeout for names (1.0s)</p>
<dt><code>-o</code> negative_timeout=T</p>
<dd> cache timeout for deleted names (0.0s)</p>
<dt><code>-o</code> attr_timeout=T</p>
<dd> cache timeout for attributes (1.0s)</p>
<dt><code>-o</code> ac_attr_timeout=T</p>
<dd> auto cache timeout for attributes (attr_timeout)</p>
<dt><code>-o</code> intr</p>
<dd> allow requests to be interrupted</p>
<dt><code>-o</code> intr_signal=NUM</p>
<dd> signal to send on interrupt (30)</p>
<dt><code>-o</code> modules=M1[:M2&#8230;]</p>
<dd> names of modules to push onto filesystem stack </p>
<dt><code>-o</code> max_write=N</p>
<dd> set maximum size of write requests</p>
<dt><code>-o</code> max_readahead=N</p>
<dd> set maximum readahead</p>
<dt><code>-o</code> async_read</p>
<dd> perform reads asynchronously (default)</p>
<dt><code>-o</code> sync_read</p>
<dd> perform reads synchronously </p>
</dl>
<h3>Module options</h3>
<dl>
<dt>[subdir]</p>
<dd>
<dt><code>-o</code> subdir=DIR</p>
<dd> prepend this directory to all paths (mandatory)</p>
<dt><code>-o</code> [no]rellinks</p>
<dd> transform absolute symlinks to relative</p>
<dt>[iconv]</p>
<dd>
<dt><code>-o</code> from_code=CHARSET</p>
<dd> original encoding of file names (default: UTF-8)</p>
<dt><code>-o</code> to_code=CHARSET</p>
<dd> new encoding of the file names (default: ISO-8859-2) </p>
</dl>
<h2>LICENSE</h2>
<p> This sofware is free software; you can redistribute it and/or modify it under the terms of the GNU Library General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Library General Public License for more details. </p>
<p> You should have received a copy of the GNU Library General Public License along with this software; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA </p>
<h2>KNOWN BUGS</h2>
<p> This is beta software and should be treated as such. Bug reports to the AUTHORS listed below would be appreciated. </p>
<p> archivemount is forced to run a single-thread mode for now. Support for stable multithreading is planned in a future release. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1), <code><a href="/docs/linux/man/1-cpio/">cpio</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/3-libarchive/">libarchive</a></code>(3), <code><a href="/docs/linux/man/1-pax/">pax</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), and <code><a href="/docs/linux/man/1-zip/">zip</a></code>(1) </p>
<p> &#8220;Filesystem in Userspace&#8221;: <a rel="nofollow" href="http://fuse.sourceforge.net/">http://fuse.sourceforge.net/</a> </p>
<p> &#8220;MacFUSE&#8221;: <a rel="nofollow" href="http://code.google.com/p/macfuse/">http://code.google.com/p/macfuse/</a> </p>
<h2>AUTHORS</h2>
<p> Archivemount is written and maintained by Andre Landwehr &lt;andrel [at] cybernoia.de&gt;. </p>
<p> This man page was written by Tom Duck &lt;tom.duck [at] dal.ca&gt; with material drawn from the page for <code><a href="/docs/linux/man/3-libarchive/">libarchive</a></code>(3). </p>
<h2>Index</h2>
