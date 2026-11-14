---
title: "vfs_streams_xattr(8)"
name: "vfs_streams_xattr"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_streams_xattr/"
description: "vfs_streams_xattr – Store alternate data streams in posix xattrs"
---

<p>vfs_streams_xattr &#8211; Store alternate data streams in posix xattrs</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = streams_xattr</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_streams_xattr enables storing of NTFS alternate data streams in the file system. As a normal posix file system does not support the concept of multiple data streams per file, the streams_xattr module stores the data in posix extended attributes (xattrs). The name of these attributes by default is user.DosStream.&quot;ADS-NAME&quot;. The prefix &quot;user.DosStream.&quot; can be changed with the module option streams_xattr:prefix, but be aware that this will also expose those ADS over the SMB extended attributes interface. </p>
<p> The file system that is shared with this module enabled must support xattrs. </p>
<p> Please note that most file systems have severe limitations on the size of xattrs. So this module might work for applications like IE that stores small zone information in streams but will fail for applications that store serious amounts of data in ADSs. </p>
<p> CAUTION: Make sure to set &quot;kernel oplocks = no&quot; in smb.conf if if you use this module because this combination is currently broken. See Bug 7537 for details.</p>
<h2>Options</h2>
<p>streams_xattr:prefix = STRING</p>
<dl>
<dd>Name prefix used when storing an ADS in an xattr, defaults to user.DosStream.. Changing this will also expose ADS over the SMB extended attributes interface.</dl>
<p> streams_xattr:store_stream_type = [yes|no]</p>
<dl>
<dd>Whether the xattr names for Alternate Data Streams of type &quot;$DATA&quot; are suffixed by the stream type string &quot;:$DATA&quot;. The default is yes.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>vfs objects = streams_xattr</code>m[]</pre>
</dl>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
