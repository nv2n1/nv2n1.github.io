---
title: "vfs_recycle(8)"
name: "vfs_recycle"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_recycle/"
description: "vfs_recycle – Samba VFS recycle bin"
---

<p>vfs_recycle &#8211; Samba VFS recycle bin</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = recycle</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_recycle intercepts file deletion requests and moves the affected files to a temporary repository rather than deleting them immediately. This gives the same effect as the Recycle Bin on Windows computers. </p>
<p> The Recycle Bin will not appear in Windows Explorer views of the network file system (share) nor on any mapped drive. Instead, a directory called .recycle will be automatically created when the first file is deleted and recycle:repository is not configured. If recycle:repository is configured, the name of the created directory depends on recycle:repository. Users can recover files from the recycle bin. If the recycle:keeptree option has been specified, deleted files will be found in a path identical with that from which the file was deleted. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>recycle:repository = PATH</p>
<dl>
<dd>Path of the directory where deleted files should be moved. </p>
<p> If this option is not set, the default path .recycle is used.</dl>
<p> recycle:directory_mode = MODE</p>
<dl>
<dd>Set MODE to the octal mode the recycle repository should be created with. The recycle repository will be created when first file is deleted. If recycle:subdir_mode is not set, MODE also applies to subdirectories. </p>
<p> If this option is not set, the default mode 0700 is used.</dl>
<p> recycle:subdir_mode = MODE</p>
<dl>
<dd>Set MODE to the octal mode with which sub directories of the recycle repository should be created. </p>
<p> If this option is not set, subdirectories will be created with the mode from recycle:directory_mode.</dl>
<p> recycle:keeptree = BOOL</p>
<dl>
<dd>Specifies whether the directory structure should be preserved or whether the files in a directory that is being deleted should be kept separately in the repository.</dl>
<p> recycle:versions = BOOL</p>
<dl>
<dd>If this option is True, two files with the same name that are deleted will both be kept in the repository. Newer deleted versions of a file will be called &quot;Copy #x of filename&quot;.</dl>
<p> recycle:touch = BOOL</p>
<dl>
<dd>Specifies whether a file&#8217;s access date should be updated when the file is moved to the repository.</dl>
<p> recycle:touch_mtime = BOOL</p>
<dl>
<dd>Specifies whether a file&#8217;s last modified date should be updated when the file is moved to the repository.</dl>
<p> recycle:minsize = BYTES</p>
<dl>
<dd>Files that are smaller than the number of bytes specified by this parameter will not be put into the repository.</dl>
<p> recycle:maxsize = BYTES</p>
<dl>
<dd>Files that are larger than the number of bytes specified by this parameter will not be put into the repository.</dl>
<p> recycle:exclude = LIST</p>
<dl>
<dd>List of files that should not be put into the repository when deleted, but deleted in the normal way. Wildcards such as * and ? are supported.</dl>
<p> recycle:exclude_dir = LIST</p>
<dl>
<dd>List of directories whose files should not be put into the repository when deleted, but deleted in the normal way. Wildcards such as * and ? are supported.</dl>
<p> recycle:noversions = LIST</p>
<dl>
<dd>Specifies a list of paths (wildcards such as * and ? are supported) for which no versioning should be used. Only useful when recycle:versions is enabled.</dl>
<h2>Examples</h2>
<p>Move files &quot;deleted&quot; on <i>share</i> to <i>/data/share/.recycle</i> instead of deleting them: </p>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>path = /data/share</code>m[]
 m[blue]<code>vfs objects = recycle</code>m[]
 m[blue]<code>recycle:repository = .recycle</code>m[]
 m[blue]<code>recycle:keeptree = yes</code>m[]
 m[blue]<code>recycle:versions = yes</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
