---
title: "docker-container-diff(1)"
name: "docker-container-diff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-diff/"
description: "docker-container-diff – Inspect changes to files or directories on a container’s filesystem"
---

<h2 class="name">NAME</h2>
<p> docker-container-diff &#8211; Inspect changes to files or directories on a container&#8217;s filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container diff CONTAINER</code> </p>
<h2>DESCRIPTION</h2>
<p> List the changed files and directories in a container᾿s filesystem since the container was created. Three different types of change are tracked: </p>
<table BORDER>
<tr VALIGN=top>
<td>Symbol</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>A</td>
<td>A file or directory was added
</td>
</tr>
<tr VALIGN=top>
<td>D</td>
<td> A file or directory was deleted
</td>
</tr>
<tr VALIGN=top>
<td>C</td>
<td> A file or directory was changed
</td>
</tr>
</table>
<p> You can use the full or shortened container ID or the container name set using <code>docker run &#8211;name</code> option. </p>
<h2>EXAMPLES</h2>
<p> Inspect the changes to an nginx container: </p>
<dl>
<dt>
<dd>
<pre>
$ docker diff 1fdfd1f54c1b
C /dev
C /dev/console
C /dev/core
C /dev/stdout
C /dev/fd
C /dev/ptmx
C /dev/stderr
C /dev/stdin
C /run
A /run/nginx.pid
C /var/lib/nginx/tmp
A /var/lib/nginx/tmp/client_body
A /var/lib/nginx/tmp/fastcgi
A /var/lib/nginx/tmp/proxy
A /var/lib/nginx/tmp/scgi
A /var/lib/nginx/tmp/uwsgi
C /var/log/nginx
A /var/log/nginx/access.log
A /var/log/nginx/error.log
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for diff</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
