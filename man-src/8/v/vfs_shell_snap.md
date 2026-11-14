---
title: "vfs_shell_snap(8)"
name: "vfs_shell_snap"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_shell_snap/"
description: "vfs_shell_snap – Shell script callouts for snapshot creation and deletion"
---

<p>vfs_shell_snap &#8211; Shell script callouts for snapshot creation and deletion</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = shell_snap</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/8-samba/">samba</a></code>(8) suite. </p>
<p> The vfs_shell_snap VFS provides shell-script callouts for snapshot creation and deletion operations issued by remote clients using the File Server Remote VSS Protocol (FSRVP). </p>
<p> The following shell callouts may be configured in smb.conf: </p>
<p> m[blue]<code>shell_snap:check path command</code>m[] </p>
<dl>
<dd>&bull; Called when an FSRVP client wishes to check whether a given share supports snapshot create/delete requests.</dl>
<dl>
<dd>&bull; The command is called with a single <i>share_path</i> argument.</dl>
<dl>
<dd>&bull; The command must return 0 if <i>share_path</i> is capable of being snapshotted.</dl>
<p> m[blue]<code>shell_snap:create command</code>m[] </p>
<dl>
<dd>&bull; Called when an FSRVP client wishes to create a snapshot.</dl>
<dl>
<dd>&bull; The command is called with a single <i>share_path</i> argument.</dl>
<dl>
<dd>&bull; The command must return 0 status if the snapshot was successfully taken.</dl>
<dl>
<dd>&bull; The command must output the path of the newly created snapshot to stdout.</dl>
<p> m[blue]<code>shell_snap:delete command</code>m[] </p>
<dl>
<dd>&bull; Called when an FSRVP client wishes to delete a snapshot.</dl>
<dl>
<dd>&bull; The command is called with <i>base_share_path</i> and <i>snapshot_share_path</i> arguments.</dl>
<dl>
<dd>&bull; The command must return 0 status if the snapshot was successfully removed.</dl>
<p> All commands are executed as the authenticated FSRVP client user. </p>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>vfs objects = shell_snap</code>m[]
 m[blue]<code>shell_snap:check path command = snap_check_path.sh</code>m[]
 m[blue]<code>shell_snap:create command = snap_create.sh</code>m[]
 m[blue]<code>shell_snap:delete command = snap_delete.sh</code>m[]</pre>
</dl>
<p> Samba&#8217;s FSRVP server must be configured in the [global] section: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>rpc_daemon:fssd = fork</code>m[]
 m[blue]<code>registry shares = yes</code>m[]
 m[blue]<code>include = registry</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.2.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
