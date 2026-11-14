---
title: "gfstat(1)"
name: "gfstat"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfstat/"
description: "gfstat – manual page for gfstat (glusterfs-coreutils) 0.2.0"
---

<h2>NAME</h2>
<p> gfstat &#8211; manual page for gfstat (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gfstat</code> [<i>OPTION</i>]&#8230; <i>URL</i></p>
<h2>DESCRIPTION</h2>
<p> Display file status from a remote Gluster volume.</p>
<dl>
<dt><code>-L</code>, <code>&#8211;dereference</code></p>
<dd> follow links</p>
<dt><code>-o</code>, <code>&#8211;xlator-option</code>=<i>OPTION</i></p>
<dd> specify a translator option for the connection. Multiple options are supported and take the form xlator.key=value.</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> specify the port on which to connect</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> gfstat <a href="glfs://host/volume/path/to/file">glfs://host/volume/path/to/file</a></p>
<dt>
<dd> Stat the file /path/to/file on the Gluster volume of groot on host localhost to standard output.</p>
<dt>
<dd> gfcli (localhost/groot)&gt; stat /file</p>
<dt>
<dd> In the context of a shell with a connection established, stat a file on the root of the Gluster volume groot on localhost.</dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gfcli/">gfcli</a>(1) </p>
<h2>Index</h2>
