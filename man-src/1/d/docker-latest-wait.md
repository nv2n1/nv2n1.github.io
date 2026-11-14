---
title: "docker-latest-wait(1)"
name: "docker-latest-wait"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-wait/"
description: "docker-wait – Block until a container stops, then print its exit code."
---

<h2 class="name">NAME</h2>
<p> docker-wait &#8211; Block until a container stops, then print its exit code. </p>
<h2>SYNOPSIS</h2>
<p> <code>docker wait</code> [<code>&#8211;help</code>] CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Block until a container stops, then print its exit code. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ docker run -d fedora sleep 99
079b83f558a2bc52ecad6b2a5de13622d584e6bb1aea058c11b36511e85e7622
$ docker wait 079b83f558a2bc
0
</pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
