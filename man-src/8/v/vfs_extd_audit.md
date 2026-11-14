---
title: "vfs_extd_audit(8)"
name: "vfs_extd_audit"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_extd_audit/"
description: "vfs_extd_audit – record selected Samba VFS operations"
---

<p>vfs_extd_audit &#8211; record selected Samba VFS operations</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = extd_audit</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The extd_audit VFS module records selected client operations to both the <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) log and system log (using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)). </p>
<p> Other than logging to the <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) log, vfs_extd_audit is identical to <code><a href="/docs/linux/man/8-vfs_audit/">vfs_audit</a></code>(8). </p>
<p> This module is stackable.</p>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
