---
title: "vfs_unityed_media(8)"
name: "vfs_unityed_media"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_unityed_media/"
description: "vfs_unityed_media – Allow multiple Avid clients to share a network drive."
---

<p>vfs_unityed_media &#8211; Allow multiple Avid clients to share a network drive.</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = unityed_media</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> Unityed Media is related with Media Harmony VFS, the main difference between Unityed Media and Media Harmony is that Unityed Media doesn&#8217;t need manual refreshing of media directories. Unityed Media handles your media files in a similar way to the way Unity, ISIS, EditShare or another dedicated solution does. Without client-side application and on hardware of your choice. </p>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<p>If Mac and Windows Avid clients will be accessing the same folder, they should be given separate share definitions, with hidden Mac files vetoed on the Windows share. See EXAMPLES.</p>
<h2>Options</h2>
<p>unityed_media:clientid = user | hostname | ip</p>
<dl>
<dd>Controls what client related identifier is appended to user specific paths: </p>
<dl>
<dd>&bull; user (default) &#8211; use the username.</dl>
<dl>
<dd>&bull; hostname &#8211; use the hostname. Note this will not work with OS X clients as these always send a generic string (&quot;workstation&quot;) to the server..</dl>
<dl>
<dd>&bull; ip &#8211; use the client&#8217;s IP address. NOTE: this is untested and may not work at all.</dl>
</dl>
<h2>Examples</h2>
<p>Enable unityed_media for Mac and Windows clients: </p>
<dl>
<dd>
<pre> <i>[avid_mac]</i>
 m[blue]<code>path = /avid</code>m[]
 m[blue]<code>vfs objects = unityed_media</code>m[]
 <i>[avid_win]</i>
 m[blue]<code>path = /avid</code>m[]
 m[blue]<code>vfs objects = unityed_media</code>m[]
 m[blue]<code>veto files = /.DS_Store/._@/.Trash@/.Spotlight@/.hidden/.hotfiles@/.vol/</code>m[]
 m[blue]<code>delete veto files = yes</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.2 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
