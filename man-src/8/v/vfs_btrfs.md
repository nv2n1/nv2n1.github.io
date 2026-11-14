---
title: "vfs_btrfs(8)"
name: "vfs_btrfs"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_btrfs/"
description: "vfs_btrfs – Utilize features provided by the Btrfs filesystem"
---

<p>vfs_btrfs &#8211; Utilize features provided by the Btrfs filesystem</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = btrfs</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/8-samba/">samba</a></code>(8) suite. </p>
<p> The vfs_btrfs VFS module exposes Btrfs specific features for use by Samba. </p>
<p> Btrfs allows for multiple files to share the same on-disk data through the use cloned ranges. When an SMB client issues a request to copy duplicate data (via FSCTL_SRV_COPYCHUNK), this module maps the request to a Btrfs clone range IOCTL, instead of performing reads and writes required by a traditional copy. Doing so saves storage capacity and greatly reduces disk IO. </p>
<p> This module also exposes Btrfs per-file compression support to SMB clients via the get/set compression fsctls. </p>
<p> Btrfs snapshots can be manipulated by Samba&#8217;s FSRVP server. Snapshot manipulation using this module is currently considered experimental, and is therefore disabled by default. The vfs_snapper module is instead recommended for this purpose. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>btrfs: manipulate snapshots = [yes|no]</p>
<dl>
<dd>When set to <i>yes</i>, experimental support for the creation and deletion of snapshots via corresponding Btrfs IOCTLs will be enabled. The default is <i>no</i>, which means that such requests are passed through to any underlying VFS module.</dl>
<h2>Configuration</h2>
<p>vfs_btrfs requires that the underlying share path is a Btrfs subvolume. </p>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>vfs objects = btrfs</code>m[]
 m[blue]<code>btrfs: manipulate snapshots = no</code>m[]</pre>
</dl>
<p> To use the experimental snapshot manipulation functionality provided by this module, it must be explicity enabled, and Samba&#8217;s FSRVP server must be running. </p>
<p> The vfs_shadow_copy module can be used to expose snapshots created by vfs_btrfs to Windows Explorer as file / directory &quot;previous versions&quot;. </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>rpc_daemon:fssd = fork</code>m[]
 m[blue]<code>registry shares = yes</code>m[]
 m[blue]<code>include = registry</code>m[]
 <i>[share]</i>
 m[blue]<code>vfs objects = btrfs shadow_copy</code>m[]
 m[blue]<code>btrfs: manipulate snapshots = yes</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.3.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
