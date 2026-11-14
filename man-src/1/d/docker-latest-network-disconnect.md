---
title: "docker-latest-network-disconnect(1)"
name: "docker-latest-network-disconnect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-network-disconnect/"
description: "docker-network-disconnect – disconnect a container from a network"
---

<h2 class="name">NAME</h2>
<p> docker-network-disconnect &#8211; disconnect a container from a network </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network disconnect</code> [<code>&#8211;help</code>] [<code>&#8211;force</code>] NETWORK CONTAINER </p>
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
<p> <code>NETWORK</code><br />
&nbsp;<wbr>&nbsp;<wbr>Specify network name </p>
<p> <code>CONTAINER</code><br />
&nbsp;<wbr>Specify container name </p>
<p> <code>&#8211;force</code><br />
&nbsp;<wbr>&nbsp;<wbr>Force the container to disconnect from a network </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>HISTORY</h2>
<p> OCT 2015, created by Mary Anthony &lt;mary [at] docker.com&gt; </p>
<h2>Index</h2>
