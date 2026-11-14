---
title: "gfls(1)"
name: "gfls"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfls/"
description: "gfls – manual page for gfls (glusterfs-coreutils) 0.2.0"
---

<h2>NAME</h2>
<p> gfls &#8211; manual page for gfls (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gfls</code> [<i>OPTION</i>]&#8230; <i>URL</i></p>
<h2>DESCRIPTION</h2>
<p> list directory contents</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> do not ignore entries starting with .</p>
<dt><code>-h</code>, <code>&#8211;human-readable</code></p>
<dd> with <code>-l</code>, print sizes in human readable format (e.g., 1K 234M 2G)</p>
<dt><code>-l</code></p>
<dd> use a long listing format</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></p>
<dd> list subdirectories recursively</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> specify the port on which to connect</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> gfls <a href="glfs://localhost/groot/directory">glfs://localhost/groot/directory</a></p>
<dt>
<dd> List the contents of /directory on the Gluster volume root on host localhost.</p>
<dt>
<dd> gfls -l <a href="glfs://localhost/groot/directory">glfs://localhost/groot/directory</a></p>
<dt>
<dd> List the contents of /directory on the Gluster volume root on host localhost using the long listing format.</p>
<dt>
<dd> gfls -Rl <a href="glfs://localhost/groot/directory">glfs://localhost/groot/directory</a></p>
<dt>
<dd> Recursively list the contents of /directory on the Gluster volume groot on host localhost using the long listing format.</p>
<dt>
<dd> gfcli (localhost/groot)&gt; ls /</p>
<dt>
<dd> List the contents of the root of the connected Gluster volume.</dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gfcli/">gfcli</a>(1) </p>
<h2>Index</h2>
