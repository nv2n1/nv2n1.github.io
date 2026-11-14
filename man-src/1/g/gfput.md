---
title: "gfput(1)"
name: "gfput"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfput/"
description: "gfput – manual page for gfput (glusterfs-coreutils) 0.2.0"
---

<h2>NAME</h2>
<p> gfput &#8211; manual page for gfput (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gfput</code> [<i>OPTION</i>]&#8230; <i>URL</i></p>
<h2>DESCRIPTION</h2>
<p> Put data from standard input on a remote Gluster volume.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;append</code></p>
<dd> append data to the end of the file</p>
<dt><code>-f</code>, <code>&#8211;overwrite</code></p>
<dd> overwrite the existing file</p>
<dt><code>-o</code>, <code>&#8211;xlator-option</code>=<i>OPTION</i></p>
<dd> specify a translator option for the connection. Multiple options are supported and take the form xlator.key=value.</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> specify the port on which to connect</p>
<dt><code>-r</code>, <code>&#8211;parents</code></p>
<dd> no error if existing, make parent directories as needed</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> gfput <a href="glfs://localhost/groot/file">glfs://localhost/groot/file</a></p>
<dt>
<dd> Write the contents of standard input to /file on the Gluster volume of groot on host localhost.</p>
<dt>
<dd> gfput -r <a href="glfs://localhost/groot/path/to/file">glfs://localhost/groot/path/to/file</a></p>
<dt>
<dd> Write the contents of standard input to /file on the Gluster volume of groot on host localhost, creating the parent directories as necessary.</dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
