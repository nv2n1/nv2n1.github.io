---
title: "gfalfs(1)"
name: "gfalfs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfalfs/"
description: "gfalFS – Filesystem client for the GFAL 2.0 toolkit"
---

<p><code>gfalFS</code> &#8211; Filesystem client for the GFAL 2.0 toolkit </p>
<h2>Synopsis</h2>
<p><code> Mount </code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> gfalFS [options] mntdir remote_url </p>
<p> <code> Umount </code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> gfalFS_umount mntdir<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </p>
<h2>Description</h2>
<p><code>gfalFS</code> is a filesystem allowing to mount any resources supported by the GFAL 2.0 toolkit.<br />
 This include any resources accessible by the following protocol : <code> WebDav/HTTP, xrootd, SRM, GridFTP, dCAP, LFC, RFIO&#8230; </code><br />
 Please refer to the GFAL 2.0 documentation for the complete list of supported protocols.<br />
 The user can seamlessly interacts with grid and cloud storage systems just as if they are local files. </p>
<p> The protocol support depends directly of the GFAL 2.0 plugin configuration. </p>
<h2>Options</h2>
<p><code>-d</code></p>
<dl>
<dd>debug mode &#8211; does not act anymore like a daemon and print usefull information about the current operations.</dl>
<p> <code>-g</code></p>
<dl>
<dd>guid mode &#8211; access directly to the file by the guid name on the current lfc.</dl>
<p> <code>-s</code></p>
<dl>
<dd>single thread mode &#8211; Use only one thread to execute the operations, this cause a major slowdown of the execution but guarantee a protection against thread safety problems.</dl>
<p> <code>-v</code></p>
<dl>
<dd>enable verbose mode &#8211; print more informations about the current execution, can be use with <code>-d</code> in case of problems .</dl>
<p> <code>-V</code></p>
<dl>
<dd>print the version number.</dl>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </p>
<h2>Examples</h2>
<p><code> Mount an WebDav over https directory and execute a directory listing </p>
<p>&nbsp;<wbr>&nbsp;<wbr>mkdir&nbsp;<wbr>~/my_mnt/<br />
&nbsp;<wbr>&nbsp;<wbr>gfalFS&nbsp;<wbr>~/my_mnt&nbsp;<wbr><a href="davs://lxfsra04a04.cern.ch/dpm/cern.ch/">davs://lxfsra04a04.cern.ch/dpm/cern.ch/</a><br />
&nbsp;<wbr>&nbsp;<wbr>/bin/ls&nbsp;<wbr>~/my_mnt </p>
<p> Mount a local folder in debug mode and execute a directory listing </p>
<p>&nbsp;<wbr>&nbsp;<wbr>mkdir&nbsp;<wbr>~/my_mnt/<br />
&nbsp;<wbr>&nbsp;<wbr>gfalFS&nbsp;<wbr>~/my_mnt -v -d file:///etc/<br />
&nbsp;<wbr>&nbsp;<wbr>/bin/ls&nbsp;<wbr>~/my_mnt </p>
<p> Mount an SRM directory with transparent file operations<br />
&nbsp;<wbr>&nbsp;<wbr>gfalFS&nbsp;<wbr>~/my_mnt&nbsp;<wbr><a href="srm://cvitbdpm1.cern.ch/dpm/cern.ch/home/dteam/">srm://cvitbdpm1.cern.ch/dpm/cern.ch/home/dteam/</a><br />
&nbsp;<wbr>&nbsp;<wbr>echo&nbsp;<wbr>&quot;Hello world&quot;&nbsp;<wbr>&gt;&nbsp;<wbr>~/my_mnt/hello<br />
&nbsp;<wbr>&nbsp;<wbr>cat&nbsp;<wbr>~/my_mnt/hello<br />
&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>~/my_mnt/hello&nbsp;<wbr>/tmp/test_hello </p>
<p> Mount an GRIDFTP directory and create a directory </p>
<p>&nbsp;<wbr>&nbsp;<wbr>gfalFS&nbsp;<wbr>~/my_mnt&nbsp;<wbr><a href="gsiftp://cvitbdpm1.cern.ch/dpm/cern.ch/home/dteam/">gsiftp://cvitbdpm1.cern.ch/dpm/cern.ch/home/dteam/</a><br />
&nbsp;<wbr>&nbsp;<wbr>mkdir&nbsp;<wbr>~/my_mnt/testdir<br />
&nbsp;<wbr>&nbsp;<wbr>stat&nbsp;<wbr>~/my_mnt/testdir Mount an LFC directory and list the replicas of a file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>gfalFS&nbsp;<wbr>~/my_mnt&nbsp;<wbr><a href="lfc://prod-lfc-shared-central.cern.ch/grid/dteam">lfc://prod-lfc-shared-central.cern.ch/grid/dteam</a>&nbsp;<wbr></code><br />
&nbsp;<wbr>&nbsp;<wbr>getfattr -n user.replicas&nbsp;<wbr>~/my_mnt/test_file&nbsp;<wbr> </p>
<p> <code> Unmount an existing gfalFS mount point </code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>gfalFS_umount&nbsp;<wbr>~/my_mnt/ </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/3-gfal2/">gfal2</a></code>(3), </p>
<h2>Links</h2>
<p><code><a rel="nofollow" href="https://svnweb.cern.ch/trac/lcgutil/wiki/gfalFS">https://svnweb.cern.ch/trac/lcgutil/wiki/gfalFS</a></code> </p>
<h2>Authors</h2>
<p>Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;, Jean-Philippe Baud.</p>
