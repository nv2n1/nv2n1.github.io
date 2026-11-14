---
title: "docker-latest-diff(1)"
name: "docker-latest-diff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-diff/"
description: "docker-diff – Inspect changes on a container’s filesystem"
---

<h2 class="name">NAME</h2>
<p> docker-diff &#8211; Inspect changes on a container&#8217;s filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>docker diff</code> [<code>&#8211;help</code>] CONTAINER </p>
<h2>DESCRIPTION</h2>
<p> Inspect changes on a container&#8217;s filesystem. You can use the full or shortened container ID or the container name set using <code>docker run &#8211;name</code> option. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>EXAMPLES</h2>
<p> Inspect the changes to on a nginx container: </p>
<dl>
<dt>
<dd>
<pre>
# docker diff 1fdfd1f54c1b
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
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
