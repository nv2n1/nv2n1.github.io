---
title: "vfs_shadow_copy(8)"
name: "vfs_shadow_copy"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_shadow_copy/"
description: "vfs_shadow_copy – Expose snapshots to Windows clients as shadow copies."
---

<p>vfs_shadow_copy &#8211; Expose snapshots to Windows clients as shadow copies.</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = shadow_copy</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_shadow_copy VFS module functionality that is similar to Microsoft Shadow Copy services. When setup properly, this module allows Microsoft Shadow Copy clients to browse &quot;shadow copies&quot; on Samba shares. </p>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<p>vfs_shadow_copy relies on a filesystem snapshot implementation. Many common filesystems have native support for this. </p>
<p> Filesystem snapshots must be mounted on specially named directories in order to be recognized by vfs_shadow_copy. The snapshot mount points must be immediate children of a the directory being shared. </p>
<p> The snapshot naming convention is @GMT-YYYY.MM.DD-hh.mm.ss, where: </p>
<dl>
<dd>&bull; YYYY is the 4 digit year</dl>
<dl>
<dd>&bull; MM is the 2 digit month</dl>
<dl>
<dd>&bull; DD is the 2 digit day</dl>
<dl>
<dd>&bull; hh is the 2 digit hour</dl>
<dl>
<dd>&bull; mm is the 2 digit minute</dl>
<dl>
<dd>&bull; ss is the 2 digit second.</dl>
<p> The vfs_shadow_copy snapshot naming convention can be produced with the following <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command: </p>
<dl>
<dd>
<pre> TZ=GMT date +@GMT-%Y.%m.%d-%H.%M.%S</pre>
</dl>
<h2>Examples</h2>
<p>Add shadow copy support to user home directories: </p>
<dl>
<dd>
<pre> <i>[homes]</i>
 m[blue]<code>vfs objects = shadow_copy</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>This is not a backup, archival, or version control solution. </p>
<p> With Samba or Windows servers, vfs_shadow_copy is designed to be an end-user tool only. It does not replace or enhance your backup and archival solutions and should in no way be considered as such. Additionally, if you need version control, implement a version control system.</p>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
