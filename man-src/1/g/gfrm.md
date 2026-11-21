---

title: "gfrm(1)"
name: "gfrm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfrm/"
description: "gfrm – manual page for gfrm (glusterfs-coreutils) 0.2.0"
---

<p> gfrm &#8211; manual page for gfrm (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gfrm</code> [<i>OPTION</i>]&#8230; <i>URL</i></p>
<h2>DESCRIPTION</h2>
<p> Remove (unlink) the files (or directories) from a remote Gluster volume.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> ignore nonexistent files, never prompt</dd>
<dt><code>-o</code>, <code>&#8211;xlator-option</code>=<i>OPTION</i></dt>
<dd> specify a translator option for the connection. Multiple options are supported and take the form xlator.key=value.</dd>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></dt>
<dd> specify the port on which to connect</dd>
<dt><code>-r</code>, <code>&#8211;recursive</code></dt>
<dd> remove directories and their contents recursively</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> gfrm <a href="glfs://localhost/groot/path/to/file">glfs://localhost/groot/path/to/file</a></dd>
<dt>
</dt><dd> Remove the file /path/to/file on the Gluster volume of groot on host localhost.</dd>
<dt>
</dt><dd> gfrm -r <a href="glfs://localhost/groot/path/to/directory">glfs://localhost/groot/path/to/directory</a></dd>
<dt>
</dt><dd> Recursively remove the directory /path/to/directory on the Gluster volume of groot on host localhost.</dd>
<dt>
</dt><dd> gfcli (localhost/groot)&gt; rm /file</dd>
<dt>
</dt><dd> In the context of a shell with a connection established, remove the file on the root of the Gluster volume groot on localhost.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gfcli/">gfcli</a>(1) </p>
