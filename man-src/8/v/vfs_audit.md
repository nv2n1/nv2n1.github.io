---
title: "vfs_audit(8)"
name: "vfs_audit"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_audit/"
description: "vfs_audit – record selected Samba VFS operations in the system log"
---

<p>vfs_audit &#8211; record selected Samba VFS operations in the system log</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = audit</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_audit VFS module records selected client operations to the system log using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). </p>
<p> The following Samba VFS operations are recorded:</p>
<dl>
<dd>connect</dl>
<dl>
<dd>disconnect</dl>
<dl>
<dd>opendir</dl>
<dl>
<dd>mkdir</dl>
<dl>
<dd>rmdir</dl>
<dl>
<dd>open</dl>
<dl>
<dd>close</dl>
<dl>
<dd>rename</dl>
<dl>
<dd>unlink</dl>
<dl>
<dd>chmod</dl>
<dl>
<dd>fchmod</dl>
<dl>
<dd>chmod_acl</dl>
<dl>
<dd>fchmod_acl</dl>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>audit:facility = FACILITY</p>
<dl>
<dd>Log messages to the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) facility.</dl>
<p> audit:priority = PRIORITY</p>
<dl>
<dd>Log messages with the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) priority.</dl>
<h2>Examples</h2>
<p>Log operations on all shares using the LOCAL1 facility and NOTICE priority: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>vfs objects = audit</code>m[]
 m[blue]<code>audit:facility = LOCAL1</code>m[]
 m[blue]<code>audit:priority = NOTICE</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
