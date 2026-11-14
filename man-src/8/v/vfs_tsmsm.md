---
title: "vfs_tsmsm(8)"
name: "vfs_tsmsm"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_tsmsm/"
description: "vfs_tsmsm – VFS module for handling offline files with Tivoli Storage Manager Space Management"
---

<p>vfs_tsmsm &#8211; VFS module for handling offline files with Tivoli Storage Manager Space Management</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = tsmsm</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The tsmsm VFS module is an extension for handling offline files with Tivoli Storage Manager Space Management. </p>
<p> It tries to avoid calling expensive DMAPI calls with some heuristics based on the fact that number of blocks reported of a file multiplied by 512 will be bigger than &#8216;online ratio&#8217; of actual size for online (non-migrated) files. If heuristic check fails, the module calls DMAPI and asks for a specific attribute which is present for offline (migrated) files. If this attribute presents, the file is considered offline. </p>
<p> This module is not stackable.</p>
<h2>Options</h2>
<p>tsmsm:hsm script = [ path to hsm script ]</p>
<dl>
<dd>hsm script should point to a shell script which accepts two arguments: operation and filepath. the tsmsm module only uses &quot;offline&quot; for operation to set the file under filepath offline.</dl>
<p> tsmsm:online ratio = [ number ]</p>
<dl>
<dd>Ratio to check reported size against actual file size. The default value is 0.5.</dl>
<p> tsmsm:dmapi attribute = [ attribute-name ]</p>
<dl>
<dd>Name of a DMAPI attribute that is present when a file is offline. The default is &quot;IBMobj&quot; (which is what GPFS uses).</dl>
<p> tsmsm:dmapi value = [ value for the DMAPI attribute ]</p>
<dl>
<dd>Value that the DMAPI attribute should have for the file to be considered offline. The default is empty (no value required).</dl>
<h2>Examples</h2>
<p>A GPFS mount with TSM support can be exported via Samba as follows: </p>
<dl>
<dd>
<pre> <i>[gpfs_tsm_share]</i>
 m[blue]<code>vfs objects = tsmsm gpfs</code>m[]
 m[blue]<code>path = /test/gpfs_mount</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
