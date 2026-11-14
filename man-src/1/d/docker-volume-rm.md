---
title: "docker-volume-rm(1)"
name: "docker-volume-rm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-volume-rm/"
description: "docker-volume-rm – Remove one or more volumes"
---

<h2 class="name">NAME</h2>
<p> docker-volume-rm &#8211; Remove one or more volumes </p>
<h2>SYNOPSIS</h2>
<p> <code>docker volume rm [OPTIONS] VOLUME [VOLUME&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Remove one or more volumes. You cannot remove a volume that is in use by a container. </p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;force</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Force the removal of one or more volumes</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for rm</p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
$ docker volume rm hello
hello
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-volume/">docker-volume</a>(1)</code> </p>
<h2>Index</h2>
