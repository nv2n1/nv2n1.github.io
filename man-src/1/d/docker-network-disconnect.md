---
title: "docker-network-disconnect(1)"
name: "docker-network-disconnect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-network-disconnect/"
description: "docker-network-disconnect – Disconnect a container from a network"
---

<h2 class="name">NAME</h2>
<p> docker-network-disconnect &#8211; Disconnect a container from a network </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network disconnect [OPTIONS] NETWORK CONTAINER</code> </p>
<h2>DESCRIPTION</h2>
<p> Disconnects a container from a network. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network disconnect multi-host-network container1
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;force</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Force the container to disconnect from a network</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for disconnect</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-network/">docker-network</a>(1)</code> </p>
<h2>Index</h2>
