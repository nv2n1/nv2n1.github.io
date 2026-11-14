---
title: "vfs_glusterfs(8)"
name: "vfs_glusterfs"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_glusterfs/"
description: "vfs_glusterfs – Utilize features provided by GlusterFS"
---

<p>vfs_glusterfs &#8211; Utilize features provided by GlusterFS</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = glusterfs</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/8-samba/">samba</a></code>(8) suite. </p>
<p> GlusterFS (<a rel="nofollow" href="http://www.gluster.org)">http://www.gluster.org)</a> is an Open Source clustered file system capable of scaling to several peta-bytes. With its FUSE based native client, GlusterFS is available as a POSIX compliant file system and can hence be shared by Samba without additional steps. </p>
<p> The vfs_glusterfs VFS module provides an alternative, and superior way to access a Gluster filesystem from Samba for sharing. It does not require a Gluster FUSE mount but directly accesses the GlusterFS daemon through its library libgfapi, thereby omitting the expensive kernel-userspace context switches and taking advantage of some of the more advanced features of GlusterFS. </p>
<p> This module can be combined with other modules, but it should be the last module in the vfs objects list. Modules added to this list to the right of the glusterfs entry may not have any effect at all.</p>
<h2>Configuration</h2>
<p>A basic configuration looks like this. </p>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>vfs objects = glusterfs</code>m[]
 m[blue]<code>path = /relative/base/path</code>m[]
 m[blue]<code>glusterfs:volume = gv0</code>m[]
 m[blue]<code>kernel share modes = no</code>m[]</pre>
</dl>
<p> Note that since vfs_glusterfs does not require a Gluster mount, the share path is treated differently than for other shares: It is interpreted as the base path of the share relative to the gluster volume used. Because this is usually not at the same time a system path, in a ctdb cluster setup where ctdb manages Samba, you need to set CTDB_SAMBA_SKIP_SHARE_CHECK=yes in ctdb&#8217;s configuration file. Otherwise ctdb will not get healthy. </p>
<p> Note that currently kernel share modes have to be disabled in a share running with the glusterfs vfs module for file serving to work properly.</p>
<h2>Options</h2>
<p>glusterfs:logfile = path</p>
<dl>
<dd>Defines whether and where to store a vfs_glusterfs specific logfile. Client variable substitution is supported (i.e. %M, %m, %I), hence per client log file can be specified. </p>
<p> Example: glusterfs:logfile = /var/log/samba/glusterfs-vol2.%M.log</dl>
<p> glusterfs:loglevel = 0-9</p>
<dl>
<dd>Defines the level of logging, with higher numbers corresponding to more verbosity. 0 &#8211; No logs; 9 &#8211; Trace log level; 7 being the info log level is preferred. </p>
<p> If this option is not defined with an explicit loglevel, the glusterfs default is used (currently loglevel 7).</dl>
<p> glusterfs:volfile_server = servername</p>
<dl>
<dd>Defines which volfile server to use, defaults to localhost.</dl>
<p> glusterfs:volume = volumename</p>
<dl>
<dd>Defines the glusterfs volumename to use for this share.</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.2.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
