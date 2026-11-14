---
title: "vfs_crossrename(8)"
name: "vfs_crossrename"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_crossrename/"
description: "vfs_crossrename – server side rename files across filesystem boundaries"
---

<p>vfs_crossrename &#8211; server side rename files across filesystem boundaries</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = crossrename</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. The vfs_crossrename VFS module allows server side rename operations even if source and target are on different physical devices. A &quot;move&quot; in Explorer is usually a rename operation if it is inside of a single share or device. Usually such a rename operation returns NT_STATUS_NOT_SAME_DEVICE and the client has to move the file by manual copy and delete operations. If the rename by copy is done by the server this can be much more efficient. vfs_crossrename tries to do this server-side cross-device rename operation. There are however limitations that this module currently does not solve:  The ACLs of files are not preserved,</dl>
<p>  meta data in EAs are not preserved,</dl>
<p>  renames of whole subdirectories cannot be done recursively, in that case we still return STATUS_NOT_SAME_DEVICE and let the client decide what to do,</dl>
<p>  rename operations of huge files can cause hangs on the client because clients expect a rename operation to return fast.</dl>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>crossrename:sizelimit = BYTES</p>
<dl>
<dd>server-side cross-device-renames are only done for files if the filesize is not larger than the defined size in MiB to prevent timeouts. The default sizelimit is 20 (MiB)</dl>
<h2>Examples</h2>
<p>To add server-side cross-device renames inside of a share for all files sized up to 50MB: </p>
<dl>
<dd>
<pre> <i>[testshare]</i>
 m[blue]<code>path = /data/mounts</code>m[]
 m[blue]<code>vfs objects = crossrename</code>m[]
 m[blue]<code>crossrename:sizelimit = 50</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.0.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
