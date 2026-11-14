---
title: "simple-mtpfs(1)"
name: "simple-mtpfs"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simple-mtpfs/"
description: "SIMPLE-MTPFS – filesystem driver for MTP based devices"
---

<h2>NAME</h2>
<p> SIMPLE-MTPFS &#8211; filesystem driver for MTP based devices</p>
<h2>SYNOPSIS</h2>
<h3>mounting</h3>
<dl>
<dt><code>simple-mtpfs &lt;device&gt;</code> <code>mountpoint</code> [<i>options</i>]</p>
<dd></dl>
<h3>unmounting</h3>
<dl>
<dt><code>fusermount -u mountpoint</code></p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> SIMPLE-MTPFS (Simple Media Transfer Protocol FileSystem) is a file system for Linux (and other operating systems with a FUSE implementation, such as Mac OS X or FreeBSD) capable of operating on files on MTP devices attached via USB to local machine. On the local computer where the SIMPLE-MTPFS is mounted, the implementation makes use of the FUSE (Filesystem in Userspace) kernel module. The practical effect of this is that the end user can seamlessly interact with MTP device files.</p>
<h2>OPTIONS</h2>
<h3>general options:</h3>
<dl>
<dt><code>-o</code> opt,[opt&#8230;]</p>
<dd> mount options</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> print help</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> print version</dl>
<h3>SIMPLE-MTPFS options:</h3>
<dl>
<dt><code>-l</code> <code>&#8211;list-devices</code></p>
<dd> list available MTP devices</p>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;device</code></p>
<dd> select device no. to mount</p>
<dt><code>-o</code> enable-move</p>
<dd> enable move operation, which can be very slow (depends on the moved content)</dl>
<h3>FUSE options:</h3>
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
<dd> perform reads synchronously</dl>
<h2>AUTHORS</h2>
<p> SIMPLE-MTPFS has been written by Peter Hatina &lt;phatina [at] gmail.com&gt;. </p>
<h2>Index</h2>
