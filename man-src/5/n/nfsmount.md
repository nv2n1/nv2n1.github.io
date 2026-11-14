---
title: "nfsmount(5)"
name: "nfsmount"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nfsmount/"
description: "nfsmount.conf – Configuration file for NFS mounts"
---

<p>nfsmount.conf &#8211; Configuration file for NFS mounts</p>
<h2>Synopsis</h2>
<p>Configuration file for NFS mounts that allows options to be set globally, per server or per mount point.</p>
<h2>Description</h2>
<p>The configuration file is made up of multiple sections followed by variables associated with that section. A section is defined by a string enclosed by <code>[</code> and <code>]</code> branches. Variables are assignment statements that assign values to particular variables using the <code>=</code> operator, as in <code>Proto=Tcp</code>. The variables that can be assigned are exactly the set of NFS specific mount options listed in <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5). </p>
<p> Sections are broken up into three basic categories: Global options, Server options and Mount Point options.</p>
<dl>
<dt> <code>[ NFSMount_Global_Options ]</code> &#8211; This statically named section</p>
<dd>defines all of the global mount options that can be applied to every NFS mount.</p>
<dt> <code>[ Server &#8220;Server_Name&#8221; ] </code> &#8211; This section defines all the mount options that should</p>
<dd>be used on mounts to a particular NFS server. The <i>&#8220;Server_Name&#8221;</i> strings needs to be surrounded by &#8216;&#8221;&#8216; and be an exact match of the server name used in the <code>mount</code> command.</p>
<dt> <code>[ MountPoint &#8220;Mount_Point&#8221; ]</code> &#8211; This section defines all the mount options that</p>
<dd>should be used on a particular mount point. The <i>&#8220;Mount_Point&#8221;</i> string needs to be surrounded by &#8216;&#8221;&#8216; and be an exact match of the mount point used in the <code>mount</code> command.</dl>
<h2>Examples</h2>
<p>These are some example lines of how sections and variables are defined in the configuration file. </p>
<p> [ NFSMount_Global_Options ] </p>
<p>&nbsp;<wbr>Proto=Tcp</p>
<dl>
<dd>
<dl>
<dd>The TCP/IPv4 protocol will be used on every NFS mount.</p>
<dt></dl>
</dl>
<p> [ Server &#8220;nfsserver.foo.com&#8221; ]</p>
<dd>&nbsp;<wbr>rsize=32k</p>
<dd>&nbsp;<wbr>wsize=32k</p>
<dd>&nbsp;<wbr>proto=udp6</p>
<dl>
<dt>
<dl>
<dd>
<dd>A 32k (32768 bytes) block size will be used as the read and write size on all mounts to the &#8216;nfsserver.foo.com&#8217; server. UDP/IPv6 is the protocol to be used.</p>
<dl>
<dt></dl>
</dl>
<p> [ MountPoint &#8220;/export/home&#8221; ]</p>
<dd>&nbsp;<wbr>Background=True</p>
<dl>
<dd>
<dl>
<dd>All mounts to the &#8216;/export/home&#8217; export will be performed in the background (i.e. done asynchronously).</p>
<dt></dl>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/nfsmount.conf</i></p>
<dd>
<dd>Default NFS mount configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), </p>
