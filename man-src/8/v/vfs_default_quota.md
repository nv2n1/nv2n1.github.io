---
title: "vfs_default_quota(8)"
name: "vfs_default_quota"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_default_quota/"
description: "vfs_default_quota – store default quota records for Windows clients"
---

<p>vfs_default_quota &#8211; store default quota records for Windows clients</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = default_quota</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> Many common quota implementations only store quotas for users and groups, but do not store a default quota. The vfs_default_quota module allows Samba to store default quota values which can be examined using the Windows Explorer interface. </p>
<p> By default, Samba returns NO_LIMIT the default quota and refuses to update them. vfs_default_quota maps the default quota to the quota record of a user. By default the root user is taken because quota limits for root are typically not enforced. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>default_quota:uid = UID</p>
<dl>
<dd>UID specifies the user ID of the quota record where the default user quota values are stored.</dl>
<p> default_quota:gid = GID</p>
<dl>
<dd>GID specifies the group ID of the quota record where the default group quota values are stored.</dl>
<p> default_quota:uid nolimit = BOOL</p>
<dl>
<dd>If this parameter is True, then the user whose quota record is storing the default user quota will be reported as having a quota of NO_LIMIT. Otherwise, the stored values will be reported.</dl>
<p> default_quota:gid nolimit = BOOL</p>
<dl>
<dd>If this parameter is True, then the group whose quota record is storing the default group quota will be reported as having a quota of NO_LIMIT. Otherwise, the stored values will be reported.</dl>
<h2>Examples</h2>
<p>Store the default quota record in the quota record for the user with ID 65535 and report that user as having no quota limits: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>vfs objects = default_quota</code>m[]
 m[blue]<code>default_quota:uid = 65535</code>m[]
 m[blue]<code>default_quota:uid nolimit = yes</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
