---
title: "vfs_media_harmony(8)"
name: "vfs_media_harmony"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_media_harmony/"
description: "vfs_media_harmony – Allow multiple Avid clients to share a network drive."
---

<p>vfs_media_harmony &#8211; Allow multiple Avid clients to share a network drive.</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = media_harmony</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_media_harmony VFS module allows Avid editorial workstations to share a network drive. It does this by: </p>
<dl>
<dd>1. Giving each client their own copy of the Avid msmMMOB.mdb and msmFMID.pmr files and Creating directories.</dl>
<dl>
<dd>2. Allowing each client to explicitly control the write time the Avid application sees on Avid media directories.</dl>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<p>vfs_media_harmony automatically redirects requests from clients for Avid database files or an Avid Creating directory to a client-specific version of the file. No configuration beyond enabling the module is needed to get this portion of its functionality working. </p>
<p> If Mac and Windows Avid clients will be accessing the same folder, they should be given separate share definitions, with hidden Mac files vetoed on the Windows share. See EXAMPLES. </p>
<p> To allow each client to control when the Avid application refreshes their Avid databases, create files for each client and each Avid media directory with the name [avid_dir_name]_[client_ip_address]_[client_username]. To trigger Avid database refreshes, update the write time on those files. See EXAMPLES. </p>
<p> It is also necessary for the cache locked write times = no option to be set for clients to be able to control their Avid media folder write times.</p>
<h2>Examples</h2>
<p>Enable media_harmony for Mac and Windows clients: </p>
<dl>
<dd>
<pre> <i>[avid_mac]</i>
 m[blue]<code>path = /avid</code>m[]
 m[blue]<code>vfs objects = media_harmony</code>m[]
 m[blue]<code>cache locked write times = no</code>m[]
 <i>[avid_win]</i>
 m[blue]<code>path = /avid</code>m[]
 m[blue]<code>vfs objects = media_harmony</code>m[]
 m[blue]<code>cache locked write times = no</code>m[]
 m[blue]<code>veto files = /.DS_Store/._@/.Trash@/.Spotlight@/.hidden/.hotfiles@/.vol/</code>m[]
 m[blue]<code>delete veto files = yes</code>m[]</pre>
</dl>
<p> Create the files that will allow users david and susan to control their own Avid database refreshes: </p>
<dl>
<dd>
<pre> touch '/avid/OMFI MediaFiles_192.168.1.10_david' \
 '/avid/OMFI MediaFiles_192.168.1.11_susan' \
 '/avid/Avid MediaFiles/MXF/1_192.168.1.10_david' \
 '/avid/Avid MediaFiles/MXF/1_192.168.1.11_susan'</pre>
</dl>
<p> Trigger an Avid database refresh for user david: </p>
<dl>
<dd>
<pre> touch '/avid/OMFI MediaFiles_192.168.1.10_david' \
 '/avid/Avid MediaFiles/MXF/1_192.168.1.10_david'</pre>
</dl>
<p> If you have a large number of Avid media folders to manage, you can give each editor a suitably modified version of examples/scripts/vfs/media_harmony/trigger_avid_update.py to create and update these files.</p>
<h2>Caveats</h2>
<p>vfs_media_harmony is designed to work with Avid editing applications that look in the Avid MediaFiles or OMFI MediaFiles directories for media. It is not designed to work as expected in all circumstances for general use. For example: It is possible to open a client-specific file such as msmMMOB.mdb_192.168.1.10_userx even though it doesn&#8217;t show up in a directory listing.</p>
<h2>Version</h2>
<p>This man page is correct for version 3.2.7 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
