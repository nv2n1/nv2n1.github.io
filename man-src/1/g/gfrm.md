---
title: "gfrm(1)"
name: "gfrm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfrm/"
description: "gfrm – manual page for gfrm (glusterfs-coreutils) 0.2.0"
---

<h2>NAME</h2>
<p> gfrm &#8211; manual page for gfrm (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gfrm</code> [<i>OPTION</i>]&#8230; <i>URL</i></p>
<h2>DESCRIPTION</h2>
<p> Remove (unlink) the files (or directories) from a remote Gluster volume.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> ignore nonexistent files, never prompt</p>
<dt><code>-o</code>, <code>&#8211;xlator-option</code>=<i>OPTION</i></p>
<dd> specify a translator option for the connection. Multiple options are supported and take the form xlator.key=value.</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> specify the port on which to connect</p>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> remove directories and their contents recursively</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> gfrm <a href="glfs://localhost/groot/path/to/file">glfs://localhost/groot/path/to/file</a></p>
<dt>
<dd> Remove the file /path/to/file on the Gluster volume of groot on host localhost.</p>
<dt>
<dd> gfrm -r <a href="glfs://localhost/groot/path/to/directory">glfs://localhost/groot/path/to/directory</a></p>
<dt>
<dd> Recursively remove the directory /path/to/directory on the Gluster volume of groot on host localhost.</p>
<dt>
<dd> gfcli (localhost/groot)&gt; rm /file</p>
<dt>
<dd> In the context of a shell with a connection established, remove the file on the root of the Gluster volume groot on localhost.</dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gfcli/">gfcli</a>(1) </p>
<h2>Index</h2>
