---
title: "vfs_snapper(8)"
name: "vfs_snapper"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_snapper/"
description: "vfs_snapper – Expose snapshots managed by snapper as shadow-copies"
---

<p>vfs_snapper &#8211; Expose snapshots managed by snapper as shadow-copies</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = snapper</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/8-samba/">samba</a></code>(8) suite. </p>
<p> The vfs_snapper VFS module exposes snapshots managed by snapper for use by Samba. This provides the ability for remote SMB clients to access shadow-copies via Windows Explorer using the &quot;previous versions&quot; dialog. </p>
<p> Snapshots can also be created and remove remotely, using the File Server Remote VSS Protocol (FSRVP). Snapshot creation and deletion requests are forwarded to snapper via DBus. </p>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<p>The underlying share path must have a corresponding snapper configuration file. The snapshot directory tree must allow access for relavent users. </p>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>vfs objects = snapper</code>m[]</pre>
</dl>
<p> For remote snapshot creation and deletion, Samba&#8217;s FSRVP server must be configured in the [global] section: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>rpc_daemon:fssd = fork</code>m[]
 m[blue]<code>registry shares = yes</code>m[]
 m[blue]<code>include = registry</code>m[]</pre>
</dl>
<h2>Permissions</h2>
<p>Snapper stores snapshots under a .snapshots subdirectory. This directory must permit traversal for any users wishing to access snapshots via the Windows Explorer previous versions dialog. By default, traversal is forbidden for all non-root users. Additionally, users must be granted permission to list snapshots managed by snapper, via snapper&#8217;s ALLOW_USERS or ALLOW_GROUPS options. Snapper can grant these users and groups .snapshots traversal access automatically via the SYNC_ACL option. </p>
<p> Remote snapshot creation and deletion is only permitted by Samba for Active Directory administrators, backup operators, or users explicitly granted SeBackupPrivilege. Snapper must also permit creation and deletion for the appropriate user, via snapper&#8217;s ALLOW_USERS or ALLOW_GROUPS options. </p>
<p> The DiskShadow.exe FSRVP client initially authenticates as the Active Directory computer account. This account must therefore be granted the same permissions as the user account issuing the snapshot creation and deletion requests.</p>
<h2>Version</h2>
<p>This man page is correct for version 4.3.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
