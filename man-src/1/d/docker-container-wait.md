---
title: "docker-container-wait(1)"
name: "docker-container-wait"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-wait/"
description: "docker-container-wait – Block until one or more containers stop, then print their exit codes"
---

<h2 class="name">NAME</h2>
<p> docker-container-wait &#8211; Block until one or more containers stop, then print their exit codes </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container wait CONTAINER [CONTAINER&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Block until a container stops, then print its exit code. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ docker run -d fedora sleep 99
079b83f558a2bc52ecad6b2a5de13622d584e6bb1aea058c11b36511e85e7622
$ docker container wait 079b83f558a2bc
0
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for wait</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
