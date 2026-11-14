---
title: "vfs_fileid(8)"
name: "vfs_fileid"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_fileid/"
description: "vfs_fileid – Generates file_id structs with unique device id values for cluster setups"
---

<p>vfs_fileid &#8211; Generates file_id structs with unique device id values for cluster setups</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = fileid</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> Samba uses file_id structs to uniquely identify files for locking purpose. By default the file_id contains the device and inode number returned by the stat() system call. As the file_id is a unique identifier of a file, it must be the same on all nodes in a cluster setup. This module overloads the SMB_VFS_FILE_ID_CREATE() operation and generates the device number based on the configured algorithm (see the &quot;fileid:algorithm&quot; option).</p>
<h2>Options</h2>
<p>fileid:algorithm = ALGORITHM</p>
<dl>
<dd>Available algorithms are fsname and fsid. The default value is fsname. </p>
<p> The fsname algorithm generates device id by hashing the kernel device name. </p>
<p> The fsid algorithm generates the device id from the f_fsid returned from the statfs() syscall.</dl>
<p> fileid:mapping = ALGORITHM</p>
<dl>
<dd>This option is the legacy version of the fileid:algorithm option, which was used in earlier versions of fileid mapping feature in custom Samba 3.0 versions.</dl>
<h2>Examples</h2>
<p>Usage of the fileid module with the fsid algorithm: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>vfs objects = fileid</code>m[]
 m[blue]<code>fileid:algorithm = fsid</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.2 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
