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
<dd>vfs objects = audit</dd></dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_audit VFS module records selected client operations to the system log using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). </p>
<p> The following Samba VFS operations are recorded:</p>
<dl>
<dd>connect</dd></dl>
<dl>
<dd>disconnect</dd></dl>
<dl>
<dd>opendir</dd></dl>
<dl>
<dd>mkdir</dd></dl>
<dl>
<dd>rmdir</dd></dl>
<dl>
<dd>open</dd></dl>
<dl>
<dd>close</dd></dl>
<dl>
<dd>rename</dd></dl>
<dl>
<dd>unlink</dd></dl>
<dl>
<dd>chmod</dd></dl>
<dl>
<dd>fchmod</dd></dl>
<dl>
<dd>chmod_acl</dd></dl>
<dl>
<dd>fchmod_acl</dd></dl>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>audit:facility = FACILITY</p>
<dl>
<dd>Log messages to the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) facility.</dd></dl>
<p> audit:priority = PRIORITY</p>
<dl>
<dd>Log messages with the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) priority.</dd></dl>
<h2>Examples</h2>
<p>Log operations on all shares using the LOCAL1 facility and NOTICE priority: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>vfs objects = audit</code>m[]
 m[blue]<code>audit:facility = LOCAL1</code>m[]
 m[blue]<code>audit:priority = NOTICE</code>m[]</pre>
</dd></dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
