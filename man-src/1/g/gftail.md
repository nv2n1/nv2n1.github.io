---
title: "gftail(1)"
name: "gftail"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gftail/"
description: "gftail – manual page for gftail (glusterfs-coreutils) 0.2.0"
---

<h2>NAME</h2>
<p> gftail &#8211; manual page for gftail (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gftail</code> [<i>OPTION</i>]&#8230; <i>URL</i></p>
<h2>DESCRIPTION</h2>
<p> Print the last 10 lines (default) of the file to standard output.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;bytes</code>=<i>K</i></p>
<dd> output the last K bytes</p>
<dt><code>-f</code>, <code>&#8211;follow</code></p>
<dd> output appended data as the file grows</p>
<dt><code>-n</code>, <code>&#8211;lines</code>=<i>K</i></p>
<dd> output the last K lines, instead of the last 10</p>
<dt><code>-o</code>, <code>&#8211;xlator-option</code>=<i>OPTION</i></p>
<dd> specify a translator option for the connection. Multiple options are supported and take the form xlator.key=value.</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> specify the port on which to connect</p>
<dt><code>-s</code>, <code>&#8211;sleep-internal</code>=<i>N</i></p>
<dd> with <code>-f</code>, sleep for approximately N microseconds (default is 50,000)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> gftail <a href="glfs://localhost/groot/file">glfs://localhost/groot/file</a></p>
<dt>
<dd> Tail the last 10 lines of the file /file on the Gluster volume groot on host localhost.</p>
<dt>
<dd> gftail -c 100 <a href="glfs://localhost/groot/file">glfs://localhost/groot/file</a></p>
<dt>
<dd> Tail the last 100 bytes of the file /file on the Gluster volume groot on host localhost.</p>
<dt>
<dd> gftail -f <a href="glfs://localhost/groot/file">glfs://localhost/groot/file</a></p>
<dt>
<dd> Tail the last 10 lines of the file /file on the Gluster volume groot on host localhost, following the file until an interrupt is received.</p>
<dt>
<dd> gfcli (localhost/groot)&gt; tail /example</p>
<dt>
<dd> In the context of a shell with a connection established, tail the file example on the root of the Gluster volume groot on localhost.</dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gfcli/">gfcli</a>(1) </p>
<h2>Index</h2>
