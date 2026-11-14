---
title: "vfs_readonly(8)"
name: "vfs_readonly"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_readonly/"
description: "vfs_readonly – make a Samba share read only for a specified time period"
---

<p>vfs_readonly &#8211; make a Samba share read only for a specified time period</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = readonly</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_readonly VFS module marks a share as read only for all clients connecting within the configured time period. Clients connecting during this time will be denied write access to all files in the share, irrespective of their actual access privileges. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>readonly:period = BEGIN, END</p>
<dl>
<dd>Only mark the share as read only if the client connection was made between the times marked by the BEGIN and END date specifiers. The syntax of these date specifiers is the same as that accepted by the -d option of GNU <code><a href="/docs/linux/man/1-date/">date</a></code>(1).</dl>
<h2>Examples</h2>
<p>Mark all shares read only: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>vfs objects = readonly</code>m[]</pre>
</dl>
<p> Mark the [backup] share as read only during business hours: </p>
<dl>
<dd>
<pre> <i>[backup]</i>
 m[blue]<code>path = /readonly</code>m[]
 m[blue]<code>vfs objects = readonly</code>m[]
 m[blue]<code>readonly:period = readonly:period = &quot;today 9:00&quot;,&quot;today 17:00&quot;</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
